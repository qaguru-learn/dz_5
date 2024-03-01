from tests.pages.registration_page import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    registration_page.open()
    (registration_page
        .fill_firstname('Yuriy')
        .fill_lastname('Choba')
        .fill_email('yuriy.choba@ex.com')
        .gender_make_choice()
        .fill_phonenumber('8987654321')
        .fill_birthday(day=15, month='March', year=1990)
        .fill_subjects('Chemistry')
        .hobbies_make_choice('Reading')
        .upload_picture()
        .fill_address('Lenin street, 28')
        .fill_state('NCR')
        .fill_city('Delhi')
        .submit()
     )

    (registration_page
        .form_should_be_completed()
        .should_registered_with(
            'Yuriy Choba',
            'yuriy.choba@ex.com',
            'Male',
            '8987654321',
            '15 March,1990',
            'Chemistry',
            'Reading',
            'rick.jpeg',
            'Lenin street, 28',
            'NCR Delhi',
        )
    )
