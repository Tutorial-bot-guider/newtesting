import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='+')

@bot.event
async def on_ready():
   print('Online')


@bot.command()
async def say(ctx,*,content):
    await ctx.send(content)
    

@bot.command()
async def ping(ctx):
     await ctx.send("Hello, How are you")
     await ctx.send("You want pinged me haha.....")
     await ctx.send('👍')
   
bot.run(TOKEN) 
