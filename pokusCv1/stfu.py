def invert(lst):
    tmp=''
    for i in lst:
        if i>='a':
            tmp+=i.upper()

        else:
            tmp+=i.lower()

    return tmp

slovnik={'hello':'ahoj',
         'one':'jedna',
         'two':'dva',
         'three':'tri',
         'four':'crtyri'}

def dict(slovnik, word):
    if word in slovnik:
        print(slovnik[word])
        # for i in slovnik:
            # print(slovnik[i])
    else:
        print('O kurwa, slovo niet')
        print(sorted(slovnik))
        return None


print(invert('aBcd'))

dict(slovnik, 'onse')
