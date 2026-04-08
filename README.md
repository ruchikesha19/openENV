# 📘 Adaptive Curriculum Learning Agent (OpenEnv)

## 🚀 Overview

This project implements a **baseline reinforcement learning-style agent** for an adaptive learning environment. The agent dynamically selects learning actions (videos, exercises, quizzes, etc.) based on student state (mastery, fatigue, engagement) to maximize learning efficiency.

The system includes:

* 🎯 **Baseline Agent** – Adaptive decision-making policy
* 📊 **Evaluation System** – Deterministic scoring across difficulty levels
* 🧠 **Curriculum Environment** – Simulated student learning dynamics

---

## 🧠 Problem Statement

Design an intelligent agent that:

* Adapts to student mastery levels
* Avoids repetitive failures and loops
* Handles fatigue and engagement
* Completes concepts efficiently within limited steps

---

## ⚙️ Features

### ✅ Baseline Agent

* Mastery-driven decision making
* Fatigue-aware (takes breaks when needed)
* Engagement-aware (adjusts learning strategy)
* Quiz-gated progression (ensures understanding before moving forward)
* Prevents infinite loops and inefficient actions

### 📊 Evaluation Metrics

The agent is evaluated using:

* **Learning Gain** = Final Mastery − Initial Mastery
* **Completion Rate** = Concepts Completed / Total Concepts
* **Efficiency** = 1 / Steps Taken

### 🧮 Final Score Formula

```
score = 0.5 * learning_gain + 0.3 * completion_rate + 0.2 * efficiency
```

* Score is clamped between **0.0 and 1.0**
* Fully deterministic (no randomness in evaluation)

---

## 🧪 Evaluation Setup

The agent is tested on three student types:

| Difficulty | Description                  |
| ---------- | ---------------------------- |
| Easy       | Fast learner, low fatigue    |
| Medium     | Balanced learner             |
| Hard       | Slow learner, higher fatigue |

---

## 📈 Results

```
Easy   → Score: 0.998
Medium → Score: 0.984
Hard   → Score: 0.898
```

### ✔ Performance Summary

* Easy & Medium: **Full success**
* Hard: **Strong partial success**
* High efficiency and learning gain across all scenarios

---

## 🏗️ Project Structure

```
openENV/
│
├── agents/
│   └── baseline_agent.py
│
├── env/
│   └── curriculum_env.py
│
├── grader/
│   └── evaluator.py
│
└── README.md
```

---

## ▶️ How to Run

### 1. Activate Virtual Environment

```
venv\Scripts\activate
```

### 2. Run Evaluation

```
python grader/evaluator.py
python inference.py

```

---

## 🧠 Agent Strategy

The agent follows a **threshold-based curriculum policy**:

* 📉 Low mastery → `show_video`
* 📈 Medium mastery → `interactive_exercise`
* 🎯 High mastery → `give_quiz`
* 😴 High fatigue → `take_break`

This ensures:

* Efficient learning progression
* Reduced unnecessary actions
* Faster concept completion

---

## 🔒 Determinism

* Evaluation is fully deterministic
* No randomness in scoring
* Ensures reproducibility and fair comparison

---

## 🚀 Future Improvements

* 🔁 Reinforcement Learning (Q-Learning / PPO)
* 📊 Learning curve visualization
* 🤖 Personalized curriculum generation
* 🧾 Explainable AI (action reasoning)

---

## 🏁 Conclusion

This project demonstrates an effective **adaptive learning agent** that:

* Maximizes learning efficiency
* Adapts dynamically to student behavior
* Achieves near-optimal performance across varying difficulty levels


---


