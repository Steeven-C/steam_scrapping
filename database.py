import psycopg2
from psycopg2 import OperationalError
import getpass

#pswd = getpass.getpass('Password')

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database  = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        print("Connetion to Scrap DB as successful")
    except OperationalError as e:
        print(f"The error '{e}' occured")
    return connection 
# connecting with HerokuDB
connection = create_connection("d6lroer2tiaago","mlrzrpdtctsdmu","d684d89def6e9e28e62a46b52c740603784a228920da1e970634fc73dc202cd0","ec2-34-253-148-186.eu-west-1.compute.amazonaws.com","5432")

# with connection.cursor() as cursor:
#     cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'scrap_steam'")
#     exists = cursor.fetchone()
#     if not exists:
#         cursor.execute('CREATE DATABASE scrap_steam')

# def create_database(connection, query):
#   connection.autocommit = True
#   cursor = connection.cursor()
#   try : 
#     cursor.execute(query)
#     print("Its work")
#   except OperationalError as e :
#     print(f"The error '{e}' as appear")

  
# create_database_query = "CREATE DATABASE scrap_steam"
# create_database(connection, create_database_query)

# connection  = create_connection(
#     "d6lroer2tiaago", "mlrzrpdtctsdmu", "d684d89def6e9e28e62a46b52c740603784a228920da1e970634fc73dc202cd0", "ec2-34-253-148-186.eu-west-1.compute.amazonaws.com","5432"
# )


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")



def create_games():
    with connection:
        with connection.cursor() as cursor : 
            cursor.execute("""CREATE TABLE IF NOT EXISTS games (
                id SERIAL PRIMARY KEY,
                game_name TEXT,
                evaluation TEXT
            );""") 

def create_player_activity():
    with connection:
        with connection.cursor() as cursor : 
            cursor.execute("""CREATE TABLE IF NOT EXISTS player_activities(
                id SERIAL PRIMARY KEY,
                day_pike INT,
                date REAL,
                game_id INT references games(id)
            );""")

def create_genre():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS genres(
                id SERIAL PRIMARY KEY,
                genre_name TEXT
            );""")

def create_game_genre():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS game_genres(
                id SERIAL PRIMARY KEY,
                game_id INT REFERENCES games(id),
                genre_id INT REFERENCES genres(id)
            );""")

def create_steam_user():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS steam_users(
            id SERIAL PRIMARY KEY,
            date DATE,
            players_pike INT
            );""")

def create_game_test():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS game_tests(
                id SERIAL PRIMARY KEY,
                game_name TEXT,
                evaluation TEXT
            );""")

