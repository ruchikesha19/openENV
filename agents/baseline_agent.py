"""
Baseline agent for CurriculumEnv
Input: state dictionary
Output: action string
"""

# simple memory to avoid loops
action_history = []
quiz_failures = 0


# def baseline_agent(state):

#     global action_history
#     global quiz_failures

#     mastery = state["concept_mastery"]
#     fatigue = state["fatigue"]
#     quiz_accuracy = state.get("quiz_accuracy", 0)
#     engagement = state.get("engagement", 1)

#     avg_mastery = sum(mastery) / len(mastery)

#     # fatigue handling
#     if fatigue > 0.75:
#         action = "take_break"

#     # early learning
#     elif avg_mastery < 0.25:
#         action = "show_video"

#     # practice phase
#     elif avg_mastery < 0.55:
#         action = "interactive_exercise"

#     # quiz phase
#     elif avg_mastery < 0.85:

#         if quiz_accuracy < 0.6:
#             quiz_failures += 1

#             if quiz_failures >= 2:
#                 action = "revision_notes"
#             else:
#                 action = "give_quiz"

#         else:
#             action = "interactive_exercise"

#     # mastery complete
#     else:
#         action = "skip_topic"

#     # prevent loops
#     action_history.append(action)
#     if len(action_history) > 5:
#         action_history.pop(0)

#     return action

import random

last_action = None  # global memory

def baseline_agent(state):
    global last_action

    mastery = state["concept_mastery"]
    fatigue = state["fatigue"]
    attempts = state["attempt_count"]

    # find current concept
    current_idx = 0
    for i, m in enumerate(mastery):
        if m < 0.8:
            current_idx = i
            break

    current_mastery = mastery[current_idx]

    # 🧠 RULE 1: fatigue handling
    if fatigue > 0.7:
        action = "take_break"

    # 🧠 RULE 2: mastery-based decisions (FIXED thresholds)
    elif current_mastery < 0.4:
        action = "show_video"

    elif current_mastery < 0.7:
        action = "interactive_exercise"

    elif current_mastery >= 0.85:
        action = "give_quiz"   # moved higher threshold

    else:
        action = "revision_notes"

    # 🧠 RULE 3: stuck condition
    if attempts >= 2 and current_mastery < 0.7:
        action = "revision_notes"

    # 🎲 RULE 4: exploration (VERY IMPORTANT)
    if random.random() < 0.15:
        action = random.choice([
            "show_video",
            "interactive_exercise",
            "give_quiz",
            "revision_notes"
        ])

    # 🔁 RULE 5: anti-repetition
    if action == last_action:
        action = "interactive_exercise"

    last_action = action
    

    return action