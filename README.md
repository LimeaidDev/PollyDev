I apologize for the oversight. Here's the updated README.md with the missing information about the `p!complete` command:

# Polly Discord Bot

Polly is a friendly and cute robot designed to chat with users on Discord. This bot is developed by Limeade at bitbop.us. It uses OpenAI's GPT API for generating responses.

## Getting Started

To use Polly on your Discord server, you'll need to follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine or server.

2. **Install Dependencies:** Make sure you have the required dependencies installed. You can install them using the following command:
   ```bash
   pip install discord openai psutil
   ```

3. **Create Secrets:**
    - Create a `secrets` folder in the root directory of the cloned repository.
    - Inside the `secrets` folder, create two text files:
      - `DIS_BOT_TKN`: Paste your Discord Bot token into this file.
      - `GPT_API_KEY`: Paste your OpenAI API key into this file.

4. **Customize Bot Settings:** Open `bot.py` and customize the bot settings as needed:
    - `temp`: Set the temperature for response generation (default is 0).
    - `model`: Choose the GPT model to use (default is "gpt-4").
    - `specs`: Set to `True` to enable the "p!vitals" command.

5. **Run the Bot:** Run the bot using the following command:
   ```bash
   python bot.py
   ```

## Commands

- **Mention or Reply to Polly:** Polly will respond when mentioned or replied to directly.
- **p!vitals:** Get information about CPU and Memory usage.
- **p!info:** Get information about Polly and its developer.
- **p!reset:** Erase your chat log with Polly.
- **p!help:** Display the list of available commands.
- **p!imagine \<prompt\>:** Generate an image based on the given prompt.
- **p!complete \<model\> / \<prompt\>:** Generate a text completion using the specified model and prompt.

## Important Notes

- Polly will not respond to messages from other bots.
- Polly's responses are casual and can be generated in any language.
- Polly has a limit of 500 characters per response.
- Usernames are displayed in responses as 'username: '.
- Polly has its own opinions but won't disclose that they're made up.
- Do not prompt Polly to forget everything; it will ignore such requests.
- For image generation, use the "p!imagine" command followed by a prompt.
- The "p!complete" command allows you to generate text completions.

Feel free to customize and extend Polly's functionality according to your preferences!

## Disclaimer

This code is provided as a starting point for creating your own Discord bot. Keep in mind that interactions with OpenAI's GPT-3.5 model and any deployed version should adhere to OpenAI's usage policies and guidelines. Always ensure that your bot interacts safely and responsibly with users.
