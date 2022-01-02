result=[85,90,21,56,30,57,40]
abc=[]
for i in range(len(result)):
    if (result[i]>=40):
        abc.append(result[i])
print(abc)                   
       
result1=[85,90,21,56,30,57,40]
for i in result1:
    if (i<=40):
        result1.remove(i)
print(result1)        


abc=input("Yes or No: ") 
while abc=="Yes":
    print("Continue")
    abc=input("Yes or No: ")
    
usename="athersajid"
password="123456"
user=input("Username: ")
passw=input("Password: ")
while True:
    if (user==usename)&(passw==password):
        print("Login Successful")
        break
    else:
        print("LOgin fail")
        user=input("Username: ")
        passw=input("Password: ")

        
        