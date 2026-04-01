import pymysql

DB_CONFIG = {
    'host':'localhost',
    'port': 3306,
    'user':'root',
    'password':"root",
    'database':'films'
}
headers = ['id','title','director','release_year']

def get_conn():
    return pymysql.connect(**DB_CONFIG)

def load_films():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from my_films')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    films_list = []
    for row in rows:
        single_film = {}
        for col_num in range(len(headers)):
            single_film[headers[col_num]] = str(row[col_num]).replace('\r','')
        films_list.append(single_film)
    return films_list

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti filmu pasirinkimus")
    print("2. Itraukti filma i sarasa")
    print("3. Koreguoti filma")
    print("4. Salinti filma")
    print("5. Iseiti is programos")
    print("-----------------------------Pasirinkite:---------------------------------")

def print_films():
    films = load_films()
    for film in films:
        print(f"{film['id']}. Filmas {film['title']}. Rezisierius {film['director']}. Isleidimo metai {film['release_year']}.")

def create_film():
    print('filmu itraukimas:')
    print("iveskite filmo pavadinima")
    title = input()
    print("iveskite rezisieriu")
    director = input()
    print('iveskite isleidimo metus')
    release_year = int(input())
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO my_films (title, director, release_year) VALUES (%s, %s, %s);',
                (title, director, release_year))
    conn.commit()
    cur.close()
    conn.close()

def edit_film():
    print('filmu redagavimas')
    print("iveskite id filmo kuri norite redaguoti")
    edit_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from my_films where id = %s', (edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        print(f"{row[0]}. Filmas {row[1]}. Rezisierius {row[2]}. Isleidimo metai {row[3]}.")
        print("iveskite filmo pavadinima")
        title = input()
        print("iveskite rezisieriu")
        director = input()
        print('iveskite isleidimo metus')
        release_year = int(input())

        conn = get_conn()
        cur = conn.cursor()
        cur.execute('UPDATE my_films SET title = %s, director = %s, release_year = %s WHERE id = %s;',
                    (title, director, release_year, edit_id))
        conn.commit()
        cur.close()
        conn.close()
    else:
        print('tokio iraso nera')

def remove_film():
    print('filmu salinimas')
    print("iveskite id filmo kuri norite pasalinti")
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('select * from my_films where id = %s', (del_id,))
    row = cur.fetchone()

    if row:
        print(f"{row[0]}. Salinamas filmas {row[1]}. Rezisierius {row[2]}. Isleidimo metai {row[3]}.")
        cur.execute('delete from my_films where id = %s', (del_id,))
        conn.commit()
    else:
        print('tokio iraso nera')
    cur.close()
    conn.close()