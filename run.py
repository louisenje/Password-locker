#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(username,password):
    """
    Function for creating new user accounts
    """
    new_user=User(username,password)
    return new_user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def finding_user(username):
    return User.find_by_username(username)

def check_user_exists(user):
    user.check_user_exists()
def confirm_user(userName,passwrd):
    return User.confirm_user(userName,passwrd)

def sign_in_user(userName,passwrd):
    return User.confirm_user(userName,passwrd)

def confirm_new(username):
    return User.confirm_new(username)

def  create_app_credential(app_name,app_username,app_email,app_password):
    new_app_credential=Credential(app_name,app_username,app_email,app_password)
    return new_app_credential

def save_app_credential(credential):
    credential.savecredentials()

def delete_app_credential(app_namea):
    app_namea.delete_app_credential()

def search_App_credential(app_name):
    return Credential.find_by_appname(app_name)

def search_App_credentials(app_Name):
    return Credential.search_app_credentials(app_Name)

def display_all_apps():
    return Credential.display_all_apps()

def generate_random_password(length):
    generate_random_password = Credential.generate_random_password(length)  
    return generate_random_password

def controls():
    print("\033[1m PROFILE CONTROLS:- "+'\033[0m'+"Use these short codes : na - Add a new appcredential, dc-Display all credential, search - find a profile, del - delete a profile, logout- logout of session, ex - exit the application")
    print("\033[1m ACCOUNT CONTROLS:- "+'\033[0m'+"Use these short codes : acp - Change your account password, delete - Delete your account")
    short_code=input()
    return (short_code)
    
def main():
    print("WELCOME TO PASSWORD LOCKER")
    while True:
        print ("DO you have  an account? Y/N")
        acc=input().upper()
        if acc =="Y":
            print ("enter Username:")
            existing_acc=input()
            print("Enter Password:")
            existing_pass=input()
            login=confirm_user(existing_acc,existing_pass)
            print(f"{login}")
            if login==False:
                print("No credentials inserted" )
                return main() 
            else:
                while True:
                    return controls()
        elif acc =="N":
            print("ENter Your  username")
            new_username=input()
            print("Enter your desired password")
            new_password=input()
            new_user= confirm_new(new_username)
            # check if user exists

            if new_user== True:
                print("User ALready exists!!!!!")
                return main
            # elif not new_username and new_password:
            #     print("KIndly fill the username and password")
            elif  not new_username :
                print("FIll  the username")
            elif not new_password:
                print("Fill the password")

            else:#succesful login and saving the new user
                while True:
                    # new_user_credentials=(new_username,new_password)
                    # ********************UNABLE TO SAVE USER!!!!1
                    
                    print("Account succefully created")
                    return acc_functions()
                    
    
def acc_functions():
    
    while True:
        print("\033[1m PROFILE CONTROLS:- "+'\033[0m'+"Use these short codes : na - Add a new appcredential, dc-Display all credential, search - find a profile, del - delete a profile, logout- logout of session, ex - exit the application")
        
        short_code=input().lower()
        if short_code=="na":
            print("Fill the neccessary fields below to create a new app_credential;")
            print("nb--Fill all spaces with asterics")
            print("ENTER APPNAME/SITENAME**....eg:Instagram")
            new_App_Name_Entered=input()

            # check_new_app_name=search_App_credential(new_App_Name_Entered)
        
            print("ENTER USERNAME FOR THE APP")
            new_App_username_Entered=input()
            print("ENTER EMAIL USED FOR THE APP")
            new_App_Email_Entered=input()
            print("Enter PASSWORD USED FOR THE APP")
            new_App_password_Entered=input()

            save_app_credential(create_app_credential(new_App_Name_Entered,new_App_username_Entered,new_App_Email_Entered,new_App_password_Entered))
            print ('\n')
            print(f"New Credential for {new_App_Name_Entered} created")
            print ('\n')
            
            # Displaying all apps
        elif short_code=="dc":
            list_apps=display_all_apps()

            if not list_apps :
                print("\n")
                print("THERE IS NO APP CREDENTIAL SAVED IN YOUR ACCOUNT")
                print("\n")
            else:
                print("Here's a list of all your profiles")
                for Credential in display_all_apps():
                    print(f"APP NAME:{Credential.app_name}")
                    print(f"PROFILE USERNAME:{Credential.app_username}")
                    print(f"PROFILE EMAIL:{Credential.app_email}")
                    print(f"PROFILE PASSWORD:{Credential.app_password}")
                    print(("-*-"*25))
                    print("\n")
            
            # Searching for a certain credential
        elif short_code=="search":
            print("ENTER APP NAME:")
            ssearch_App_credential=search_App_credential(input())
            if ssearch_App_credential:
                print("\n")
                print("SEARCH RESULTS")
                print("\n")
                print(f"APP NAME:{ssearch_App_credential.app_name}")
                print(f"PROFILE USERNAME:{ssearch_App_credential.app_username}")
                print(f"PROFILE EMAIL:{ssearch_App_credential.app_email}")
                print(f"PROFILE PASSWORD:{ssearch_App_credential.app_password}")
            else:
                print("\n")
                print("OPS!No App FOund.")
                print("\n")

        
        elif short_code=="del":
            print("ENTER NAME OF APP CREDENTIAL:")
            app_del=input()
            app_name_delete=search_App_credential(app_del)
            # print(f"FOund {app_name_delete}")
            print(f"Are you sure you want to delete {app_del}? Y/N")
            confirmation=input().upper()
            # print (f"{confirmation} ascsdf")
            if confirmation=="Y":
                delete_app_credential(app_name_delete)
                print("\n")
                print(f"SUCCESFULLY DELETED {app_del}")
                print("\n")
            elif confirmation=="N":
                return main()
            else:
                print("No credentials input")

        elif short_code == "gp":
            print("Kindly enter the APP name you want to generate a password for")            
            app_gen_passwrd = input()
            app_to_change = search_App_credential(app_gen_passwrd)
            if app_to_change:
                print("Input the length of password you want:")
                passwrd_length = int(input())
                
                new_passwrd = generate_random_password(passwrd_length)
                app_to_change.app_password = new_passwrd
                print("\n")
                print("A New Password was Generated and has been Successfully Saved")
                print("\n")
                     
            else:
                print("\n")        
                print("There is no app credential with That Name")
                print("\n")
        elif short_code=="logout":
            return main()
        elif short_code=="ex":
            print ("bye...")
            break
        else:
            print("Kindly input the right keyword")


if __name__=='__main__':
    main()

