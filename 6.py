list1=['1','7','4','9','3','5']
min =sorted(list1) 
print(type(min))
max=sorted(min,reverse=True) 
m1 =int(''.join(min)) 
m2 =int(''.join(max))
print(m2-m1)