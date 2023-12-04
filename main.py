import os

import discord
import requests
from discord.ext.commands import Bot

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
    "X-RapidAPI-Key": os.environ['RAPIDAPI_KEY'],
    "X-RapidAPI-Host": os.environ['RAPIDAPI_HOST'],
}

intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')


@bot.command()
async def joke(ctx):
  response = requests.get(url, headers=headers)
  j = response.json()
  setup = j['body'][0]['setup']
  punchline = j['body'][0]['punchline']

  await ctx.send(f'{setup}\n{punchline}')


bot.run(os.environ['DISCORD_TOKEN'])
