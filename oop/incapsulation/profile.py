class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError(f'The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_lengthy_enough = len(value)
        is_upper_case_presented = [char for char in value if char.isupper()]
        is_there_digit = [char for char in value if char.isdigit()]

        if not is_upper_case_presented or not is_there_digit or not is_lengthy_enough:
            raise ValueError(f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

#profile_with_invalid_username = Profile('Too_long_username', 'Any')
#profile_with_invalid_password = Profile('My_username', 'My-password')
