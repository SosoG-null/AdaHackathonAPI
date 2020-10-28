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

# login test
print("Good login request")
result=requests.post(adress+"login",{"username":"soso", "password":"1234"})
print (result.status_code)

print("Bad login request")
result=requests.post(adress+"login",{"username":"soso", "password":"bad"})
print (result.status_code)

username=input("Please enter your username.\n")
password=input("Please enter your password.\n")
result=requests.post(adress+"login",{"username":username, "password":password})
print (result.status_code)

test_data = {"message_id":1, "title": "Test", "body": "A clever post"}
test_data2 = {"message_id":2, "title": "Test2", "body": "A clever post2", "views":10}
test_data3 = {"user_id":2, "name":"Soso", "age":13, "gender":"female", "views":10, "password":"1234"}

result=requests.post(adress+"messages",test_data)
print (result.json())

result=requests.post(adress+"messages",test_data2)
print (result.json())

# result=requests.post(adress+"/messages/1/likes")
# # print (result())

# result=requests.get(adress+"messages")
# print (result.json())
# # print ("messsages added")

# result=requests.post(adress+"users", test_data3)
# print (result.json())
# # print ("user added")

# print ("attempting to delete message")
# result=requests.delete(adress+"messages/2")
# print (result.status_code)

# result=requests.get(adress+"messages")
# print (result.json())

