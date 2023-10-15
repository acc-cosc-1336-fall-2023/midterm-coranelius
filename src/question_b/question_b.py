#write functions here, don't add input('') statements here!

def reverse_string(string1):
    reverse_str = ""
    index = len(string1) - 1

    while index >= 0:
        reverse_str += string1[index]
        index -= 1

    return reverse_str


def test_reverse_string():
    assert reverse_string("hello world") == "dlrow olleh", "Test Case 1 Failed"
    assert reverse_string("hello") == "olleh", "Test Case 2 Failed"
    print("All tests past")

test_reverse_string()