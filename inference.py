import os
from schemas import Action
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from env.curriculum_env import CurriculumEnv
from env.openenv_wrapper import OpenEnvWrapper
from agents.baseline_agent import baseline_agent


API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME", "baseline")
HF_TOKEN = os.getenv("HF_TOKEN")
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")


def main():
    task = "adaptive_learning"
    env_name = "openenv"

    client = OpenAI(
        base_url=API_BASE_URL,
        api_key=HF_TOKEN,
    )

    env = OpenEnvWrapper(CurriculumEnv())
    # agent = baseline_agent

    observation = env.reset()

    print(f"[START] task={task} env={env_name} model={MODEL_NAME}")

    done = False
    step_count = 0
    rewards = []

    while not done and step_count < 20:
        try:
            action_raw = baseline_agent(observation.state)
            #action = {"action": action_raw}
            action = Action(action=action_raw)
            observation, reward, done, info = env.step(action)

            reward_value = float(reward.value)
            rewards.append(reward_value)

            print(
                f"[STEP] step={step_count} action={action_raw} "
                f"reward={reward_value:.2f} done={str(done).lower()} error=null"
            )

        except Exception as e:
            print(
                f"[STEP] step={step_count} action=null reward=0.00 "
                f"done=true error={str(e)}"
            )
            done = True
            break

        step_count += 1

    # Calculate score as average reward normalized to [0,1]
    score = sum(rewards) / len(rewards) if rewards else 0.0
    score = min(max(score / 10.0, 0.0), 1.0)  # Normalize assuming max reward per step is 10.0
    
    success = score >= 0.1  # Success threshold as in sample

    rewards_str = ",".join([f"{r:.2f}" for r in rewards])

    print(
        f"[END] success={str(success).lower()} steps={step_count} score={score:.3f} rewards={rewards_str}"
    )


if __name__ == "__main__":
    main()