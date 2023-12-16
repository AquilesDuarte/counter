print('Hello, welcome to the best guest counter for your party! \n')

print('I am a Python-developed robot, and I will help you. First, tell me how many people you want to invite \n')

x = int(input('Enter the number of guests:'))
y = []

i = 1

while i <= int(x):
    guest_name = input('Enter the name of guest #' + str(i) + ':')
    y.append(guest_name)
    i += 1

print('There will be', x, 'guests!')

print('\nGuest list')
for guest in y:
    print(guest)
