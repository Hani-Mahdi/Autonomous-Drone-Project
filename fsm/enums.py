"""
Docstring for fsm.enums

Stores names and values, acts like a dictionary for the program
"""
from enum import Enum, auto

class TopState(Enum):
    DIAGNOSTICS = auto()
    TAKEOFF = auto()
    FLIGHT = auto()
    LANDING = auto()
    EMERGENCY_LANDING = auto()

class FlightSubState(Enum):
    SEARCH = auto()
    TO_TARGET = auto()
    DROP_OFF = auto()

class DropOffSubState(Enum):
    DESCENT = auto()
    RELEASE = auto()
    ASCENT = auto()


