from selene import browser, have, be, by
import os

from tests.data.users import User, Genders, Hobbies


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_firstname(self, cur_user: User):
        browser.element('#firstName').should(be.blank).type(cur_user.fullname.split(' ')[0])
        return self

    def fill_lastname(self, cur_user: User):
        browser.element('#lastName').should(be.blank).type(cur_user.fullname.split(' ')[-1])
        return self

    def fill_email(self, cur_user: User):
        browser.element('#userEmail').should(be.blank).type(cur_user.email)
        return self

    def gender_make_choice(self, cur_user: User):
        choice = {Genders.MALE.value: 1, Genders.FEMALE.value: 2}
        browser.element(f"#gender-radio-{choice[cur_user.gender]}").double_click()
        return self

    def fill_phone_number(self, cur_user: User):
        browser.element('#userNumber').should(be.blank).type(cur_user.phone_number)
        return self

    def fill_birthday(self, cur_user: User):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click()\
            .element(by.text(f'{cur_user.birthday.year}')).click()
        browser.element(".react-datepicker__month-select").click()\
            .element(by.text(f'{cur_user.birthday.strftime("%B")}')).click()
        browser.element(f".react-datepicker__week .react-datepicker__day--0{cur_user.birthday.day}").click()
        return self

    def fill_subjects(self, cur_user: User):
        browser.element('#subjectsInput').type(cur_user.subject).press_enter()
        return self

    def hobbies_make_choice(self, cur_user: User):
        choice = {Hobbies.SPORTS.value: 1,
                  Hobbies.READING.value: 2, Hobbies.MUSIC.value: 3}
        browser.element(f'[for=hobbies-checkbox-{choice[cur_user.hobby]}]').click()
        return self

    def upload_picture(self, cur_user: User):
        browser.element('#uploadPicture').type(os.path.abspath(cur_user.photo))
        return self

    def fill_address(self, cur_user: User):
        browser.element('#currentAddress').should(be.blank).type(cur_user.address)
        return self

    def fill_state_city(self, cur_user: User):
        browser.element('#react-select-3-input').should(be.blank).type(cur_user.state_city.split(' ')[0]).press_enter()
        browser.element('#react-select-4-input').should(be.blank).type(cur_user.state_city.split(' ')[-1]).press_enter()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def form_should_be_completed(self):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        return self

    def register(self, cur_user: User):
        (self
            .fill_firstname(cur_user)
            .fill_lastname(cur_user)
            .fill_email(cur_user)
            .gender_make_choice(cur_user)
            .fill_phone_number(cur_user)
            .fill_birthday(cur_user)
            .fill_subjects(cur_user)
            .hobbies_make_choice(cur_user)
            .upload_picture(cur_user)
            .fill_address(cur_user)
            .fill_state_city(cur_user)
            .submit())
        return self

    def should_registered_with(self, cur_user: User):
        self.form_should_be_completed()
        browser.element('.table').all('td').even.should(have.exact_texts(
            cur_user.fullname,
            cur_user.email,
            cur_user.gender,
            cur_user.phone_number,
            cur_user.birthday.strftime('%d %B,%Y'),
            cur_user.subject,
            cur_user.hobby,
            cur_user.photo.split('/')[-1],
            cur_user.address,
            cur_user.state_city
        ))
        return self
