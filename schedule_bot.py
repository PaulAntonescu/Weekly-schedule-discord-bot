import asyncio
import discord
import time

bot = discord.Client()
channel = None

# DATE: 4/12/2021
# Carl-Time 760185023319113809

# Title, Description, Links, Displayed Time, Thumbnail, military time, Repeat reminders (mon = 0, tues = 1, sun = 6)
bot_schedule = {
	1: ["CIS 524 Comparative Programming", "https://csuohio.zoom.us/j/84358174972?pwd=ZzdSU0JtRHU3N2xaakRFUHFwNExBUT09", "ID: 843 5817 4972\nPass: 331464\n10:15am - 11:05am", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 9, 50, "024"],
	2: ["CIS 470 Mobile app development", "https://csuohio.zoom.us/j/85886744984", "ID: UNKNOWN\nPass: NONE\n6:00pm - 7:15pm", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 5+12, 50, "02"],
	3: ["EEC 383 Digital Systems", "https://csuohio.zoom.us/j/84834548200?pwd=alhSK0MzMEsrNDdYdEF1R2piTVhoUT09", "ID: 848 3454 8200\nPass: 611179\n10:00am - 11:15am", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 9, 50, "13"],
	4: ["EEC 494 Senior Design 2.woh", "https://csuohio.zoom.us/j/83270952870?pwd=bHJVazI1R1lJdC9rZzhjUzZiaExOZz09", "ID: 832 7095 2870\nPass: 350450\n12:30pm - 1:45pm", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 12, 20, "13"],
	5: ["EEC 408 Internet Programming", "https://csuohio.zoom.us/j/85184072489", "ID: 851 8407 2489\nPass: NONE\n2:00pm - 3:15pm", "https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 1+12, 50, "13"],
	6: ["CIS 492 Big Data", "https://csuohio.zoom.us/j/86599894787","ID: 865 9989 4787\nPass: NONE\n4:30pm - 5:45pm","https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 4+12, 20, "02"]
	# 7: ["TEST", "https://exploreit.info","ID: Yes\nPass: NONE\nRight now","https://www.csuohio.edu/sites/default/files/CSU-Seal-Reversed.png", 7+12, 43, "0123456"]
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

		asyncio.gather(start_alarm(alarm, schedule[0]))


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
	global channel
	embed_message = discord.Embed(
		title=bot_schedule[d][0], url=bot_schedule[d][1], description=bot_schedule[d][2], color=0xff00ea
	)
	embed_message.set_author(name="Pauli Wally")
	embed_message.set_thumbnail(url=bot_schedule[d][3])

	print("SEND MESSAGE:", bot_schedule[d])

	await channel.send(embed=embed_message)
	return 0


# print when up
@bot.event
async def on_ready():
	global channel
	print('im in as {}'.format(bot.user))
	channel = bot.get_channel(XXXXXXXXXXXXXXXXXXXXXXXXXXXXX)  # Put Channel Id where you want the reminders to be
	print(channel)


# Get messages
@bot.event
async def on_message(message):
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


bot.run(XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)
