import time
import random
import os
print('This Little Program has been brought to you by cursordance')
time.sleep(2)
total = 0
print('The Math Question')
name = input('please enter your name)')
print('Question 1th')
time.sleep(1)
print('what is the answer for : 2 divided 5x5+5:')
time.sleep(1)
print('A:15')
print('B:25')
print('C:17.5')

if input()[0].lower() == 'a':
    print(f'good answer! {name}!')
    print('lets go for the next question!')
    total += 1
else:
    print(f'wrong answer! {name} better chance next time!')

time.sleep(2)

print('Question 2th')
time.sleep(1)
print('how much state are in the United State of America')
time.sleep(1)
print('A:52')
print('B:45')
print('C:50')

if input()[0].lower() == 'c':
    print(f'good answer! {name}!')
    print('lets go for the next question!')
    total += 1
else:
    print(f'wrong answer! {name} better chance next time!')

time.sleep(2)

print('Question 3th')
time.sleep(1)
print('what is the solution for those equation')

a = random.randint(0, 10)
b = random.randint(2, 15)
print(a,'+',b)
x = int(input())
if x == (a+b):
    print(f'good answer! {name}!')
    print('lets go for the next question!')
    total += 1
else:
    print(f'wrong answer! {name} better chance next time!')

time.sleep(2)

print('Question 4th')
time.sleep(1)
print('can you do this 1 ?')

time.sleep(2)

a = random.randint (2, 12)
b = random.randint (3, 7)
print(a,'x',b)
x = int(input())
if x == (a*b):
    print(f'good answer! {name}!')
    print('lets go for the next question!')
    total += 1
else:
    print(f'wrong answer! {name} better chance next time!')

time.sleep(2)

print('Question 5th')
time.sleep(1)
print('alright you may or may not have failed the older 1 but shall we go harder?')

time.sleep(2)

a = random.randint (4, 7)
b = random.randint (12, 15)
c = random.randint (2, 6)
print(a,'x',b,'x',c)
x = int(input())
if x == (a*b*c):
    print(f'good answer! {name}!')
    print('lets go for the next question!')
    total += 1
else:
    print(f'wrong answer! {name} better chance next time!')

time.sleep(2)

print('Question 6th')
time.sleep(1)
print('I am quite impress you didnt forfeited yet!')
a = random.randint (1, 7)
b = random.randint (2, 5)
def pow(a, b):
  return a ** b
print(a,'to the power of',b)
x = int(input())
if x == (a ** b):
    print(f'good answer! {name}!')
    print('lets go for the next question!')
    total += 1

else:
    print(f'wrong answer! {name} better chance next time!')

time.sleep(2)

print('Question 7th')
time.sleep(1)
print('alright last question!')
time.sleep(1)
print('what is the circumference of the sun?')
time.sleep(1)
print('A:4,379 millions km2')
print('B:5,423 millions km2')
print('C:4,135 millions km2')
if input()[0].lower() == 'a':
    print(f'good answer! {name}!')
    print('lets go for the next question!')
    total += 1
else:
    print(f'wrong answer! {name} better chance next time!')

time.sleep(2)

print('thanks you for doing the quiz!')
print(f'you got a grant total of {total}/7!')
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')
