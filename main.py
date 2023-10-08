import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

memes_rarity = {
    'images/meme1.jpg': 10,
    'images/meme2.jpg': 5,
    'images/meme3.jpg': 2,
     }

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    memelist = []
    for meme, rarity in memes_rarity.items():
        memelist.extend([meme] * rarity)

    chosen_meme = random.choice(memelist)
    
    with open(chosen_meme, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTE1Mjk2MzQyNTQ1NTA1ODk0NA.G7QF6y.hUn-N4f4jWaC0I-_kr3bYQsi-Z5WgeqFgXev2c")
