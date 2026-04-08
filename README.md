# Adaptive Learning Agent (OpenEnv)

An **Agentic AI system using Reinforcement Learning** that dynamically personalizes learning paths for students based on their performance, engagement, and behavior.

---

#  Problem Statement

Traditional learning systems follow a **static, one-size-fits-all approach**, leading to:

* Low engagement 
* Inefficient learning 
* Lack of personalization 

---

#  Solution

We built an **Adaptive Curriculum Environment** where an AI agent:

* Observes student learning state
* Decides the next best action
* Learns from rewards and feedback
* Optimizes long-term learning outcomes

---

# System Architecture

```text
Student State → Agent → Action → Environment → Reward → Next State
```

###  Components

* **Environment (`env/curriculum_env.py`)**

  * Simulates student learning behavior

* **Agent (`agents/baseline_agent.py`)**

  * Selects optimal learning actions

* **Grader (`grader/evaluator.py`)**

  * Evaluates agent performance across difficulty levels

* **Inference (`inference.py`)**

  * Runs the agent in the environment and logs results

* **Schemas (`schemas.py`)**

  * Defines structured observation, action, and reward models

---

#  Action Space

The agent can perform:

*  show_video
*  give_quiz
*  interactive_exercise
*  revision_notes
* skip_topic
*  take_break

---

# Observation Space

The agent observes:

* concept_mastery (list of floats)
* quiz_accuracy
* time_spent
* attempt_count
* fatigue
* engagement

---

#  Tasks & Evaluation

We simulate 3 types of learners:

| Difficulty | Description     |
| ---------- | --------------- |
| Easy       | Fast learner    |
| Medium     | Average learner |
| Hard       | Slow learner    |

###  Evaluation Metrics

```text
score = 0.5 * learning_gain
      + 0.3 * completion_rate
      + 0.2 * efficiency
```

---

#  Sample Output (Inference)

```text
[START] task=adaptive_learning env=openenv model=baseline

[STEP] step=1 action=show_video reward=5.00 done=false error=null
[STEP] step=2 action=interactive_exercise reward=6.00 done=false error=null
[STEP] step=3 action=give_quiz reward=12.00 done=false error=null

...

[END] success=true steps=12 rewards=5.00,6.00,12.00,...
```

---

#  Project Structure

```bash
.
├── env/
│   └── curriculum_env.py
├── agents/
│   └── baseline_agent.py
├── grader/
│   └── evaluator.py
├── config/
├── inference.py
├── app.py
├── openenv.yaml
├── requirements.txt
├── Dockerfile
├── schemas.py
├── README.md
```

---

#  How to Run

### 1️ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2️ Run inference

```bash
python inference.py
```

---

### 3️ Run evaluation

```bash
python grader/evaluator.py
```

---

#  Docker Setup

### Build

```bash
docker build -t adaptive-agent .
```

### Run

```bash
docker run adaptive-agent
```

---

#  OpenEnv Compliance

* ✔ Implements `step()`, `reset()`, `state()`
* ✔ Structured schemas using `schemas.py`
* ✔ `openenv.yaml` configured
* ✔ Compatible with OpenEnv validation

---

#  Results

* Agent adapts learning strategy dynamically
* Handles multiple student types
* Demonstrates real-world decision-making

---

# Team Contributions

* **P A Mannaswini**
  Designed environment, reward system, and student simulation

* **Ruchikesha**
  Built adaptive agent and evaluation logic

* **Sakthi Rishikesh**
  Implemented OpenEnv compliance, inference pipeline, and Docker setup

---

#  Key Highlights

* Agentic AI using Reinforcement Learning
* Real-world EdTech application
* Adaptive decision-making system
* OpenEnv-compatible environment
* Fully containerized (Docker-ready)

---

#  Future Improvements

* Add interactive UI (Gradio)
* Deploy on Hugging Face Spaces
* Integrate real student datasets
* Train advanced RL models

---

# Tech Stack

* Python
* NumPy
* OpenEnv
* Pydantic
* Docker

---

# 🏁 Conclusion

This project demonstrates how **AI agents can autonomously optimize learning experiences**, making education more personalized, scalable, and efficient.

---

