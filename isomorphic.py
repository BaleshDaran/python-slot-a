def isIso(a,b):
        if(len(a) != len(b)):
                return false
        x=[a.count(char1) for char1 in a]
        y=[b.count(char1) for char1 in b]
        return x==y                   
string1 = input("Input string1..")
string2 = input("Input string2..")
print(isIso(string1,string2))
