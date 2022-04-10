# Ajnur Bogucanin | Graficari | for HackAtHome2022

# This is just a simple User Interface since this client is only for companies that
# want to implement our system. The goal of this UI is very simple, we need to display
# does the user form a scanned card own a ticket. For the example I made this client to
# be used by Stadion Grbavica

#

#IMPORTS 
import tkinter as tk     #Tkinter is Python library used for making UI'
import util as util      #util.py for connecting to scanner and db
import arduino as ard    #arduino for connecting to scanner


#START:TKINTER
root = tk.Tk()
root.title('TicketSA')

#FUNC

#Function that reads card and initates check for ticket validation
def readC():
    #currnet port
    port = currentPort.get() 

    #GET user ID from card
    userID = ard.readCard('com3')
    #GET username from database using ID
    userName = util.pullUserName(userID)

    #Change text value of labels showing name and ID
    user_ID['text'] = 'ID: '+ userID
    user_name['text'] = 'Name: '+ userName

    #Checks if user has valid ticket
    ticket_data = util.getTicketData(currnetEventID ,userID)
    if ticket_data != 0:
        user_ticketStatus['text'] = 'Status: Valid'
        event_name.config(text='Utakmica: Zeljo - Sarajevo', bg='green', fg='black',height=3 , width=48, font=("Arial", 13))
    else:
        user_ticketStatus['text'] = 'Status: Invalid'
        event_name.config(text='Utakmica: Zeljo - Sarajevo', bg='red', fg='black',height=3 , width=48, font=("Arial", 13))
    


#VARS
currnetEventID = 'SAZLEJ'
currentPort = tk.StringVar()


#TKINTER WIDGETS

#Frames
top_frame = tk.Frame(root)
center_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)
end_port = tk.Frame(bottom_frame)

#Common
top_color_bar = tk.Label(top_frame, bg='#0C2D48', fg='white' , height=3 , width=40, text="TicketSA", font=("Arial", 15))
bottom_color_bar = tk.Label(end_port, bg='#0C2D48', width=63)
today_events_label = tk.Label(center_frame, text='Current events:')
devider = tk.Label(center_frame,height=20 , width=40)

#Events
event_name = tk.Label(center_frame, text='Utakmica: Zeljo - Sarajevo', bg='yellow', fg='black',height=3 , width=48, font=("Arial", 13) )

#User Info
user_info = tk.Label(center_frame, text='Cardholder Information', bg='lightgray', width=40)
user_name = tk.Label(center_frame, text='Name:          ')
user_ID = tk.Label(center_frame, text='ID:         ')
user_ticketStatus = tk.Label(center_frame, text='Status:         ') 

#Settings
portNumber = tk.Entry(end_port, textvariable='currentPort')
portSubmit = tk.Button(end_port, text='Scan', command=readC)
portText = tk.Label(end_port, text='Port Settings', bg='lightgray', width=40)



#TKINTER PACKING

#frame packing
top_frame.pack(side='top')
center_frame.pack(side='top')
bottom_frame.pack(side='bottom')
end_port.pack(side='bottom')

#common packing
top_color_bar.pack(side='top')
today_events_label.pack(side='top')

#event packing
event_name.pack(side='top')

#common packing
devider.pack(side='top')

#user packing
user_info.pack(side='top')
user_name.pack(side='left')
user_ID.pack(side='left')
user_ticketStatus.pack(side='right')

#common packing
devider.pack(side='top')

#settings packing
portText.pack(side='top')
portNumber.pack(side='top')
portSubmit.pack(side='top')
bottom_color_bar.pack(side='top')




#END:TKINTER
root.mainloop()

