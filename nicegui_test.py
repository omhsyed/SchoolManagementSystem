from nicegui import app, ui

username_input = ''

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
                #validation={'Input too long': lambda value: len(value) < 20}
                ).props('rounded outlined dense').props('clearable')


    def read_username(value):
        global username_input
        username_input = value



ui.run(title='Test site', 
       #native = True, 
       #window_size = (800, 600), 
       #fullscreen = False
       )