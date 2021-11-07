from instabot import Bot
from source.Destroyer import Destroyer

Destroyer.destroyConfig()

bot = Bot()
bot.login(username="riseandbusiness", password="PaulWalcher69")
bot.upload_photo("frog_sitting_0.jpg", caption="Nice pic!")
