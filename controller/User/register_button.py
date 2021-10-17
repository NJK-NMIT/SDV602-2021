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
        from model.user_manager import UserManager
        a_user_manager = UserManager()

    else:
        keep_going = True

    return keep_going 