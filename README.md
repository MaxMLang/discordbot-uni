# The Idea
Now that my semester is over and  I do not have a lot of lectures anymore, I decided to continue focusing on studying Python in addition to R. My first project however is not a Data Analysis one - it is a bot.
Due to the Covid-19 Pandemic my friends and I were more or less forced to start our Bachelor studies online. Most of them I have not even met in real life yet. So our main tool to communicate, study together and meet up is our own Discord server. On that server are almost 200 students that use it to meet up and connect. It is kind of like an virtual campus. While we were chatting and preparing for our exams, we discussed how cool it would be to have a bot that makes our virtual college life a bit easier. We discussed over a couple of functions it should have and already had some pretty cool ideas. Those ideas were now transformed into a working bot! 

# Preparations
Here we just link our code to our specific bot we created in the Github Developer Portal via the Discord Token. I have to omit this token because it is kind of the key to the whole bot. After that we create the bot itself and assign in to the bot variable. Pay attention to the `commands.Bot(command_prefix="uni$")` call. Here we specified the prefix of UNIMUC. So by using `uni$some_command` we can tell our bot what to do specifically.
```{python, eval= FALSE}
# INSERT THE SPECIFIC DISCORD TOKEN
DISCORD_TOKEN = "XXXXXXXXXXXXXXX"

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX
bot = commands.Bot(command_prefix="uni$")
```

# Main Functions
In the following I want to present a couple of functions I implemented into the UNIMUC (the bot) and how I believe this could make everyones online college life a bit more easy. I will only focus on the functions and not go into detail on the packages I used. If you're interested in that check out the code on my [Github](https://github.com/MaxMLang/DiscordBot_Uni)

## Sending useful Links
Many students struggle to keep an overview over all the websites. Lecture Periods, Moodle (Platform for courses in Statistics), Uni2Work (Platform for courses in Mathematics or Computer Science) and many more. This problem belongs now to the past. UNIMUC offers multiple functions to send them the links right into the channel. These functions are simple but really powerful. 

All those functions work exactly the same, so I will just take one or two examples out. If you are interested in the whole source-code you can find it on my [Github](https://github.com/MaxMLang/DiscordBot_Uni) .

```{python, eval= FALSE}
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
```
As you can see  I extracted the two functions `vz` and `website`. If a student types now `uni$vz` or `uni$website` UNIMUC will send him the specific link.
On Discord this looks then like this:
![Photo of the commands and bot reponse in Discord](images/Bildschirmfoto 2021-02-28 um 19.38.31.png){width=600px height=600px}

## Fun Facts
Sometimes you might be in the mood for some quick fun facts. "Did you know... 

... that UNIMUC can help you with that?"

What UNIMUC basically does is take random string out of the `all_fun_facts` string array by using the `random.choice()` function from the `random` package. This simply gets assigned to a variable `fact` which UNIMUC will send back to the author.
```{python, eval= FALSE}
# Creating the String array (could also be outsourced to another doc)
all_fun_facts = [ "53.091 students were enrolled @LMU in the WS 2019/2020", "787 Professors performed research @LMU", "LMU was Bavaria's first University", "LMU was founded in 1472", "1918 wurde der erste Studenten Ausschuss an der LMU gegründet", "1919 Max Weber joins the LMU faculty", "The Simpsons Paradox is not really a paradox"]

@bot.command(
	help= "Get a funfact",
	brief= "Get a funfact"
)
async def funfact(ctx):
	fact= random.choice(all_fun_facts)
	await ctx.channel.send(fact)
```

The output on Discord looks like this:
![Screenshot Output](images/Bildschirmfoto 2021-02-28 um 19.48.59.png){width=600px height=300px}

## Encouragements
Life can be frustrating. Student life can be even more frustrating, sometimes. UNIMUC will cheer you up again! You can use `uni$enc` to get some encouragement. The function works exactly the same as `uni$funfact`. However, UNIMUC can encourage you just by reading what you write in the chat. So e.g. if you write "Ich geb auf" ("I give up" in German) UNIMUC will send you some encouragement. So how does this work?

First we have two arrays. The first one `sad_words` contains all the phrases UNIMUC identifies as something sad/frustrated people would write. The second one `starter_encouragements` contains the phrases UNIMUC will answer. 

So by using `on_message(message)` UNIMUC looks out for those phrases. To prevent endless bot replies I included the first `if` statement. The rest is pretty straightforward.
```{python, eval= FALSE}
sad_words = ["Ich geb auf", "Ich schaffe das nicht", "Das ist schwer", "traurig", "schwer", "hart", "So ein Müll"]

starter_encouragements= ["Du schaffst das!", "Niemals aufgeben!", "Glaub an dich!", "Es ist immer ein Licht am Ende des Tunnels", "Work hard, cry later!"]

@bot.event
async def on_message(message):
		if message.author == bot.user:
			return

		msg = message.content
		if any(word in msg for word in sad_words):
			await message.channel.send(random.choice(starter_encouragements))
		await bot.process_commands(message)
```

Let's have a look how it works on Discord:
![Output](images/Bildschirmfoto 2021-02-28 um 20.01.09.png){width=600px height=300px}

As you can see the message just needs to contain the one word out of the `sad_words` array for UNIMUC to reply. 

## Quotes
Best comes last. This is one of my favorite features of UNIMUC. By using the `uni$quote` command, students can get an almost infinite amount of quotes from [Zenquotes](https://zenquotes.io). To work this out, I defined a `getQuote` function that will store the random quote from the website in a variable quote. The command `uni$quote` will just simply print the string into the channel on Discord.

```{python, eval= FALSE}
# THIS FUNCTION WILL EXTRACT A QUOTE FROM ZENQUOTES.IO
def getQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
```
The output looks like this:
![](images/Bildschirmfoto 2021-02-28 um 20.09.37.png){width=600px height=300px}

So whenver you need an inspirational quote `uni$quote` is the way to go!
