from list_CRUD import *

while True:
    print_info()
    opt = input()
    match opt:
        case '1':
            print_films()
        case '2':
            id_counter = create_films()
        case '3':
            edit_films()
        case '4':
            remove_films()
        case'5':
            print("Viso gero liaudis")
            break