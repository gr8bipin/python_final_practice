# Open the file, read the password, and close it automatically

with open('SecretPasswordFile.txt') as passwordFile:
    secretPassword = passwordFile.read().strip()

print('Enter your password:')
typedPassword = input()

if typedPassword == secretPassword:
    print('Access granted')

    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')

else:
    print('Access denied')