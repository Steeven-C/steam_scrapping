from fastapi import FastAPI
import uvicorn
from bson.objectid import ObjectId
from typing import List, Optional
import psycopg2
from game_class import Game


app = FastAPI()

# Connection a la base Postgre distante


try:
    connection = psycopg2.connect(user = "mlrzrpdtctsdmu",
                                  password = "d684d89def6e9e28e62a46b52c740603784a228920da1e970634fc73dc202cd0",
                                  host = "ec2-34-253-148-186.eu-west-1.compute.amazonaws.com",
                                  port = "5432",
                                  database = "d6lroer2tiaago")
                                              
    
    connection.autocommit = True                            
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)


#test API

@app.get("/")
async def root():
    return {"message": "Hello Toto tata"}



#post test qui marche
@app.post("/games")
    async def create_game(game: Game):
        
        game = game.__dict__
        cursor = connection.cursor()
        cursor.execute("INSERT INTO game_tests (game_name, evaluation) VALUES ( %s, %s)", ( game['name'], game['evaluation']))
        return game['name']


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


