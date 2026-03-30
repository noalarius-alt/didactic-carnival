import discord
from discord.ext import commands
from google.cloud import translate_v2 as translate
import pyttsx3

# Initialize the Discord bot
bot = commands.Bot(command_prefix='!')

# Initialize Google Cloud Translation client
translate_client = translate.Client()

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def translate(ctx, *, message):
    # Translate the message to a specified target language
    target_language = 'es'  # You can change this to the desired language code
    translation = translate_client.translate(message, target_language=target_language)

    # Fetch the translated text
    translated_text = translation['translatedText']
    await ctx.send(translated_text)

    # Speak the translated text in voice channel if the user is in one
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()

        tts_engine.say(translated_text)
        tts_engine.runAndWait()

        await voice_client.disconnect()
    else:
        await ctx.send("You need to be in a voice channel to use this feature.")

# Run the bot with the token
bot.run('YOUR_DISCORD_BOT_TOKEN')