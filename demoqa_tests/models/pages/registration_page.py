from selene import browser, have, be, by
from demoqa_tests.models import resources


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_firstname(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_lastname(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def gender_make_choice(self):
        browser.element("#gender-radio-1").double_click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_birthday(self, day: int, month: str, year: int):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click().element(by.text(f'{year}')).click()
        browser.element(".react-datepicker__month-select").click().element(by.text(f'{month}')).click()
        browser.element(f".react-datepicker__week .react-datepicker__day--0{day}").click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def hobbies_make_choice(self, value):
        choice = ['Sports', 'Reading', 'Music'].index(value) + 1
        browser.element(f'[for=hobbies-checkbox-{choice}]').click()
        return self

    def upload_picture(self):
        browser.element('#uploadPicture').type(resources.path('rick.jpg'))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        browser.element('#react-select-3-input').should(be.blank).type(value).press_enter()
        return self

    def fill_city(self, value):
        browser.element('#react-select-4-input').should(be.blank).type(value).press_enter()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def form_should_be_completed(self):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        return self

    def should_registered_with(self,
                               fullname, email, gender, phone_number, birthday,
                               subject, hobby, photo, address, state_city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            fullname,
            email,
            gender,
            phone_number,
            birthday,
            subject,
            hobby,
            photo,
            address,
            state_city
        ))
        return self
