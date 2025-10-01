from enum import Enum


class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"


class Environment(str, Enum):
    DEV = "DEV"
    TEST = "TEST"
    STAGING = "STAGING"
    PROD = "PROD"
