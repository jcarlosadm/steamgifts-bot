import configparser
from main import SteamGifts as SG

config = configparser.ConfigParser()
config.read('config.ini')
cookie = config['DEFAULT'].get('cookie')

s = SG(cookie, 'Wishlist', False, 1)
s.start()