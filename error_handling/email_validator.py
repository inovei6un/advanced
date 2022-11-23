from advanced.error_handling.custom_exceptions import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

possible_domains = {'.com', '.bg', '.org', '.net'}

command = input()

while command != "End":
    email_parts = command.split('@')
    if len(email_parts) != 2:
        raise MustContainAtSymbolError('Email must contain @')
    username, full_domain = email_parts

    if len(username) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    if f".{full_domain.split('.')[1]}" not in possible_domains:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(possible_domains)}')

    print(f"Email is valid")

    command = input()
