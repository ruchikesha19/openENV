from schemas import Observation, Action, Reward


class OpenEnvWrapper:
    def __init__(self, env):
        self.env = env
        self._state = None

    def reset(self):
        obs = self.env.reset()
        self._state = obs
        return Observation(state=obs)

    def step(self, action: Action):
        obs, reward, done, info = self.env.step(action.action)
        self._state = obs

        return (
            Observation(state=obs),
            Reward(value=float(reward)),
            done,
            info,
        )

    def state(self):
        return Observation(state=self._state)