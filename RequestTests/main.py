import requests
import pytest

token = '869f15aaf8edc8c8d08e736ddacf2d3c'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json',          
   "trainer_token": token}, 
   json = {
 
    "name": "Пикачушка",
    "photo": "https://dolnikov.ru/pokemons/05.png"

})
print (response.text)

response = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type': 'application/json',          
   "trainer_token": token}, 
   json = {
    
    "pokemon_id": 3200,
    "name": "ПикаПикаЧу",
    "photo": "https://dolnikov.ru/pokemons/05.png"


})
print (response.text)

response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type': 'application/json',          
   "trainer_token": token},
   json = {
   
    "pokemon_id": "3200"
})

