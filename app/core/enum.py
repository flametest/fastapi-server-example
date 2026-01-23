from enum import Enum


class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"


class Environment(str, Enum):
    LOCAL = "LOCAL"
    DEV = "DEV"
    TEST = "TEST"
    STAGING = "STAGING"
    PROD = "PROD"
