# developer-defined module(s)
from sources.validate_password import ValidatePassword

# 3rd-party module(s)
import pytest
from pytest import raises as raised_error


# common flow
def then_assert(given_utility, when_expected_error, then_failed_assertion_message)->None:
    with raised_error(Exception) as actual_error:
        assert given_utility(), then_failed_assertion_message
    # and
    failed_assertion_message = f'''expected_error="{when_expected_error}";
    is not equal to actual_error="{actual_error}"!'''
    # and
    assert actual_error.type is when_expected_error, failed_assertion_message
    pass

# utilities under test
@pytest.mark.parametrize('password', [None, '', ' '])
def test_is_password_provided(password:str)->None:
    then_assert(
        given_utility=ValidatePassword(password).is_password_provided,
        when_expected_error=AssertionError,
        then_failed_assertion_message=f'password="{password}", was provided!'
    )
    pass


@pytest.mark.parametrize('password', [None,'test-password'])
def test_is_password_length_below_max_length(password:str)->None:
    then_assert(
        given_utility=ValidatePassword(password).is_password_length_below_max_length,
        when_expected_error=TypeError if password is None else AssertionError,
        then_failed_assertion_message=f'password="{password}", is above max length!'
    )
    pass


@pytest.mark.parametrize('password', [None, '', ' ', 'test-password'])
def test_is_password_including_upper_cases(password:str)->None:
    then_assert(
        given_utility=ValidatePassword(password).is_password_including_upper_cases,
        when_expected_error=TypeError if password is None else AssertionError,
        then_failed_assertion_message=f'password="{password}", include an upper case!'
    )
    pass


@pytest.mark.parametrize('password', [None, '', ' ', 'TEST-PASSWORD'])
def test_is_password_including_lowwer_cases(password:str)->None:
    then_assert(
        given_utility=ValidatePassword(password).is_password_including_lowwer_cases,
        when_expected_error=TypeError if password is None else AssertionError,
        then_failed_assertion_message=f'password="{password}", include a lowwer case!'
    )
    pass


@pytest.mark.parametrize('password', [None,'',' '])
def test_is_password_including_numbers(password:str)->None:
    then_assert(
        given_utility=ValidatePassword(password).is_password_including_numbers,
        when_expected_error=TypeError if password is None else AssertionError,
        then_failed_assertion_message=f'password="{password}", include a number!'
    )
    pass


@pytest.mark.parametrize('password', [None, '', ' '])
def test_is_password_including_special_characters(password:str)->None:
    then_assert(
        given_utility=ValidatePassword(password).is_password_including_special_characters,
        when_expected_error=TypeError if password is None else AssertionError,
        then_failed_assertion_message=f'password="{password}", include a special character!'
    )
    pass


