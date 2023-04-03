# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def register(users):
    usr = input('username:')
    pwd = input('password:')
    em = input('email:')
    new = {'usr': usr, 'pwd': pwd, 'em': em}
    users.append(new)
    print('register successfully')

def signIn(users):
    usr = input('username:')
    pwd = input('password:')
    em = input('email:')
    new = {'usr': usr, 'pwd': pwd, 'em': em}
    if new in users:
        print('sign in successfully')
        return 1
    else:
        print('wrong username,password or email')
        return 0

def menu():
    choose = input('input 1 to add,2 to update, 3 to delete,4 to query')
    return choose

def add(users):
    usr = input('username:')
    pwd = input('password:')
    em = input('email:')
    new = {'usr': usr, 'pwd': pwd, 'em': em}
    users.append(new)
    print('add successfully')

def update(users):
    usr = input('username:')
    pwd = input('password:')
    em = input('email:')
    new = {'usr': usr, 'pwd': pwd, 'em': em}
    if new in users:
        newPwd = input('new password:')
        newEm = input('new email:')
        users[users.index(new)] = {'usr': usr, 'pwd': newPwd, 'em': newEm}
        print('update successfully')
    else:
        print('wrong username,password or email')

def delete(users):
    usr = input('username:')
    pwd = input('password:')
    em = input('email:')
    new = {'usr': usr, 'pwd': pwd, 'em': em}
    if new in users:
        users.remove(new)
        print('remove successfully')
    else:
        print('wrong username,password or email')

def query():
    str = input('input your question here:')
    print('thannks for query, we will reply back soon!')
    return str

users = [{'usr':'myUsrName', 'pwd': '111', 'em': '11@qq.com'}]
while 1:
    choose = input('input 1 to register ,2 to sign in ')
    if choose == '1':
        register(users)
    else:
        a = signIn(users)
        if a == 1:
           choose = menu()
           if choose == '1':
               add(users)
           elif choose == '2':
               update(users)
           elif choose == '3':
               delete(users)
           elif choose =='4':
                query()


