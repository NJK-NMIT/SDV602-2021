import PySimpleGUI as sg
import controller.DES.exit_button as exit_button
import controller.User.chat_button as chat_button
from model.user_manager import UserManager 
from time import sleep
from threading import Thread
import threading
import signal
from datetime import datetime

from view import update_file_view

class ChatView(object):

    def __init__(self):
        
        self.window = None
        self.layout = []
        self.components = {"has_components":False}
        self.controls = []
        self.values = None
        # The following will only work if we have logged in!
        self.JsnDrop = UserManager.this_user_manager.jsnDrop
        # Thread for chat
        self.chat_count = 0
        self.exit_event = threading.Event()
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self,signum, frame):
        self.exit_event.set()   

    def set_up_chat_thread(self):
        UserManager.chat_thread = Thread(target=self.chat_display_update,args=(UserManager,))
        UserManager.chat_thread.setDaemon(True)
        UserManager.stop_thread = False
        UserManager.chat_thread.start()

    def chat_display_update(self, UserManager):
        print("Thread chat")
        #sleep(2)
        if self.window != None:
            self.chat_count += 1
            result = self.JsnDrop.select("tblChat",f"DESNumber = '{UserManager.current_screen}'")
            print(result)
            if result != "Data error. Nothing selected from tblChat":
                messages = ""
                
                sorted_chats = sorted(result,key = lambda i : i['Time'] )
                for record in sorted_chats:
                    messages +=   f"{record['PersonID']}[{record['Chat']}]\n"
                UserManager.chat_list += [messages]
                if len(UserManager.chat_list) > 5:
                    UserManager.chat_list = UserManager.chat_list[:-5]
                
                Update_Messages = ""
                for messages in UserManager.chat_list:
                    Update_Messages+= messages
                
                if not UserManager.stop_thread:
                    self.window.write_event_value('-CHATTHREAD-', Update_Messages)  
                        
                     
    def set_up_layout(self,**kwargs):

        sg.theme('LightGreen')
        
        # define the form layout
        
        # one variable per call to sg 
        # if there is a control / input with it add the name to the controls list
        self.components['ChatDisplay'] = sg.Multiline('CHATTY',autoscroll=True,disabled=True, key='ChatDisplay',size=(20,10))
        self.components['Message'] =sg.InputText('Type a message', key='Message',size=(20,50))
        self.components['Send'] = sg.Button('Send', key='Send', size=(10,2))
        self.controls += [chat_button.accept]


        self.components['exit_button'] = sg.Exit(size=(5, 2))        
        self.controls += [exit_button.accept]

        row_buttons = [ 
                        self.components['exit_button'] 
                      ]
        self.components['header'] =   sg.Text('Log in', font=('current 18'))
        self.layout = [
                        
                        [self.components['ChatDisplay'] ], 
                        [self.components['Message']],
                        [self.components['Send']], 
                        row_buttons
                      ]

    def render(self):
        if self.layout != [] :
            self.window =sg.Window('Chat', self.layout, grab_anywhere=False, finalize=True)
            # Need a window before chat
            self.set_up_chat_thread()
  
    def accept_input(self):

        if self.window != None :
            keep_going = True
            
            while keep_going == True:
                event, values = self.window.read()
                if event == "Exit" :
                    UserManager.stop_thread = True
                    
                    
                elif event == "-CHATTHREAD-" and not UserManager.stop_thread:
                    UserManager.stop_thread = True
                    self.window['ChatDisplay'].Update(values[event])
                    if UserManager.stop_thread:
                        UserManager.stop_thread = False
                        self.set_up_chat_thread()


                for accept_control in self.controls:
                    keep_going = accept_control(event,values,{'view':self})
            self.window.close()
        