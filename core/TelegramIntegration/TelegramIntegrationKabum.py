import telepot
from dotenv import load_dotenv
import os
from .Strategy import Strategy

'''
Design Pattern: Strategy
'''

class TelegramIntegrationKabum(Strategy):

    def __init__(self):
        load_dotenv(verbose=True)

        self.bot_key = os.getenv("BOT_KEY")
        self.group_id = os.getenv("GROUP_ID")

    def send(self, data):
        config = {'bot_key': self.bot_key, 'group_id': int(self.group_id)}
        bot = telepot.Bot(config['bot_key'])
        group = config['group_id']

        data_processed = "Produto: {}\nValor Anterior: {}\nParcelado: {}\nA vista: {}".format(
            data[0], data[1], data[2], data[3])

        return ("[+] Success!" if bot.sendMessage(
            group, data_processed) else "[!] Not sent. Find the problem.")
