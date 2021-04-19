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
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
# **********************************Third test to check if multiple users can be saved into the contact list...****************************************************
    def test_save_multiple_users(self):
        '''
            test_save_multiple_users to check if we can save multiple users
            objects to our user_list
        '''
        self.new_user.save_user()
        test_user=User("Loui","123")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
# **********************************Fourth test to delete users from an user list...****************************************************
    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_user.save_user()
            test_user = User("Loui","123") # new contact
            test_user.save_user()

            self.new_user.delete_contact()# Deleting a contact object
            self.assertEqual(len(User.user_list),1)

# **********************************Fifth test to find a user from user list...****************************************************
    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Loui","123") # new contact
        test_user.save_user()

        found_user = User.find_by_username("Loui")

        self.assertEqual(found_user.username,test_user.username)
#  **********************************Sixth test to check if a usernmae that is been passed actually exists in the list....****************************************************
    


if __name__ == '__main__':
    unittest.main()