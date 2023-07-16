# Discord Music Bot
A discord bot that can play music from youtube links. <br>
Invite the bot to your server: [Invite link](https://discord.com/api/oauth2/authorize?client_id=1129949491324268635&permissions=8&scope=bot).

# Commands
* `/help` - displays all the available commands
* `/p "keywords"` - finds the song on youtube and plays it in your current channel. Will resume playing the current song if it was paused
* `/q` - displays the current music queue
* `/skip` - skips the current song being played
* `/clear` - Stops the music and clears the queue
* `/leave` - Disconnected the bot from the voice channel
* `/pause` - pauses the current song being played or resumes if already paused
* `/resume` - resumes playing the current song

# Installation
To run the discord bot all you need is `python 3.4` or above.\
install dependencies of the python that are needed for the bot.\
  \
youtube_dl:
  ```md
  pip install yt-dlp
  ```

ffmpeg:
  ```md
  pip install ffmpeg
  ```
You can also use homebrew if you are using mac:
  ```md
  brew install ffmpeg
  ```

PyNaCl:
  ```md
  pip install PyNaCl
  ```

# Token
Add your Bot Token by going to the [DEVELOPER PORTAL](https://discord.com/developers/applications/).
  1. Login by using your discord account.
  2. Create New Application.
  3. Go to Bot then Add Bot.
  4. Reset Token then Copy the new Token the Paste it in the File Token in the Bot folder.
  5. Go to Privileged Gateway Intents and Enable `PRESENCE INTENT` , `SERVER MEMBERS INTENT` , `MESSAGE CONTENT INTENT` .

# Invite to Discord Server
  1. To invite the Bot to ur server go to `OAuth2` -> `URL Generator`.
  2. Set the `SCOPES" to "Bot`.
  3. Set the `BOT PERMISSIONS` to `Administrator`.
  4. Copy the `GENERATED URL` the paste it in the browser, then invite your Bot.

# Creating a bot
To create a bot follow Pawel Bes [tutorial](https://www.youtube.com/watch?v=PJDuI9n7rWE&t=325s&ab_channel=Computeshorts). 

# Deploying your bot
Lastly you'll need to deploy your bot. 
Navgate to the Bot Folder in command line:
  ```md
python main.py
  ```

