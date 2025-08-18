import configparser
import os
import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file", "upload.jpeg")


class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path
        self.file_path = file_path

    def read_data(self):
        f = open(self.data_path, encoding="utf8")
        data = yaml.safe_load(f)
        # print(data)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config

    def read_file(self):
        file = open(self.file_path, 'rb')
        return {'file': ('upload.jpeg', file, 'image/jpeg')}


base_data = FileRead()
# print(base_data.read_ini()['host']['meike_url'])
