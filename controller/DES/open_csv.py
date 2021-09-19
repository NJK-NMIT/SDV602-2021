"""
OpenCSV button controller
"""
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
from model.model import Model

def accept( event, values, state):
    
    keep_going = True
    if event == 'Open CSV':
       
        
        file_name = sg.PopupGetFile('Please select file to open', file_types=(("Comma separated value", "*.csv"),)) 
        if file_name != None :
            
            view = state['view']
            model = Model(data_source = file_name)
            fin_liabilities = model.get_column('    D3. Total interest payments as a percentage of household disposable income')
            stats_months = model.get_column('Year')
            view.update_current_data(values,file_name,data=fin_liabilities,x_values=stats_months,y_values=fin_liabilities,
                                     x_label='Year Month',y_label='Interest %',title_label='Interest payments % of disposable income')

    return keep_going