def minion_game(string):
    # your code goes here
    length = len(string)
    vowels = ['A','E','I','O','U']
    stuart = 0
    kevin = 0
    for i in range(length):
        if(string[i] in vowels):
            kevin += length - i
        else:
            stuart += length - i
    if (stuart > kevin):
        print "Stuart", stuart
    elif(stuart == kevin):
        print "Draw"
    else:
        print "Kevin", kevin
    return
