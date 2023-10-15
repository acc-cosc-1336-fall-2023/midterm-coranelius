#write function tests here, don't add input('') statements here!
import unittest


#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())



from src.question_c.question_c import get_random_number, test_get_random_number

class TestQuestionC(unittest.TestCase):

    def test_get_random_number(self):
      random_number = get_random_number()
      assert 1 <= random_number <= 5, f"{random_number} is not 1-5"


from src.question_b.question_b import reverse_string

class TestQuestionB(unittest.TestCase):
    
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("hello"), "olleh")






from src.question_d.question_d import test_get_fahrenheit, get_fahrenheit

class TestQuestionD(unittest.TestCase):

  def test_get_fahrenheit(self):
      test_cases = [(0, 32), (5, 41), (10, 50)]

      for celsius, expected_fahrenheit in test_cases:
          result = get_fahrenheit(celsius)
          self.assertEqual(result,expected_fahrenheit, f"Should be {expected_fahrenheit}, not {result}")

