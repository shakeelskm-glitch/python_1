#lists 
names=["shakeel","tarun","shrenik","prudhvi"]
#append- adds elements to the end of the list
names.append("teja")
print(names)
#extend- adds elements from another list to the end of the list
names.extend(["sai","karthik"])
print(names)
#insert- adds an element at a specific index in the list
names.insert(2,"sai teja")
print(names)
#remove- removes the first occurrence of a specific element from the list
names.remove("sai")
print(names)
#pop- removes and returns the last element from the list
last_name=names.pop()   
print(last_name)
print(names)
#clear- removes all elements from the list
names.clear()
print(names)
#len- returns the number of elements in the list  
print(len(names))
#index- returns the index of the first occurrence of a specific element in the list
names=["shakeel","tarun","shrenik","prudhvi"]
print(names.index("shrenik"))
#count- returns the number of occurrences of a specific element in the list
names.append("shakeel")
print(names.count("shakeel"))
#sort- sorts the elements of the list in ascending order
names.sort()
print(names)
#reverse- reverses the order of the elements in the list
names.reverse()
print(names)
#copy- creates a shallow copy of the list
names_copy=names.copy()
print(names_copy)


#example 
students=["Sita","Ram","Nira","John","Tarun","Nira"]
print(students)
students.append("Shrenik")
print(students)
students.extend(["Shakeel","Prudhvi"])
print(students)
students.remove("Shakeel")
print(students)
students.insert(2,"Prudhvi")
print(students)
students.sort()
print(students)
students.pop()
print(students)
students.reverse()
print(students)
print(students.count("Nira"))
print(students.index("John"))
print(students.copy())
students.clear()
print(students)

students={"Sita","Ram","Nira","John","Tarun","Nira"}
print(students)

numbers={1,2,2,3,3,4}
print(numbers)

fruits={"apple","banana"}
fruits.add("mango")
print(fruits)

data=[1,2,2,3]
ud=set(data)
print(ud)

num=[1,2,3,2,4]
print(num.index(2))

set1={1,2,3,4}
set2={3,4,5,6}
#union- returns a new set that contains all unique elements from both sets  
union_set=set1.union(set2)
print(union_set)

num1={1,2,3}
num1.add(2)
print(num1)

set1={1,2,3,4}
set2={3,4,5,6}
result=set1.difference(set2)
print(result)

data=[1,2,3]
print(data[1:3])