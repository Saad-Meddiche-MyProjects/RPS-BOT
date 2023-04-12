#There are other files, but I didn't publish them.
#So these imports will may not make sense.
import discord
import random
from keep_alive import keep_alive 
from discord.ext import commands, tasks
from discord.utils import get

#configs of bot
bot = commands.Bot(
  command_prefix='*', 
  case_insensitive=False,
  description=None,
  intents=discord.Intents.all(), 
  help_command=None
)

@bot.command()
async def RPS(ctx):
  #Display Message
  message = await ctx.send('Choose rock :rock: , paper 📜, or scissors :scissors: . You have 30 seconds ⏱ to respond.')

  #Add Reactions to message 
  reactions = ['🪨', '📜', '✂']
  for emoji in reactions:
    await message.add_reaction(emoji)

  #Check if the same user who started the game is the same and not someone else
  def check(reaction, user):
      return user == ctx.author
    
  #Waiting for user to reacte, If the time across 30sec , then display message and stop
  try:
     reaction, user = await bot.wait_for('reaction_add', check=check, timeout=30)
  except:
    await ctx.send("Huh?! I Don't have all the day for You . Byeeee dummyy")

  #Transform the reaction to a word
  user_choice = 'none'
  if str(reaction.emoji) == '🪨':
    user_choice = 'rock'
  elif str(reaction.emoji) == '📜':
    user_choice = 'paper'
  elif str(reaction.emoji) == '✂':
    user_choice = 'scissors'
  
  # Check if the user's choice is valid
  if user_choice not in ['rock', 'paper', 'scissors']:
    await ctx.send(f'Come onnnn😡😡😡😡, It\'s only ROCK PAPER OR SCISSORS, NOT {reaction}')
    return
  
  # Generate a random choice for the bot
  bot_choice = random.choice(['rock', 'paper', 'scissors'])

  bot_sad_replies = [ 
    "Aww, I lost! 😢",
    "You got lucky this time! 😒",
    "I'll let you have that one. For now. 🙄",
    "Looks like you're getting better, but you still can't beat me! 😜",
    "That was a great move... for a human. 🤖",
    "Well played... for someone who's not a bot. 😏",
    "I need to practice more... against someone more challenging. 😴",
    "I'm so bad at this... I must be playing with a kid. 😒",
    "You're too good for me... said no bot ever. 😏",
    "I should have seen that coming... if I wasn't programmed to be so overconfident. 😒",
    "I need a hug... from someone who knows how to play this game. 😔",
    "I surrender... for now. 😜"
  ]
  bot_win_replies = [
    "Haha, I win! 😂",
    "You can't beat me! I'm a bot! 😎",
    "Better luck next time, human! 🤞",
    "Sorry, not sorry! 😔",
    "I'm just too good! 💪",
    "That was too easy! 😜",
    "You put up a good fight, but I won! 🥊",
    "I knew I could beat you! 😉",
    "I'm the champion of rock-paper-scissors! 🏆",
    "I'm unstoppable! 🚀",
    "Looks like I'm not playing with the big leagues yet. 😏",
    "You're not even a challenge! 😒",
    "I was born to play this game... you were not. 😎"
  ]
  bot_tie_replies = [
  "Hmph, we both chose the same thing. How boring. 😴",
  "A tie? I expected more from you. 🙄",
  "You got lucky this time, human. Don't count on it happening again. 😤",
  "Tie game. We'll see who wins next time... spoiler alert: it's me. 😏",
  "Well, well, well... looks like we're evenly matched. For now. 🤨"
  ]


  #Determine the winner
  if user_choice == bot_choice:
      user_win = '-'
  elif user_choice == 'rock' and bot_choice == 'scissors':
      user_win = 'yes'
  elif user_choice == 'paper' and bot_choice == 'rock':
      user_win = 'yes'
  elif user_choice == 'scissors' and bot_choice == 'paper':
      user_win = 'yes'
  else:
      user_win = 'no'

  #Determine the result
  if user_win == 'yes':
    result = random.choice(bot_sad_replies)
  elif user_win == 'no':
    result = random.choice(bot_win_replies)
  else:
    result = random.choice(bot_tie_replies)

  
  #Determine choice icon
  bot_choice_icon=''
  if bot_choice == 'rock':
    bot_choice_icon = ":rock:"
  elif bot_choice == 'scroll':
    bot_choice_icon = ':scroll:'
  elif bot_choice == 'scissors':
    bot_choice_icon = ':scissors:'
      
  # Send the results to the user
  await ctx.send(f'**============Bot Choice==========**\nI chose the {bot_choice} {bot_choice_icon}')
  await ctx.send(f'**============Bot Reply===========**\n{result}')

  #Ask user if they want to play again
  message = await ctx.send("**============Rematch ?===========**\n Wanna Play Again 🥱? ")
  
  #Add Reactions to message
  reactions = ['👍', '👎']
  for emoji in reactions:
    await message.add_reaction(emoji)
  
  #Check if the same user who started the game is the same and not someone else
  def check_again(reaction, user):
    return user == ctx.author
  
  try:
    reaction, user = await bot.wait_for('reaction_add', check=check_again, timeout=30)
  except:
    await ctx.send("Huh?! I Don't have all the day for You . Byeeee dummyy")
    return
  
  #Determine if the user wants to play again
  if str(reaction.emoji) == '👍':
    await RPS(ctx)
  else:
    await ctx.send('Then go awaiy. Don\'t waist my time! 😠')


#Make the bot Online, and change the display of its status
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=f"Rock , Paper , Scissors"))
keep_alive()

# Run the bot
# Your Token Bot
bot.run("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
