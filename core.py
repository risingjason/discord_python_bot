import discord
import user
import os
import sys
import random
import urllib.request

help_msg =  "```+-------------- Chinatown Discord Bot --------------+\n" +\
			"- !help: Gives list of commands avaliable to you.\n" +\
			"- !author: Gives the name of the creator of this bot.\n" +\
			"- !hello: Bot says hi to you.\n" +\
			"- !flipcoin : Makes the bot flip a coin.\n" +\
			"- !rolldie : Makes the bot roll a die.\n" +\
			"- !logo : Syntax: !logo @user. Uploads an image file of the mentioned user's logo. (Currently bugged)\n" +\
			"- Twitch Emotes have been implemented. Only the first emote of each line will be read in order to reduce spam.\n" +\
			"+---------------------------------------------------+```"
#Type a question after this and the bot will give you an answer
help_chinese =  "```+-------------- Chinatown Discord Bot --------------+\n" +\
				"- 我是中国人\n" +\
				"- 你好吗\n" +\
				"- 拉啊啦啦啦\n" +\
				"+---------------------------------------------------+```"

look_son = 	"─────────────────────────▄▀▄\n" +\
			"─────────────────────────█─█  \n" +\
			"─────────────────────────█─█  \n" +\
			"─────────────────────────█─█  \n" +\
			"─────────────────────────█─█  \n" +\
			"─────────────────────────█─█  \n" +\
			"─────────────────────────█─▀█▀█▄  \n" +\
			"─────────────────────────█──█──█  \n" +\
			"─────────────────────────█▄▄█──▀█  \n" +\
			"────────────────────────▄█──▄█▄─▀█  \n" +\
			"────────────────────────█─▄█─█─█─█  \n" +\
			"────────────────────────█──█─█─█─█  \n" +\
			"────────────────────────█──█─█─█─█  \n" +\
			"────▄█▄──▄█▄────────────█──▀▀█─█─█  \n" +\
			"──▄█████████────────────▀█───█─█▄▀  \n" +\
			"─▄███████████────────────██──▀▀─█  \n" +\
			"▄█████████████────────────█─────█  \n" +\
			"██████████───▀▀█▄─────────▀█────█  \n" +\
			"████████───▀▀▀──█──────────█────█  \n" +\
			"██████───────██─▀█─────────█────█  \n" +\
			"████──▄──────────▀█────────█────█ Look son\n" +\
			"███──█──────▀▀█───▀█───────█────█ a rat!\n" +\
			"███─▀─██──────█────▀█──────█────█  \n" +\
			"███─────────────────▀█─────█────█  \n" +\
			"███──────────────────█─────█────█  \n" +\
			"███─────────────▄▀───█─────█────█  \n" +\
			"████─────────▄▄██────█▄────█────█  \n" +\
			"████────────██████────█────█────█  \n" +\
			"█████────█──███████▀──█───▄█▄▄▄▄█  \n" +\
			"██▀▀██────▀─██▄──▄█───█───█─────█  \n" +\
			"██▄──────────██████───█───█─────█  \n" +\
			"─██▄────────────▄▄────█───█─────█  \n" +\
			"─███████─────────────▄█───█─────█  \n" +\
			"──██████─────────────█───█▀─────█  \n" +\
			"──▄███████▄─────────▄█──█▀──────█  \n" +\
			"─▄█─────▄▀▀▀█───────█───█───────█  \n" +\
			"▄█────────█──█────▄███▀▀▀▀──────█  \n" +\
			"█──▄▀▀────────█──▄▀──█──────────█  \n" +\
			"█────█─────────█─────█──────────█  \n" +\
			"█────────▀█────█─────█─────────██  \n" +\
			"█───────────────█──▄█▀─────────█  \n" +\
			"█──────────██───█▀▀▀───────────█  \n" +\
			"█───────────────█──────────────█  \n" +\
			"█▄─────────────██──────────────█  \n" +\
			"─█▄────────────█───────────────█  \n" +\
			"──██▄────────▄███▀▀▀▀▀▄────────█  \n" +\
			"─█▀─▀█▄────────▀█──────▀▄──────█  \n" +\
			"─█────▀▀▀▀▄─────█────────▀─────█  \n" +\
			"─█─────────▀▄──▀───────────────﻿█\n"

author = "Jason Zhang"

#implement this message when logged in
#online_message = 	"```Chinatown Discord Bot is now online!\n" +\
#					" type !help for commands.```\n"

async def cmd_shitgame(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/shitgame.png')
	await client.delete_message(msg)

async def cmd_author(client, msg, cmds):
	await client.send_message(msg.channel, author)

async def cmd_add(client, msg, cmds):
	mentions = msg.raw_mentions
	if len(mentions) > 0:
		usr = user.User(mentions[0], 0)
		await client.send_message(msg.channel, "The userID of {} is {}".format(usr.mention, usr.id))

async def cmd_mentioned(client, msg, cmds):
	client.send_file(msg.channel, './ctMemes/whyamihere.jpg')

async def cmd_okay(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/ok.png')
	#await client.delete_message(msg)

async def cmd_shutup(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/shutup.jpg')
	await client.delete_message(msg)

async def cmd_help(client, msg, cmds):
	await client.send_message(msg.channel, help_msg)

async def cmd_helpCN(client, msg, cmds):
	await client.send_message(msg.channel, help_chinese)

async def cmd_hello(client, msg, cmds):
	await client.send_message(msg.channel, "Hello, " + msg.author.mention + "!")

async def cmd_colin(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/5dollarnip.png')

async def cmd_kenneth(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/kennethSearch.png')

async def cmd_fuckboi(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/fuckboiface.jpg')

async def cmd_nelsonSeal(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/nelsonSeal.png')

async def cmd_nelsonPussySlayer(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/turtleneckFuckboi.png')

async def cmd_muscle(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/abs.png')

async def cmd_trapCard(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/trap_card_270deg.png')

async def cmd_playcsgo(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/wan_csgo.jpg')

async def cmd_partners(client, msg, cmds):
	await client.send_file(msg.channel, './ctMemes/sidecar.png')

async def cmd_online(client, msg, cmds):
	await client.send_message(msg.channel, online_message)

async def cmd_lookson(client, msg, cmds):
	await client.send_message(msg.channel, look_son)
	await client.delete_message(msg)

async def cmd_flipCoin(client, msg, cmds):
	coin = random.randint(1,2)
	if coin == 1:
		await client.send_message(msg.channel, "```The coin has flipped to {}.```".format("tails"))
	elif coin == 2:
		await client.send_message(msg.channel, "```The coin has flipped to {}.```".format("heads"))

async def cmd_rollDie(client, msg, cmds):
	die = random.randint(0,5) + 1
	await client.send_message(msg.channel, "```You have rolled a {}```".format(die))

async def cmd_8ball(client, msg, cmds):
	eight_ball = [""]

async def cmd_kappaLibrary(client, msg, cmds, word):
	await client.send_file(msg.channel, './emotes/{}.png'.format(word))

async def cmd_logo(client, msg, cmds):
	ments = msg.mentions
	if len(ments) == 0:
		await client.send_message(msg.channel, "```Invalid syntax. No user mentioned. Correct syntax example: !logo @me```")
	elif len(ments) != 1:
		await client.send_message(msg.channel, "```Invalid syntax. Only one user can be mentioned. Correct syntax example: !logo @me```")
	else:
		mentioned_user = ments[0]
		try:
			print(mentioned_user.name.encode('utf-8'))
		except UnicodeDecodeError:
			print("This user's name contains a special character.")

		avatar_url = mentioned_user.avatar_url
		
		if avatar_url=='':
			await client.send_message(msg.channel, "This user is using the default logo.")
			return

		print(avatar_url)
		dl_logo(avatar_url)
		await client.send_message(msg.channel, "Here is the logo for {}".format(mentioned_user.name))
		await client.send_file(msg.channel, './temp/logo.jpg')

def dl_logo(url):
	user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19'
	u = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': user_agent}))
	raw_data = u.read()
	u.close()
	f = open('./temp/logo.jpg', 'wb')
	f.write(raw_data)
	f.close()

commands = { "!author":cmd_author, "!add":cmd_add, "shit game":cmd_shitgame,
			 "okay":cmd_okay, "stfu":cmd_shutup, "@Me":cmd_mentioned, "!help":cmd_help, 
			 "!hello":cmd_hello, "!help_cn":cmd_helpCN, "!colinchenidentity":cmd_colin, 
			 "!whoiskennethlee":cmd_kenneth, "!rito":cmd_fuckboi, "!nelsonSeal":cmd_nelsonSeal, "pussyslayer":cmd_nelsonPussySlayer,
		   	 "musclehead":cmd_muscle, "trapcard":cmd_trapCard, "playcsgo":cmd_playcsgo, "!lookson":cmd_lookson,
		   	 "!flipcoin":cmd_flipCoin, "!rolldie":cmd_rollDie, "!partners":cmd_partners, "!online":cmd_online, "kappa_library":cmd_kappaLibrary, "!logo":cmd_logo
		   }