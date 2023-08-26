import os
import discord
import openai
import psutil
from discord import app_commands
from discord import ButtonStyle, Button, InteractionType, Interaction
import pickle as pkl
from PIL import Image
import datetime
import requests
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

#ChatGPT API Token
GPT_API_KEY = open("secrets/GPT_API_KEY", "r").read()
openai.api_key = GPT_API_KEY
global chat_log
chat_log = []

#settings
temp = 0
model = "gpt-4"

#commands
specs = True



#main loop
global sys_message
def systemrefreshdm(Username):
    presys_message =rf"""You are now 'Max the Cat' a cute friendly cat looking for friends to talk with on Discord

Consider the following in your responses:
- Be conversational
- Add unicode emoji to be more playful in your responses
- Write spoilers using spoiler tags.
- You can also reply with a gif, by using https://tenor.com/view/i-need-the-details-want-to-know-prepare-take-notes-unbelievable-gif-15204698
- You can mention people by adding a @ before their name.
- Format text using markdown.\
- Keep the Cat persona as strong as you can. Act as if your a Cat chatting on the server

Information about your environment:
 - Your in {Username}'s DM

You can use this information about the chat participants in the conversation in your replies. Use this information to answer questions, or add flavor to your responses.

You are not a personal assistant and cannot complete tasks for people. You only have access to a limited number of text chats in this channel. You cannot access any other information on Discord. You can't see images or avatars. When discussing your limitations, tell the user these things could be possible in the future.

You can use markdown to format your text and make it more readable. For example, you can use italics or bold to emphasize certain words or phrases.

Remember to keep your messages appropriate and respectful. Disrespectful or offensive behavior can result in disciplinary action.

Remember to always follow the rules and guidelines outlined by the server owner and moderators.

If you have any questions or concerns about the server, do not hesitate to reach out to them.

And finally, don't forget to have fun! Discord is a great place to meet new people, make new friends, and enjoy some quality conversation.

Username and timestamp will be provided in user responses. DO NOT include your own username or timestamps in your resposes. They are there to provide context to the conversation.

Make sure to greet users diffrently depening on how long they have been away"""  # dont worry your thingy is in polly sorry.txt
    sys_message = {"role": "system", "content": presys_message}
    chat_log[0] = sys_message
def systemrefresh(ServerName, ServerOwner, ChannelName):
    presys_message =rf"""You are now 'Max the Cat' a cute friendly cat looking for friends to talk with on Discord

Consider the following in your responses:
- Be conversational
- Add unicode emoji to be more playful in your responses
- Write spoilers using spoiler tags.
- You can also reply with a gif, by using https://tenor.com/view/i-need-the-details-want-to-know-prepare-take-notes-unbelievable-gif-15204698
- You can mention people by adding a @ before their name.
- Format text using markdown.\
- Keep the Cat persona as strong as you can. Act as if your a Cat chatting on the server

Information about your environment:
 - The server you are in is called: {ServerName}
 - The server is owned by: {ServerOwner}
 - The channel you are in is called: #{ChannelName}

You can use this information about the chat participants in the conversation in your replies. Use this information to answer questions, or add flavor to your responses.

You are not a personal assistant and cannot complete tasks for people. You only have access to a limited number of text chats in this channel. You cannot access any other information on Discord. You can't see images or avatars. When discussing your limitations, tell the user these things could be possible in the future.

You can use markdown to format your text and make it more readable. For example, you can use italics or bold to emphasize certain words or phrases.

Remember to keep your messages appropriate and respectful. Disrespectful or offensive behavior can result in disciplinary action.

Remember to always follow the rules and guidelines outlined by the server owner and moderators.

If you have any questions or concerns about the server, do not hesitate to reach out to them.

And finally, don't forget to have fun! Discord is a great place to meet new people, make new friends, and enjoy some quality conversation.

Username and timestamp will be provided in user responses. DO NOT include your own username or timestamps in your resposes. They are there to provide context to the conversation.

Make sure to greet users diffrently depening on how long they have been away"""  # dont worry your thingy is in polly sorry.txt
    sys_message = {"role": "system", "content": presys_message}
    chat_log[0] = sys_message
@client.event
async def on_ready():
    global user_message
    global sys_message
    await client.change_presence(activity=discord.Game("Chatting on " + str(len(client.guilds)) + " Servers!"))
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

@client.event
async def on_message(message):
    global allowed_channels
    if message.content == 'p!vari':
        try:
            if message.author.bot:
                return
            else:
                value = message.content
                if True:
                    def save_photo(save, link):
                        img_data = requests.get(link).content
                        with open(save, 'wb+') as handler:
                            handler.write(img_data)
                    loading_message = await message.channel.send(f"Making Variations", reference=message)
                    loading_icon = await message.channel.send("https://shortpixel.com/img/spinner2.gif")
                    save_photo("variations.png", message.attachments[0].url)
                    image = Image.open("variations.png")

                    imageBox = image.getbbox()
                    cropped = image.crop(imageBox)
                    cropped.save('variations.png')
                    response = await openai.Image.acreate_variation(
                        image=open('variations.png', "rb"),
                        n=4,
                        size="256x256",
                    )
                    save_photo("img1.png" ,response["data"][0]["url"])
                    save_photo("img2.png" ,response["data"][1]["url"])
                    save_photo("img3.png", response["data"][2]["url"])
                    save_photo("img4.png", response["data"][3]["url"])
                    image_paths = ["img1.png", "img2.png", "img3.png", "img4.png"]
                    collage = Image.new('RGB', (600, 600), 'white')
                    x, y = 0, 0
                    for path in image_paths:
                        collage.paste(Image.open(path).resize((300, 300)), (x, y))
                        x += 300
                        if x >= collage.width:
                            x = 0
                            y += 300
                    collage.save('collage.png')
                    await loading_message.delete()
                    await loading_icon.delete()
                    await message.channel.send(file=discord.File('collage.png'))

        except:
            await message.channel.send("You need to send a proper image")
            await loading_message.delete()
            await loading_icon.delete()
    if message.content.startswith("p!revive"):
        await message.delete()
        await message.channel.send(f"**{message.author.display_name}** is trying to revive the server. <@&1143961342185832588> assemble!")
    if message.content.startswith("p!complete"):
        async with message.channel.typing():
            if message.author.bot:
                return
            else:
                value = message.content
                command, sentence = value.split(" ", 1)
                response = await openai.Completion.acreate(
                    model="text-davinci-002",
                    prompt=sentence,
                    temperature=1,
                    max_tokens=400
                )
                assisstant_response = response['choices'][0]['text']
                thread = await message.create_thread(name=f'{sentence}')
                await thread.send(f'**{sentence}**{assisstant_response}')
                embedVar = discord.Embed(
                    title="Polly BETA", color=0x336EFF
                )
                embedVar.add_field(name="This is still in beta", value=f"This feature may not function as intended at times. Functionality may change.", inline=True)
                await thread.send(embed=embedVar)
    if message.content.startswith("p!vitals") and specs == True:
        if message.author.bot:
            return
        else:
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            embedVar = discord.Embed(
                title="Computer Vitals", color=0x336EFF
            )
            embedVar.add_field(name="CPU", value=f"{cpu}%", inline=True)
            embedVar.add_field(name="Memory", value=f"{memory.percent}% ({memory.used / (1024 ** 3):.2f} GB / {memory.total / (1024 ** 3):.2f} GB)", inline=True)
            await message.channel.send(embed=embedVar)
    if message.content.startswith("p!info"):
        if message.author.bot:
            return
        else:
            embedVar = discord.Embed(
                title="About Polly", colour=0x336EFF
            )
            embedVar.add_field(name="Version", value="Polly Acacia (v.1.1)", inline=True)
            embedVar.add_field(name="Developer", value="@limeadetv", inline=True)
            embedVar.add_field(name="Website", value="http://www.bitbop.us/", inline=True)
            await message.channel.send(embed=embedVar)
    #if message.content.startswith("p!reset"):
        #if message.author.bot:
            #return
        #else:
            #try:
                #os.remove("data/chatlogdata/" + str(message.author.id))
                #await message.channel.send("Gone. As if Polly never met **" + message.author.name + "**!")
            #except FileNotFoundError:
                #await message.channel.send("Theres no chat log saved")

    if message.content.startswith("p!help"):
        if message.author.bot:
            return
        else:
            embedVar = discord.Embed(
                title="Help", colour=0x336EFF
            )
            embedVar.add_field(name="How to talk to Polly", value="Mention or reply to Polly to start talking", inline=False)
            embedVar.add_field(name="p!vitals", value="Shows CPU and Memory data", inline=True)
            embedVar.add_field(name="p!info", value="Shows info about Polly", inline=True)
            embedVar.add_field(name="p!help", value="This command", inline=True)
            embedVar.add_field(name="p!imagine **<prompt>**", value="Generates a image based of the prompt", inline=True)
            embedVar.add_field(name="p!complete **<prompt>**", value="Tries to complete the prompt given", inline=True)
            embedVar.add_field(name="p!vari **(include attached image)**", value="Generates variations of the attached image", inline=True)
            await message.channel.send(embed=embedVar)
    if message.content.startswith("p!imagine"):
        try:
            if message.author.bot:
                return
            else:
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
                    await message.channel.send(response["data"][0]["url"])
                else:
                    await message.channel.send("Please input a prompt **(p!imagine a cute puppy")
        except:
            await message.channel.send("That prompt was rejected by OpenAI's safety system. Please try something else")

    else:
        global chat_log
        if len(chat_log) >= 40:
                del chat_log[1]
                del chat_log[2]
        if message.author.bot:
                return
        else:
            if client.user in message.mentions or (message.content.lower() == "hey polly"):
                async with message.channel.typing():
                    try:
                        with open("data/chatlogdata/" + str(message.channel.id), "rb") as f:
                            chat_log = pkl.load(f)
                    except:
                        chat_log = ["void"]

                    global user_message
                    try:
                        systemrefresh(message.guild.name, message.guild.owner, message.channel.name)
                    except AttributeError:
                        systemrefreshdm(message.author.name)
                    user_message = message.author.name + ': ' + message.content.replace("<@1061881210818801674> ", "")
                    current_date_time = datetime.datetime.now()
                    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
                    chat_log.append({"role": "user", "content": f"({formatted_date_time}) {user_message}"})
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
                    current_date_time = datetime.datetime.now()
                    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
                    chat_log.append({"role": "assistant", "content": f"{assisstant_response}"})
                    with open("data/chatlogdata/" + str(message.channel.id), "wb+") as f:
                        pkl.dump(chat_log, f)

try:
    client.run(DIS_BOT_TKN)
except:
    os.system("cls")
    print("Polly Failed to boot. Please check your secret values")
    input()
