from db_CRUD import *

while True:
    print_info()
    opt = input()
    match opt:
        case '1':
            print_films()
        case '2':
            create_film()
        case '3':
            edit_film()
        case '4':
            remove_film()
        case'5':
            print("Viso gero liaudis")
            break