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