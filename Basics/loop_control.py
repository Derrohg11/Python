#Break statement in a loop
name= 'university'
for letter in name:
    if letter == 'r':
        break
#    print(letter)

#Continue statement in a loop
for letter in name:
    if letter == 'r':
        continue
#    print(letter)

#Pass statement in a loop
for letter in name:
    if letter == 'r':
        pass
    print(letter)