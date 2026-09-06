luvut = [] 

for i in range(100):
    num = input("Anna luku ") 
    if num == "": 
        break 
    luku = int(num) 
    luvut.append(luku) 

luvut.sort(reverse=True) 
print(luvut[:5])
