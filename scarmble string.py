from random import sample

test_list = ['gfg', 'is', 'best', 'for', 'geeks']
print("The original list : " + str(test_list))
res = [''.join(sample(ele, len(ele))) for ele in test_list]
print("Scrambled strings in lists are : " + str(res))
