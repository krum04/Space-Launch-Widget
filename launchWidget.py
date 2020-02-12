import PySimpleGUI as sg
import launchlibrary as ll
from datetime import datetime, timezone
import time

# Setup launch info object


class Launch():
    def __init__(self):
        self.api = ll.Api()
        self.launches = ll.Launch.fetch(self.api)
        self.properties = self.launches[0].param_names
        self.launch_loc = self.launches[0].location.name
        self.launch_agency = self.launches[0].agency.name
        self.windowStart = self.launches[0].windowstart
        self.rocket = self.launches[0].rocket.name
        self.pic = self.launches
        self.tMinus = self.windowStart-(datetime.now(timezone.utc))

    def updateTminus(self):
        self.tMinus = self.windowStart-(datetime.now(timezone.utc))


nextLaunch = Launch()

# Define theme and layout for GUI
sg.theme('Purple')

layout = [
    [sg.Text('Next Launch', size= (20,1), font=('Helvetica', 20),
             justification='left')],
    [sg.Text('', size=(30, 2), font=('Digital-7', 20),
             justification='center', key='_TMINUS_')],
    [sg.Text('Agency: {}'.format(nextLaunch.launch_agency))],
    [sg.Text('Rocket: {}'.format(nextLaunch.rocket))],
    [sg.Text('Location: {}'.format(nextLaunch.launch_loc))],
]

window = sg.Window('Next Ride Out', layout,
                   alpha_channel=.9)

while True:
    event, values = window.read(timeout=1000)

    # Watch for exit even in window
    if event in (None, 'Exit'):
        break

    nextLaunch.updateTminus()
    time = str(nextLaunch.tMinus)
    window['_TMINUS_'].update(time.split(".")[0])
    
    print (time.split(".")[0])
