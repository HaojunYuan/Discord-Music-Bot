# Siren
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

