# You can rename the py file to your choosing. This is a example name. Now, heres the bot code.
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.all()
intents.message_content = True # Make sure to enable this setting for your bot in the Dev Portal. It needs this to send the messages after the command is sent.

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='', intents=intents)
# ^ change the prefix to your liking :)
@bot.event
async def on_ready():
    print(f'(bot name) is online and ready to go!')
    await bot.change_presence(activity=discord.Game(name="Testing..."), status=discord.Status.online)
#Feel free to change the Game status to whatever you like. :)

try:
    bot.run('YOUR_BOT_TOKEN_HERE')
except KeyboardInterrupt:
    print('Bot is shutting down...')
    bot.logout()
    bot.close()
