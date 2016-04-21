import discord
import random
import urllib.request

help_msg =  "```+-------------- Chinatown Discord Bot --------------+\n" +\
			"- !help: Gives list of commands avaliable to you.\n" +\
			"- !author: Gives the name of the creator of this bot.\n" +\
			"- !hello: Bot says hi to you.\n" +\
			"- !flipcoin : Makes the bot flip a coin.\n" +\
			"- !rolldie : Makes the bot roll a die.\n" +\
			"- !avatar : Syntax: !logo @user. Uploads an image file of the mentioned user's logo. (Currently bugged)\n" +\
			"- Twitch Emotes have been implemented. Only the first emote of each line will be read in order to reduce spam.\n" +\
			"+---------------------------------------------------+```"

author = "Jason Zhang"

#!author command
async def cmd_author(client, msg, cmds):
	await client.send_message(msg.channel, author)

#!help command
async def cmd_help(client, msg, cmds):
	await client.send_message(msg.channel, help_msg)

#!hello command
async def cmd_hello(client, msg, cmds):
	await client.send_message(msg.channel, "Hello, " + msg.author.mention + "!")

#!flipcoin command
async def cmd_flipCoin(client, msg, cmds):
	coin = random.randint(1,2)
	if coin == 1:
		await client.send_message(msg.channel, "```The coin has flipped to {}.```".format("tails"))
	elif coin == 2:
		await client.send_message(msg.channel, "```The coin has flipped to {}.```".format("heads"))

#!rolldie command
async def cmd_rollDie(client, msg, cmds):
	die = random.randint(0,5) + 1
	await client.send_message(msg.channel, "```You have rolled a {}```".format(die))

#8BALL function WIP
async def cmd_8ball(client, msg, cmds):
	eight_ball = [""]

#Twitch Chat emoticons get sent here
async def kappaLibrary(client, msg, cmds, word):
	await client.send_file(msg.channel, './emotes/{}.png'.format(word))

#!avatar command
async def cmd_avatar(client, msg, cmds):
	ments = msg.mentions
	if len(ments) == 0: #if user types !logo
		await client.send_message(msg.channel, "```Invalid syntax. No user mentioned. Correct syntax example: !logo @me```")
		return
	elif len(ments) != 1: #if user mentions more than one person
		await client.send_message(msg.channel, "```Invalid syntax. Only one user can be mentioned. Correct syntax example: !logo @me```")
		return
	else: #if user inputs correct syntax
		mentioned_user = ments[0]

		try: #makes sure a name's special character doesn't break the bot
			print(mentioned_user.name.encode('utf-8'))
		except UnicodeDecodeError:
			print("This user's name contains a special character.")

		avatar_url = mentioned_user.avatar_url
		
		if avatar_url=='': #if mentioned user is using the default avatar
			await client.send_message(msg.channel, "This user is using the default avatar.")
			return

		print(avatar_url)
		dl_avatar(avatar_url)
		await client.send_message(msg.channel, "Here is the logo for {}".format(mentioned_user.name))
		await client.send_file(msg.channel, './avatar/logo.jpg')

#downloads the logo used in cmd_logo
def dl_avatar(url):
	#prevents HTTP access denied error
	user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19'
	u = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': user_agent}))
	raw_data = u.read()
	u.close()
	#to save space, the logo gets replaced everytime !avatar is called correctly
	f = open('./avatar/logo.jpg', 'wb')
	f.write(raw_data)
	f.close()

commands =  { "!author":cmd_author, "!help":cmd_help, "!hello":cmd_hello, "!flipcoin":cmd_flipCoin, "!rolldie":cmd_rollDie,
			  "!avatar":cmd_avatar
			}