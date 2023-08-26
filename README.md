# Polly Discord Bot

Polly is a friendly and interactive Discord bot developed by Limeade. Polly is powered by OpenAI's GPT models and is designed to engage in casual conversations with users. This repository contains the code for the Polly Discord bot, allowing you to customize and deploy your own version of Polly.

## Setup

Follow the steps below to set up and customize your own Polly Discord bot:

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Add Tokens**: Open `secrets/DIS_BOT_TKN` and add your Discord bot token, and open `secrets/GPT_API_KEY` and add your OpenAI API key.

3. **Customize Settings**: Open `pollyruntime.py` and modify the settings according to your preferences:

   - `temp`: The temperature parameter controls the randomness of the bot's responses. Adjust this value to make Polly's responses more focused or creative.
   - `model`: Specify the GPT model to be used. You can choose from models like "gpt-3.5-turbo" or "gpt-4", depending on your OpenAI subscription.
   - `specs`: Set this variable to `True` if you want to enable the `p!vitals` command, which displays CPU and memory usage statistics.

4. **Run the Bot**: Double-click `start.bat` to run the bot. This script installs dependencies and runs the bot.

## Usage

Polly comes with a set of commands that users can interact with:

- Mention or reply to Polly to start a conversation.
- `p!vitals`: If enabled, displays CPU and memory usage data.
- `p!info`: Shows information about Polly.
- `p!help`: Displays the list of available commands.
- `p!imagine **<prompt>**`: Generates an image based on the provided prompt.
- `p!complete **<prompt>**`: Initiates completion of a sentence using OpenAI's language model.
- `p!vari **(include attached image)**`: Generates variations of the attached image.

## Customization

You can customize Polly's introduction message based on the environment it's in: main server channels or direct messages (DMs). Open `pollyruntime.py` and locate the `presys_message` variable. Depending on the context, you can modify both the main `presys_message` for server channels and the DM `presys_message` for direct messages.

### Main Server Channels (presys_message)

The `presys_message` variable controls what Polly says when introduced in a main server channel. Customize it to match your desired persona and behavior for interactions in server channels. Here are a few tips:

- Be conversational and playful to engage users.
- Use Unicode emojis to add a playful touch to your responses.
- Consider the cat persona and act as if you're a cat chatting on the server.
- Use markdown to format text and make it more readable.
- You can mention participants by adding a `@` before their names.

Information about the environment, server, and channel can be included in your responses for context. Remember to follow the server's rules and guidelines.

### Direct Messages (DM) (presys_message)

The DM `presys_message` variable controls Polly's introduction in direct messages. Customize it to create a distinct persona for interactions in DMs. Here are some suggestions:

- Adjust your tone to be more personal and friendly.
- Tailor your responses to a one-on-one conversation context.
- Provide information about Polly's capabilities and limitations.
- Mention that usernames and timestamps will be included in user responses for context.

Feel free to add a warm welcome to users who reach out to Polly via DMs.

Remember to save your changes and restart the bot for them to take effect.

## Running the Bot

The provided `start.bat` batch file takes care of installing necessary packages and running the bot. To keep the bot running, the batch file executes the `loop.py` script, which continuously runs the `pollyruntime.py` code, ensuring that the bot stays active.

Please note that running the bot in a production environment might require additional considerations, such as hosting and proper error handling.

## Disclaimer

Keep in mind that this code is provided as-is and may require updates or modifications to work with future changes in dependencies or APIs. Additionally, please review and comply with the terms of use for both Discord and OpenAI when deploying and using the bot.
