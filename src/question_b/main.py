from question_b import reverse_string, test_reverse_string


while True:
    user_input = input("Enter a string or type 'quit' to leave: ")

    if user_input == "quit":
        break

    reverse_value = reverse_string(user_input)
    print(f"The reverse of '{user_input}' is  '{reverse_value}'")