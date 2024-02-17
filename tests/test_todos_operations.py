from selene import browser, have, be, by
import os


def test_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Yuriy')
    browser.element('#lastName').should(be.blank).type('Choba')
    browser.element('#userEmail').should(be.blank).type('yuriy.choba@ex.com')
    browser.element("#gender-radio-1").double_click()
    browser.element('#userNumber').should(be.blank).type('8987654321')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").click().element(by.text('1990')).click()
    browser.element(".react-datepicker__month-select").click().element(by.text('March')).click()
    browser.element(".react-datepicker__week .react-datepicker__day--015").click()
    browser.element('#subjectsInput').type('Chemistry').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').type(os.path.abspath('pictures/rick.jpeg'))
    browser.element('#currentAddress').should(be.blank).type('Lenin street, 28')
    browser.element('#react-select-3-input').should(be.blank).type('NCR').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    # проверяем что форма заполнилась
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))

    # проверяем что данные внесены корректно
    browser.element('.table').should(have.text('Yuriy Choba'))
    browser.element('.table').should(have.text('yuriy.choba@ex.com'))
    browser.element('.table').should(have.text('Male'))
    browser.element('.table').should(have.text('8987654321'))
    browser.element('.table').should(have.text('15 March,1990'))
    browser.element('.table').should(have.text('Chemistry'))
    browser.element('.table').should(have.text('Reading'))
    browser.element('.table').should(have.text('rick.jpeg'))
    browser.element('.table').should(have.text('Lenin street, 28'))
    browser.element('.table').should(have.text('NCR Delhi'))

    print(10)