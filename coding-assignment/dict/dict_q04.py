#Python program to find the sum of all items in a dictionary
import functools

dic = {'a': 100, 'b': 200, 'c': 300}

sum_dic = functools.reduce(lambda ac,k: ac+dic[k], dic, 0)

print("Sum :", sum_dic)
