from enum import Enum, unique


@unique
class ProfileType(Enum):
    BASIC = 'BASIC'
    PREMIUM = 'PREMIUM'
