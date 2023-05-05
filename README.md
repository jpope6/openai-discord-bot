# Customizable Discord Bot

A Discord bot built using OpenAI's GPT-3.5 Turbo that can be easily customized by changing the `MY_PROMPT` variable. This allows you to make the bot take on any personality or style you want.

## Features

- Powered by OpenAI's GPT-3.5 Turbo
- Customizable behavior by changing `MY_PROMPT`
- Responds to user messages in a consistent manner according to the defined prompt

## Prerequisites

To use this Discord bot, you'll need:

- A Discord API token
- An OpenAI API key

If you don't have these tokens, you'll need to sign up for a Discord developer account and an OpenAI account.

## Customizing the Bot

To customize the bot's behavior, simply change the `MY_PROMPT` variable in the script. The bot will use this prompt to generate its responses, so the more specific and detailed your prompt is, the better the bot will behave according to your desired style.

Example:
```
MY_PROMPT = """
You are an informative and helpful Discord bot. Always answer the user's questions accurately and politely.
Your main focus is to assist users with their queries.
"""
```

## Setting Up

1. Clone this repository
2. Install the required dependencies: `pip install openai discord.py python-dotenv`
3. Create a `.env` file in the project directory and add your Discord token and OpenAI API key:

```
API_KEY=your_openai_api_key
DISCORD_TOKEN=your_discord_token
```

4. Run the bot: `python bot.py`

Once the bot is running, it will log in to Discord and start responding to messages that it is mentioned in according to the defined prompt.

Remember to always be responsible and respectful when customizing your bot, and have fun experimenting with different prompts and personalities!
