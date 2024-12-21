import requests
import pytest



URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0cbd3a7e8a6f3ccd386fc8aaad28dab7'
HEADER = {
    "Content-Type" : "application/json",
    "trainer_token": "0cbd3a7e8a6f3ccd386fc8aaad28dab7"
    }
TRAINER_ID = "12626"
NAME_TRAINER = "Виталий"

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons' , params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_name_check():
    response_get = requests.get(url = f'{URL}/trainers' , params = {'name' : NAME_TRAINER})
    assert response_get.json()["data"][0]["trainer_name"] == 'Виталий'

