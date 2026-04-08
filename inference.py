# import os
# from agents.baseline_agent import baseline_agent
# from env.curriculum_env import CurriculumEnv

# TASK_NAME = "adaptive_learning"
# BENCHMARK = "openenv"
# MODEL_NAME = os.getenv("MODEL_NAME", "baseline")


# def run(student_type):
#     env = CurriculumEnv(student_type)
#     state = env.reset()

#     print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}")

#     rewards = []
#     step_num = 0
#     done = False

#     while not done and step_num < 20:
#         action = baseline_agent(state)
#         state, reward, done, _ = env.step(action)

#         rewards.append(reward)
#         step_num += 1

#         print(f"[STEP] step={step_num} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

#     print(f"[END] success={str(done).lower()} steps={step_num} rewards={','.join([f'{r:.2f}' for r in rewards])}")


# if __name__ == "__main__":
#     for level in ["easy", "medium", "hard"]:
#         run(level)



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

    success = all(r > 0 for r in rewards)

    rewards_str = ",".join([f"{r:.2f}" for r in rewards])

    print(
        f"[END] success={str(success).lower()} steps={step_count} rewards={rewards_str}"
    )


if __name__ == "__main__":
    main()