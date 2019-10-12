import unittest

def is_prime(number):
    """Return True if *number* is prime."""
    if number in (0, 1):
        return False
    for element in range(2,number):
        if number % element == 0:
               return False
    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""
    
    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))
     
    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg='Four is not prime!')
        
    #test edge class
    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))
        

if __name__ == '__main__':
    unittest.main()
