import os
import wikipedia
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
# def get_info(lkp):
#   try:
#     info = wikipedia.summary(lkp,sentences=4) 
#     emb=discord.embed(title=wikipedia.page(lkp).title,description=info,color=0x0FF00)
#   except wikipedia.exceptions.DisambiguationError as e:
#     return(e)
#   except:
#     return("Please be more specific")
#   else:
#     await channel.send(embed=emb)
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
@bot.command()
async def lookup(ctx,* , arg): 
  try:
    info = wikipedia.summary(arg,sentences=6) 
    emb=discord.Embed(title=wikipedia.page(arg).title,url=wikipedia.page(arg).url,description=info,color=0xFFFFFF)
  except wikipedia.exceptions.DisambiguationError as e:
    return(e)
  except:
    return("Please be more specific")
  else:
    await ctx.send(embed=emb)

@bot.command()
async def image(ctx,* , arg):
  i=0
  while(wikipedia.page(arg).images[i].endswith(".svg") or wikipedia.page(arg).images[i].endswith(".png")):
    i=i+1

  await ctx.channel.send(wikipedia.page(arg).images[i])


bot.run(os.getenv('TOKEN'))

my_secret = os.environ['TOKEN']
