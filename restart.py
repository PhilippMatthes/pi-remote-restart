import os
import telepot
from time import sleep
import datetime
import telepot.api
import urllib3

telepot.api._pools = {
    'default': urllib3.PoolManager(num_pools=3, maxsize=10, retries=5, timeout=30),
}

telepot_api_key = "INSERT TELEPOT API KEY HERE"
telepot_user_key = 0000000


class RestartBot:
    def __init__(self):
        self.bot = telepot.Bot(telepot_api_key)

    def send(self, text):
        self.bot.sendMessage(telepot_user_key, text)

    @staticmethod
    def restart():
        os.system('sudo shutdown -r now')

    def get_current_message(self):
        updates = self.bot.getUpdates()
        if len(updates) == 0:
            return ""
        else:
            message_offset = updates[len(updates) - 1]["update_id"]
            current_message = self.bot.getUpdates(offset=message_offset)
            return current_message[0]["message"]["text"]


if __name__ == "__main__":
    while True:
        try:
            restart_bot = RestartBot()
            if restart_bot.get_current_message() == "Restart":
                restart_bot.send("Restarting the system!")
                RestartBot.restart()

            if restart_bot.get_current_message() == "Quit":
                restart_bot.send("Quitting!")
                break

            sleep(5)

        except:
            sleep(60)
