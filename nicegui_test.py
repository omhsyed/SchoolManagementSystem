from nicegui import app, ui
import mysql.connector
#from dotenv import load_dotenv
import os


#load_dotenv()


username_input = ''
password_input = ''
schoolcode_input = ''

bg = "#8688A1"


@ui.page('/')
def index():

    ui.query('body').style(f'background-color: {bg}')
    ui.colors(primary = "#FFFFFF")

    with ui.row():
        ui.input(label='Username', 
                #placeholder = 'start typing', 
                on_change = lambda e: read_username(e.value), 
                #validation = {'Input too long': lambda value: len(value) < 20}
                ).props('rounded outlined dense').props('clearable')

        ui.input(label='Password', 
                #placeholder='start typing', 
                on_change = lambda e: read_password(e.value),
                #validation={'Input too long': lambda value: len(value) < 20}
                ).props('rounded outlined dense').props('clearable')


def read_username(value):
     global username_input
     username_input = value


def read_password(value):
     global password_input
     password_input = value



connection = mysql.connector.connect(host = "localhost", user = "root", password = os.environ["DB_PASSWORD"])

if connection.is_connected():
     cursor = connection.cursor()






ui.run(title='Al-Falah Classroom', 
       on_air = 'oSvftbTFTzgTVIGa',
       favicon = '🏫'
       #native = True, 
       #window_size = (800, 600), 
       #fullscreen = False
       )