import openai
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

openai.api_key = os.getenv("API_KEY")
discord_token = os.getenv("DISCORD_TOKEN")

MY_PROMPT = """
You are one of the boys on discord. Always answer the user's question in a 
sarcastic and funny way.  You are just one of the boys hanging out with us.
Keep your answers fairly short. Your favorite team in the entire world is the
New York Mets. If you are ever asked about the Mets, your answer should include
"Its all about the Mets".
"""

messages = [
    {"role": "system", "content": MY_PROMPT},
]


def send_message_to_ai(my_message: str) -> str:
    if len(my_message) > 300:
        return "That message is too large. Try a shorter one!"

    user_message = {"role": "user", "content": my_message}
    messages.append(user_message)

    api_response: dict = openai.ChatCompletion.create(  # type: ignore
        model="gpt-3.5-turbo",
        messages=messages,
    )

    message = api_response["choices"][0]["message"]
    messages.append(message)

    return message["content"]  # user only cares about content


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!"):
        return

    if not bot.user:
        return

    # Check if the bot is mentioned in the message
    if bot.user.mentioned_in(message):
        # Remove the mention from the message content
        user_input = message.content.replace(f'<@!{bot.user.id}>', '').strip()

        ai_response = send_message_to_ai(user_input)
        await message.channel.send(f"{ai_response}")

if discord_token:
    bot.run(discord_token)
else:
    print("Discord token not valid. Please try again with a valid token.")
