import random
feet=5280
minkm=1000
beatles=["John","Paul","George","Ringo"]

def getFileExtension(filename):
    return filename[filename.index(".")+1:]
def rollDice(num):
    return  random.randint(1,num)