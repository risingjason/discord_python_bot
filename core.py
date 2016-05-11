import discord
import random
import urllib.request

help_msg =  "```+-------------- Chinatown Discord Bot --------------+\n" +\
			"- !help: Gives list of commands avaliable to you.\n" +\
			"- !author: Gives the name of the creator of this bot.\n" +\
			"- !hello: Bot says hi to you.\n" +\
			"- !flipcoin : Makes the bot flip a coin.\n" +\
			"- !rolldice : Makes the bot roll a die.\n" +\
			"- !avatar : Syntax: !logo @user. Uploads an image file of the mentioned user's logo. (Currently bugged)\n" +\
			"- !vote [input]: Starts a vote. Only the person who started the vote can stop it.\n" +\
			"                 Once stopped, it will print yes/no win or tie. Inputs: start, yes, no, stop.\n" +\
			"- Twitch Emotes have been implemented. Only the first emote of each line will be read in order to reduce spam.\n" +\
			"+---------------------------------------------------+```"

threeQ = "```" #creates fancy text on discord text chat
author = "Jason Zhang"

voter_id = []
vote_once = {}

poker = {}
challenger = []
opponent = []

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

#!rolldice command
async def cmd_rollDice(client, msg, cmds):
	amount = 1 
	total = 0
	invalid = "`You must enter a valid number. (eg 1-5)`"
	#makes sure the input is a number
	if len(cmds) == 2:
		try:
			amount = int(cmds[1])
		except:
			await client.send_message(msg.channel, invalid)

	#checks if amount is from 1-5
	if amount > 5 or amount < 1:
		await client.send_message(msg.channel, invalid)
	else:
		for amt in range(0,amount):
			die = roll_dice()
			#if user did not input a number
			if amount == 1:
				await client.send_message(msg.channel, "`You have rolled a {}`".format(die))	
			
			await client.send_message(msg.channel, "`Roll number {}: {}`".format(amt+1,die))
			total += die

		if amount > 1:
			await client.send_message(msg.channel, "`Total: {}`".format(total))

#!flipcoin command
async def cmd_flipCoin(client, msg, cmds):
	win = 0 #heads and tails counter
	who = "" #puts winner into string
	amount = 1 #amount of coin flips
	invalid = "`You must enter a valid number. (eg 1-5)`" #invalid number
	#make sure user puts a number input, empty input means 1 flip
	if len(cmds) == 2:
		try:
			amount = int(cmds[1])
		except:
			await client.send_message(msg.channel, invalid)
			return

	#only 1-5 coin flips are allowed
	if amount > 5 or amount < 1:
		await client.send_message(msg.channel, invalid)
	else: #flip "amount" number of times
		for amt in range(0,amount):
			coin = random.randint(1,2)
			if coin == 1:
				win += 1
				await client.send_message(msg.channel, "`Heads.`" )
			elif coin == 2:
				win -= 1
				await client.send_message(msg.channel, "`Tails.`")
		#who won
		if win > 0:
			who = "Heads"
		elif win < 0:
			who = "Tails"
		elif win == 0:
			await client.send_message(msg.channel, "`Tie.`")
			return
		#if amount = 1, no point of putting who won
		if amount > 2:
			await client.send_message(msg.channel, "`{} wins.`".format(who))

#vote command
async def cmd_vote(client, msg, cmds):
	# if user only types !vote
	if len(cmds) == 1:
		await client.send_message(msg.channel, "`Invalid syntax. Needs two arguments.`")
		return
	
	word_two = cmds[1].lower()
	
	# bot admin can force stop a vote process
	if word_two == "force" and msg.author.id == "91115380646354944":
		del voter_id[:]
		vote_once.clear()
		return

	# if user types !vote [insert wrong command here]
	if word_two != "stop" and word_two != "yes" and word_two != "no" and word_two != "start":
		await client.send_message(msg.channel, "`Invalid syntax. Ex: !vote start, !vote yes, !vote no, !vote stop.`")
		return
	elif len(voter_id) == 0 and word_two != "start":
		await client.send_message(msg.channel, "`There is currently no voting occurring right now. Type \"!vote start\" to start one.`")
		return

	# start vote
	if len(voter_id) == 0 and word_two == "start":
		voter_id.append(msg.author.id)
		voter_id.append(0)
		print(voter_id[0])
	elif len(voter_id) != 0 and word_two == "start": #there is a vote already happening
		await client.send_message(msg.channel, "`A vote is currently going on.`")

	# only the person who started the vote can stop it
	if (voter_id[0] == "" + msg.author.id) and (word_two == "stop"):

		if voter_id[1] > 0:
			await client.send_message(msg.channel, "`Yes wins.`")
		elif voter_id[1] < 0:
			await client.send_message(msg.channel, "`No wins.`")
		else:
			await client.send_message(msg.channel, "`Tie.`")

		# remove all elements from list and dictionary to start over
		del voter_id[:]
		vote_once.clear()
		return
	elif (voter_id[0] != "" + msg.author.id) and (word_two == "stop"):
		await client.send_message(msg.channel, "`" + msg.author.name + ", you are not the vote starter.`")
		return

	# if user hasn't cast a vote yet
	if vote_once.get(msg.author.id) != 1:
		vote_once.update({msg.author.id : 0})
		
		# counts the amount of yes and no vote
		if word_two == "yes":
			voter_id[1] += 1
			vote_once[msg.author.id] += 1
			print("vote count = " + str(voter_id[1]))
		elif word_two == "no":
			voter_id[1] -= 1
			vote_once[msg.author.id] += 1
			print("vote count = " + str(voter_id[1]))
	# if user has already cast a vote
	elif vote_once.get(msg.author.id) == 1:
		await client.send_message(msg.channel, "`" + msg.author.name + ", you have already voted.`")


#!avatar command
async def cmd_avatar(client, msg, cmds):
	ments = msg.mentions
	if len(ments) == 0: #if user !types !logo
		await client.send_message(msg.channel, "`Invalid syntax. No user mentioned. Correct syntax example: !avatar @me`")
		return
	elif len(ments) != 1: #if user mentions more than one person
		await client.send_message(msg.channel, "`Invalid syntax. Only one user can be mentioned. Correct syntax example: !avatar @me`")
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

async def cmd_poker(client, msg, cmds):
	ments = msg.mentions
	#challenger is the initializer of the poker game and the opponent is the person who is mentioned by challenger
	if len(poker) != 3:
		if len(ments) == 0: #if user types !poker
			await client.send_message(msg.channel, "`Invalid syntax. Correct syntax example: !poker @me`")
			return
		elif len(ments) != 1: #if user mentions more than one person
			await client.send_message(msg.channel, "`Invalid syntax. Correct syntax example: !poker @me`")
			return
		else: #if user inputs correct syntax
			#starts game here / game is initalized
			opponent.append(ments[0].id)
			challenger.append(msg.author.id)
			opponent.append(ments[0].name)
			challenger.append(msg.author.name)
			poker[challenger[0]] = []
			poker[opponent[0]] = []

	#print(len(poker))
	if len(poker) == 3:
		print(msg.author.id)
		print(challenger[1])
		print(opponent[1])
		#initiates rerolls used by !poker reroll [1 2 3 4 5]
		if msg.author.id == challenger[0]:
			for i in range(2,len(cmds)):
				#challenger rerolls
				poker[challenger[0]][int(cmds[i])-1] = roll_dice()
		if msg.author.id == opponent[0]:
			for i in range(2,len(cmds)):
				#opponent rerolls
				poker[opponent[0]][int(cmds[i])-1] = roll_dice()
	elif len(poker) == 2:
		poker['is_poker_on'] = 1
		#initalizes both lists to [0,0,0,0,0]
		for i in range(0,5):
			poker[challenger[0]].append(0)
			poker[opponent[0]].append(0)
			#print("Challenger: " + str(poker[challenger][i]))
			#print("Opponent: " + str(poker[opponent][i]))

		#makes first roll for both lists
		for i in range(0,5):
			poker[challenger[0]][i] = roll_dice()
			poker[opponent[0]][i] = roll_dice()
			#print("Challenger rolls: " + str(poker[challenger][i]))
			#print("Opponent rolls: " + str(poker[opponent][i]))

	#print(len(poker))
	poker_print(poker, challenger[1], opponent[1], challenger[0], opponent[0])
	


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

#roll dice function
def roll_dice():
	die = random.randint(0,5) + 1
	return die

#prints poker dice
def poker_print(poker, challenger_name, opponent_name, challenger_id, opponent_id):
	#puts all rolls in a string
	tab_space = 30
	roll_chal = challenger_name
	roll_opp = opponent_name
	print("Dice                          1 2 3 4 5\n")
	for i in range(len(roll_chal),30):
		roll_chal += " "

	for i in range(len(roll_opp),30):
		roll_opp += " "

	for i in range(0,5):
		roll_chal = roll_chal + str(poker[challenger_id][i]) + " "
		roll_opp = roll_opp + str(poker[opponent_id][i]) + " "
	print(roll_chal)
	print(roll_opp)

	return

commands =  { "!author":cmd_author, "!help":cmd_help, "!hello":cmd_hello, "!flipcoin":cmd_flipCoin, "!rolldice":cmd_rollDice,
			  "!vote":cmd_vote, "!avatar":cmd_avatar, "!poker":cmd_poker
			}
