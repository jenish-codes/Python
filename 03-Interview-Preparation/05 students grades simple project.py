import statistics

admins = {'Python':'Pass123@','user2':'pass2'}


def main():
    print('''
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    ''')

    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        print('1')
    elif action == '2':
        print('2')
    elif action == '3':
        print('3')
    else:
        print('No valid choice was given try again')

login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('\nWelcome', login)
        while True:
            main()
    else:
        print('Invalid Password, will detnate in 5 seconds!')
else:
    print('Invalid Username! This action will be Reported')
















