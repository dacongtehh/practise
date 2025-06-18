import emoji
import time
import random

print('Sony: Howdy, my name is Sony, your chatbot assistant 😄')
time.sleep(1.3)
print('Sony: What can i do for you today?')
time.sleep(1)
user_input = input('You: ')

if user_input.lower() in ['sad', 'stress','trouble','bad' ]:
        print('Sony: Oh thats unfortunate...')
        time.sleep(1.2)
        print('Sony: What happend?')
