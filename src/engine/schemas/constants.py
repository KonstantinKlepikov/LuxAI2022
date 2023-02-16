from enum import Enum, auto
from dataclasses import dataclass


class GlobalSpace(Enum):
    step = auto()
    remaining_time = auto()
    reward = auto()


class BoardSpace(Enum):
    factories_per_team = auto()
    lichen = auto()
    lichen_strains = auto()
    rubble = auto()


class PlayerSpace(Enum):
    bid = auto()
    faction = auto()
    factories_to_place = auto()
    factory_strains = auto()
    metal = auto()
    place_first = auto()
    team_id = auto()
    water = auto()


class FactorieSpace(Enum):
    ice = auto()
    metal = auto()
    ore = auto()
    water = auto()
    pos: auto()
    power = auto()
    strain_id = auto()
    team_id = auto()
    unit_id = auto()


class UnitSpace(Enum):
    action_queue = auto()
    ice = auto()
    metal = auto()
    ore = auto()
    water = auto()
    pos: auto()
    power = auto()
    team_id = auto()
    unit_id = auto()
    unit_type = auto()


@dataclass(frozen=True)
class GameConstants:
    """Game constants

        actTimeout: Maximum runtime (seconds) to obtain an action from an agent. Minimum - 0.
        episodeSteps: Maximum number of steps the environment can run. Total is this number -1.
                      One complete game is 1000 + N * 2 + 1 steps where N is number
                      of factories each player is given. Minimum - 2.
        max_episode_length: Max game steps the environment can run, not including
                            the early phase of the game. Minimum - 2.
        runTimeout: Maximum runtime (seconds) of an episode (not necessarily DONE). Minimum - 0.

    """
    actTimeout: int = 3
    BIDDING_SYSTEM: bool = True
    CYCLE_LENGTH: int = 50
    DAY_LENGTH: int = 30
    FACTORY_CHARGE: int = 50
    FACTORY_PROCESSING_RATE_METAL: int = 50
    FACTORY_PROCESSING_RATE_WATER: int = 100
    FACTORY_RUBBLE_AFTER_DESTRUCTION: int = 50
    FACTORY_WATER_CONSUMPTION: int = 1
    ICE_WATER_RATIO: int = 4
    INIT_POWER_PER_FACTORY: int = 1000
    INIT_WATER_METAL_PER_FACTORY: int = 150
    LICHEN_GAINED_WITH_WATER: int = 1
    LICHEN_LOST_WITHOUT_WATER: int = 1
    LICHEN_WATERING_COST_FACTOR: int = 10
    MAX_FACTORIES: int = 5
    MAX_LICHEN_PER_TILE: int = 100
    MAX_RUBBLE: int = 100
    MIN_FACTORIES: int = 2
    MIN_LICHEN_TO_SPREAD: int = 20
    ORE_METAL_RATIO: int = 5
    POWER_LOSS_FACTOR: float = 0.5
    POWER_PER_CONNECTED_LICHEN_TILE: int = 1
    UNIT_ACTION_QUEUE_SIZE: int = 20
    map_size: int = 48
    max_episode_length: int = 1000
    max_transfer_amount: int = 3000
    episodeSteps: int = 1020
    max_episode_length: int = 1000
    runTimeout: int = 9600


@dataclass(frozen=True)
class RobotConstants:
    ACTION_QUEUE_POWER_COST: int
    BATTERY_CAPACITY: int
    CARGO_SPACE: int
    CHARGE: int
    DIG_COST: int
    DIG_LICHEN_REMOVED: int
    DIG_RESOURCE_GAIN: int
    DIG_RUBBLE_REMOVED: int
    INIT_POWER: int
    METAL_COST: int
    MOVE_COST: int
    POWER_COST: int
    RUBBLE_AFTER_DESTRUCTION: int
    RUBBLE_MOVEMENT_COST: float
    SELF_DESTRUCT_COST: int


GCONST = GameConstants()
HROBOT = RobotConstants(**{
    'ACTION_QUEUE_POWER_COST': 10,
    'BATTERY_CAPACITY': 3000,
    'CARGO_SPACE': 1000,
    'CHARGE': 10,
    'DIG_COST': 60,
    'DIG_LICHEN_REMOVED': 100,
    'DIG_RESOURCE_GAIN': 20,
    'DIG_RUBBLE_REMOVED': 20,
    'INIT_POWER': 500,
    'METAL_COST': 100,
    'MOVE_COST': 20,
    'POWER_COST': 500,
    'RUBBLE_AFTER_DESTRUCTION': 10,
    'RUBBLE_MOVEMENT_COST': 1,
    'SELF_DESTRUCT_COST': 100
        })
LROBOT = RobotConstants(**{
    'ACTION_QUEUE_POWER_COST': 1,
    'BATTERY_CAPACITY': 150,
    'CARGO_SPACE': 100,
    'CHARGE': 1,
    'DIG_COST': 5,
    'DIG_LICHEN_REMOVED': 10,
    'DIG_RESOURCE_GAIN': 2,
    'DIG_RUBBLE_REMOVED': 2,
    'INIT_POWER': 50,
    'METAL_COST': 10,
    'MOVE_COST': 1,
    'POWER_COST': 50,
    'RUBBLE_AFTER_DESTRUCTION': 1,
    'RUBBLE_MOVEMENT_COST': 0.05,
    'SELF_DESTRUCT_COST': 10
        })


if __name__ == '__main__':

    print(LROBOT.RUBBLE_MOVEMENT_COST)
    print(HROBOT.DIG_COST)
    print(GCONST.actTimeout)
