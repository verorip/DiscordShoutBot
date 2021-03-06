# bot.py
import os
import time
import discord
from discord.ext import commands
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix='$')


blacklist = []

@commands.command()
async def p(ctx, member:discord.Member, *args):

    await ctx.message.channel.purge(limit=1)
    if(any([blacklist[i] in member.display_name for i in range(len(blacklist))])):
        print('nope')
        return

    guild = ctx.guild
    old_channel = member.voice.channel
    channel = discord.utils.get(guild.voice_channels, name='PunishChanel')
    if channel==None: return
    await member.edit(voice_channel=channel)
    vc = await channel.connect()

    vc.play(discord.FFmpegPCMAudio(executable="D:/Python/DiscordShoutBot/ffmpeg-20200831-4a11a6f-win64-static/bin/ffmpeg.exe", source="testing.mp3"), after=lambda e: print('done', e))
    while vc.is_playing():
        time.sleep(1.0)
    await member.edit(voice_channel=old_channel)
    await vc.disconnect()



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


bot.add_command(p)
bot.run('token')
