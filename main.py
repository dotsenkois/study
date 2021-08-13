import requests

def super_heroes(token : str):

    my_token = token
    super_heros = ['Hulk', 'Captain America', 'Thanos']

    max_intelligence = 0
    most_intelligence_hero = ''

    for name in super_heros:
        response = requests.get(f'https://superheroapi.com/api/{my_token}/search/{name}')
        if int(response.json()['results'][0]['powerstats']['intelligence']) > max_intelligence:
            max_intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
            most_intelligence_hero = name

    print(f'Самый умный герой {most_intelligence_hero}. Его интеллект составляет {max_intelligence}')


super_heroes('6169178613107460')
