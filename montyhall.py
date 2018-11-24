from random import randint

doors = [1,2,3]

carDoor = randint(1,3)

chosen = int(input('choose a door 1, 2 or 3\n'))

doorstoshow = doors.copy()
del doorstoshow[doorstoshow.index(chosen)]
if(carDoor in doorstoshow):
    del doorstoshow[doorstoshow.index(carDoor)]
# print(doorstoshow)
# print(doors)

if(len(doorstoshow) == 2):
    show = doorstoshow[randint(0,1)]
else:
    show = doorstoshow[0]
print('DOOR SHOWN:' + str(show))

flip = input('Do you want to change? "y" or "n"\n')
if(flip == 'n'):
    if(chosen == carDoor):
        print('you won... you chose' + str(chosen) + ' "' + str(flip) + '" car was firstly in ' + str(carDoor))
    else:
        print('you lose... you chose' + str(chosen) + ' "' + str(flip) + '" car was firstly in ' + str(carDoor))
elif(flip == 'y'):
    if(show == chosen):
        del doors[doors.index(show)]
    else:
        del doors[doors.index(show)]
        del doors[doors.index(chosen)]

    # seeing the two delete above it seems quite awkward that it's nearly obvious to win
    # deleting the shown one and the chosen one too (i.e. deleting two elements) while there's only three elements to choose from

    if(doors[0] == carDoor):
        print('you won... you chose ' + str(chosen) + ' "' + str(flip) + '" car was firstly in ' + str(carDoor))
    else:
        print('you lose... you chose ' + str(chosen) + ' "' + str(flip) + '" car was firstly in ' + str(carDoor))


