def isOperator(x):
    #Function to check if the string x is an operator or not
    # INPUT Parameters:
    # x : string
    # OUTPUT Parameters:
    # bool :
    if x=='+' or '-' or '*' or '//' or '>' or '<' or '>=' or '<=' or '==' or'!=' or 'and' or 'or':
        return True
    return False

def Binary(x,a,b):
    #Function to perform binary operation x on a and b
    if x=='+':
        return a+b
    elif x=='-':
        return a-b
    elif x=='*':
        return a*b
    elif x=='/':
        return a//b
    elif x=='>':
        return a>b
    elif x=='<':
        return a<b
    elif x== '>=': 
        return a>=b
    elif x== '<=':
        return a<=b
    elif '==' :
        return a==b
    elif x=='!=':
        return a!=b
    elif x== 'and':
        return a and b
    else:
        return a or b

def Unary(x,a):
    if x=='not':
        return not a
    return -a

def isNegation(x):
    return (x=='-' or x=='not')

def isEqual(x):
    return x=='='
    
def Search_int(L,i):              #L is a list of tupules and numerals
    j=0
    found=False
    while j < len(L) and not found:
        if isinstance(L[j],tuple):
            j+=1
        else:
            if L[j] is i:
                found=True
            else:
                j+=1
    return (found,j)


def Search_tuple(L,x):              #L is a list of tupules and numerals
    j=0
    found=False
    while j < len(L) and not found:
        if not isinstance(L[j],tuple):
            j+=1
        else:
            if L[j][0]==x:
                found=True
            else:
                j+=1
    return (found,j)

def isint(s):
    return s.isnumeric()

def isbool(s):
    return s=='True' or s== 'False'

def isvar(s):
    return s.isalpha()

def f(s):
    if s== 'True':
        return True
    elif s== 'False':
        return False
    else:
        return int(s)

lines = [] # initalise to empty list
with open('D:/Users/Kushagra Gupta/Downloads/input_file.txt') as g:
    lines = g.readlines() # read all lines into a list of strings

DATA_list=[]

for statement in lines: # each statement is on a separate line
    token_list = statement.split() # split a statement into a list of tokens

    # now process each statement
    if len(token_list)==3:
        if isvar(token_list[0]) and isEqual(token_list[1]) and (isvar(token_list[2]) or isint(token_list[2] or isbool(token_list[2]))):       
            (bool,k)=Search_tuple(DATA_list,token_list[0])
            if not bool:
                if isint(token_list[2]) or isbool(token_list[2]):
                    (u,v)=Search_int(DATA_list,f(token_list[2]))
                    if not u:
                        DATA_list.append(f(token_list[2]))
                        DATA_list.append((token_list[0], len(DATA_list)-1))
                    else:
                        DATA_list.append((token_list[0], v))
                else:
                    (u,v)=Search_tuple(DATA_list,token_list[2])
                    if u:
                        DATA_list.append((token_list[0],DATA_list[v][1]))
                    else:
                        print('Variable',token_list[2],'is not defined')
                        exit()      
            else:
                if isint(token_list[2]) or isbool(token_list[2]):
                        (u,v)=Search_int(DATA_list,f(token_list[2]))
                        if not u:
                            DATA_list.append(f(token_list[2]))
                            DATA_list[k]=(token_list[0],len(DATA_list)-1)
                        else:
                            DATA_list[k]=(token_list[0], v)
                else:
                    (u,v)=Search_tuple(DATA_list,token_list[2])
                    if u:
                        DATA_list[k]=(token_list[0],DATA_list[v][1])
                    else:
                        print('Variable',token_list[2],'is not defined')
                        exit()    
        else:
            print ('SYNTAX ERROR')
            exit()

    elif len(token_list)==4:
        if isvar(token_list[0]) and isEqual(token_list[1]) and isNegation(token_list[2]) and (isvar(token_list[3]) or isint(token_list[3]) or isbool(token_list[3])):
            (bool,k)=Search_tuple(DATA_list,token_list[0])
            if not bool:
                if isint(token_list[3]) or isbool(token_list[3]):
                    (u,v)=Search_int(DATA_list,f(token_list[3]))
                    if not u:
                        DATA_list.append(f(token_list[3]))
                        f,t = Search_int(DATA_list,Unary(token_list[2],f(token_list[3])))
                        if not f:
                            DATA_list.append(Unary(token_list[2],f(token_list[3])))
                            DATA_list.append((token_list[0], len(DATA_list)-1))
                        else:
                            DATA_list.append((token_list[0], t))
                    else:
                        f,t = Search_int(DATA_list,Unary(token_list[2],(DATA_list[v])))
                        if not f:
                            DATA_list.append(Unary(token_list[2],(DATA_list[v])))
                            DATA_list.append((token_list[0], len(DATA_list)-1))
                        else:
                            DATA_list.append((token_list[0], t))
                else:
                    (u,v)=Search_tuple(DATA_list,token_list[3])
                    if u:
                        f,t = Search_int(DATA_list,Unary(token_list[2],DATA_list[DATA_list[v][1]]))
                        if not f:
                            DATA_list.append(Unary(token_list[2],DATA_list[DATA_list[v][1]]))
                            DATA_list.append((token_list[0],len(DATA_list)-1))
                        else:
                            DATA_list.append((token_list[0], t))
                    else:
                        print('Variable',token_list[3],'is not defined')
                        exit()
            else:
                if isint(token_list[3]) or isbool(token_list[3]):
                    (u,v)=Search_int(DATA_list,token_list[3])
                    if not u:
                        f,t = Search_int(DATA_list,Unary(token_list[2],f(token_list[3])))
                        if not f:
                            DATA_list.append(f(token_list[3]))
                            DATA_list.append(Unary(token_list[2],f(token_list[3])))
                            DATA_list[k]=(token_list[0], len(DATA_list)-1)
                        else:
                            DATA_list[k]=(token_list[0], t)
                    else:
                        f,t = Search_int(DATA_list,Unary(token_list[2],(DATA_list[v])))
                        if not f:
                            DATA_list.append(Unary(token_list[2],DATA_list[v]))
                            DATA_list[k]=(token_list[0], len(DATA_list)-1)
                        else:
                            DATA_list[k]=(token_list[0], t)
                else:
                    (u,v)=Search_tuple(DATA_list,token_list[3])
                    if u:
                        f,t = Search_int(DATA_list,Unary(token_list[2],DATA_list[DATA_list[v][1]]))
                        if not f:
                            DATA_list.append(Unary(token_list[2],DATA_list[DATA_list[v][1]]))
                            DATA_list[k]=(token_list[0],len(DATA_list)-1)
                        else:
                            DATA_list[k]=(token_list[0],t)
                    else:
                        print('Variable',token_list[3],'is not defined')
                        exit()
        else:
            print ('SYNTAX ERROR')
            exit()
    elif len(token_list)==5:
        if isvar(token_list[0]) and isEqual(token_list[1]) and (isvar(token_list[2]) or isint(token_list[2]) or isbool(token_list[2])) and (isvar(token_list[4]) or isint(token_list[4]) or isbool(token_list[4])) and isOperator(token_list[3]):   
            (bool,k)=Search_tuple(DATA_list,token_list[0])
            if not bool:
                if (isint(token_list[2]) or isbool(token_list[2])) and (isint(token_list[4]) or isbool(token_list[4])):
                    (u,v)=Search_int(DATA_list,f(token_list[2]))
                    (w,z)=Search_int(DATA_list,f(token_list[4]))
                    if u and w:
                        f,t = Search_int(DATA_list,Binary(token_list[3],DATA_list[v],DATA_list[z]))
                        if not f:
                            DATA_list.append(Binary(token_list[3],DATA_list[v],DATA_list[z]))
                            DATA_list.append((token_list[0], len(DATA_list)-1))
                        else:
                            DATA_list.append((token_list[0],t))
                    elif not u and not w:
                        DATA_list.append(f(token_list[2]))
                        DATA_list.append(f(token_list[4]))
                        f,t = Search_int(DATA_list,Binary(token_list[3],f(token_list[2]),f(token_list[4])))
                        if not f:
                            DATA_list.append(Binary(token_list[3],f(token_list[2]),f(token_list[4])))
                            DATA_list.append((token_list[0], len(DATA_list)-1))
                        else:
                            DATA_list.append((token_list[0],t))
                    elif not u and w:
                        DATA_list.append(token_list[2])
                        f,t = Search_int(DATA_list,Binary(token_list[3],f(token_list[2]),f(token_list[4])))
                        if not f:
                            DATA_list.append(Binary(token_list[3],f(token_list[2]),DATA_list[z]))
                            DATA_list.append((token_list[0], len(DATA_list)-1))
                        else:
                            DATA_list.append((token_list[0],t))
                    else:
                        DATA_list.append(f(token_list[4]))
                        DATA_list.append(Binary(token_list[3],DATA_list[v],f(token_list[4])))
                        DATA_list.append((token_list[0], len(DATA_list)-1))

                elif not (isint(token_list[2]) and isbool(token_list[2])) and not (isint(token_list[4]) and isbool(token_list[4])):
                    (u,v)=Search_tuple(DATA_list,token_list[2])
                    (w,z)=Search_tuple(DATA_list,token_list[4])
                    if u and w:
                        DATA_list.append(Binary(token_list[3],DATA_list[DATA_list[v][1]],DATA_list[DATA_list[z][1]]))
                        DATA_list.append((token_list[0],len(DATA_list)-1))
                    elif not u and w:
                        print('Variable',token_list[2],'is not defined')
                        exit()
                    elif not w and u:
                        print('Variable',token_list[4],'is not defined')
                        exit()
                    else:
                        print('Variables',token_list[2],token_list[2],'are not defined')
                        exit()
                elif not (isint(token_list[2]) and isbool(token_list[2])) and (isint(token_list[4]) and isbool(token_list[4])):
                    (u,v)=Search_tuple(DATA_list,token_list[2])
                    (w,z)=Search_int(DATA_list,f(token_list[4]))
                    if u and w:
                        DATA_list.append(Binary(token_list[3],DATA_list[DATA_list[v][1]],DATA_list[z]))
                        DATA_list.append((token_list[0],len(DATA_list)-1))
                    elif not w and u:
                        DATA_list.append(f(token_list[4]))
                        DATA_list.append(Binary(token_list[3],DATA_list[DATA_list[v][1]],f(token_list[4])))
                        DATA_list.append((token_list[0],len(DATA_list)-1))
                    else:
                        print('Variable',token_list[2],'is not defined')
                        exit()
                else:
                    (u,v)=Search_int(DATA_list,f(token_list[2]))
                    (w,z)=Search_tuple(DATA_list,token_list[4])
                    if u and w:
                        DATA_list.append(Binary(token_list[3],DATA_list[v],DATA_list[DATA_list[z][1]]))
                        DATA_list.append((token_list[0],len(DATA_list)-1))
                    elif not u and w:
                        DATA_list.append(int(token_list[2]))
                        DATA_list.append(Binary(token_list[3],f(token_list[2]),DATA_list[DATA_list[z][1]]))
                        DATA_list.append((token_list[0],len(DATA_list)-1))
                    else:
                        print('Variable',token_list[4],'is not defined')
                        exit()
            else:
                if (isint(token_list[2]) or isbool(token_list[2])) and (isint(token_list[4]) or isbool(token_list[4])):
                    (u,v)=Search_int(DATA_list,f(token_list[2]))
                    (w,z)=Search_int(DATA_list,f(token_list[4]))
                    if u and w:
                        DATA_list.append(Binary(token_list[3],DATA_list[v],DATA_list[z]))
                        DATA_list[k]=(token_list[0], len(DATA_list)-1)
                    elif not u and not w:
                        DATA_list.append(f(token_list[2]))
                        DATA_list.append(f(token_list[4]))
                        DATA_list.append(Binary(token_list[3],f(token_list[2]),f(token_list[4])))
                        DATA_list[k]=(token_list[0], len(DATA_list)-1)
                    elif not u and w:
                        DATA_list.append(token_list[2])
                        DATA_list.append(Binary(token_list[3],f(token_list[2]),DATA_list[z]))
                        DATA_list[k]=(token_list[0], len(DATA_list)-1)
                    else:
                        DATA_list.append(f(token_list[4]))
                        DATA_list.append(Binary(token_list[3],DATA_list[v],f(token_list[4])))
                        DATA_list[k]=(token_list[0], len(DATA_list)-1)

                elif not (isint(token_list[2]) and isbool(token_list[2])) and not (isint(token_list[4]) and isbool(token_list[4])):
                    (u,v)=Search_tuple(DATA_list,token_list[2])
                    (w,z)=Search_tuple(DATA_list,token_list[4])
                    if u and w:
                        DATA_list.append(Binary(token_list[3],DATA_list[DATA_list[v][1]],DATA_list[DATA_list[z][1]]))
                        DATA_list[k]=(token_list[0],len(DATA_list)-1)
                    elif not u and w:
                        print('Variable',token_list[2],'is not defined')
                        exit()
                    elif not w and u:
                        print('Variable',token_list[4],'is not defined')
                        exit()
                    else:
                        print('Variables',token_list[2],token_list[2],'are not defined')
                        exit()
                elif not (isint(token_list[2]) and isbool(token_list[2])) and (isint(token_list[4]) and isbool(token_list[4])):
                    (u,v)=Search_tuple(DATA_list,token_list[2])
                    (w,z)=Search_int(DATA_list,f(token_list[4]))
                    if u and w:
                        DATA_list.append(Binary(token_list[3],DATA_list[DATA_list[v][1]],DATA_list[z]))
                        DATA_list[k]=(token_list[0],len(DATA_list)-1)
                    elif not w and u:
                        DATA_list.append(f(token_list[4]))
                        DATA_list.append(Binary(token_list[3],DATA_list[DATA_list[v][1]],f(token_list[4])))
                        DATA_list[k]=(token_list[0],len(DATA_list)-1)
                    else:
                        print('Variable',token_list[2],'is not defined')
                        exit()
                else:
                    (u,v)=Search_int(DATA_list,f(token_list[2]))
                    (w,z)=Search_tuple(DATA_list,token_list[4])
                    if u and w:
                        DATA_list.append(Binary(token_list[3],DATA_list[v],DATA_list[DATA_list[z][1]]))
                        DATA_list[k]=(token_list[0],len(DATA_list)-1)
                    elif not u and w:
                        DATA_list.append(int(token_list[2]))
                        DATA_list.append(Binary(token_list[3],f(token_list[2]),DATA_list[DATA_list[z][1]]))
                        DATA_list[k]=(token_list[0],len(DATA_list)-1)
                    else:
                        print('Variable',token_list[4],'is not defined')
                        exit()                 
        else:
            print ('SYNTAX ERROR')
            exit() 
    else:
        print ('SYNTAX ERROR')
        exit()

j=0
l2=[]
while j<len(DATA_list):
    if isinstance(DATA_list[j],tuple):
        k = DATA_list[j][1]
        print(DATA_list[j][0],'=',DATA_list[k])
        l2.append(k)
        l2.append(j)
        j+=1
    else:
        j+=1

i=0
Garbage_list=[]
while i <len(DATA_list):
    if i not in l2:
        Garbage_list.append(DATA_list[i])
    i+=1
print('Garbage list is', Garbage_list)
