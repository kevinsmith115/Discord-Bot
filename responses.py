import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll d6':
        return "Result: " + str(random.randint(1, 6)) + " :game_die:"

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    if p_message == '!commands':
        return "The commands are \nHello \nRoll d6 /n Roll d20 \n!Help \n!Commands"

    if p_message == 'roll d20':
        return "Result: " + str(random.randint(1, 20)) + " :game_die:"
    
   
