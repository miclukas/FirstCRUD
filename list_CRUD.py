def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti filmu pasirinkimus")
    print("2. Itraukti filma i sarasa")
    print("3. Koreguoti filma")
    print("4. Salinti filma")
    print("5. Iseiti is programos")
    print("-----------------------------Pasirinkite:---------------------------------")

def print_films(films):
    for film in films:
        print(
            f"{film['id']}. Filmas: {film['title']}, "
            f"Rezisierius: {film['director']}, Isleidimo metai: {film['release_year']}.")

def create_films(films, id_counter):
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
    return id_counter

def edit_films(films):
    print('filmu redagavimas')
    print('iveskite filmo id, kuri norite redaguoti')
    edit_id = input()
    for film in films:
        if edit_id == str(film['id']):
            print(
                f'{film['id']}. Redaguojama: Filmas {film['title']}, rezisierius {film['director']}, isleidimo metai {film['release_year']}.')
            print("iveskite filma")
            film['title'] = input()
            print("iveskite rezisieriu")
            film['director'] = input()
            print("iveskite isleidimo metus")
            film['release_year'] = int(input())
            break

def remove_films(films):
    print("filmo salinimas")
    print("iveskite filmo id, kuri norite pasalinti")
    del_id = input()
    for film in films:
        if del_id == str(film['id']):
            print(
                f"{film['id']}. Salinamas filmas: {film['title']}, režisierius {film['director']}, išleidimo metai {film['release_year']}.")
            films.remove(film)
            break