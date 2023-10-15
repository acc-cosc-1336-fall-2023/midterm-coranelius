#write functions here, don't add input('') statements here!

import random

def get_random_number():
    return random.randint(1,5)


def test_get_random_number():
    random_number = get_random_number()
    assert 1 <= random_number <= 5, f"{random_number} is not 1-5"



