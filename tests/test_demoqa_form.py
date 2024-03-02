import datetime

from tests.data.users import User, Genders, Hobbies, SimpleUser
from tests.pages.registration_page import RegistrationPage
from tests.pages.simple_registration_page import SimpleRegistrationPage


def test_registration_page():
    registration_page = RegistrationPage()
    yuriy = User(
        fullname='Yuriy Choba',
        email='yuriy.choba@ex.com',
        gender=Genders.MALE.value,
        phone_number='8987654321',
        birthday=datetime.date(1990, 3, 15),
        subject='Maths',
        hobbie=Hobbies.READING.value,
        photo='pictures/rick.jpeg',
        address='Lenin street, 28',
        state_city='NCR Delhi',
    )

    registration_page.open()
    registration_page.register(yuriy)
    registration_page.should_registered_with(yuriy)


def test_simple_registration_page():
    simple_registration_page = SimpleRegistrationPage()
    yuriy = SimpleUser(
        fullname='Yuriy Choba',
        email='yuriy.choba@ex.com',
        current_address='NCR, Delhi, Lenin street, 28',
        permanent_address='NCR, Delhi, Lenin street, 28',
    )

    simple_registration_page.open()
    simple_registration_page.register(yuriy)
    simple_registration_page.should_registered_with(yuriy)
