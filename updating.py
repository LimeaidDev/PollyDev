import os
import discord
from discord import app_commands
os.system("cls")

if open("secrets/DIS_BOT_TKN", "r").read() == "":
    print("It seems like theres no Discord Bot token. Please Enter your token below\n")
    open("secrets/DIS_BOT_TKN", "w").write(input())
if open("secrets/GPT_API_KEY", "r").read() == "":
    print("It seems like theres no OpenAI API key. Please Enter your key below\n")
    open("secrets/GPT_API_KEY", "w").write(input())

#Discord Bot Token
DIS_BOT_TKN = open("secrets/DIS_BOT_TKN", "r").read()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    global user_message
    global sys_message
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Working On Updates"))
    os.system("cls")

try:
    client.run(DIS_BOT_TKN)
except:
    os.system("cls")
    print("Polly Failed to boot. Please check your secret values")
    input()
