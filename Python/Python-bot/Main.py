# Import from discord files
import discord
from discord.ext import commands
from discord import Intents

# Import from bot files
import Math
import Help
import plt

bot = commands.Bot(command_prefix="!", description="The description", intents=Intents.all())

@bot.event
async def  on_ready():
    print("Ready!")

@bot.command()
async def chelp(ctx, cat=None):
    if cat:
        embed = Help.help(cat)
    else:
        embed = Help.help()
    await ctx.send(embed=embed)
    
@bot.command()
async def helloworld(ctx):
    await ctx.send('**Hello World! :robot:**')


@bot.command()
async def creeper(ctx):
    await ctx.send('Creeper, Aww Man')

@bot.command()
async def whats9plus10(ctx):
    await ctx.send('**21 :nerd:**')

@bot.command()
async def low(ctx):
    await ctx.send('''
Shawty had them apple bottom jeans (jeans)
Boots with the fur (with the fur)
The whole club was lookin' at her
She hit the floor (she hit the floor)
Next thing you know
Shawty got low, low, low, low, low, low, low, low
''')

@bot.command()
async def embedtest(ctx):
    embed = discord.Embed(title="this is a test", description ="creeper aw man", color=0xff0000)
    await ctx.send(embed=embed)

@bot.command()
async def nerd(ctx):
    await ctx.send(":nerd:")

@bot.command()
async def sonothalal(ctx):
    await ctx.send("https://tenor.com/view/walter-white-walter-arabic-arab-muslim-gif-18401301")


@bot.command()
async def countto(ctx,number):
    i = 1
    while i <= int(number):
      await ctx.send(i)
      i += 1


@bot.command()
async def fact(ctx, num):
    numatstart = int(num)
    result = Math.fact(int(num))
    await ctx.send(f"Factorial of {numatstart} is {result}")
    
@bot.command()
async def oddoreven(ctx, num):
    result = Math.oddoreven(int(num))
    await ctx.send(result)
    
@bot.command()
async def remainder(ctx, num1, num2):
    result = Math.remainder(int(num1), int(num2))
    await ctx.send(result)

@bot.command()
async def rint(ctx, num1, num2):
    value = Math.rint(int(num1), int(num2))
    await ctx.send(f"From {num1} and {num2} i choose {value}")
    
@bot.command()
async def tobinary(ctx, txt):
    result = Math.tobinary(txt)
    await ctx.send(f"The binary of '{txt}' is {result}")
    
@bot.command()
async def fib(ctx, num):
    await ctx.send(Math.fib(int(num)))
    
@bot.command()
async def graph(message):
    plt.graph()
    with open('graph.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
            
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().count('skull') > 0:
        await message.channel.send(':skull:')
    await bot.process_commands(message)
    
bot.run("MTA0NDY3Mjk2MDkyNzExMzMxNw.GTcmg_.E8dOiUAwX0aetZgSi9MMfUcZJN_J2hsFawl2SA")