print('Hello, Django girls!')
5 + 2
participant = {'name': 'Jonathan', 'country': 'Germany', 'favorite_numbers': [7,9,17]}
ceo = "Moritz"
print(ceo)
if ceo == "Moritz": 
    print(participant) 
if 3 > 2:
    print('It works!')
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')
name = 'Jonathan'
if name == 'Joni':
    print('Hey Joni!')
elif name == 'Jonathan':
    print('Hey Jonathan!')
else:
    print('Hey anonymous!')
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
# Change the volume if it's too loud or too quiet
volume = 10
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")

def hi():
    print('Hi there!')
    print('How are you?')

hi()
def hi(name):
    if name == 'Jonathan':
        print('Hi Jonathan!')
    elif name == 'Joni':
        print('Hi Joni!')
    else:
        print('Hi anonymous!')

hi('Jonathan')
hi('Samuel')
def hi(name):
    print('Hi ' + name + '!')

hi("Jonathan")

def hi(name):
    print ('Hi ' + name + "!")

girls = ['Mkay', 'Kathy', 'Katharina', 'Rine', 'Maria']
for name in girls: 
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)
