#Python | Check order of character in string using OrderedDict( )
from collections import OrderedDict 
 
def checkOrder(input, pattern): 
     
    # create empty OrderedDict 
    # output will be like {'a': None,'b': None, 'c': None} 
    dict = OrderedDict.fromkeys(input) 
 
    # traverse generated OrderedDict parallel with 
    # pattern string to check if order of characters 
    # are same or not 
    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
         
        # check if we have traverse complete 
        # pattern string 
        if (ptrlen == (len(pattern))): 
            return 'true'
 
    # if we come out from for loop that means 
    # order was mismatched 
    return 'false'
 
# Driver program 
if __name__ == "__main__": 
    input = 'engineers rock'
    pattern = 'er'
    print (checkOrder(input,pattern)) 