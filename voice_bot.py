from asyncio.windows_events import NULL
import discord
import youtube_dl
from discord.ext import commands
import time

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("login")
    print("-------------------")

@client.event
async def on_message(message):
    if message.content.startswith("/퇴장"):

        try:
            voice = await message.author.voice.channel.connect()
        except:
            print("Already connected to a voice channel.")
            
        await voice.disconnect()
        await message.channel.send("보이스채널에 퇴장 ㅋ")

    if message.content.startswith("/재생"):
        voice = await message.author.voice.channel.connect()
            
        url = message.content.split(" ")[1]
        option = {
            'outtmpl' : "file/" + url.split('=')[1],
            'postprocessors' : [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',

                'preferredquality': '60',
            }],
        }


        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url, download=False)
            title = info['title']

            print(info['duration'])
        try:
            if voice.is_playing():
                print("실행중")
            else:  
                voice.play(discord.FFmpegPCMAudio("file/" + url.split('=')[1] + ".mp3")) 
                await message.channel.send(title + "틀음 ㅋ")
                time.sleep(info['duration'])
                await voice.disconnect()
                print("zzzzz")
        except:
            print("ERROR")


        
client.run('ODk3MDEyNzUzNTg2MzM1Nzc0.YWPeOg.8o8bi5-fu_9GEDo76LBFgmWbuq8')

