from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class Genders(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class Hobbies(Enum):
    READING = 'Reading'
    MUSIC = 'Music'
    SPORTS = 'Sports'


@dataclass
class User:
    fullname: str
    email: str
    gender: Genders
    phone_number: str
    birthday: datetime.date
    subject: str
    hobbie: Enum
    photo: str
    address: str
    state_city: str


@dataclass
class SimpleUser:
    fullname: str
    email: str
    current_address: str
    permanent_address: str
