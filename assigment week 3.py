# Set Question:
# Question 1:
# Create a set of your favorite 5 fruits. Add one more fruit and remove one fruit from the set. Print  the final set ?
# Coding:
# Answer:
fruits ={"apple,"banana","orange","mango","grape":}
# add one ,more fruit to the set 
fruits.add("kiwi")
# Remove one fruit from the set(e.g,remove"banana")
fruits.remove("banana")
#print the finial set
prints(fruits)
#Question 2:
# Write a program to find theunion and intersection of the following sets:
# set1 ={1 ,2 ,3 ,4 }
# set2 ={3 ,4 , 5, 6}
# coding:
set 1 ={1 ,2 ,3 ,4}
set 2={3, 4 ,5 ,6}
union = set1.union(set2)
intersection =set1.intersection(set2)
print("Union:",union)
print("intersection:",intersection)
# Tuple Question:
# Create a tuple with 5 numbers. print the first and last number ?
# coding:
numbers=(10,20,30,40,50)
print("first number:", numbers[0])
print("Last number:",numbers[-1])
# question 4:
# Given the  tuple (10,20,30,40,50),write a program to find the sum of all element.
# coding
t = (10,20,30,40,50)
total = sum(t)
print("sum:",total)
#question 5:
#try to change the second element of the turple (1,2,3) to 5. Observe what happens and explain why.
t=(1,2,3)
#t[1] 5 # uncommenting this line will cause an error
#tuples; are immutable in python, meaning their contents cannot be modified after creation.
print ("Tuples are immutable.")
# question 6:
#create a list of cities. Add one more city at the end and insert another city at the second position. Print the updated list.
# coding
cities =['Karachi', 'Lahore', 'Islamabad', 'Peshawar']
cities.append ('Multan')
cities.insert(1,- 'Faisalabad')
print (cities)
# Question 7:
# given the list [2 ,4 , 6, 8,10]/
#write a program to double each number and store it in the same list ?
# coding :
numbers = [2 ,4 ,6 ,8, 10]
numbers = [x * 2 for x in numbers]
print (numbers)
# Dictionary Questions:
# Question 8:
# create a dictionary to store student marks for 3 subjects. Print the marks of one subject ?
# coding
student _marks = {'math': 89, 'Science': 99,'English':87}
print("Math marks:",student_marks['Math'])
 #Question 10 :
 # Write a program tonloop through a dictionary and print all keys and values in the format: Subject: Marks ?
 # coding:
 student_marks ={'Math': 89 ,'Science':99,'english':87}
 for subject , marks in student_marks.items():
 print (f"{subject}: {Marks}")
 # MINI PROJECT STUDENT RESULT MANAGER :
 # coding:
 def student_result_manager():
 # Take marks of 3 subject as input from the user.
 marks ={}
 subjects =['Math', 'Science', ' English']
 for subject in subjects:
 marks[subject]= float(input(f" Enter marks for {subject}:"))
 # Calculate total and average marks.
 total_marks = sum(marks.values())
 average_marks = total_marks/ len(marks)
 # display grade based on average.
 if average_marks>= 79:
 grade ='A'
 elif average_marks.=70:
 grade = 'B'
 Else :
 grade ='C'
 Print("Student Marks:")
 for subject, mark in mark.item():
 print (f"{subject}:{total_marks}")
 print(f"Total Marks:{total_marks}:{total_marks}")
 print(f"Average Marks :{averane_marks}")
 print (f"Grade:{grade}")
student_result_manager() 
 
 
 
 

 
 
