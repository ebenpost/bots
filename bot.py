# bot.py
import discord
import os
import random

from discord.ext import commands
#from dotenv import load_dotenv

print("Starting bot...")

#load_dotenv()
#TOKEN_START = '.X0EBAw.y5XXTUrcbUmCcElSAQW3tnN2e0U'
TOKEN = os.getenv('DISCORD_TOKEN')
#TOKEN = TOKEN+TOKEN_START

bot = commands.Bot(command_prefix = '.', case_insensitive=True)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)}ms ')

@bot.command()
async def kills(ctx):
    await ctx.send("you made kills")

@bot.command()
async def place(ctx):
    await ctx.send("you where placed 6th")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. {error}')


@bot.event
async def on_message(msg):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	await bot.process_commands(msg)
	if msg.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await msg.channel.send("hey you sexy thing")

print("Bot is ready!")
bot.run(TOKEN)
print("Bot is closing!")
