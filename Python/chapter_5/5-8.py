usernames = ['robin', 'kuzeyli5758', 'admin', 'denix', 'whoopty']
for username in usernames:
    if username == 'admin':
        print("Hello " + username + ", would you like to see a status report?")
    else:
        print("Hello " + username.title() + ", thank you for logging in again.")
