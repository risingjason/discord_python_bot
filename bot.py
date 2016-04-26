#AUTHOR: Jason Yatfai Zhang
#GITHUB: risingjason

import discord
import core
import asyncio
import enum

#email@email.com:password
fp_infos = open("infos.txt", "r")
infos = fp_infos.read().split(':')
fp_infos.close()

client = discord.Client()

online_message = "```Chinatown Discord Bot v1.1.3 is now online!\n" +\
				 "Type !help for a list of commands.```"


fp_kappa = open("kappaLibrary.txt", "r")
kappa_library = fp_kappa.read().split('\n')
fp_kappa.close()

@client.event
async def on_ready():
	print("Bot is running as the user '{}'".format(client.user.name))
	channel = client.get_all_channels()
	for channel in client.get_all_channels():
		if channel.type is discord.ChannelType.text: #notifies all registered text channels that the bot is online
			print("Bot is running on server: {}, name: {}, id: {}, type: {}".format(channel.server, channel.name.encode("utf-8"), channel.id, channel.type))
			await client.send_message(channel, online_message)

@client.event
async def on_message(msg):
	cmds = msg.content.split(' ') # seperates the message word by word
	cmd = cmds[0].lower() # takes the first word (most commands are called using the first word of message)
	mentions = msg.raw_mentions


	if cmd in core.commands:
		await core.commands[cmd](client, msg, cmds)

	for i,word in enumerate(cmds):
		if word in kappa_library:
			await core.kappaLibrary(client, msg, cmds, word)
			break



print("Starting bot...")
client.run(infos[0], infos[1])
