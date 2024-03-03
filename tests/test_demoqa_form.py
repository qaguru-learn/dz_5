import datetime
from demoqa_tests.models.appmanager import app
from demoqa_tests.data.users import User, Genders, Hobbies, SimpleUser


def test_registration_page():
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
    (
        app
        .left_panel
        .open_registration_form()
        .register(yuriy)
        .should_registered_with(yuriy)
    )


def test_simple_registration_page():
    yuriy = SimpleUser(
        fullname='Yuriy Choba',
        email='yuriy.choba@ex.com',
        current_address='NCR, Delhi, Lenin street, 28',
        permanent_address='NCR, Delhi, Lenin street, 28',
    )

    (
        app
        .left_panel
        .open_simple_registration_form()
        .register(yuriy)
        .should_registered_with(yuriy)
    )
