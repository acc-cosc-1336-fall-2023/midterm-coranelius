from question_a import use_local_variable

num = 20

print(f"In num in main is {num}")

use_local_variable(num)

print(f"The value of num in the main program is {num} after calling the function")