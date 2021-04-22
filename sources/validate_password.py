# built-in modules
import re


class ValidatePassword(object):
    def __init__(self, password:str)->None:
        self.password:str = password
        pass

    def is_password_provided(self)->bool:
        return self.password and not self.password.isspace()

    def get_actual_length_of_the_password(self)->int:
        return len(self.password)

    def is_password_length_below_max_length(self, max_length:int=8)->bool:
        return self.get_actual_length_of_the_password() < max_length

    def is_password_including_upper_cases(self)->bool:
        return re.match(pattern='(.*[A-Z].*)', string=self.password)
    
    def is_password_including_lowwer_cases(self)->bool:
        return re.match(pattern='(.*[a-z].*)', string=self.password)
    
    def is_password_including_numbers(self)->bool:
        return re.match(pattern='(.*[0-9].*)', string=self.password)
    
    def is_password_including_special_characters(self)->bool:
        return re.match(pattern='(.*[@,#,$,%].*$)', string=self.password)

