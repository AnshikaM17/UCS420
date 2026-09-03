L = [ 10 , 0 , 20 , 40 , 10 , 70 , 0 , 40 , 0 , 90 ]
print(L)
L.append(100) # append(100) adds 100 to the end of the list,
print(L)
L.insert(0, 50) # insert(0, 50) adds 50 at index 0, shifting all other elements to the right
print(L)
L.remove(0) 
print(L)
L.pop() 
print(L)
L.pop(2)
print(L)
L.sort()
print(L)
L.sort(reverse=True)
print(L)
print(L[:3], L[-3:])
average = sum(L)/len(L) # average of the list
print(average)
new_list = [x for x in L if x > average]
print(new_list)