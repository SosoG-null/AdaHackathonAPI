import requests

adress="http://127.0.0.1:5000/"
print(adress)

result=requests.get(adress+"messages")
print (result.json())

# class Student:
     
#     def __init__(self,age,name,year,gender):
#         self.age = age
#         self.name = name
#         self.year =year
#         self.gender = gender

#     def introduce(self):
#         print (f"Hello! My name is {self.name} and I can {self.age} years old. I'm in year {self.year} and am a {self.gender}.")
        
# student1= Student(14,"Jane",10,"female")
# student2= Student(15,"John",11,"male")

# print (student1)
# print (student2) 
# student1.introduce()
# student2.introduce()

test_data = {"message_id":1, "topic": "Test", "body": "A clever post", "author": "soso", "views":0}

result=requests.post(adress+"messages",test_data)
print (result.json())

result=requests.get(adress+"messages")
print (result.json())