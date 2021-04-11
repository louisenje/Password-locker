class User:
    """
    Class for holding the login and password credentials of a certain user.
    also Its required to enable validations of getting the right users
    """
    def __init__(self,username,password):
        self.username=username
        self.password=password

    user_list=[]
    # method for saving a user by appending it to the user_list

    def save_user(self):

        '''
        save_user method for saving a user by appending it to the user_list
        '''
        User.user_list.append(self)

    # method for deleting users
    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for User in cls.user_list:
            if User.username== username:
                return User

    @classmethod
    def Username_exist(cls,username):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for User in cls.user_list:
            if User.username==username:
                return True
        return False

    @classmethod
    def confirm_user(cls, userName, passwrd):
        """
        confirm_user method that checks if a password matches a username
        """
        for User in cls.user_list:
            if User.username & User.password == True:
                return True
            else:
                return False
        else:
            return False
    @classmethod
    def confirm_new(cls, userName):
        """
        confirm_user method that checks if a password matches a username
        """
        for User in cls.user_list:
            if User.username == True:
                return True
            else:
                return False
        else:
            return False