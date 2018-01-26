def printl(list = []):
    i=0
    for i in list:
        print(list)
        i=i+1
        
n = int((input("give n ")))
m = int((input("give m ")))
pile_1 = []
pile_2 = []
for i in range(n):
    x = int(input())
    pile_1.append(x)
for j in  range(m):
    y = int(input())
    pile_2.append(y)
count = 0;
while(1):
    print("This is x's turn")
    ans = input("from where do you want to take a/b/c?")
    if ans == "a":
        del(pile_1[-1])
        printl(pile_1)
        if not pile_1:
            print("x won")
            break
    elif ans == "b":
        del(pile_2[-1])
        printl(pile_2)
        if not pile_2:
            print("x won")
            break
    elif ans == "c":
        if pile_1[-1]==pile_2[-1]:
            del(pile_1[-1])
            del(pile_2[-1])
            printl(pile_1)
            print("/n")
            printl(pile_2)
            if not pile_1:
                print("x won")
                break
            if not pile_2:
                print("x won")
                break
        else:
            print("you have to take from pile 1 or pile 2")
            ans = input("from where do you want to take a/b/c?")
            if ans == "a":
               del(pile_1[-1])
               printl(pile_1)
               if not pile_1:
                  print("x won")
                  break
            elif ans == "b":
               del(pile_2[-1])
               printl(pile_2)
               if not pile_2:
                  print("x won")
                  break
    print("This is y's turn")
    ans = input("from where do you want to take a/b/c?")
    if ans == "a":
        del(pile_1[-1])
        printl(pile_1)
        if not pile_1:
            print("y won")
            break
    elif ans == "b":
        del(pile_2[-1])
        printl(pile_2)
        if not pile_2:
            print("y won")
            break
    elif ans == "c":
        if pile_1[-1]==pile_2[-1]:
            del(pile_1[-1])
            del(pile_2[-1])
            printl(pile_1)
            print("/n")
            printl(pile_2)
            if not pile_1:
                print("y won")
                break
            if not pile_2:
                print("y won")
                break
        else:
            print("you have to take from pile 1 or pile 2")
            ans = input("from where do you want to take a/b/c?")
            if ans == "a":
               del(pile_1[-1])
               printl(pile_1)
               if not pile_1:
                  print("y won")
                  break
            elif ans == "b":
               del(pile_2[-1])
               printl(pile_2)
               if not pile_2:
                  print("y won")
                  break
    

        
            
            

        

    
    

