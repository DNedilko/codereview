'''
Вивести кількість дійсних чисел у списку
'''

list=[1,3,5,5,6,8,1.4,5,6,8,"gf","i","ew","iu",True,9,0,6,7,3,5,8,1.5]
n=0
for index in range(0,len(list)):
    if type(list[index]) == int:
        n=n+1
    if type(list[index]) == float:
        n+=1
print(n)