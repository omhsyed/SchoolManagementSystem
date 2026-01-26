from nicegui import app, ui
import mysql.connector
import os




# Variables

username_input = ''
password_input = ''
schoolcode_input = ''
clr_bg = "#53745B"
clr_accent = "#2D4232"
clr_text = "#FCFFE8"
clr_button = "#C8DFAC"
clr_error = "#511E0B"




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
     else:
          ui.html(f"<h7 style = 'color: {clr_error};'> Incorrect Log-in Credentials. </h7>", sanitize = False)




with ui.header().style(f'background-color: {clr_accent}').classes("justify-center"):
     ui.html(f"<h4 style = 'color: {clr_text};'> <strong> Al-Falah Classroom </strong> </h4>", sanitize = False)



ui.query('body').style(f'background-color: {clr_bg}')
ui.colors(primary = "#FBFFCA", secondary = "#FBFFCA", accent = "#FBFFCA")




def login_page():

     #ui.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoqY44qpHka0eUDqpKu-tpY8nJe4B0QIbXFw&s')

     ui.html(f"<h6 style = 'color: {clr_text};'> Welcome to Al-Falah Academy's <strong>School System.</strong> </h6>", sanitize = False)
     
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

     
     login_button = ui.button(color = clr_button, text = "Log In", on_click = login)
     



def other():

     ui.html(f"<h7 style = 'color: {clr_text};'> Page Two!!! </h7>", sanitize = False)
     ui.button(color = clr_button, text = "go back", on_click = lambda e: ui.navigate.to('/'))


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