import discord
import core
import asyncio
import enum

#email@email.com:password
fp_infos = open("infos.txt", "r")
infos = fp_infos.read().split(':')
fp_infos.close()


client = discord.Client()

array_of_fuckbois = ["rito yi"]
nelsonArr = ["nice", "10/10", "beautiful", "ass", "yoona", "taeyeon"]
musclehead = ["gains", "lift", "gym", "protein", "situp", "pushup", "squat", "bench"]
wan = ["wan", "csgo", "play", "wan?"]
drive_array = ["drive", "drove", "driving"]
#online_message = "```Chinatown Discord Bot is now online!\n" +\
#				 "Type !help for a list of commands.```"


fp_kappa = open("kappaLibrary.txt", "r")
kappa_library = fp_kappa.read().split('\n')
fp_kappa.close()


#[c for c in client.get_all_channels() if c.server.id == "SERVER_ID" and c.type == discord.ChannelType.text]
@client.event
async def on_ready():
	print("Bot is running as the user '{}'".format(client.user.name))
	channel = client.get_all_channels()
	for channel in client.get_all_channels():
		#print("Bot is running on server: {}, name: {}, id: {}, type: {}".format(channel.server, channel.name.encode("utf-8"), channel.id, channel.type))
		if channel.type is discord.ChannelType.text:
			print("Bot is running on server: {}, name: {}, id: {}, type: {}".format(channel.server, channel.name.encode("utf-8"), channel.id, channel.type))
			await client.send_message(channel, online_message)

@client.event
async def on_message(msg):
	cmds = msg.content.split(' ')
	cmd = cmds[0].lower()
	mentions = msg.raw_mentions

	#Ban Wesley Here
	#if msg.author.id == "153753304751538176":
	#	ban_count = ban_count + 1
	#	if ban_count % 10 == 0:
	#		await client.send_message(msg.channel, "<@153753304751538176>, you are currently banned from using bot commands. Please contact Jason Zhang for details.")
	#		return

	for i,word in enumerate(cmds):
		if word.lower() == "trap":
			print("found, {}".format(cmds[i]))
			if cmds[i+1].lower() == "card":
				await core.commands["trapcard"](client, msg, cmds)
				break
			if cmds[i+1].lower() == "card!":
				await core.commands["trapcard"](client, msg, cmds)
				break

		if word in kappa_library:
			await core.commands["kappa_library"](client, msg, cmds, word)
			break

		if word in musclehead:
			await core.commands["musclehead"](client, msg, cmds)
			break

		if word in wan:
			await core.commands["playcsgo"](client, msg, cmds)
			break

		# posts picture only when nelson says "drive"
		#print (word.lower())
		if word.lower() in drive_array:
			print("drive author is {}".format(msg.author))
			print("drive userID is {}".format(msg.author.id))
			if msg.author.id == "93561304119255040": # Nelson's ID
				await core.commands["!partners"](client, msg, cmds)
			break

	if cmd == "shit":
		if cmds[1].lower() == "game":
			await core.commands["shit game"](client, msg, cmds)



	if cmd in core.commands:
		await core.commands[cmd](client, msg, cmds)
	if cmd in array_of_fuckbois:
		await core.commands["!rito"](client, msg, cmds)
	if cmd in nelsonArr:
		await core.commands["!nelsonSeal"](client, msg, cmds)

	if len(mentions) > 0:
		print(mentions[0])
		if mentions[0] == "142847411604160513": # userID is the bot
			await core.commands["@Me"](client, msg, cmds)
		if mentions[0] == "93775949279010816": # userID is rito
			await core.commands["!rito"](client, msg, cmds)
		# if mentions[0] == "93561304119255040": # userID is nelson


print("Starting bot...")
client.run(infos[0], infos[1])