from luxai_s2.state import ObservationStateDict
import numpy as np


class BuildSomething:
    """Base class to build something"""

    def __init__(
        self,
        obs: ObservationStateDict,
        agent: str
            ) -> None:
        self.obs = obs
        self.agent = agent

    def build_multiple_heavy(self, actions: dict) -> dict:
        factories = self.obs["factories"][self.agent]
        for unit_id in factories:
            factory = factories[unit_id]
            if factory["cargo"]["metal"] >= 100 and factory["power"] >= 500:
                actions[unit_id] = 1
        return actions

    def build_multiple_light(self, actions: dict) -> dict:
        factories = self.obs["factories"][self.agent]
        units = self.obs["units"][self.agent]
        units_positions = [units[unit_id]['pos'] for unit_id in units]
        for unit_id in factories:
            factory = factories[unit_id]
            compare = [np.array_equal(factory['pos'], unit_pos) for unit_pos in units_positions]

            if not any(compare) \
                    and factory["cargo"]["metal"] >= 10 \
                    and factory["power"] >= 50:
                actions[unit_id] = 0
        return actions
