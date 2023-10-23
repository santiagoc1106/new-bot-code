# new-bot-code

# Brief summary of this project prompt in your own words
The project prompt was to make a bot that could be accessed and interacted with in the Discord server.

# Explanation of what you chose and why, and what “being successful” meant to you
I chose to make a bot that could play music, pause it, and resume. Being successful really means just being able to make the bot play and pause music.

# Full explanation of what your program does
My bot can join/leave voice channels at the request of the user. It can also play, pause, and resume music. 
- The playsong command works by having the bot recognize if it's in a voice channel. If not, then the bot sends the message: "I am not connected to a voice channel rn". If it is, then it will extract an audio file, then play it using ffmpeg.exe
-The pause command works by seeing if anything is playing at the moment. If not, then it sends the message: "I am not playing anything at the moment!!!!!". If there is something playing, then it pauses the music using await voice_client.pause(). 
-The resume command makes the bot resume any music that has been paused. If nothing is paused, then it sends the message: "I was not playing anything before this!!!! Use playsong command!!!!". If there is something paused, then it will use the command await voice_client.resume().
- The bot can also put a gif and say hello when it is activated, using the on_ready command. So whenever it is activated, the but checks what server it's in, then sends the message "Bot activated.." and a gif. The deets of the server are also posted on the terminal.

# ID any “skeleton” sources that make up the bones of your code
- https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1
- This source helped me understand and build my bot line by line as I did not understand it at first. I broke down the code into sections and tried to explain as best as I can how the code worked

- https://www.youtube.com/watch?v=dRHUW_KnHLs
-  This source helped me mainly on how to use ffmpeg.exe on my Python code.

# Full explanation of how your code improves upon any skeleton code
I used the code given to me to make my bot more like my bot, so it doesn't behave or have responses like a normal bot. 

Any other info that will help your target audience understand your code
Not applicable.
