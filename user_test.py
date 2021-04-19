import unittest 
from user import User

class TestUser(unittest.TestCase):

    """
      Test class that defines test cases for the user class behaviours.
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Louise","0714871787") # create user object
    def tearDown(self):
        '''
            tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
 
 # ********First test to check if the user details are being instantiated properly****************************************************
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Louise")
        self.assertEqual(self.new_user.password,"0714871787")

# **********************************Second test to check if the USer details has been added to the user list...****************************************************
    
# **********************************Third test to check if multiple users can be saved into the contact list...****************************************************
    
# **********************************Fourth test to delete users from an user list...****************************************************
    

# **********************************Fifth test to find a user from user list...****************************************************
    
#  **********************************Sixth test to check if a usernmae that is been passed actually exists in the list....****************************************************
    


if __name__ == '__main__':
    unittest.main()