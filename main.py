import requests



URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0cbd3a7e8a6f3ccd386fc8aaad28dab7'
HEADER = {
    "Content-Type" : "application/json",
    "trainer_token": "0cbd3a7e8a6f3ccd386fc8aaad28dab7"
    }

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_patch_name = {
    "pokemon_id": "164515",
    "name": "George",
    "photo_id": 63
}


body_add_pokebol = {
    "pokemon_id": "164513"
}


response = requests.post(url = f'{URL}/pokemons' , headers = HEADER ,   json = body_create )
print (response.text)


response_patch_name = requests.put(url =f'{URL}/pokemons' , headers = HEADER , json = body_patch_name)
print (response_patch_name.text)
 

response_add_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER , json = body_add_pokebol) 
print (response_add_pokebol.text)