import random

def generator():
    row=random.randint(5,15)
    col=random.randint(5,15)
    numb=''

    for x in range(row*col):
        numb=numb+str(random.randint(0,1))

    line=str(row)+'x'+str(col)+':'+str(numb)

    return line

with open("mat.in", "w") as file:
    for x in range(110000):
        line=generator()
        file.write(line + '\n')


