
successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("u have attempted 3 times and failed")
