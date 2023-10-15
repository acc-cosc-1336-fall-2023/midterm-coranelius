#add import
from question_d  import get_fahrenheit, test_get_fahrenheit

def display_temperature_table():
    print("Celcius    Farenheit")
    print("======================")

    for celsius in range(21):
        fahrenheit = get_fahrenheit(celsius)
        print(   f"{celsius}           {fahrenheit}")

test_get_fahrenheit()

display_temperature_table()