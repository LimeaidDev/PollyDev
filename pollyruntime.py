import os
import aiohttp.client_exceptions
import discord
import discord.errors
import openai
import openai.error
import psutil
from discord import app_commands
import pickle as pkl
from PIL import Image
import datetime
import requests
import asyncio
os.system("cls")

try:
    os.remove("kill.txt")
except:
    print()

def unlockkill():
    os.remove(".lock")
    exit()


def update_log(text: str):
    with open("data/settingsdata/text.txt", "a+") as log:
        log.seek(0)
        content = log.read()
        print(content + text + "\n")
        print(content)
        print(text)
        log.write(text + "\n")

def settingsrefresh():
    global temp
    global model
    global prefix
    temp = int(open("data/settingsdata/temp").read())
    model = str(open("data/settingsdata/model").read())
    prefix = str(open("data/settingsdata/prefix").read())

if open("secrets/DIS_BOT_TKN", "r").read() == "":
    update_log("[ERROR] Discord bot token is missing. Please check your secret values.")
    unlockkill()
if open("secrets/GPT_API_KEY", "r").read() == "":
    update_log("[ERROR] Openai API key is missing. Please check your secret values.")
    unlockkill()

#Discord Bot Token
DIS_BOT_TKN = open("secrets/DIS_BOT_TKN", "r").read()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#ChatGPT API Token
GPT_API_KEY = open("secrets/GPT_API_KEY", "r").read()
openai.api_key = GPT_API_KEY
global chat_log
chat_log = []

version = "Polly Begonia v.1.0Alpha"

#commands
specs = True

#main loop
global temp
global model
global sys_message
def systemrefreshdm(Username):
    systemfile = str(open("data/settingsdata/system").read())
    presys_message = rf"""{str(open(f"data/systems/{systemfile}").read())}

Consider the following in your responses:
- Be conversational
- Write spoilers using spoiler tags.
- You can mention people by adding a @ before their name.
- Format text using markdown.\

Information about your environment:
 - Your in {Username}'s DM

You can use this information about the chat participants in the conversation in your replies. Use this information to answer questions, or add flavor to your responses.

You are not a personal assistant and cannot complete tasks for people. You only have access to a limited number of text chats in this channel. You cannot access any other information on Discord. You can't see images or avatars. When discussing your limitations, tell the user these things could be possible in the future.

You can use markdown to format your text and make it more readable. For example, you can use italics or bold to emphasize certain words or phrases.

Remember to keep your messages appropriate and respectful. Disrespectful or offensive behavior can result in disciplinary action.

Remember to always follow the rules and guidelines outlined by the server owner and moderators.

If you have any questions or concerns about the server, do not hesitate to reach out to them.

And finally, don't forget to have fun! Discord is a great place to meet new people, make new friends, and enjoy some quality conversation.

DO NOT include your own username or timestamps in your resposes. They are there to provide context to the conversation.

Make sure to greet users diffrently depening on how long they have been away\

Try to match the size of the users chats to your own

The usernames provided are Display names so dont use @ symbolises

Keep your messages short"""  # For main channels
    sys_message = {"role": "system", "content": presys_message}
    chat_log.insert(0, sys_message)

def systemrefresh(ServerName, ServerOwner, ChannelName, ChannelTopic, username):
    systemfile = str(open("data/settingsdata/system").read())
    try:
        systemmessage = str(open(f"data/systems/{systemfile}").read())
    except:
        systemmessage = str(open(f"data/systems/polly.txt").read())
    presys_message = rf"""{systemmessage}

Consider the following in your responses:
- Be conversational
- Write spoilers using spoiler tags.
- You can mention people by adding a @ before their name.
- Format text using markdown.\

Information about your environment:
 - The server you are in is called: {ServerName}
 - The server is owned by: {ServerOwner}
 - The channel you are in is called: #{ChannelName}
 - The channel topic provided is: {ChannelTopic}
 - and the user that messaged you is {username} but call them by the name given in there messages\
 
Heres a list of the commands users can use from you:\
 - {prefix}vari
 - {prefix}complete
 - {prefix}vitals
 - {prefix}help
 - {prefix}imagine
You can use this information about the chat participants in the conversation in your replies. Use this information to answer questions, or add flavor to your responses.

You are not a personal assistant and cannot complete tasks for people. You only have access to a limited number of text chats in this channel. You cannot access any other information on Discord. You can't see images or avatars. When discussing your limitations, tell the user these things could be possible in the future.

You can use markdown to format your text and make it more readable. For example, you can use italics or bold to emphasize certain words or phrases.

Remember to keep your messages appropriate and respectful. Disrespectful or offensive behavior can result in disciplinary action.

Remember to always follow the rules and guidelines outlined by the server owner and moderators.

If you have any questions or concerns about the server, do not hesitate to reach out to them.

And finally, don't forget to have fun! Discord is a great place to meet new people, make new friends, and enjoy some quality conversation.

DO NOT include your own username or timestamps in your resposes. They are there to provide context to the conversation.

Make sure to greet users diffrently depening on how long they have been away

Try to match the size of the users chats to your own

The usernames provided are Display names so dont use @ symbolises

Keep your messages short"""  # For
    sys_message = {"role": "system", "content": presys_message}
    chat_log.insert(0, sys_message)


async def killcheck():
    while True:
        if os.path.isfile("kill.txt"):
            os.remove("kill.txt")
            update_log(f"[INFO] Disconnected from {client.user.name}")
            exit()
        await asyncio.sleep(1)



@client.event
async def on_ready():
    update_log(f"[INFO] Connected to {client.user.name}")
    settingsrefresh()
    global user_message
    global sys_message
    await client.change_presence(activity=discord.Streaming(name=version, url="https://bitbop.us"))
    os.system("cls")
    print(r"""
,-.----.
\    /  \              ,--,    ,--,
|   :    \           ,--.'|  ,--.'|
|   |  .\ :   ,---.  |  | :  |  | :
.   :  |: |  '   ,'\ :  : '  :  : '
|   |   \ : /   /   ||  ' |  |  ' |        .--,
|   : .   /.   ; ,. :'  | |  '  | |      /_ ./|
;   | |`-' '   | |: :|  | :  |  | :   , ' , ' :
|   | ;    '   | .; :'  : |__'  : |__/___/ \: |
:   ' |    |   :    ||  | '.'|  | '.'|.  \  ' |
:   : :     \   \  / ;  :    ;  :    ; \  ;   :
|   | :      `----'  |  ,   /|  ,   /   \  \  ;
`---'.|               ---`-'  ---`-'     :  \  \
  `---`                                   \  ' ;
                                           `--`  """)
    print(r"""Polly Build 2
Developed By: Limeade                bitbop.us""")
    await killcheck()

@client.event
async def on_message(message):
    settingsrefresh()
    if not message.author.bot:
        if message.content == f'{prefix}vari':
            try:
                def save_photo(save, link):
                    img_data = requests.get(link).content
                    with open(save, 'wb+') as handler:
                        handler.write(img_data)

                loading_message = await message.channel.send(f"Making Variations", reference=message)
                loading_icon = await message.channel.send("https://shortpixel.com/img/spinner2.gif")
                save_photo("data/imgtemp/variations.png", message.attachments[0].url)
                image = Image.open("data/imgtemp/variations.png")

                imageBox = image.getbbox()
                cropped = image.crop(imageBox)
                cropped.save('data/imgtemp/variations.png')

                # Request variation of sent image
                response = await openai.Image.acreate_variation(
                    image=open('data/imgtemp/variations.png', "rb"),
                    n=4,
                    size="256x256",
                    )

                save_photo("data/imgtemp/img1.png", response["data"][0]["url"])
                save_photo("data/imgtemp/img2.png", response["data"][1]["url"])
                save_photo("data/imgtemp/img3.png", response["data"][2]["url"])
                save_photo("data/imgtemp/img4.png", response["data"][3]["url"])
                image_paths = ["data/imgtemp/img1.png", "data/imgtemp/img2.png", "data/imgtemp/img3.png", "data/imgtemp/img4.png"]

                collage = Image.new('RGB', (600, 600), 'white')
                x, y = 0, 0
                for path in image_paths:
                    collage.paste(Image.open(path).resize((300, 300)), (x, y))
                    x += 300
                    if x >= collage.width:
                        x = 0
                        y += 300

                collage.save('data/imgtemp/collage.png')

                await loading_message.delete()
                await loading_icon.delete()
                await message.channel.send(file=discord.File('data/imgtemp/collage.png'))

            except:
                await message.channel.send("You need to send a proper image")
                await loading_message.delete()
                await loading_icon.delete()

        if message.content.startswith(f"{prefix}revive"):
            await message.delete()
            await message.channel.send(f"**{message.author.display_name}** is trying to revive the server. <@&1143961342185832588> assemble!")

        if message.content.startswith(f"{prefix}complete"):
            async with message.channel.typing():
                value = message.content
                command, sentence = value.split(" ", 1)

                # Send completion request
                response = await openai.Completion.acreate(
                    model="text-davinci-002",
                    prompt=sentence,
                    temperature=1,
                    max_tokens=400
                )

                # Pick response
                assisstant_response = response['choices'][0]['text']

                thread = await message.create_thread(name=f'{sentence}')

                # Create a thread for the response
                await thread.send(f'**{sentence}**{assisstant_response}')

                embedVar = discord.Embed(
                    title="Polly BETA", color=0x336EFF
                )
                embedVar.add_field(name="This is still in beta", value=f"This feature may not function as intended at times. Functionality may change.", inline=True)
                await thread.send(embed=embedVar)

        if message.content.startswith(f"{prefix}vitals") and specs == True:
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            embedVar = discord.Embed(
                title="Computer Vitals", color=0x336EFF
            )

            embedVar.add_field(name="CPU", value=f"{cpu}%", inline=True)
            embedVar.add_field(name="Memory", value=f"{memory.percent}% ({memory.used / (1024 ** 3):.2f} GB / {memory.total / (1024 ** 3):.2f} GB)", inline=True)

            await message.channel.send(embed=embedVar)

        if message.content.startswith(f"{prefix}info"):
            embedVar = discord.Embed(
                title="About Polly", colour=0x336EFF
            )

            embedVar.add_field(name="Version", value="Polly Begonia v2.1Aplha", inline=True)
            embedVar.add_field(name="Developer", value="@limeadetv", inline=True)
            embedVar.add_field(name="Website", value="http://www.bitbop.us/", inline=True)

            await message.channel.send(embed=embedVar)

        if message.content.startswith(f"{prefix}help"):
            embedVar = discord.Embed(
                title="Help", colour=0x336EFF
            )

            embedVar.add_field(name=f"How to talk to {client.user.name}", value=f"Mention or reply to {client.user.name} to start talking", inline=False)
            embedVar.add_field(name="p!vitals", value="Shows CPU and Memory data", inline=True)
            embedVar.add_field(name="p!info", value=f"Shows info about {client.user.name}", inline=True)
            embedVar.add_field(name="p!help", value="This command", inline=True)
            embedVar.add_field(name="p!imagine **<prompt>**", value="Generates a image based of the prompt", inline=True)
            embedVar.add_field(name="p!complete **<prompt>**", value="Tries to complete the prompt given", inline=True)
            embedVar.add_field(name="p!vari **(include attached image)**", value="Generates variations of the attached image", inline=True)
            await message.channel.send(embed=embedVar)

        if message.content.startswith(f"{prefix}imagine"):
            try:
                value = message.content
                command, sentence = value.split(" ", 1)
                if not sentence == "":
                    loading_message = await message.channel.send(f"Generating **{sentence}**", reference=message)
                    loading_icon = await message.channel.send("https://shortpixel.com/img/spinner2.gif")

                    response = await openai.Image.acreate(
                        prompt=sentence,
                        n=1,
                        size="1024x1024",
                    )

                    await loading_message.delete()
                    await loading_icon.delete()# Remove loading message
                    await message.channel.send(f"# {sentence}")
                    await message.channel.send(response["data"][0]["url"])
                else:
                    await message.channel.send("Please input a prompt **(p!imagine a cute puppy**")
            except:
                await loading_message.delete()
                await loading_icon.delete()  # Remove loading message
                await message.channel.send("That prompt was rejected by OpenAI's safety system. Please try something else")

        else:
            global chat_log
            if len(chat_log) >= 60:
                del chat_log[0]
            if client.user in message.mentions or message.content.lower() == "hey polly" or str(message.channel.type) == "private":
                async with message.channel.typing():
                    try:
                        with open("data/chatlogdata/" + str(message.channel.id), "rb") as f:
                            chat_log = pkl.load(f)
                    except:
                        chat_log = []

                    global user_message

                    try:
                        systemrefresh(message.guild.name, message.guild.owner.display_name, message.channel.name, message.channel.topic, message.author.name)
                    except AttributeError:
                        systemrefreshdm(message.author.display_name)

                    print(message.author.display_name)

                    user_message = message.author.display_name + ': ' + message.content.replace("<@1061881210818801674> ", "")

                    current_date_time = datetime.datetime.now()
                    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

                    chat_log.append({"role": "user", "content": f"({formatted_date_time}) {user_message}"})
                    os.system("cls")
                    chat_log_readable = '\n'.join(str(item) for item in chat_log)
                    chat_log_readable = chat_log_readable.encode('utf-8', 'replace')
                    os.system("cls")
                    print(chat_log_readable.decode())
                    response = await openai.ChatCompletion.acreate(
                        model=model,
                        messages=chat_log,
                        temperature=temp
                    )

                    del chat_log[0]
                    assisstant_response = response['choices'][0]['message']['content']

                    try:
                        await message.channel.send(assisstant_response.strip("\n").strip(), reference=message)
                    except:
                        await message.channel.send("Sorry, that was on us 😅", reference=message)

                    chat_log.append({"role": "assistant", "content": f"{assisstant_response}"})

                    with open("data/chatlogdata/" + str(message.channel.id), "wb+") as f:
                        pkl.dump(chat_log, f)

                    chat_log_readable = '\n'.join(str(item) for item in chat_log)
                    chat_log_readable = chat_log_readable.encode('utf-8', 'replace')
                    open("data/chatlogdata/" + str(message.channel.id) + "_readable.txt", "wb+").write(chat_log_readable)
                    os.system("cls")
                    print(chat_log_readable.decode())


try:
    client.run(DIS_BOT_TKN)
except aiohttp.client_exceptions.ClientConnectionError:
    os.system("cls")
    update_log("[ERROR] Unable to connect to Bot. Please check your internet and try again")
    unlockkill()
except discord.errors.LoginFailure:
    update_log("[ERROR] Invalid Bot key provided. Please check Bot token")
    unlockkill()
