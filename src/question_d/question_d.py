#write functions here, don't add input('') statements here!


def get_fahrenheit(celsius):
    return (9/5) * celsius + 32

print(get_fahrenheit(100))

def test_get_fahrenheit():
    test_cases = [(0, 32), (5, 41), (10, 50)]

    for celsius, expected_fahrenheit in test_cases:
        result = get_fahrenheit(celsius)
        assert result == expected_fahrenheit, f"Should be {expected_fahrenheit}, not {result}"

