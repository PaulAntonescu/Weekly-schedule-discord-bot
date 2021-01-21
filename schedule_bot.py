@@ -0,0 +1,86 @@
import asyncio
import discord
import time

bot = discord.Client()

# Title, Description, Links, Displayed Time, Thumbnail, military time, Repeat reminders (mon = 0, tues = 1, sun = 6)
bot_schedule = {
	1: ["CIS 524 Comparative Programming", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO", "10:15am - 11:05am", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 10, 15, "024"],
	2: ["CIS 470 Mobile app development", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO", "6:00pm - 7:17pm", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 6+12, 00, "02"],
	3: ["EEC 383 Digital Systems", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO", "10:00am - 11:15am", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 10, 00, "13"],
	4: ["EEC 494 Senior Design 2.woh", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO", "12:30pm - 1:45pm", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 12, 30, "13"],
	5: ["EEC 408 Internet Programming", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO", "2:00pm - 3:15pm", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 2+12, 00, "13"],
}


# get schedule and start alarms
def start_up_alarm():
	today_wday = time.localtime().tm_wday

	for schedule in bot_schedule.items():
		if str(today_wday) not in schedule[1][6]:
			print(schedule[1][0]+" is not today!")
			continue

		alarm = get_second(schedule[1][4], schedule[1][5])
		print(schedule[1][0]+" is today!")
		print(alarm)
		if alarm < 0:
			continue

		asyncio.gather(
			start_alarm(alarm, schedule[0])
		)


# put to sleep then send an alert
async def start_alarm(alarm, description):
	await asyncio.sleep(alarm)
	await alert(description)


# get seconds until event
def get_second(hour, minutes):
	hour_to_min = hour * 60
	seconds = (minutes + hour_to_min) * 60
	current_time_in_seconds = time.localtime().tm_hour * 60 * 60 + time.localtime().tm_min * 60
	seconds = seconds - current_time_in_seconds

	return seconds


# Send message to channel
async def alert(d):
	channel = discord.utils.get(bot.get_all_channels(), name="carl-time")
	mod = discord.utils.get(channel.guild.roles, name="mod")
	embed_message = discord.Embed(title=bot_schedule[d][0], url=bot_schedule[d][1], description=bot_schedule[d][2]+mod.mention, color=0xff00ea)
	embed_message.set_author(name="Pauli Wally")
	embed_message.set_thumbnail(url=bot_schedule[d][3])

	await channel.send(embed=embed_message)
	return 0


# print when up
@bot.event
async def on_ready():
	#asyncio.gather(start_up_alarm())
	print('im in as {}'.format(bot.user))


# Get messages
@bot.event
async def on_message(message):
	print(message.content)

	if message.content.lower() == "test":
		await message.channel.send("Testing")

	elif message.content.lower() == "start-alarm":
		send_reply = "starting alarms"
		await message.channel.send(send_reply)
		while True:
			start_up_alarm()

			# sleep until 12 am tomorrow (86400 seconds)
			current_time_in_seconds = time.localtime().tm_hour*60*60 + time.localtime().tm_min*60
			sleep_till = 86400 - current_time_in_seconds
			await asyncio.sleep(sleep_till)


bot.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')