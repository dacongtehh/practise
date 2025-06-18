from linecache import clearcache

#Practice starts from here
#Lets make: Number Guessing Game
import time

print("Hello User")
time.sleep(2)

guess = input("Take a guess between 1-100: ")
time.sleep(1)
print("Hmmmmmm......")
time.sleep(3)

if guess.isdigit():
    guess = int(guess)

    if int(guess) == 47:
        print('Grats, you are lucky')
    elif 1 <guess< 10:
        print('Hey, too low man')

elif guess.upper() == 'NO':
    print(' ? ')

