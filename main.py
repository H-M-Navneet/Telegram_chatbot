from imaplib import Commands
import telebot

from constants import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=["help", "hello", "start"])
def send_help_message(msg):
    bot.reply_to(msg, "Hello! Welcome to INSUREGO! \nfollow the below commands to chat: \n/how_to_proceed_further - to get website link and more info about our insurance policies. \n/thanks or /thank_you - for ending the chat. \n/yes - yes and /no - no")

@bot.message_handler(content_types=["photo", "sticker"])
def send_contents_message(msg):  
    bot.reply_to(msg, "Please enter only text messages")

@bot.message_handler(commands=["how_to_proceed_further", "which_insurance_policy_suits_me_the_best?"])
def send_enquiry_message(msg):
    bot.reply_to(msg, "Please visit our official website or INSUREGO mobile app! \nLink for the websit: https://tinder-clone-d74e7.web.app/")
    bot.reply_to(msg, "Are you intrested to take online consultancy for better understanding of the policies ?")

@bot.message_handler(commands=["yes"])
def send_help_message(msg):
    bot.reply_to(msg, "Click the following link to join the meeting: https://meet.jit.si/18389911 \n \nRoom ID: 18389911 \nClick this link to see the dial in phone numbers for this meeting \nhttps://meet.jit.si/static/diallninfo.html?room=18389911")
    bot.reply_to(msg, "Please enter your metamask id in order to receive rewards")

@bot.message_handler(commands=["no"])
def send_help_message(msg):
    bot.reply_to(msg, "Please enter your metamask id in order to receive rewards")

@bot.message_handler(commands=["thanks", "thank_you"])
def send_help_message(msg):
    bot.reply_to(msg, "Thank you! for visiting INSUREGO  :)")

bot.polling()
