import numpy as np


class CurriculumEnv:
    def __init__(self, student_type="medium"):
        self.student_type = student_type
        self.num_concepts = 4
        self.max_steps = 50
        self.reset()

    def reset(self):
        self.concept_mastery = np.random.uniform(0.2, 0.5, self.num_concepts)
        self.quiz_accuracy = 0.0
        self.time_spent = 0
        self.attempt_count = 0
        self.fatigue = 0.2
        self.engagement = 0.8
        self.current_concept = 0
        self.done = False
        self.steps = 0
        return self.get_state()

    def get_state(self):
        return {
            "concept_mastery": self.concept_mastery.tolist(),
            "quiz_accuracy": self.quiz_accuracy,
            "time_spent": self.time_spent,
            "attempt_count": self.attempt_count,
            "fatigue": self.fatigue,
            "engagement": self.engagement
        }

    def step(self, action):
        if self.done:
            return self.get_state(), 0, True, {}

        reward = 0
        idx = min(self.current_concept, self.num_concepts - 1)
        prev_mastery = self.concept_mastery[idx]

        if action == "show_video":
            self._learn(0.05)

        elif action == "interactive_exercise":
            self._learn(0.08)

        elif action == "revision_notes":
            self._learn(0.04)

        elif action == "give_quiz":
            reward += self._quiz()

        elif action == "skip_topic":
            self.current_concept += 1

        elif action == "take_break":
            self.fatigue = max(0, self.fatigue - 0.2)
            self.engagement = min(1.0, self.engagement + 0.1)

        idx = min(self.current_concept, self.num_concepts - 1)
        new_mastery = self.concept_mastery[idx]

        improvement = new_mastery - prev_mastery
        if improvement > 0:
            reward += 5 * improvement * 10

        if self.engagement < 0.3:
            reward -= 8

        if self.engagement < 0.1:
            reward -= 20
            self.done = True

        self.time_spent += 1
        self.steps += 1
        self.fatigue = min(1.0, self.fatigue + 0.02)

        if self.current_concept >= self.num_concepts:
            reward += 20
            self.done = True

        if self.steps >= self.max_steps:
            self.done = True

        return self.get_state(), reward, self.done, {}

    def _learn(self, amount):
        rate = self._learning_rate()
        idx = min(self.current_concept, self.num_concepts - 1)

        if self.concept_mastery[idx] > 0.9:
            return

        self.concept_mastery[idx] += amount * rate

        if self.attempt_count > 0:
            self.concept_mastery[idx] += 0.02

        self.concept_mastery[idx] = min(1.0, self.concept_mastery[idx])
        self.engagement = max(0.0, self.engagement - 0.02)

    def _quiz(self):
        self.attempt_count += 1
        idx = min(self.current_concept, self.num_concepts - 1)
        mastery = self.concept_mastery[idx]

        if mastery >= 0.6:
            self.quiz_accuracy = mastery
            self.current_concept += 1
            self.attempt_count = 0
            return 12
        else:
            self.concept_mastery[idx] += 0.1
            self.concept_mastery[idx] = min(1.0, self.concept_mastery[idx])
            return -1

    def _learning_rate(self):
        if self.student_type == "easy":
            return 1.5
        elif self.student_type == "hard":
            return 0.7
        return 1.0