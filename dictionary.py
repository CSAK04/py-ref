info=[{"id":1,"name":"ak",
       "place":"mgm","pass":"pgmak"},
      {"id":2,"name":"tomorrow",
       "place":"marscolony","pass":"mars1"}]

"""print(words)
print(words[0].get("name"))
print(words[0].get("place"))"""

'''a=input("enter your name")

if(a==words[0].get("name")):
    print(words[0].get("place"))'''

a=int(input("enter ID"))

for i in range(0,len(info)):
    if(a==info[i].get("id")):
        password=input("enter password")
        sp=info[i].get("pass")
        if(len(password)<4):
            print("password cannot be less than 4 characters")
        if(password==sp):    
            place=info[i].get("place")
            name=info[i].get("name")
            print("you are",name)
            print("you are from",place)
            a="nothing"
        break    
