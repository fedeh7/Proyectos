import discord
from discord.ext import commands
import random
import asyncio


bot = commands.Bot(command_prefix='pl ')
cogs = ["cogs.basic"]


#description = '''An example bot to showcase the discord.ext.commands extension
#module.
#There are a number of utility commands being showcased here.'''
#bot = commands.Bot(command_prefix='?', description=description)
@bot.command()
async def pruebita(ctx):
    await ctx.send("Probando llamado de funciones")
    creador(ctx)

    
@bot.command()
async def pinger(ctx):
    channel = ctx.message.channel
    author = ctx.message.author
    name = ctx.message.author.name
    await ctx.send(channel)
    await ctx.send(author)
    await ctx.send(name)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    for cog in cogs:
        bot.load_extension(cog)
        print("loaded: ",cog)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(str(i) + content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

#######################################################divisor

@bot.command()
async def rol(ctx, num: str, mod = 0):
    lista = []
    tot = 0
    z = num.split("d")
    for i in range(int(z[0])):
        x = random.randint(1, int(z[1]))
        tot = tot + x
        lista.append(x)
        #await ctx.send(f"Tirada {i+1}: {x}")
    await ctx.send(f"Las Tiradas fueron:\n{lista}")
    await ctx.send(f'El total fue de {tot} + {mod} = {tot+mod}')  

@bot.command()
async def crear(ctx):
    pass  

@bot.command()
async def preguntas(ctx):
    user = ctx.message.author.name
    await ctx.send(f"{user}")
    def autor(m):
        return m.author == ctx.author
    nombre = ""
    raza = ""
    clase = ""
    data = ["nombre\n","raza\n","clase\n","0\n","0\n"]
    #try:
    #    with open (f"personjes/{user}", "r") as f:
    #        data = list(f.readlines())
    #except Exception:
    #    with open (f"personajes/{user}", "w") as f:
    #        f.writelines("test")
    #    await ctx.send("Primera ves que creas un personaje")
        
    try:
        await ctx.send("Primera pregunta: Como se va a llamar tu personaje? ")
        nombre = await bot.wait_for("message", check = autor, timeout=20.0)
        await ctx.send(f'Tu nombre es: {nombre.content}')
        data[0] = nombre.content + "\n"
        await ctx.send(f"el dato que se guardo es {data[0]}")
        
        
        
    except Exception:
        await ctx.send('Tardaste mucho')
    try:
        await ctx.send("Segunda pregunta: Que Raza sera tu personaje?")
        raza = await bot.wait_for("message", check = autor, timeout=20.0)
        await ctx.send(f'Tu raza es: {raza.content}')
        data[1] = raza.content + "\n"
        await ctx.send(f"el dato que se guardo es {data[1]}")
    
        
    except Exception:
        await ctx.send('Tardaste mucho')
    try:
        await ctx.send("Tercera pregunta: Que clase sera tu personaje?")
        clase = await bot.wait_for("message", check = autor, timeout=20.0)
        await ctx.send(f'Tu clase es: {clase.content}')
        data[2] = clase.content + "\n"
        await ctx.send(f"el dato que se guardo es {data[2]}")
        print(data)
        
        
    except Exception:
        await ctx.send('Tardaste mucho')
    
    #try:
    with open(f"personajes/{user}.txt", "w") as f:
        f.writelines(data)
    #except Exception:
    #    await ctx.send('Fallo la escritura')


    
     
    

bot.run('NTcwNjAxMDczNjE4NzE0NjM3.XMBjvQ.tsokha-W0r9XsDyS8KsVxQrYrOo')

#client.run('NTcwNjAxMDczNjE4NzE0NjM3.XMBjvQ.tsokha-W0r9XsDyS8KsVxQrYrOo')