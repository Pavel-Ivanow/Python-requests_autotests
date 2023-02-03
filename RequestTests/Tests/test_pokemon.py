import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/pokemons', params = {'pokemon_id':'5079'})
    assert response.status_code == 200


def test_fragment_of_response():
    response = requests.get('https://pokemonbattle.me:5000/pokemons', params = {'pokemon_id':'5079'})
    assert response.json()['name'] == 'Пикачушка'

@pytest.mark.parametrize('key, value',[('trainer_name','pashka')])

def test_of_names(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id':'2084'})
    assert response.json()[key] == value