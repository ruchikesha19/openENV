import random
from typing import Dict
from .models import Observation, Action, Reward


class AdaptiveLearningEnv:

    ACTIONS = [
        "show_video",
        "give_quiz",
        "interactive_exercise",
        "revision_notes",
        "skip_topic",
        "take_break"
    ]

    def __init__(self, difficulty="medium"):

        self.difficulty = difficulty
        self.num_concepts = 5
        self.max_steps = 40

        self.reset()

    def reset(self):

        self.steps = 0

        self.state_data = {
            "concept_mastery": [0.0] * self.num_concepts,
            "quiz_accuracy": 0.0,
            "time_spent": 0.0,
            "attempt_count": 0,
            "fatigue": 0.0,
            "engagement": 1.0
        }

        if self.difficulty == "easy":
            self.learning_rate = 0.15
        elif self.difficulty == "hard":
            self.learning_rate = 0.05
        else:
            self.learning_rate = 0.1

        return self.state()

    def state(self):

        return Observation(**self.state_data)

    def step(self, action: Action):

        self.steps += 1

        action_type = action.action_type

        reward = 0.0

        if action_type == "show_video":

            gain = random.uniform(0.05, 0.1) * self.learning_rate
            self._improve_mastery(gain)
            reward += gain

        elif action_type == "interactive_exercise":

            gain = random.uniform(0.1, 0.2) * self.learning_rate
            self._improve_mastery(gain)
            reward += gain * 1.5

        elif action_type == "give_quiz":

            accuracy = sum(self.state_data["concept_mastery"]) / self.num_concepts
            noise = random.uniform(-0.1, 0.1)

            quiz_score = max(0.0, min(1.0, accuracy + noise))

            self.state_data["quiz_accuracy"] = quiz_score
            avg_mastery = sum(self.state_data["concept_mastery"]) / self.num_concepts

            if avg_mastery < 0.5:
                reward -= 1.0   # 🚨 punish early quiz HARD

            elif quiz_score > 0.75:
                reward += 2.0   # 🎯 strong reward

            elif quiz_score > 0.6:
                reward += 0.5

            else:
                reward -= 0.5
        elif action_type == "revision_notes":

            gain = random.uniform(0.02, 0.06) * self.learning_rate
            self._improve_mastery(gain)
            reward += gain

        elif action_type == "skip_topic":

            reward -= 0.2

        elif action_type == "take_break":

            self.state_data["fatigue"] = max(0, self.state_data["fatigue"] - 0.2)
            reward += 0.2

        # fatigue and engagement update
        self.state_data["fatigue"] += 0.05
        self.state_data["engagement"] -= 0.01

        self.state_data["time_spent"] += 1
        self.state_data["attempt_count"] += 1

        done = False

        if all(m > 0.85 for m in self.state_data["concept_mastery"]):
            done = True

        if self.steps >= self.max_steps:
            done = True

        return self.state(), Reward(value=reward), done, {}

def _improve_mastery(self, gain):

    concept = random.randint(0, self.num_concepts - 1)

    before = self.state_data["concept_mastery"][concept]

    after = min(1.0, before + gain)

    self.state_data["concept_mastery"][concept] = after

    return after - before  # 🔥 return actual improvement