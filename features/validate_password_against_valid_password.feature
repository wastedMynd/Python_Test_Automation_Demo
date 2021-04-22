Feature: Password Validation
  Scenario: test the password validation, has been implemented by sources/main_validate_password.py
    Given that a vaild password; is provided by the user as 'T3stP@55w0rD' 
    When the implemented functionality provided by the 'is_password_valid'; is given the user password 
    Then test the assertion of the functionality is successful.
