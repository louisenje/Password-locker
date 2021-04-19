import unittest
from credential import Credential
 
class TestUSer (unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_app=Credential("Instagram","njerimanyara","louisenje@gmail.com","password")
        
 # **********************************First test to check if the app credential details are being instantiated properly****************************************************
    def test_init(self):
        """
           test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_app.app_name,"Instagram")
        self.assertEqual(self.new_app.app_username,"njerimanyara")
        self.assertEqual(self.new_app.app_email,"louisenje@gmail.com")
        self.assertEqual(self.new_app.app_password,"password")

# **********************************Second test to check if the credential details has been added to the user list...****************************************************
    def test_save_credentials(self):
        """
        test to check if a new object can be saved
        """
        self.new_app.savecredentials()
        self.assertEqual(len(Credential.app_list),1)

# **********************************Third test to check if multiple users can be saved into the contact list...****************************************************
    def test_save_multiple_credentials(self):
        """
        """
        self.new_app.savecredentials()
        test_credential=Credential("facebook","loui","loui@gmail.com","passi")
        test_credential.savecredentials()
        self.assertEqual(len(Credential.app_list),2)

        
# **********************************Fourth test to delete credential from an applist...****************************************************
    def test_delete_credential(self):
        """

        """
        self.new_app.savecredentials()
        test_credential=Credential("facebook","loui","loui@gmail.com","passi")
        test_credential.savecredentials()

        self.new_app.delete_credential()
        self.assertEqual(len(Credential.app_list),1)

# **********************************Fifth test to find credentials from app list...****************************************************
    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_app.savecredentials()
        test_credential=Credential("facebook","loui","loui@gmail.com","passi")
        test_credential.savecredentials()

        found_credential = Credential.find_by_appname("facebook")

        self.assertEqual(found_credential.app_name,test_credential.app_name)

    def test_generate_random_password(self):
        """
        test_generate_random_password to test if a user can generate a random password with a set length
        """
        test_app = Credential("snapchat","pmahuthu","pmahuthu@mail.com","wanjohi")
        generated_password = test_app.generate_random_password
        test_app_password = generated_password
        test_app.savecredentials()
        self.assertTrue(test_app_password)

if __name__ == '__main__':
    unittest.main()