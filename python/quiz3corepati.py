name=input("enter your name")
print(" good to have you",name,"\n" ,"welcome to kaun bangega carore pati\n")

print("here is your questions")
questions=["which is the best team of ipl\n ","which is the best cricktr in world\n",""
"which is king of fruits\n","which is king of flowers\n"]

answers=["rcb","viratkohli","mango","rose"]

a=10000
b=20000
c=30000
d=40000

answer1=input(questions[0])
if(answer1==answers[0]):
    print("correct you want",a)
    answer2=input(questions[1])
    if(answer2==answers[1]):
        print("correct you won",b)
        answer3=input(questions[2])
        if(answer3==answers[2]):
            print("correct you won",c)
            answer4=input(questions[3])
            if(answer4==answers[3]):
                print("correct you won",d)
                print("you are winner of koun banega crore pati")
            else:
                print("incoorect take home ",c)
        else:
            print("incoorect take home money",b)
    else:
        print("wrong you take ",a,"to your home")
else:
    print("sorry you have won 0")