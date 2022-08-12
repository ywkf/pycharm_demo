def login(username, password):
    if username == 'admin' and password == '123456':
        return 'success'
    else:
        return 'failed'

