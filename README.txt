Overview:

	Discord bot that will send weekly messages to users in the channel.
	Using this code for class reminders 	

Set up:

	bot_schedule var stores information of classes
	structure is
		number key : [Class name, Zoom link or any other link, time (send to channel), embeded image, military time hour, min, day (sunday = 0)]

	bot.run("Put discord bot token");
	If you do not know how to get a token go to discords developers page and make one.

	To Start the alarm/s type "start-alarm" to the bot
		The bot will respond by sending "starting alarms"

	Install Discord py api
		Make sure you have the correct python version

created on:
	Python v3.8
	Discord pypi v1.5.1
