import random

num = random.randint(0, 10)
print('homo: ', num)
attempt = 4
msg = 'You lost!'

while attempt > -1:
    user_input = int(input('enter number: '))
    if user_input == num:
        msg = 'You won!'
        break
    else:
        print(f'try again! attempts left {attempt}')
        attempt -= 1
        continue
print(msg)