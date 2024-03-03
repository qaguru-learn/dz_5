from selene import browser, have, be
from demoqa_tests.data.users import SimpleUser


class SimpleRegistrationPage:

    def open(self):
        browser.open('/text-box')
        return self

    def fill_fullname(self, cur_user: SimpleUser):
        browser.element('#userName').should(be.blank).type(cur_user.fullname)
        return self

    def fill_email(self, cur_user: SimpleUser):
        browser.element('#userEmail').should(be.blank).type(cur_user.email)
        return self

    def fill_current_address(self, cur_user: SimpleUser):
        browser.element('#currentAddress').should(be.blank).type(cur_user.current_address)
        return self

    def fill_permanent_address(self, cur_user: SimpleUser):
        browser.element('#permanentAddress').should(be.blank).type(cur_user.permanent_address)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def register(self, cur_user: SimpleUser):
        (self
         .fill_fullname(cur_user)
         .fill_email(cur_user)
         .fill_current_address(cur_user)
         .fill_permanent_address(cur_user)
         .submit()
         )
        return self

    def should_registered_with(self, cur_user: SimpleUser):
        browser.element('#name').matching(have.text(cur_user.fullname))
        browser.element('#email').matching(have.text(cur_user.email))
        browser.element('#currentAddress').matching(have.text(cur_user.current_address))
        browser.element('#permanentAddress').matching(have.text(cur_user.permanent_address))
        return self
