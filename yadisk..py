import  requests

class YaUploader:
    def __init__(self, token: str):
        self.headers = {'Authorization': token}

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        self.home_url = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path=disk:/{file_path}&overwrite=true'
        response = requests.get(self.home_url, headers=self.headers)
        self.src_url = response.json()['href']
        r = requests.put(self.src_url, data=open(file_path, "rb"))
        return f'{file_path} загружен на диск'


if __name__ == '__main__':
    uploader = YaUploader()
    result = uploader.upload('1.txt')
    print(result)