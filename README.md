---
title: OpenEnv - Adaptive Learning Environment
emoji: 🚀
colorFrom: blue
colorTo: indigo
sdk: docker
sdk_version: "0.104.1"
python_version: "3.10.13"
app_file: app.py
pinned: false
---

# OpenEnv - Adaptive Learning Environment

An **Agentic AI system using Reinforcement Learning** that dynamically personalizes learning paths for students based on their performance, engagement, and behavior.

## 🚀 Features

- **Adaptive Learning**: Dynamically adjusts curriculum based on student performance
- **Multi-modal Actions**: Video lessons, quizzes, interactive exercises, and more
- **Real-time Feedback**: Immediate rewards and progress tracking
- **OpenEnv Compliant**: Fully compatible with OpenEnv specification

## 📋 Requirements

- Python 3.10+
- FastAPI
- OpenEnv Core
- NumPy
- Pydantic

## 🛠️ Installation

### Local Development
```bash
git clone https://github.com/ruchikesha19/openENV.git
cd openENV
pip install -r requirements.txt
```

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Generate lock file (optional)
uv lock

# Validate OpenEnv compliance
openenv validate
```

## 🏃‍♂️ Running

### Local Server
```bash
python app.py
```
The server will start on `http://localhost:7860`

### Inference Script
```bash
# Set environment variables
export API_BASE_URL="your-api-endpoint"
export MODEL_NAME="your-model-name"
export HF_TOKEN="your-hf-token"

# Run inference
python inference.py
```

## 📊 API Endpoints

### Health Check
```
GET /
```

### Reset Environment
```
POST /reset
```

### Take Action
```
POST /step
Content-Type: application/json

{
  "action": "interactive_exercise"
}
```

## 🧪 Testing

### Run Validation
```bash
openenv validate
```

### Test Inference
```bash
python inference.py
```

Expected output format:
```
[START] task=adaptive_learning env=openenv model=baseline
[STEP] step=0 action=show_video reward=2.50 done=false error=null
[END] success=true steps=20 score=0.155 rewards=2.50,4.00,4.00,...
```

## 📁 Project Structure

```
openENV/
├── app.py                 # FastAPI server for HF Spaces
├── inference.py           # Inference script for evaluation
├── openenv.yaml          # OpenEnv specification
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project metadata
├── uv.lock             # Dependency lock file
├── Dockerfile           # Docker configuration
├── env/                # Environment implementation
│   ├── curriculum_env.py
│   ├── openenv_wrapper.py
│   └── models.py
├── agents/             # Agent implementations
├── grader/            # Evaluation graders
└── schemas.py         # Pydantic models
```

## 🐳 Docker Deployment

The project includes a Dockerfile for containerized deployment:

```bash
docker build -t openenv .
docker run -p 7860:7860 openenv
```

## 📝 Environment Variables

| Variable | Description | Default |
|----------|-------------|----------|
| `API_BASE_URL` | LLM API endpoint | - |
| `MODEL_NAME` | Model identifier | `baseline` |
| `HF_TOKEN` | Hugging Face token | - |
| `LOCAL_IMAGE_NAME` | Docker image name | - |

## 🎯 Actions Available

- `show_video` - Display educational video content
- `interactive_exercise` - Interactive learning activities
- `give_quiz` - Assessment questions
- `revision_notes` - Study materials review
- `skip_topic` - Move to next topic
- `take_break` - Rest period

## 📈 Reward System

- **Positive rewards**: Learning progress, engagement
- **Range**: -10.0 to 10.0 per step
- **Success threshold**: Score ≥ 0.1

## 🔧 Development

### Adding New Tasks
1. Create environment in `env/`
2. Add grader in `grader/`
3. Update `openenv.yaml`
4. Add task to `inference.py`

### Running Tests
```bash
# Test individual components
python -m pytest tests/

# Validate OpenEnv compliance
openenv validate
```

## 📄 License

MIT License - see LICENSE file for details

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make your changes
4. Add tests if applicable
5. Submit pull request

## 📞 Support

For issues and questions:
- GitHub Issues: [ruchikesha19/openENV](https://github.com/ruchikesha19/openENV/issues)
- Documentation: See `docs/` folder

---

**Built with ❤️ for the OpenEnv Challenge**

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

