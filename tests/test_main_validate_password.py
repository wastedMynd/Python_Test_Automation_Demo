#------------------------------------------------------------------------------------
"""Modules"""
#------------------------------------------------------------------------------------

"""developer-defined module(s)"""
from sources.main_validate_password import is_password_valid

"""3rd-party module(s)"""
import pytest
from pytest import raises as raised_assertion

#------------------------------------------------------------------------------------
"""Test Cases"""
#------------------------------------------------------------------------------------

@pytest.mark.parametrize('password', [None, '', ' ', 'test-password',])
def test_is_password_valid_with_provided_invalid_password(password:str)->None:
    with raised_assertion(AssertionError):
        is_password_valid(password)
    pass


@pytest.mark.parametrize('password', ['T3stP@55w0rd',])
def test_is_password_valid_with_provided_valid_password(password:str)->None:
    assert is_password_valid(password), f'password="{password}", is not valid!'
    pass

#------------------------------------------------------------------------------------

