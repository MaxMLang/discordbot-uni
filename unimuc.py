# IMPORTS (DISCORD PACKAGE)

import discord
from discord.ext import commands


# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = "XXXXXXXXXXXXXX"

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="uni$")

##Several Commands used on our Students Discord Server

@bot.command(
	help="Print out the link to the lecture periods",
	brief="Prints link to lecture periods"
)
async def vz(ctx):
	await ctx.channel.send("https://www.lmu.de/de/workspace-fuer-studierende/1x1-des-studiums/vorlesungszeiten/index.html")

@bot.command(
	help="Print out the link to the university website",
	brief="Prints link to university website"
)
async def website(ctx):
	await ctx.channel.send("https://www.lmu.de/de/index.html")

@bot.command(
	help="Print out the link to all 'applications' by the university",
	brief="Prints link to link collection"
)
async def menu(ctx):
	await ctx.channel.send("https://www.lmu.de/lmu-intern/index.html")

@bot.command(
	help= "Verschicke Ehre an deine Kommilitionen",
	brief="Versende Ehre"
)
async def ehre(ctx, *args):
	response = "hat von "+ format(ctx.author.display_name) +" 1000 Ehre bekommen!"
	# LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
	for arg in args:
		response =  arg + " " + response

	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send(response)

@bot.command(
	help= "Show Credits",
	brief= "Credits"
)
async def credits(ctx):
	await ctx.channel.send("Max M. Lang / Github @MaxMLang")



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.

bot.run(DISCORD_TOKEN)





