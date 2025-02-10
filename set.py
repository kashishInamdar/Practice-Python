'''
set is unorded collection of elements. ( means set does not mantain positions on element )
set only contain  unique elements (means set does not contain duplicate)

 '''

# set add or remove Items from set
fruits = {"apple","gvava","greps",99,'banana',99};
fruits.add("sana")
fruits.remove(99)
print("fruits :",fruits)
print('-' * 50)

# conver list to set usning set() method

students = ["kashish","sana","mujju","shabana","rishad","soyab","sonya","meher","karishma","sadiya" ,"kashish","sana"];

print("student list:" , students);
print("length",len(students));
print("--" * 25);

students2 = set(students)
print("students tuple",students2);
print("length",len(students2));  


