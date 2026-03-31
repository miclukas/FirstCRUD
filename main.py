from list_demo_data import load_films
from list_CRUD import *

films = load_films()
id_counter = 3
while True:
    print_info()
    opt = input()
    match opt:
        case '1':
            print_films(films)
        case '2':
            id_counter = create_films(films, id_counter)
        case '3':
            edit_films(films)
        case '4':
            remove_films(films)
        case'5':
            print("iseinu is programos")
            break