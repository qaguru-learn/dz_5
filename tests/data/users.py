from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class Genders(str, Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class Hobbies(str, Enum):
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
    hobby: Hobbies
    photo: str
    address: str
    state_city: str
