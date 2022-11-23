def flights(*args):
    current_key = None
    flights_dict = {}
    for el in args:
        if el == "Finish":
            break
        is_string = isinstance(el, str)
        is_number = isinstance(el, int)
        if is_string:
            if el in flights_dict:
                flights_dict[el] += 0
                current_key = el
            else:
                flights_dict[el] = 0
                current_key = el
        elif is_number:
           flights_dict[current_key] += el
    return flights_dict


#print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

#print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
