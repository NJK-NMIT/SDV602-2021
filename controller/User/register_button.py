"""
Register controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def accept( event, values,state):
    
    keep_going = True
    if event == "Register":   
        # Just testing
        print("Got Register - just testing")

        # Work with a UserManager object
        from model.user_manager import UserManager
        # get user name and password from the "values" or "state"
        a_user_manager = UserManager()

        # Just a Test
        register_status = a_user_manager.register("Todd", "12345") 
        print(f"REGISTER STATUS {register_status}")

        login_status = a_user_manager.login("Todd","12345")
        print(f"LOGIN STATUS {login_status}")

        chat_status = a_user_manager.chat("Hello 1")
        print(f"CHAT STATUS {chat_status}")

        login_status = a_user_manager.login("Todd","12")
        print(f"LOGIN STATUS {login_status}")

        chat_status = a_user_manager.chat("Hello 2")
        print(f"CHAT STATUS {chat_status}")




    else:
        keep_going = True

    return keep_going 