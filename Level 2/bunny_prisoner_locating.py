#This is the one I had to actually do

def answer(x, y):

    i = (x+y-2)
    num = int((i * (i+1))/2)
    num += x

    return str(num)

print(answer(3, 2))
print(answer(5, 10))
