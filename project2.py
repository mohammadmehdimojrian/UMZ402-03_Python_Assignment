import keyword
import random
from inputimeout import inputimeout          #pip install inputimeout
import time
from string import punctuation           
import turtle
ket_list=[]
#تابع مربوط به ماموریت اول
def decrypt_clue(text):
    s=[]
    lr=text.readlines()
    st=''.join(lr)
    for i in keyword.kwlist:
        for j in range(0,len(lr)):
            if i in lr[j]:
                s.append(i)
    s=list(set(s))
    s.sort(key=st.find)
    return s
#تابع مربوط به ماموریت دوم
def solve_puzzles(puzzles):
    so=list()
    l=puzzles.readlines()
    for i in range(0,len(l)):
        l[i]=l[i].replace("\n","")
    for j in l:
        try:
            so.append(bool(eval(j)))
        except:
            so.append(None)
    return so

#ایجاد لیستی از اعداد رندوم با کمک گرفتن از زمان مروط به ماموریت سوم
def calculate_magic_numbers(start, end):
    maagic=list()
    x=time.time()-int(time.time())
    for cj in range(10):
        z=int(x*(end-start)+start)
        maagic.append(z)
        x=2*x-int(2*x)
    return maagic
#تابع ساخت ازمون اعداد مربوط به ماموریت سوم
def exam_numbers():
    correct=0
    incorrect=0
    while(True):
        start=time.time()
        exam_list=[]
        while(True):
            test=1
            number=format(random.randint(0,15),"04b")
            try:
                num_user=int(inputimeout(prompt="%s enter the DES: "%number,timeout=20-(time.time()-start)))
            except ValueError:
                num_user=16
                test=0
                print("Only the number can be calculated!")
            except Exception:
                break
            num_user=format(num_user,"04b")
            if number==num_user:
                correct+=1
                if test:
                    exam_list.append(True)
            else:
                if test:
                    incorrect+=1
                    exam_list.append(False)
        if len(exam_list)>=1:
            ket_list.append(str(exam_list[0]))
            break
        print("Rstart....,please,fill in the blank with a num in 20sec again....")
    print("the correct is %i"%correct)
    print("the incorrect is %i"%incorrect)
#تابع یوزر و پسورد مروبط به ماموریت سوم
def check_pass():
    list_user=list()
    correct_user=list()
    user=0
    while(user<5):
        karbari=input("Enter your user %i: "%(user+1))
        if karbari.strip()=='':
            while(True):
                print("fill in the blank")
                karbari=input("Enter your user %i: "%(user+1))
                if karbari.strip()!='':
                    break;
        password=input("Enter your pass %i: "%(user+1))
        if password.strip()=='':
            while(True):
                print("fill in the blank")
                password=input("Enter your pass %i: "%(user+1))
                if password.strip()!='':
                    break;
        if password.strip()!='' and  karbari.strip()!='':
            list_user.append((karbari,password))
            user+=1
    for (x,y) in list_user:
        con1=0
        con2=0
        con3=0
        con4=0
        for character in y:
            if ord(character)>=65 and ord(character)<=90:
                con1=1
            if len(y)>=8:
                con2=1
            if character in punctuation:
                con3=1
            if ord(character)>=97 and ord(character)<=122:
                con4=1
        if con1 and con2 and con3 and con4:
            correct_user.append(x)
    if len(correct_user)>=1:
        ket_list.append(correct_user[0])
        return correct_user
    else:
        return (" Not found!... ")

#تابع رسم لاترجی 
def tarji():
    wn=turtle.Screen()
    laki=turtle.Turtle()
    turtle.setup(width=1200,height=630)
    laki.speed(2)
    laki.pensize(10)
    laki.right(75)
    laki.forward(200)
    laki.right(105)
    laki.forward(100)  
    laki.right(120)
    laki.forward(220)
    laki.penup()
    laki.backward(80)
    laki.left(120)
    laki.penup()
    laki.forward(100)
    laki.left(90)
    laki.pendown()
    laki.forward(70)
    laki.right(90)
    laki.fd(30)
    laki.penup()
    laki.right(90)
    laki.fd(90)
    laki.stamp()
    laki.left(90)
    laki.shape("circle")
    laki.stamp()
    laki.fd(40)
    laki.stamp()
    laki.shape("classic")
    laki.left(90)
    laki.fd(90)
    laki.right(90)
    laki.backward(40)
    laki.pendown()
    laki.fd(70)
    laki.left(60)
    laki.forward(110)
    laki.penup()
    laki.backward(110)
    laki.right(60)
    laki.fd(60)
    laki.right(90)
    laki.pendown()
    laki.fd(90)
    laki.left(90)
    laki.fd(50)
    laki.backward(50)
    laki.right(90)
    laki.backward(90)
    laki.left(90)
    laki.forward(105)
    laki.right(90)
    laki.backward(45)
    laki.penup()
    laki.right(90)
    laki.fd(55)
    laki.shape("circle")
    laki.stamp()
    laki.backward(55)
    laki.left(90)
    laki.shape("classic")
    laki.pendown()
    laki.backward(40)
    laki.left(90)
    laki.fd(100)
    laki.right(90)
    laki.fd(40)
    wn.mainloop()    #اگه ندیدیش ،حتما داره توی دسکتاپ اجرا میشه،توی تسکبار  بزنی سرش میبینیش یا اینکه دسکتاپ رو ببین،برای ادامه برنامه  هم صفحه رو ببند
def unlock_vault(clues):
    passwordend=list()
    for i in clues:
        passwordend.append(i[0])
    passwordend=''.join(passwordend)
    return passwordend
#ماموریت اول
fid1=open("mysterious.txt")
print("The output of the first mission: ")
form=decrypt_clue(fid1)
print(form)
ket_list.append(form[0])
fid1.close()
print("\n")

#ماموریت دوم
fid2=open("puzzles.txt","r")
print("The output of the second mission: ")
form=solve_puzzles(fid2)
print(form)
ket_list.append(str(form[0]))
fid2.close()
print("\n")
#ماموریت سوم
a1=10
a2=100
print("The output of the third mission: ")
form=calculate_magic_numbers(a1,a2)
print(form)
ket_list.append(str(form[0]))
exam_numbers()

print(check_pass())

#ماموریت جهارم
tarji()    #برای ادامه مسیر باید صفحه گرافیکی را ببندی 
print("Legendary password: %s"%unlock_vault(ket_list))





