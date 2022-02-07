current_users = ['robinop', 'kuzeyli5758', 'whoopty', 'doruk', 'denix']
new_users = ['yorichi', 'Secrethunter', 'FutureTroy', 'Robinop', 'Denix']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("This username is currently being used, please enter new username")
    else:
        print("Username is available")
