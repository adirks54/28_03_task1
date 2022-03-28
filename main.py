import requests

class Super_Hero:
    url = ' https://superheroapi.com/api/'
    token = '2619421814940190'

    def __init__(self, name):
        self.name = name
        self.id = ''
        self.intelligence = ''

    def get_id(self):
        self.id = requests.get(self.url + self.token + '/search/' + self.name).json()['results'][0]['id']
        return self.id

    def get_intelligence(self):
        self.get_id()
        self.intelligence = requests.get(self.url + self.token + '/' + self.id + '/powerstats').json()['intelligence']
        return self.intelligence


def most_intelligence(heros):
    for hero in heros:
        hero.get_intelligence()
    sorted_list_of_intelligence = sorted(heros, key=lambda hero: hero.intelligence)
    return sorted_list_of_intelligence[0]


if __name__ == "__main__":
    Super_Heros = [Super_Hero('Thanos'), Super_Hero('Captain America'), Super_Hero('Hulk')]
    winner = most_intelligence(Super_Heros)
    print(f"Самый умный супер герой - {winner.name}, его интеллект {winner.intelligence}")
