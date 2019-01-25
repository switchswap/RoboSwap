import requests
from discord import Embed
from discord.ext import commands
from bs4 import BeautifulSoup


class Gruntle:
    def __init__(self, bot):
        self.bot = bot

    async def get_image(self):
        try:
            r = requests.get("https://www.gruntle.me")
            soup = BeautifulSoup(r.text, 'html.parser')
            image = soup.find("img", {"title": "un-disgruntle yourself with this!"})
            return "https://www.gruntle.me" + image['src'][1:]
        except (requests.exceptions.Timeout, requests.exceptions.RequestException):
            return None

    @commands.command(name='gruntle', alias=['cute'])
    @commands.guild_only()
    async def gruntle(self, ctx):
        image_url = await self.get_image()
        if image_url is None:
            embed = Embed(color=0xFDFBF7, description=":x: Error retrieving image!")
        else:
            embed = Embed(color=0xFDFBF7, title="Gruntle.me", url=image_url)
            embed.set_image(url=image_url)
        await ctx.send(embed=embed)


# Important!
def setup(bot):
    bot.add_cog(Gruntle(bot))
