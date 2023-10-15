#write functions here, don't add input('') statements here!
def test_config():
    return True

def use_local_variable(num):
    num = 10
    print(f"The num in the function is {num}")
          

def test_use_local_variable():

    num = 100
    
    print(f"Before calling the function the number is {num}")
    
    use_local_variable(num)
    
    assert num == 100, "The value of num in the test case is not 100"
    return True



