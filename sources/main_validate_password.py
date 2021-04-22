# developer-defined modules
from sources.validate_password import ValidatePassword 


def is_password_valid(password:str)->bool:
    # Given
    password_validator = ValidatePassword(password)
    # Then
    assert password_validator.is_password_provided(), f'password="{password}" is invalid!'
    # And
    max_length = 26
    failure_message = f'password="{password}" is above max_length="{max_length}". and thus is invalid!'
    assert password_validator.is_password_length_below_max_length(max_length), failure_message
    # And
    failure_message = f'password="{password}" does not contain an upper case character(s), and thus is invalid!'
    assert password_validator.is_password_including_upper_cases(), failure_message
    # And
    failure_message = f'password="{password}" does not contain a lowwer case character(s), and thus is invalid!'
    assert password_validator.is_password_including_lowwer_cases(), failure_message
    # And
    failure_message = f'password="{password}" does not contain a number(s), and thus is invalid!'
    assert password_validator.is_password_including_numbers(), failure_message
    # And
    failure_message = f'password="{password}" does not contain special character(s), and thus is invalid!'
    assert password_validator.is_password_including_special_characters(), failure_message
    # And
    return True
