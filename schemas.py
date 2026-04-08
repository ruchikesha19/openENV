from pydantic import BaseModel
from typing import Dict, Any


class Observation(BaseModel):
    state: Dict[str, Any]


class Action(BaseModel):
    action: Any


class Reward(BaseModel):
    value: float