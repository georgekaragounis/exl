def removeDupliatesd(x):
   res = {}
   for key,value in x.items(): 
       if value not in res.values(): 
           res[key] = value
   return res  
def sortListd(x):
    b = sorted(x.items(), key=lambda item: item[1])
    return b   
def removeDupliates(x):
   res = [] 
   for i in x: 
       if i not in res:
           res.append(i) 
   return res  
def sortList(x): 
    swapped = True
    while swapped: 
        swapped = False
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                y = x[i]
                x[i] = x[i + 1]
                x[i+1] = y
                swapped = True
    return x
a_list = [30,28,28,16,14,14,12,10]        
a_list = removeDupliates(a_list)
print(a_list)   
a_list = sortList(a_list)    
print(a_list)
a_dict = {"a":30, "b":28, "c":28, "d":16, "e":14, "f":14, "g":12, "h":10}
a_dict = removeDupliatesd(a_dict)
print(a_dict)
a_dict = sortListd(a_dict)
print(a_dict)     