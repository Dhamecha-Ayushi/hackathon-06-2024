def biggest_number(matchsticks):
    if matchsticks == 0 or matchsticks == 1:
        return 0
    if matchsticks % 2 != 0:
        return '7' + '1' * ((matchsticks - 3) // 2)
    else:
        return '1' * (matchsticks // 2)

matchsticks = int(input("Enter matchstick: "))
print(biggest_number(matchsticks))