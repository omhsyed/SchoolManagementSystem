from nicegui import app, ui
import mysql.connector
#from dotenv import load_dotenv
import os


#load_dotenv()


username_input = ''
password_input = ''
schoolcode_input = ''

bg = "#51785A"


def read_username(value):
     global username_input
     username_input = value


def read_password(value):
     global password_input
     password_input = value

def login():
     if username_input == "test1" and password_input == "test2":
          ui.label("it worked!")
          ui.navigate.to('/other')


with ui.header().style('background-color: #3874c8').classes("justify-center"):
     ui.label("Al-Falah Classroom").classes("justify-center")


ui.query('body').style(f'background-color: {bg}')
ui.colors(primary = "#FBFFCA", secondary = "#FBFFCA", accent = "#FBFFCA")


#@ui.page('/')
def login_page():

     
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

     
     login_button = ui.button(color = "#FBFFCA", text = "Log In", on_click = login)
     



def other():

     ui.label("different page!")
     ui.button(text = "go back", on_click = lambda e: ui.navigate.to('/'))


ui.sub_pages({'/': login_page, '/other': other}).classes('w-full items-center')


#connection = mysql.connector.connect(host = "localhost", user = "root", password = os.environ["DB_PASSWORD"])

#if connection.is_connected():
     #cursor = connection.cursor()






ui.run(title='Al-Falah Classroom', 
       on_air = 'oSvftbTFTzgTVIGa',
       favicon = '🏫'
       #native = True, 
       #window_size = (800, 600), 
       #fullscreen = False
       )