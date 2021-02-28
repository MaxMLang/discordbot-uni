# IMPORTS (DISCORD PACKAGE)

import discord
from discord.ext import commands
import random
import json
import os
import requests


# INSERT THE SPECIFIC DISCORD TOKEN
DISCORD_TOKEN = "XXXXXXXXXXXXXXX"

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="uni$")

# SOME SCRATCHWORK (FUNCTIONS;ARRAYS) WE WILL NEED LATER
all_fun_facts = ["Banging your head against a wall for one hour burns 150 calories.",
					 "Snakes can help predict earthquakes.",
					 "7% of American adults believe that chocolate milk comes from brown cows.",
					 "If you lift a kangaroo’s tail off the ground it can’t hop.",
					 "Bananas are curved because they grow towards the sun.", "53.091 students were enrolled @LMU in the WS 2019/2020",
				 "787 Professors performed research @LMU", "LMU was Bavaria's first University", "LMU was founded in 1472",
				 "1918 wurde der erste Studenten Ausschuss an der LMU gegründet", "1919 Max Weber joins the LMU faculty",
				 "The Simpsons Paradox is not really a paradox"]

sad_words = ["Ich geb auf", "Ich schaffe das nicht", "Das ist schwer", "traurig", "schwer", "hart", "So ein Müll"]

starter_encouragements= ["Du schaffst das!", "Niemals aufgeben!", "Glaub an dich!",
						 "Es ist immer ein Licht am Ende des Tunnels", "Work hard, cry later!"]

# THIS FUNCTION WILL EXTRACT A QUOTE FROM ZENQUOTES.IO
def getQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

##Several Commands used on our Students Discord Server

# Printing out useful Links for our students
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
	help="Print out the link to Uni2Work",
	brief="Print out the link to Uni2Work"
)
async def towork(ctx):
	await ctx.channel.send("https://uni2work.ifi.lmu.de")

@bot.command(
	help= "Print out the link to Moodle",
	brief= "Print out the link to Moodle"
)
async def moodle(ctx):
	await ctx.channel.send("https://moodle.lmu.de")

@bot.command(
	help= "Print the link to the students council (Fachschaft)",
	brief= "Print the link to the students council (Fachschaft)"
)
async def fs(ctx):
	await ctx.channel.send("https://www.fachschaft.statistik.uni-muenchen.de/index.html")

@bot.command(
	help= "Print the link to GAF Altklausuren",
	brief= "Print the link to GAF Altklausuren"
)
async def ak(ctx):
	await ctx.channel.send("https://gaf.fs.lmu.de/rund-ums-studium/klausuren-und-pruefungsprotokolle")


# Small Easter Eggs and some fun Commands
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
	help= "Get a funfact",
	brief= "Get a funfact"
)
async def funfact(ctx):
	fact= random.choice(all_fun_facts)
	await ctx.channel.send(fact)

@bot.command(
	help= "Get a small encouragement",
	brief= "Get a small encouragement"
)
async def enc(ctx):
	await ctx.channel.send(random.choice(starter_encouragements))

@bot.command(
	help= "Get a random quote from https://zenquotes.io",
	brief= "Get random quote"
)
async def quote(ctx):
	quote= getQuote()
	await ctx.channel.send(quote)

@bot.command(
	help= "Get the link to play scribble.io with your friends",
	brief= "Get scibble.io link"
)
async def scribble(ctx):
	await ctx.channel.send("https://skribbl.io")

@bot.command(
	help= "Show Credits",
	brief= "Credits"
)
async def credits(ctx):
	await ctx.channel.send("Version 1.1.2/ Max M. Lang / Github @MaxMLang")


@bot.event
async def on_message(message):
		if message.author == bot.user:
			return

		msg = message.content
		if any(word in msg for word in sad_words):
			await message.channel.send(random.choice(starter_encouragements))
		await bot.process_commands(message)




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.

bot.run(DISCORD_TOKEN)
