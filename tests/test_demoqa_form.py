import datetime
from demoqa_tests.data.users import User, Genders, Hobbies
from demoqa_tests.models.pages.registration_page import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    yuriy = User(
        fullname='Yuriy Choba',
        email='yuriy.choba@ex.com',
        gender=Genders.MALE.value,
        phone_number='8987654321',
        birthday=datetime.date(1990, 3, 15),
        subject='Maths',
        hobby=Hobbies.READING.value,
        photo='rick.jpeg',
        address='Lenin street, 28',
        state_city='NCR Delhi',
    )

    registration_page.open()
    registration_page.register(yuriy)
    registration_page.should_registered_with(yuriy)
