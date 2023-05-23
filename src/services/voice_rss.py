import urllib
from http import client
import os
import configparser

# read config ini
script_dir = os.path.dirname(__file__)
config = configparser.ConfigParser()
config_file_path = os.path.join(script_dir, '../config/config.ini')
config.read(config_file_path)

VOICE_RSS_KEY = config['VoiceRSS']['api_key']

class VoiceRSS:

    def __init__(self):
        self.__voice_params = {
            'key': VOICE_RSS_KEY,
            'hl': 'pt-br',
            'src': '',
            'v': 'Yara',
            'c': 'MP3',
            'f': '44khz_16bit_stereo'
        }

    def get_voice(self, text):
        self.__voice_params['src'] = text
        params = urllib.parse.urlencode(self.__voice_params)
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        conn = client.HTTPSConnection("api.voicerss.org")
        conn.request("POST", "/?%s" % params, headers=headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data