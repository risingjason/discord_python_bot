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

threeQ = "```" #creates fancy text on discord text chat
author = "Jason Zhang"

voter_id = []
vote_once = {}

#!help command
async def cmd_help(client, msg, cmds):
	await client.send_message(msg.channel, help_msg)

#!author command
async def cmd_author(client, msg, cmds):
	await client.send_message(msg.channel, author)

#!hello command
async def cmd_hello(client, msg, cmds):
	await client.send_message(msg.channel, "Hello, " + msg.author.mention + "!")

#8BALL function WIP
async def cmd_8ball(client, msg, cmds):
	eight_ball = [""]

#Twitch Chat emoticons get sent here
async def kappaLibrary(client, msg, cmds, word):
	await client.send_file(msg.channel, './emotes/{}.png'.format(word))

#!rolldie command
async def cmd_rollDie(client, msg, cmds):
	die = random.randint(0,5) + 1
	await client.send_message(msg.channel, threeQ + "You have rolled a {}".format(die) + threeQ)

#!flipcoin command
async def cmd_flipCoin(client, msg, cmds):
	coin = random.randint(1,2)
	if coin == 1:
		await client.send_message(msg.channel, threeQ + "The coin has flipped to {}.".format("tails") + threeQ)
	elif coin == 2:
		await client.send_message(msg.channel, threeQ + "The coin has flipped to {}.".format("heads") + threeQ)

#vote command
async def cmd_vote(client, msg, cmds):
	# if user only types !vote
	if len(cmds) == 1:
		await client.send_message(msg.channel, "`Invalid syntax. Needs two arguments.`")
		return

	# if user types !vote [insert wrong command here]
	if cmds[1] != "stop" and cmds[1] != "yes" and cmds[1] != "no" and cmds[1] != "start":
		await client.send_message(msg.channel, "`Invalid syntax. Needs two arguments.`")
		return

	# start vote
	if len(voter_id) == 0 and cmds[1] == "start":
		voter_id.append(msg.author.id)
		voter_id.append(0)
		print(voter_id[0])
	elif len(voter_id) != 0: #there is a vote already happening
		await client.send_message(msg.channel, "`A vote is currently going on.`")

	# only the person who started the vote can stop it
	if (voter_id[0] == "" + msg.author.id) and (cmds[1].lower() == "stop"):
		if voter_id[1] > 0:
			await client.send_message(msg.channel, "`Yes wins.`")
		elif voter_id[1] < 0:
			await client.send_message(msg.channel, "`No wins.`")
		else:
			await client.send_message(msg.channel, "`Tie.`")

		del voter_id[:]
		return

	# if user hasn't cast a vote yet
	if vote_once.get(msg.author.id) != 1:
		vote_once.update({msg.author.id : 0})
		
		# counts the amount of yes and no vote
		if cmds[1].lower() == "yes":
			voter_id[1] += 1
			vote_once[msg.author.id] += 1
			print("vote count = " + voter_id[1])
		elif cmds[1].lower() == "no":
			voter_id[1] += 1
			vote_once[msg.author.id] += 1
			print("vote count = " + voter_id[1])
	# if user has already cast a vote
	elif vote_once.get(msg.author.id) == 1:
		await client.send_message(msg.channel, "`" + msg.author.name + ", you have already voted.`")

#!avatar command
async def cmd_avatar(client, msg, cmds):
	ments = msg.mentions
	if len(ments) == 0: #if user !types !logo
		await client.send_message(msg.channel, "`Invalid syntax. No user mentioned. Correct syntax example: !logo @me`")
		return
	elif len(ments) != 1: #if user mentions more than one person
		await client.send_message(msg.channel, "`Invalid syntax. Only one user can be mentioned. Correct syntax example: !logo @me`")
		return
	else: #if user inputs correct syntax
		mentioned_user = ments[0]

		try: #makes sure a name's special character doesn't break the bot
			print(mentioned_user.name.encode('utf-8'))
		except UnicodeDecodeError:
			print("`This user's name contains a special character.`")

		avatar_url = mentioned_user.avatar_url
		
		if avatar_url=='': #if mentioned user is using the default avatar
			await client.send_message(msg.channel, "`This user is using the default avatar.`")
			return

		print(avatar_url)
		dl_avatar(avatar_url)
		await client.send_message(msg.channel, "`Here is the logo for {}`".format(mentioned_user.name))
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
			  "!avatar":cmd_avatar, "!vote":cmd_vote
			}
