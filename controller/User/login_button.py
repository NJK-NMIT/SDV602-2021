"""
Login controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def accept( event, values,state):
    
    keep_going = True
    if event == "Login":   
        # Just testing
        print("Got login")
    else:
        keep_going = True

    return keep_going 