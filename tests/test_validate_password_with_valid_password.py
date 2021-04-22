# developer-defined module(s)
from sources.validate_password import ValidatePassword

# 3rd-party module(s)
import pytest


@pytest.mark.parametrize('password', ['T3stP@55w0rd'])
def test_is_password_provided(password:str)->None:
    # given
    password_validator = ValidatePassword(password)
    # then
    assert password_validator.is_password_provided(), 'password, was not provided!'
    pass


@pytest.mark.parametrize('password', ['T3stP@55w0rd'])
def test_is_password_length_below_max_length(password:str)->None:
    # given
    password_validator = ValidatePassword(password)
    # then
    assert password_validator.is_password_length_below_max_length(26), 'password, is above max length!'
    pass


@pytest.mark.parametrize('password', ['T3stP@55w0rd'])
def test_is_password_including_upper_cases(password:str)->None:
    # given
    password_validator = ValidatePassword(password)
    # then
    assert password_validator.is_password_including_upper_cases(), 'password, does not include an upper case!'
    pass


@pytest.mark.parametrize('password', ['T3stP@55w0rd'])
def test_is_password_including_lowwer_cases(password:str)->None:
    # given
    password_validator = ValidatePassword(password)
    # then
    assert password_validator.is_password_including_lowwer_cases(), 'password, does not include a lowwer case!'
    pass


@pytest.mark.parametrize('password', ['T3stP@55w0rd'])
def test_is_password_including_numbers(password:str)->None:
    # given
    password_validator = ValidatePassword(password)
    # then
    assert password_validator.is_password_including_numbers(), 'password, does not include a number!'
    pass


@pytest.mark.parametrize('password', ['T3stP@55w0rd'])
def test_is_password_including_special_characters(password:str)->None:
    # given
    password_validator = ValidatePassword(password)
    # then
    assert password_validator.is_password_including_special_characters(), 'password, does not include a special character!'
    pass
