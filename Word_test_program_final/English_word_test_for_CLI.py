import random
import time
import sys
import getpass
import msvcrt

try:
    day = input("Please input number of Day test : ")
except:
    print("You should input only number! Please try again.")

f1 = open(f'./storage/eDay{day}.txt',mode='rt',encoding='UTF8')
f2 = open(f'./storage/kDay{day}.txt',mode='rt',encoding='UTF8')

number_of_english_word = f1.read().count("\n")
number_of_korean_word = f2.read().count("\n")
f1.seek(0,0)
f2.seek(0,0)

if number_of_english_word != number_of_korean_word:
    print("Word file has different number of argument. Please check and try again.")
    ValueError

word,temp = list(),list()

lower_number = 0
if number_of_english_word>=number_of_korean_word:
    lower_number = number_of_korean_word
else:
    lower_number = number_of_english_word

for i in range(lower_number):
    temp.append(f1.readline().rstrip('\n'))
    temp.append(f2.readline().rstrip('\n'))
    word.append(temp)
    temp = []

random.shuffle(word)


for i in range(lower_number):
    print('%-50s' % f'{word[i][0]}',end='')
    msvcrt.getch()
    input(f'{word[i][1]}')

print('\nProgram will be terminated in 5 seconds... ')
time.sleep(5)



# developer's code #
'''
for i in range(lower_number):
    input('%-50s' % f'{word[i][0]}')
    print('\x1b[1A\x1b[2K',end='')
    print('%-50s' % f'{word[i][0]}',end='')
    print(f'{word[i][1]}')
    input()
'''