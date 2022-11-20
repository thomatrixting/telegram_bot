try:
    with open('users.txt', 'x') as f :
        pass

except Exception as e:
    print('file already created')
else:
    print('users created')

try:
    
    with open('file.txt', 'w') as f :
        pasword = input('set pasword: ')
        f.write(pasword)
except Exception as e:
    print('error in creating pasword')

else:
    print('set up complete')
