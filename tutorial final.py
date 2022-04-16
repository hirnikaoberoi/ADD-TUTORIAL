while True:
    print('\033[0;031;046m                       The Addion Tutorial')
    name=str(input(print('\033[0;033;046m Enter your name-')))
    if len(name)<=20:
        pass
    else:
        print('''\033[0;031;046m   
name limit exceed
Please reopen the program
''')
        break
    print('\033[0;033;046m','Hi',name,'Welcome to addition tutorial by- Hirnika Oberoi')
    print(''' Following are given the levels of the tutorial .Select one of them-
                 1. begginers level(for classes nursery to pre- primary) -1 digit addition
                 2. moderate level (for classes 1 to 2) -2 digit addition
                 3. high level (for classes 3 to 4)-3 to 4 digit addition
                 4. the advanced level(for higher classes)
                 5. exit the tutorial''')
    level=int(input(print('\033[0;035;046m ENTER THE LEVEL WHICH YOU WANT TO PRACTICE(enter the level no.eg=1,2) -')))
    while level==1:
            print('\033[0;031;046m           Level-1')
            a=int(input(print('\033[0;035;046m ','enter the no. of questions you want to practice -')))
            n=0
            for i in range(1,a +1): 
                import random
                num1=random.randrange(1,10)
                num2=random.randrange(1,10)
                print('\033[0;035;046m solve',num1,'+',num2,'=')
                sum1=num1+ num2
                ans1=int(input(print('\033[0;035;046m ENTER ANSWER-''ENTER ANSWER=')))
                if ans1==sum1:
                    n+=1
                    print('\033[0;032;046mWoohhoo...your answer is correct.')
                    if i==5:
                        level=2
                else:
                     print('\033[0;031;046m OOPS! incorrect answer.The correct answer was',sum1)
            print('\033[0;032;046m',  'Your score is ',n,'out of',a)
            m=input('''\033[0;033;046m 
Do you want to continue with is level ?
    or
move to next level?
write "yes"if you want to continue with this level or 'no' to move to next level
    or
if you want to exit the module write '0'-
''')
            if m=='yes':
                print('\033[0;035;046m OK,there we go again')
                level=1
            elif m=='0':
                level=0
            else:
                level=2
    while level==2:
            print('\033[0;031;046m          Level-2')
            b=int(input(print('\033[0;035;046m enter the no. of questions you want to practice -')))
            o=0
            for i in range(1,b+1): 
                import random
                num3=random.randrange(1,100)
                num4=random.randrange(1,100)
                print('\033[0;035;046m','solve',num3,'+',num4,'=')
                sum2=num3+num4
                ans2=int(input(print('\033[0;035;046m ENTER ANSWER-''ENTER ANSWER=')))
                if ans2==sum2:
                    o+=1
                    print('\033[0;032;046mWoohhoo...your answer is correct.')
                    if i==5:
                      level=3
                else:
                     print('\033[0;031;046m OOPS! incorrect answer. The correct answer was',sum2)
            print('\033[0;032;046m',  'Your score is ',o,'out of',b)
            r=input('''\033[0;033;046m 
Do you want to continue with is level ?
    or
move to next level?
write "yes"if you want to continue with this level or 'no' to move to next level
    or
if you want to exit the module write '0' -
''')
            if r=='yes':
                     print('\033[0;035;046m OK,there we go again')
                     level=2
            elif r=='0':
                level=0
            else:
                     level=3
    while level==3:
            print('\033[0;031;046m            Level-3')
            c=int(input(print('\033[0;035;046m enter the no.of questions you want to practice-')))
            p=0
            for i in range(1,c+1): 
                import random
                num5=random.randrange(1,1000)
                num6=random.randrange(1,1000)
                print('\033[0;035;046m ','solve',num5,'+',num6,'=')
                sum3=num5+num6
                ans3=int(input(print('\033[0;035;046m ENTER ANSWER-''ENTER ANSWER=')))
                if ans3==sum3:
                    p+=1
                    print('\033[0;032;046mWoohhoo...your answer is correct.')
                    if i==5:
                      level=4
                else:
                     print('\033[0;031;046m OOPS! incorrect answer.The correct answer was',sum3)
            print('\033[0;032;046m',  'Your score is ',p,'out of',c)
            s=input(print('''\033[0;033;046m
Do you want to continue with is level ?
    or
move to next level?
write "yes"if you want to continue with this level or 'no' to move to next level
    or
if you want to exit the module write '0'-'''))
            if s=='yes':
                print('\033[0;035;046m OK,there we go again')
                level=3
            elif s=='0':
                level=0
            else:
                level=4
    while level==4:
            print('\033[0;031;046m            Level-4')
            d=int(input(print('\033[0;035;046m enter the no. of questions you want to practice-')))
            q=0
            for i in range(1,d+1): 
                import random
                num7=random.randrange(1,10000)
                num8=random.randrange(1,10000)
                print('\033[0;035;046m ','solve',num7,'+',num8,'=')
                sum4=num7+num8
                ans4=int(input(print('\033[0;035;046m ENTER ANSWER-''ENTER ANSWER=')))
                if ans4==sum4:
                    q  =1
                    print('\033[0;032;046mWoohhoo...your answer is correct.')
                else:
                     print('\033[0;031;046m OOPS! incorrect answer.The correct answer was',sum4)
            print('\033[0;032;046m',  'Your score is ',q,'out of',d)
            print('\033[0;031;046m CONGRATULATONS!You have successfully completed your addition tutorial')
            t=input('''
Do you want to continue with is level ?
    or
you want to exit the module write '0'-''')
            if t=='0':
                level=0
            elif t=='yes':
                print('\033[0;035;046m OK,there we go again')
                level=4
    while level==0 or level==5:
        print('\033[0;031;046m THANK YOU FOR USING THE ADDITION TUTORIALS BY HIRNIKA OBEROI')
        break
   


    

  

    





