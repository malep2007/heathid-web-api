import re
from functools import wraps

from graphql import GraphQLError

from .validations import ValidateUser


class UpdateUser:

    # This class contains methods to help with updating of user details

    def update_user(self, instance, **kwargs):
        password = None
        for key, value in kwargs.items():
            if key == 'password':
                password = value[0].new_password

            if key is not None:
                setattr(instance, key, value)
        instance.set_password(password) if password!=None else None
        instance.save()

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if kwargs.get('mobile_number') is not None:
                mobile_number = kwargs.get('mobile_number')
                ValidateUser().validate_mobileNumber(mobile_number)
            if kwargs.get('password') is not None:
                password_input = kwargs.get('password')
                new_password = password_input[0]['new_password']
                ValidateUser().validate_password(new_password)            
            return func(*args, **kwargs)
        return wrapper


user_update_instance = UpdateUser()
