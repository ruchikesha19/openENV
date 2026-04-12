import asyncio
from openenv.core import create_app
from env.curriculum_env import CurriculumEnv
from env.openenv_wrapper import OpenEnvWrapper
from schemas import Action, Observation

def create_wrapped_env():
    """Factory function to create wrapped environment"""
    base_env = CurriculumEnv()
    return OpenEnvWrapper(base_env)

async def main():
    # Create the FastAPI app with environment factory function
    app = create_app(create_wrapped_env, action_cls=Action, observation_cls=Observation)
    
    # Import uvicorn to run the server
    import uvicorn
    config = uvicorn.Config(app, host="0.0.0.0", port=7860)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
