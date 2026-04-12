from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
import os

app = FastAPI()

class Action(BaseModel):
    action: str

class Observation(BaseModel):
    state: Dict[str, Any]

class Reward(BaseModel):
    value: float

# Simple environment instance
from env.curriculum_env import CurriculumEnv
from env.openenv_wrapper import OpenEnvWrapper

env_instance = None

def get_env():
    global env_instance
    if env_instance is None:
        base_env = CurriculumEnv()
        env_instance = OpenEnvWrapper(base_env)
    return env_instance

@app.get("/")
def root():
    return {"message": "OpenEnv Server is running"}

@app.post("/reset")
def reset():
    try:
        env = get_env()
        obs = env.reset()
        return {
            "observation": obs.state,
            "done": False,
            "info": {}
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/step")
def step(action: Action):
    try:
        env = get_env()
        obs, reward, done, info = env.step(action)
        return {
            "observation": obs.state,
            "reward": reward.value,
            "done": done,
            "info": info
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)