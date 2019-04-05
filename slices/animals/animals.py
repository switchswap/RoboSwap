import config
import aiohttp
from discord.ext import commands
from discord import Embed


class Animals:
    def __init__(self, bot):
        self.bot = bot

    async def get_image(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                if r.status == 200:
                    response = await r.json()
                    return response[0]
                else:
                    return None

    @commands.command(name='shibe')
    @commands.guild_only()
    async def get_shibe(self, ctx):
        image_url = await self.get_image("https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
        if image_url is None:
            embed = Embed(color=config.default_color, description=":x: Error retrieving image!")
        else:
            embed = Embed(color=config.default_color, title="Shibe", url=image_url)
            embed.set_image(url=image_url)
        await ctx.send(embed=embed)

    @commands.command(name='cat')
    @commands.guild_only()
    async def get_cat(self, ctx):
        image_url = await self.get_image("https://shibe.online/api/cats?count=1&urls=true&httpsUrls=true")
        if image_url is None:
            embed = Embed(color=config.default_color, description=":x: Error retrieving image!")
        else:
            embed = Embed(color=config.default_color, title="Cat", url=image_url)
            embed.set_image(url=image_url)
        await ctx.send(embed=embed)

    @commands.command(name='bird')
    @commands.guild_only()
    async def get_bird(self, ctx):
        image_url = await self.get_image("https://shibe.online/api/birds?count=1&urls=true&httpsUrls=true")
        if image_url is None:
            embed = Embed(color=config.default_color, description=":x: Error retrieving image!")
        else:
            embed = Embed(color=config.default_color, title="Bird", url=image_url)
            embed.set_image(url=image_url)
        await ctx.send(embed=embed)


# Important!
def setup(bot):
    bot.add_cog(Animals(bot))
