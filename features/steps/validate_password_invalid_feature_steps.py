# 3rd-party modules
from behave import given, when, then

"""
Feature: Password Validation - source file (features/validate_password_against_invalid_password.feature)
Scenario: test the password validation, has been implemented by sources/main_validate_password.py
Steps:
"""
@given("that an invaild <password>; is provided by the user")
def step_impl(context:object)->None:
    for row in context.table:
        context.password = row['password']
    pass


@then("test the assertion of the functionality is unsuccessful.")
def step_impl(context:object)->None:
    try:
        context.functionality(context.password)
    except Exception as actual_error:
        assertion_fail_message = f'''
        the test assertion on the {context.functionality} was successful!'''
        assert actual_error is not AssertionError, assertion_fail_message
    pass


