from discord.ext import commands
from datetime import datetime as d

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        start = d.timestamp(d.now())
        await ctx.send("pingping")
    
    @commands.command()
    async def pingers(self, ctx):
        channel = ctx.message.channel
        author = ctx.message.author
        name = ctx.message.author.name
        await ctx.send(channel)
        await ctx.send(author)
        await ctx.send(name)
    
    @commands.command(name = "say")
    async def say_command(self, ctx):
        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]
        
        if text == "":
            await ctx.send(content="you need to specify the text!")
            pass
        else:
            await ctx.send(content=f"**{msg}**")
            pass
        return

def setup(bot):
    bot.add_cog(Basic(bot))