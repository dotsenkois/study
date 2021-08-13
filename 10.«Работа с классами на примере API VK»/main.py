import  requests
api_id = '7921620'

class User():

    def __init__(self,user_id,):
        self.access_token = ''
        home_url = 'https://api.vk.com/method/'
        metod = 'users.get'
        url = f'{home_url}{metod}'
        self.user_id = user_id
        self.params = {
            'user_ids': self.user_id,
            'v': '5.21',
            'access_token': self.access_token
        }
        response = requests.get(url, params=self.params)
        # print(response.status_code)
        # print(response.json())
        self.first_name = response.json()['response'][0]['first_name']
        self.last_name = response.json()['response'][0]['last_name']

    def user_print(self):
        print(f'{self.first_name} {self.last_name}')

    def mutual_friends(self,friend):
        url = 'https://api.vk.com/method/friends.getMutual'
        self.params = {
            'user_ids': self.user_id,
            'v': '5.21',
            'access_token': self.access_token,
            'source_uid':self.user_id,
            'target_uid':friend.user_id,
        }
        resp = requests.get(url, params = self.params)
        # print(resp.json())
        print(f'Список общих друзей пользователей {self.first_name} {self.last_name} и {friend.first_name} {friend.last_name} ')
        mutual_f=[]
        for i in resp.json()['response']:
            temp_user = User(i)
            temp_user.user_print()
            print(temp_user)

        # print(x for x in mutual_f)

    def __str__(self, *args, **kwargs):
        base_url = 'https://vk.com/'
        return f'{base_url}id{self.user_id}'


user_1 = User('144969178')
user_2 = User('585205933')

user_1.user_print()
user_1.mutual_friends(user_2)

# print(user_1)