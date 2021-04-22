# 3rd-party modules
from behave import given, when, then

"""
Feature: Password Validation - source file (features/validate_password_against_valid_password.feature)
Scenario: test the password validation, has been implemented by sources/main_validate_password.py
Steps:
"""
@given("that a vaild password; is provided by the user as '{password}'")
def step_impl(context:object, password:str)->None:
    context.password = password
    pass


@when("the implemented functionality provided by the '{function}'; is given the user password")
def step_impl(context:object, function:str)->None:
    from sources import main_validate_password
    assertion_fail_message = f"function='{function}' was not implemented!"
    assert hasattr(main_validate_password, function), assertion_fail_message
    context.functionality = getattr(main_validate_password, function)
    pass


@then("test the assertion of the functionality is successful.")
def step_impl(context:object)->None:
    assertion_fail_message = f'''
    the test assertion on the {context.functionality} was unsuccessful!'''
    assert context.functionality(context.password), assertion_fail_message
    pass


