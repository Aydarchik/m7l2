# Вставляй код функции сюда и сдавай задание на проверку!
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
from model.py import *   
@bot.command()
async def check(ctx):
    attachments = ctx.message.attachments
    
    if attachments:
        for attachment in attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'{check}.jpg')
            await ctx.send('картинка скачена')
            print(type(check))
            
    else:
        await ctx.send('нет картинки ')


bot.run("")