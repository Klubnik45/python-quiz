import random
import json

def password_gen(word):
    t=random.randint(1,3)
    print(t)
    password=""
    if t==1:
       if len(word)<=2:
           password+=(word*2 if len(word)==2 else word*4)+str(random.randint(100,999))+((word*2)[::-1][1:] if len(word)==2 else (word*3).upper()) #использоум Ternary Operators
       else:
           password+=word[::-1][0]+word[-1]+str(random.randint(10000,99999))+word[:3].upper()

    if t==2:
       if len(word)<=2:
           password+=str(random.randint(1000,9999))+random.choice(["!","@","#","$","%"])+(((word*2)[1:][:-1])*2 if len(word)==2 else (word*4))+random.choice(["&","*"])
       else:
           password+=random.choice([word[0].upper(), word[-1].upper(), word[0].lower(), word[-1]])+word[:3].upper()+str(random.randint(1000,9999))+word[1].upper()+word[-2]

    if t==3:
        if len(word)<=2:
            password+=(random.choice(["!","@","#","$","%"]))*2+str(random.randint(1000,9999))+(word[::-1]+ str(random.randint(1,9)) if len(word)==2 else (word*3))+(random.choice(["&","*"]))
        else:
            password+=(word[:3].upper())+str(random.randint(1000,9999))+random.choice(["!","@","#","$","%"])+word[::-1][0]+random.choice([word[0].upper(), word[-1].upper()])

    return password

def get_name():
    name=input("Name: ").strip().capitalize()#убираем пробелы, записываем с заглавной буквы
    while (len(name)==0) or (name in "!@#$%^&*()=+\,/|"):
        name=input("Name: ").strip().capitalize()
    return name

def get_age():
    age=input("Age: ")
    while not(age.isnumeric()) or (int(age) not in list(range(13,121))):
        age=input("Age: ")
    return int(age)

def get_country():
    country=input("Country: ").strip().capitalize()
    while (len(country)==0) or not(country.isalpha()):
        country=input("Country: ").strip().capitalize()
    return country

def get_user_info():
    name=get_name()
    age=get_age()
    country=get_country()
    return[name,age,country]

def display_user_info(info):
    print(f"{info[0]} is {info[1]} years old. {info[0]} is from {info[2]}.")

def load_json(f): #загрузка файла json
    try:
        with open(f"{f}.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return "File not found"

if __name__=="__main__": #файл позвали напрямую, используя команду Питона
    user_input=" "
    while len(user_input)==0 or user_input==" ":
        user_input=input("Please enter your word:\n")
    print(password_gen(user_input))
    print(load_json("tudents"))
