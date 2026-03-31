films = [
    {
        'id': 1,
        "title": "Oppenheimer",
        "director": "Christopher Nolan",
        "release_year": 2023
    },
    {
        'id': 2,
        "title": "Dune",
        "director": "Denis Villeneuve",
        "release_year": 2021
    },
    {
        'id': 3,
        "title": "Avengers",
        "director": "Anthony Russo",
        "release_year": 2019
    },
]
id_counter = 3
while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti filmu pasirinkimus")
    print("2. Itraukti filma i sarasa")
    print("3. Koreguoti filma")
    print("4. Salinti filma")
    print("5. Iseiti is programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    opt = input()
    match opt:
        case '1':
            for film in films:
                print(f"{film['id']}. Filmas: {film['title']}, Rezisierius: {film['director']}, Isleidimo metai: {film['release_year']}.")
        case '2':
            print('filmu itraukimas:')
            print("iveskite filmo pavadinima")
            title = input()
            print("iveskite rezisieriu")
            director = input()
            print("iveskite isleidimo metus")
            release_year = int(input())
            id_counter += 1
            film = {
                'id': id_counter,
                'title': title,
                'director': director,
                'release_year': release_year
            }
            films.append(film)
        case '3':
            print('filmu redagavimas')
            print('iveskite filmo id, kuri norite redaguoti')
            edit_id = input()
            for film in films:
                if edit_id == str(film['id']):
                    print(f'{film['id']}. Redaguojama: Filmas {film['title']}, rezisierius {film['director']}, isleidimo metai {film['release_year']}.')
                    print("iveskite filma")
                    film['title'] = input()
                    print("iveskite rezisieriu")
                    film['director'] = input()
                    print("iveskite isleidimo metus")
                    film['release_year'] = int(input())
                    break
        case '4':
            print("filmo salinimas")
            print("iveskite filmo id, kuri norite pasalinti")
            del_id = input()
            for film in films:
                if del_id == str(film['id']):
                    print(
                        f"{film['id']}. Salinamas filmas: {film['title']}, režisierius {film['director']}, išleidimo metai {film['release_year']}.")
                    films.remove(film)
                    break
        case'5':
            print("iseinu is programos")
            break