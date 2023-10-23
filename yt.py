import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import yt_dlp
from yt_dlp import YoutubeDL
from discord import Embed, FFmpegPCMAudio
import asyncio

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = ".", intents = intents)

yt_dlp.utils.bug_reports_message = lambda: ''
#using youtube_dl source: "https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1"
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename
    

#allow bot to join voice channel where the person wants source: "https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1"
@bot.command()
async def join_me(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You're not connected to a voice channel rn".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

#makes bot leave channel
@bot.command()
async def leave_me(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("I am not connected to a voice channel rn")

#commands for music


@bot.command()
async def playsong(ctx,url):
    
    try :
        #sees if bot is in the vc
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            #grabs file from downloaded url
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            #plays song using ffmpeg
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
            await ctx.send('**Now playing:** {}'.format(filename))

    except :
        await ctx.send("I am not connected to a voice channel rn")


@bot.command()
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    #sees if music/audio is playing
    if voice_client.is_playing():
        #pauses
        await voice_client.pause()
    else:
        await ctx.send("I am not playing anything at the moment!!!!!")

@bot.command()
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("I was not playing anything before this!!!! Use playsong command!!!!")

@bot.command()
async def pausesong(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
       await voice_client.stop()

    else:
        await ctx.send("There is nothing to pause :(")



@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "santi-botting" :
                await channel.send('Bot Activated..')
                await channel.send(('https://tenor.com/view/kid-named-finger-wawa-gif-26530459'))
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))

@bot.command()
async def who_r_u(ctx):
    text = "I am the second bot after the first one broke\nI was birthed by santi."
    await ctx.send(text) 

bot.run(TOKEN)