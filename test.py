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
#         print (f"Hello! My name is {self.name} and I am {self.age} years old. I'm in year {self.year} and am a {self.gender}.")
        
# student1= Student(14,"Jane",10,"female")
# student2= Student(15,"John",11,"male")

# print (student1)
# print (student2) 
# student1.introduce()
# student2.introduce()

test_data = {"message_id":1, "topic": "Test", "body": "A clever post", "author": "soso"}
test_data2 = {"message_id":2, "topic": "Test2", "body": "A clever post2", "author": "soso", "views":10}
test_data3 = {"user_id":2, "name":"Soso", "age":13, "gender":"female", "views":10, "password":"1234"}

result=requests.post(adress+"messages",test_data)
print (result.json())

result=requests.post(adress+"messages",test_data2)
print (result.json())

result=requests.post(adress+"/messages/1/likes")
print (result.json())

result=requests.get(adress+"messages")
print (result.json())
# print ("messsages added")

result=requests.post(adress+"users", test_data3)
print (result.json())
# print ("user added")

print ("deleting message")
result=requests.delete(adress+"messages/2")
print (result.status_code)

result=requests.get(adress+"messages")
print (result.json())

# login test
result=requests.post(adress+"login",{"user_id":1, "password":"1234"})
print (result.status_code)

result=requests.post(adress+"login",{"user_id":1, "password":"bad"})
print (result.status_code)