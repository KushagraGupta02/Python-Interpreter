class instruction:
    #Class instruction -- objects are either STATEMENT or while EXPRESSION : or Branch and corresponding address 
    def __init__(self, type, statement='', addr = -1):
        self.type = type 
        # Type -> 0 -> Statement
        #     -> 1 -> Branch 
        #     -> 2 -> BLE 
        #     -> 3 -> BLT
        #     -> 4 -> BE (Branch equal to)
        #     -> 5 -> BNE (Branch not equal to)
        self.statement = statement
        self.addr=addr
    def printinstr(self):
        # Method to print an object of class instruction, prints in a similar manner we need to print in the instruction list
        # prints statement directly, while condition replaced by appropriate branch and branch statement using address
        if self.type==0:
            print(self.statement.strip())
        if self.type==1:
            print('Branch',self.addr)
        if self.type==2:
            print('BLE '+self.statement+',',self.addr)
        if self.type==3:
            print('BLT '+self.statement+',',self.addr)
        if self.type==4:
            print('BE '+self.statement+',',self.addr)
        if self.type==5:
            print('BNE '+self.statement+',',self.addr)
    def execute(self,DATA,i):
        # Method to execute an object of class Instruction, the other paramaters provided are a global DATA list maintaining the values of variables
        # and i, which is the counter which we are traversing upon the instruction list, if we encounter a branch we shift the counter to the destination given by self.address
        # and if we encounter a while, we branch or enter depending on the expression condition      
        if self.type==1:
            # Branch
            print(DATA)
            garbage()
            print()
            return self.addr
        else:
            if self.type==0:
                statement=self.statement.strip()
            if self.type==2:
                statement= 'dummy = '+self.statement.split()[0]+' <= '+self.statement.split()[2]
            elif self.type==3:
                statement= 'dummy = '+self.statement.split()[0]+' < '+self.statement.split()[2]
            elif self.type==4:
                statement= 'dummy = '+self.statement.split()[0]+' != '+self.statement.split()[2]
            elif self.type==5:
                statement= 'dummy = '+self.statement.split()[0]+' == '+self.statement.split()[2]

            # Now that we have our statement, we can work upon it using and modifying the DATA list  
            
              
            # REUSING CODE FROM ASSIGNMENT 5 PART-1
            def isOperator(x):
                # Function to check if the string x is a Binary Operator or not
                # INPUT Parameters:
                # x : string -- the string we have to check to be a Binary Operator or not
                # OUTPUT: Bool -- Returns True if x is 'Binary Operator' and False otherwise
                if x=='+' or x=='-' or x=='*' or x=='/' or x=='>' or x=='<' or x=='>=' or x=='<=' or x=='==' or x=='!=' or x=='and' or x=='or':
                    return True
                else:
                    return False
                # Time Complexity -- O(1) since constant time is taken to check a condition and return a value

            def Binary(x,a,b):
                #Function to perform binary operation x on a and b
                # INPUT Parameters:
                # x : string -- the binary operator respresented by a string
                # a,b : string -- the first and the second term on which we have to perform the Binary Operation
                # OUTPUT : int or bool depending on a and b -- Returns the binary operation a x b
                if x=='!=':
                    return a!=b
                elif x=='+':
                    return a+b
                elif x=='-':
                    return a-b
                elif x=='*':
                    return a*b
                elif x=='/':
                    return a//b         #implemented integer division
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
                elif x== 'and':
                    return a and b
                elif x== 'or':
                    return a or b
                # Binary Operation can also be performed using eval as follows
                # def Binary(x,a,b):
                # if x!='/':
                #     return eval('a '+x+' b')
                # else:
                #     return a//b
                # Time Complexity -- O(1) since constant time is taken to check a condition and return a value

            def Unary(x,a):
                # Function to perform unary operation x on a
                # INPUT Parameters:
                # x : string -- the binary operator respresented by a string
                # a : string -- the term on which we have to perform the Binary Operation
                # OUTPUT : int or bool depending on a and b -- Returns the unary operation x a
                if x=='not':
                    return not a
                elif x=='-':
                    return -a
                # Time Complexity -- O(1) since constant time is taken to check a condition and return a value

            def isNegation(x):
                # Function to check if the string x is a Unary Operator or not
                # INPUT Parameter x : string  and OUTPUT : bool -- Returns True if x is ' Unary Operator' and False otherwise
                return (x=='-' or x=='not')
                # Time Complexity -- O(1) since constant time is taken to check a condition and return a value

            def isEqual(x):
                # Function to check if the string x is '='
                # INPUT Parameter x : string  and OUTPUT : bool -- Returns True if x is ' =' and False otherwise
                return x=='='
                # Time Complexity -- O(1) since constant time is taken to check a condition and return a value

            def Search_int(L,i):
            # INPUT Parameters
            # L -- List and i -- int
            # L is a list of tuples and integers
            # i is the integer which is checked in the List L
            # OUTPUT parameters -- (found,k)
            # found -- Bool and k -- int
            # found is True if i is found in the list and False otherwise; k is the position where i is found 
            # Initialisation
                j=0
                found=False
                # LOOP INVARIANT -- found = False implies that forall 0 < m <= j, L[m] != i and found = True implies L[k]= i
                while j < len(L) and not found:
                    if isinstance(L[j],tuple):
                        j+=1
                    else:
                        if L[j] is i:
                            found=True
                        else:
                            j+=1
                # EXIT WHEN j==len(L) or found== True
                # EXIT AND INVARIANT IMPLY OUTPUT SPEC AS WHEN j==len(L), found= False as i is not in list and otherwise found=True for L[k]=i
                # TIME COMPLEXITY -- O(len(L)) as linear search is performed and len(L) times the loop is iterated
                return (found,j)

            def Search_var(L,x):
                #L is a list of tupules and numeral
                # Analysis Done in a similar manner as Search_int x is string(alpha) instead of int
                # INPUT Parameters
                # L -- List and x -- string (alpha)
                # L is a list of tuples and integers
                # OUTPUT parameters -- (found,k)
                # found -- Bool and k -- int
                # found is True if x is found in the tuples in list and False otherwise; k is the position where i is found 
                # Initialisation
                j=0
                found=False
                # LOOP INVARIANT -- found = False implies that forall 0 < m <= j, L[m] != x and found = True implies L[k][0]= x
                while j < len(L) and not found:
                    if not isinstance(L[j],tuple):
                        j+=1
                    else:
                        if L[j][0]==x:          #Checking if x is same as x0 in tuple (x0,y0) = L[j] where x is the variable to be checked
                            found=True
                        else:
                            j+=1
                # TIME COMPLEXITY -- O(len(L)) as linear search is performed and len(L) times the loop is iterated
                return (found,j)

            def isint(s):
                # INPUT : s -- string and OUTPUT : bool -- Returns True if s is an integer and False otherwise
                return s.isnumeric()
                # Time Complexity -- O(1) since constant time is taken to check a condition and return a value

            def isbool(s):
                # INPUT : s -- string and OUTPUT : bool -- Returns True if s is an bool and False otherwise
                return s=='True' or s== 'False'
                # Time Complexity -- O(1) since constant time is taken to check a condition and return a value

            def isvar(s):
                # INPUT : s -- string and OUTPUT : bool -- Returns True if s is an string of alphabets and False otherwise
                return s.isalpha()
                # Time Complexity -- O(1) since constant time is taken to check a condition and return a value

            def f(s):
                # Function returning the integer or bool represented by the string s
                # INPUT : s -- string and OUTPUT : bool or int
                if s== 'True':
                    return True
                elif s== 'False':
                    return False
                else:
                    return int(s)
                # Time Complexity -- O(1) since constant time is taken to perform int(s) and return a value

            def modify(DATA,bool,k,tup):
                # Function to modify the DATA list where tup is the tuple that represents (variable, reference) where reference is to the value of the variable
                # Modify DATA list if bool is True using k othertwise append tuple
                # INPUT Parameters -- DATA: list, bool: Bool, k -- int, tup: tuple
                # OUTPUT Paramters -- DATA: list -- returns the mdoified list
                if bool:
                    DATA[k]=tup
                else:
                    DATA.append(tup)
                return DATA
                # Time Complexity -- O(1) since constant time is taken to append a tuple or modify an element of the DATA list

            def Answer(DATA,val,bool,k,tup):
                # Fuction to search if val calculated using our operation is present in the DATA list or not, if not append it and modify DATA list
                # otherwise modify DATA list using reference of val
                # INPUT Parameters -- DATA: list, val: bool or int, bool: Bool, k -- int, tup: tuple
                # OUTPUT Paramters -- DATA: list -- returns the mdoified list
                if Search_int(DATA,val)[0]:         #if val found in DATA
                    tup=(tup[0],Search_int(DATA,val)[1])      # change second element of tup to reference pointing to val in DATA list
                else:
                    DATA.append(val)
                    tup=(tup[0],len(DATA)-1)
                return modify(DATA,bool,k,tup)
                # Time Complexity -- O(len(DATA)) since O(len(L)) time is taken to search for an element in L and rest operations take constant time
            token_list = statement.split() # split a statement into a list of tokens
            # now processing each statement on the basis of length of the statement
            if len(token_list)==3:                  # Variable = Term
                if isvar(token_list[0]):            # Variable Name is Valid
                    if isEqual(token_list[1]):      # '=' is Valid
                        if (isvar(token_list[2]) or isint(token_list[2] or isbool(token_list[2]))):     #Term is Valid
                            (bool,k)=Search_var(DATA,token_list[0])
                            if isint(token_list[2]) or isbool(token_list[2]):       #Performed depending on Term is variable or integer
                                (u,v)=Search_int(DATA,f(token_list[2]))
                                if not u:
                                    DATA.append(f(token_list[2]))
                                    modify(DATA,bool,k,(token_list[0], len(DATA)-1))
                                else:
                                    modify(DATA,bool,k,(token_list[0], v))
                            else:
                                (u,v)=Search_var(DATA,token_list[2])
                                if u:
                                    modify(DATA,bool,k,(token_list[0],DATA[v][1]))
                                else:
                                    print(f"Variable '{token_list[2]}' is not defined")
                                    exit()
                        else:
                            print('Syntax ERROR -- Invalid Term in Expression')
                            exit()
                    else:
                        print('Syntax ERROR -- Incorrect Format Variable = Expression')
                        exit()
                else:
                    print('Syntax ERROR -- Incorrect Variable Name')
                    exit()
            elif len(token_list)==4:            # Variable = Unary_Operator Term
                if isvar(token_list[0]):        # Variable Name is Valid
                    if isEqual(token_list[1]):  # '=' is Valid
                        if isNegation(token_list[2]):       # Operator is Valid
                            if (isvar(token_list[3]) or isint(token_list[3]) or isbool(token_list[3])):     #Term is Valid
                                (bool,k)=Search_var(DATA,token_list[0])
                                if isint(token_list[3]) or isbool(token_list[3]):   #Performed depending on Term is variable or integer
                                    (u,v)=Search_int(DATA,f(token_list[3]))
                                    if not u:
                                        DATA.append(f(token_list[3]))
                                        val=Unary(token_list[2],f(token_list[3]))
                                        Answer(DATA,val,bool,k,(token_list[0], len(DATA)-1))
                                    else:
                                        val=Unary(token_list[2],(DATA[v]))
                                        Answer(DATA,val,bool,k,(token_list[0], len(DATA)-1))
                                else:
                                    (u,v)=Search_var(DATA,token_list[3])
                                    if u:
                                        val=Unary(token_list[2],DATA[DATA[v][1]])
                                        Answer(DATA,val,bool,k,(token_list[0],len(DATA)-1))
                                    else:
                                        print(f"Variable '{token_list[3]}' is not defined")
                                        exit()
                            else:
                                print('Syntax ERROR -- Invalid Term in Expression')
                                exit()
                        else:
                            print('Syntax ERROR -- Invalid Operator', token_list[2])
                            exit()
                    else:
                        print('Syntax ERROR -- Incorrect Format Variable = Expression')
                        exit()
                else:
                    print('Syntax ERROR -- Incorrect Variable Name')
                    exit()

            elif len(token_list)==5:               # Variable = Binary_Operator Term Binary_Operator
                if isvar(token_list[0]):           # Variable Name is Valid
                    if isEqual(token_list[1]):     # '=' is Valid
                        if (isvar(token_list[2]) or isint(token_list[2]) or isbool(token_list[2])) and(isvar(token_list[4]) or isint(token_list[4]) or isbool(token_list[4])):  #Term is Valid
                            if isOperator(token_list[3]):   #Operator is Valid
                                (bool,k)=Search_var(DATA,token_list[0])
                                if (isint(token_list[2]) or isbool(token_list[2])) and (isint(token_list[4]) or isbool(token_list[4])): #Performed depending on Terms are variable or integer
                                    (u,v)=Search_int(DATA,f(token_list[2]))
                                    (w,z)=Search_int(DATA,f(token_list[4]))
                                    if u and w:
                                        val=Binary(token_list[3],DATA[v],DATA[z])
                                        Answer(DATA,val,bool,k,(token_list[0], len(DATA)-1))
                                    elif not u and not w:
                                        if token_list[2] != token_list[4]:          #if both terms are same so append only once
                                            DATA.append(f(token_list[2]))
                                        DATA.append(f(token_list[4]))
                                        val=Binary(token_list[3],f(token_list[2]),f(token_list[4]))
                                        Answer(DATA,val,bool,k,(token_list[0], len(DATA)-1))
                                    elif not u and w:
                                        DATA.append(token_list[2])
                                        val=(Binary(token_list[3],f(token_list[2]),DATA[z]))
                                        Answer(DATA,val,bool,k,(token_list[0], len(DATA)-1))
                                    else:
                                        DATA.append(f(token_list[4]))
                                        val=(Binary(token_list[3],DATA[v],f(token_list[4])))
                                        Answer(DATA,bool,k,(token_list[0], len(DATA)-1))

                                elif not (isint(token_list[2]) or isbool(token_list[2])) and not (isint(token_list[4]) or isbool(token_list[4])):
                                    (u,v)=Search_var(DATA,token_list[2])
                                    (w,z)=Search_var(DATA,token_list[4])
                                    if u and w:
                                        val=Binary(token_list[3],DATA[DATA[v][1]],DATA[DATA[z][1]])
                                        Answer(DATA,val,bool,k,(token_list[0],len(DATA)-1))
                                    elif not u and w:
                                        print(f"Variable '{token_list[2]}' is not defined")
                                        exit()
                                    elif not w and u:
                                        print(f"Variable '{token_list[4]}' is not defined")
                                        exit()
                                    else:
                                        print(f"Variables '{token_list[2]}','{token_list[4]}' are not defined")
                                        exit()
                                elif not (isint(token_list[2]) or isbool(token_list[2])) and (isint(token_list[4]) or isbool(token_list[4])):
                                    (u,v)=Search_var(DATA,token_list[2])
                                    (w,z)=Search_int(DATA,f(token_list[4]))
                                    if u and w:
                                        val=Binary(token_list[3],DATA[DATA[v][1]],DATA[z])
                                        Answer(DATA,val,bool,k,(token_list[0],len(DATA)-1))
                                    elif not w and u:
                                        DATA.append(f(token_list[4]))
                                        val=Binary(token_list[3],DATA[DATA[v][1]],f(token_list[4]))
                                        Answer(DATA,val,bool,k,(token_list[0],len(DATA)-1))
                                    else:
                                        print(f"Variable '{token_list[2]}' is not defined")
                                        exit()
                                else:
                                    (u,v)=Search_int(DATA,f(token_list[2]))
                                    (w,z)=Search_var(DATA,token_list[4])
                                    if u and w:
                                        val=(Binary(token_list[3],DATA[v],DATA[DATA[z][1]]))
                                        Answer(DATA,val,bool,k,(token_list[0],len(DATA)-1))
                                    elif not u and w:
                                        DATA.append(int(token_list[2]))
                                        val=(Binary(token_list[3],f(token_list[2]),DATA[DATA[z][1]]))
                                        Answer(DATA,val,bool,k,(token_list[0],len(DATA)-1))
                                    else:
                                        print(f"Variable '{token_list[4]}' is not defined")
                                        exit()
                            else:
                                print('Syntax ERROR -- Invalid Operator',token_list[3])
                                exit()
                        else:
                            print('Syntax ERROR -- Invalid Term in Expression')
                            exit()
                    else:
                        print('Syntax ERROR -- Incorrect Format Variable = Expression')
                        exit()
                else:
                    print('Syntax ERROR -- Incorrect Variable Name')
                    exit()
            else:
                print('Syntax ERROR -- STATEMENT has more than 5 or less than 3 tokens')
                exit()
            if self.type==0:        # when there is a statement return value is increasing the counter by 1 since we traverse forward
                return i+1
            else:                   # we check if the variable dummy is true or not and work accordingly
                k=Search_var(DATA,'dummy')[1]
                if DATA[DATA[k][1]]==True:
                    return self.addr
                else:
                    return i+1
 
def garbage():
    #Whenever called, returns the current values of variables and the garbage list
    def Search_int(L,i):
            # INPUT Parameters
            # L -- List and i -- int
            # L is a list of tuples and integers
            # i is the integer which is checked in the List L
            # OUTPUT parameters -- (found,k)
            # found -- Bool and k -- int
            # found is True if i is found in the list and False otherwise; k is the position where i is found 
            # Initialisation
                j=0
                found=False
                # LOOP INVARIANT -- found = False implies that forall 0 < m <= j, L[m] != i and found = True implies L[k]= i
                while j < len(L) and not found:
                    if isinstance(L[j],tuple):
                        j+=1
                    else:
                        if L[j] is i:
                            found=True
                        else:
                            j+=1
                # EXIT WHEN j==len(L) or found== True
                # EXIT AND INVARIANT IMPLY OUTPUT SPEC AS WHEN j==len(L), found= False as i is not in list and otherwise found=True for L[k]=i
                # TIME COMPLEXITY -- O(len(L)) as linear search is performed and len(L) times the loop is iterated
                return (found,j)
        #PRINTING VALUES OF VARIABLES
    #INITIALISATION
    j=0
    l2=[]           #References pointing to tuples and already referenced objects
    # LOOP INVARIANT -- Printed values of variables occuring from 0 till j in DATA
    while j<len(DATA):
    # Printing the values of variables occuring in the DATA list
        if isinstance(DATA[j],tuple):
            k = DATA[j][1]
            if DATA[j][0] != 'dummy':       #As usual
                print(DATA[j][0],'=',DATA[k])
                l2.append(k)    #Object referenced in tuple
                l2.append(j)    #Tuple reference
            else:
                l2.append(j)            #Add the tuple but not the value as it is referenced to dummmy might also be referenced to something else
            j+=1
        else:
            j+=1
    # Time Complexity -- O(len(DATA)) since loop is iterated len(DATA) times
    #PRINTING GARBAGE VALUES
    #INITIALISATION
    i=0
    Garbage_list=[]
    # LOOP INVARIANT -- Printed values of garbage by checking if present in l2 occuring till i in DATA
    while i <len(DATA):
    # printing the garbage values present in DATA list
        if not Search_int(l2,i)[0]:
            Garbage_list.append(DATA[i])
        i+=1
    print('Garbage list -', Garbage_list)
    # Time Complexity -- O(len(l2)) since loop is iterated len(l2) times  


# Function to count number of Tabs
def give_tab(statement):
    tabs=0
    statement = statement.replace("    ", '\t')
    while statement[tabs] == '\t':
        tabs += 1
    return tabs
# Time complexity == O(len(statement))

#Function to give the length of the loop
def loop_length(lines,i):
    j=0
    while j+i+1<len(lines):
        if give_tab(lines[j+i+1])>give_tab(lines[i]):
            j+=1
        else:
            break
    return j+1
# Time compleixty == O(len(lines)) as loop iterated len(lines) times

# Now using the input to construct and execute the instruction list
lines = [] # initalise to empty list
with open('D:/Users/Kushagra Gupta/Downloads/test.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
    instr_list=[]
    while_list=[]
    k=0
    while k< len(lines): # each statement is on a separate line
        statement=lines[k]
        token_list = statement.split() # split a statement into a list of tokens
        # now process each statement
        if token_list[0]=='while':
            while_list.append(k)
        k+=1
    g=len(while_list)+len(lines)
    j=0  
    while j < g:
        statement=lines[j]
        token_list = statement.split() # split a statement into a list of tokens
        # now process each statement
        if token_list[0]=='while':
            # print(loop_length(lines,j)-1)
            o=give_tab(lines[j])
            lines.insert(j+loop_length(lines,j),'\t'*(o+1)+'Branch '+ str(j))
        j+=1
    i=0
    while i< len(lines): # each statement is on a separate line
        statement=lines[i]
        token_list = statement.strip().split() # split a statement into a list of tokens
        # now process each statement
        if token_list[0]=='while':
            j=loop_length(lines,i)
            # print(j)
            # print(i+j)
            if token_list[2]=='<':          #BLE opp
                instr_list.append(instruction(2,token_list[3]+' , '+token_list[1],i+j))
            elif token_list[2]=='>':        #BLE     
                instr_list.append(instruction(2,token_list[1]+' , '+token_list[3],i+j))
            elif token_list[2]=='<=':       #BLT opp
                instr_list.append(instruction(3,token_list[3]+' , '+token_list[1],i+j))
            elif token_list[2]=='>=':       #BLT 
                instr_list.append(instruction(3,token_list[1]+' , '+token_list[3],i+j))
            elif token_list[2]=='==':
                instr_list.append(instruction(5,token_list[1]+' , '+token_list[3],i+j))
            elif token_list[2]=='!=':
                instr_list.append(instruction(4,token_list[1]+' , '+token_list[3],i+j))
            else:
                print('SYNTAX ERROR')
                exit()
        elif token_list[0]=='Branch':
            instr_list.append(instruction(1,'',int(token_list[1])))
        else:
            instr_list.append(instruction(0,statement,-1))
        i+=1

#Printing the instructions list, each object printed on a different line
print('Instructions list --')
for i in instr_list:
    i.printinstr()      #using the method defined in the instruction class
print()

#Executing the instructions line by line using method execute defined in the instruction class
# when it exits a branch statement, the values of the variables and the garbage list is printed since it signifies the termination of the loop. 
h=0
DATA=[]
while h<len(instr_list):
    h=instr_list[h].execute(DATA,h)
print('Final iteration')
print(DATA)
garbage()  


# ERROR HANDLING:
# There are 2 classes of errors/exceptions handled in my program:
# 1) INVALID SYNTAX of the statement in the statement list:
# It has mainly errors such as Variable is not defined
#'Syntax ERROR -- Invalid Term in Expression'
#'Syntax ERROR -- Invalid Operator'
#'Syntax ERROR -- Incorrect Format Variable = Expression'
#'Syntax ERROR -- Incorrect Variable Name'
# I have used the same approach as in assignment 5 part - 1 to raise these errors by noticing the wrong syntax on going line by line
# 2) Invalid syntax or operator in the expression of while loop
# I have raised this error by using the fact that there needs to be a proper comparision sign between the expression comparables in the while statement.


# REPRESENTATIVE TEST CASE 1:
# INPUT:
# i = 0
# while i < 3 :
#   j = 1
# 	while j < 2 :
# 		x = i + j
# 		j = j + 1
# 	i = i + 1
# y = 0
#
# Time complexity calculation done after the last iteration output
#OUTPUT
# Instructions list --
# i = 0
# BLE 3 , i, 9
# j = 1
# BLE 2 , j, 7
# x = i + j
# j = j + 1
# Branch 3
# i = i + 1
# Branch 1
# y = 0

# [0, ('i', 0), 3, False, ('dummy', 3), 1, ('j', 7), 2, ('x', 5)]
# i = 0
# j = 2
# x = 1
# Garbage list - [3, False]

# [0, ('i', 5), 3, False, ('dummy', 9), 1, ('j', 7), 2, ('x', 5), True]
# i = 1
# j = 2
# x = 1
# Garbage list - [0, 3, False, True]

# [0, ('i', 5), 3, False, ('dummy', 3), 1, ('j', 7), 2, ('x', 7), True]
# i = 1
# j = 2
# x = 2
# Garbage list - [0, 3, False, True]

# [0, ('i', 7), 3, False, ('dummy', 9), 1, ('j', 7), 2, ('x', 7), True]
# i = 2
# j = 2
# x = 2
# Garbage list - [0, 3, False, 1, True]

# [0, ('i', 7), 3, False, ('dummy', 3), 1, ('j', 7), 2, ('x', 2), True]
# i = 2
# j = 2
# x = 3
# Garbage list - [0, False, 1, True]

# [0, ('i', 2), 3, False, ('dummy', 9), 1, ('j', 7), 2, ('x', 2), True]
# i = 3
# j = 2
# x = 3
# Garbage list - [0, False, 1, True]

# Final iteration
# [0, ('i', 2), 3, False, ('dummy', 9), 1, ('j', 7), 2, ('x', 2), True, ('y', 0)]
# i = 3
# j = 2
# x = 3
# y = 0
# Garbage list - [False, 1, True]

# Time complexity  in terms of number of instructions and exit value of while loop
# eg. (for while i<3 - the instructions inside the while loop runs for 3*n times)
# since there are two nested loops:
# Time Complexity -- O(i*j*n) where i is exit value of i and j is the exit value of j and n is the length of the instruction list
# Time Complexity -- O(i*j*n) and the loop is run 6n times as i=3, j=2

# REPRESENTATIVE TEST CASE 2:
# INPUT:
# a = 10
# b = 1
# while a > b :
#   a = a − 1
#   c = 1
#
# Time complexity calculation done after the last iteration output
# OUTPUT:
# Instructions list --
# a = 10
# b = 1
# BLE a , b, 5
# a = a - 1
# Branch 2
# c = 1

# [10, ('a', 6), 1, ('b', 2), False, ('dummy', 4), 9]
# a = 9
# b = 1
# Garbage list - [10, False]

# [10, ('a', 7), 1, ('b', 2), False, ('dummy', 4), 9, 8]
# a = 8
# b = 1
# Garbage list - [10, False, 9]

# [10, ('a', 8), 1, ('b', 2), False, ('dummy', 4), 9, 8, 7]
# a = 7
# b = 1
# Garbage list - [10, False, 9, 8]

# [10, ('a', 9), 1, ('b', 2), False, ('dummy', 4), 9, 8, 7, 6]
# a = 6
# b = 1
# Garbage list - [10, False, 9, 8, 7]

# [10, ('a', 10), 1, ('b', 2), False, ('dummy', 4), 9, 8, 7, 6, 5]
# a = 5
# b = 1
# Garbage list - [10, False, 9, 8, 7, 6]

# [10, ('a', 11), 1, ('b', 2), False, ('dummy', 4), 9, 8, 7, 6, 5, 4]
# a = 4
# b = 1
# Garbage list - [10, False, 9, 8, 7, 6, 5]

# [10, ('a', 12), 1, ('b', 2), False, ('dummy', 4), 9, 8, 7, 6, 5, 4, 3]
# a = 3
# b = 1
# Garbage list - [10, False, 9, 8, 7, 6, 5, 4]

# [10, ('a', 13), 1, ('b', 2), False, ('dummy', 4), 9, 8, 7, 6, 5, 4, 3, 2]
# a = 2
# b = 1
# Garbage list - [10, False, 9, 8, 7, 6, 5, 4, 3]

# [10, ('a', 2), 1, ('b', 2), False, ('dummy', 4), 9, 8, 7, 6, 5, 4, 3, 2]
# a = 1
# b = 1
# Garbage list - [10, False, 9, 8, 7, 6, 5, 4, 3, 2]

# Final iteration
# [10, ('a', 2), 1, ('b', 2), False, ('dummy', 14), 9, 8, 7, 6, 5, 4, 3, 2, True, ('c', 2)]
# a = 1
# b = 1
# c = 1
# Garbage list - [10, False, 9, 8, 7, 6, 5, 4, 3, 2, True]

# Time complexity  in terms of number of instructions and exit value of while loop
# eg. (for while i<3 - the instructions inside the while loop runs for 3*n times)
# since there is one loop:
# Time Complexity -- O(n*ai-bi) where ai is initial value of a and bi is the initial value of b and n is the length of the instruction list
# Time Complexity -- O(ai-bi*n) and the loop is run 9n times as ai=10, bi= 1


# TEST CASE - 3
# INPUT
# i = 0
# while i < 3 :
# 	j = 1
# 	while j < 2 :
# 		x = i + j
# 		j = j + 1
# 		k = 0
# 		while k < 4 :
# 			k = k + 2
# 			x = x + k
# 		z = 0
# 	i = i + 1
# y = 0
# print(i, j, x, k, z, y) gives 3 2 9 4 0 0 and our program gives the same values to these variables:
# OUTPUT
# Instructions list --
# i = 0
# BLE 3 , i, 15
# j = 1
# BLE 2 , j, 13
# x = i + j
# j = j + 1
# k = 0
# BLE 4 , k, 11
# k = k + 2
# x = x + k
# Branch 7
# z = 0
# Branch 3
# i = i + 1
# Branch 1
# y = 0

# [0, ('i', 0), 3, False, ('dummy', 3), 1, ('j', 7), 2, ('x', 2), ('k', 7), 4]
# i = 0
# j = 2
# x = 3
# k = 2
# Garbage list - [False, 1, 4]

# [0, ('i', 0), 3, False, ('dummy', 3), 1, ('j', 7), 2, ('x', 11), ('k', 10), 4, 7]
# i = 0
# j = 2
# x = 7
# k = 4
# Garbage list - [3, False, 1]

# [0, ('i', 0), 3, False, ('dummy', 12), 1, ('j', 7), 2, ('x', 11), ('k', 10), 4, 7, True, ('z', 0)]
# i = 0
# j = 2
# x = 7
# k = 4
# z = 0
# Garbage list - [3, False, 1, True]

# [0, ('i', 5), 3, False, ('dummy', 12), 1, ('j', 7), 2, ('x', 11), ('k', 10), 4, 7, True, ('z', 0)]
# i = 1
# j = 2
# x = 7
# k = 4
# z = 0
# Garbage list - [3, False, True]

# [0, ('i', 5), 3, False, ('dummy', 3), 1, ('j', 7), 2, ('x', 10), ('k', 7), 4, 7, True, ('z', 0)]
# i = 1
# j = 2
# x = 4
# k = 2
# z = 0
# Garbage list - [3, False, 7, True]

# [0, ('i', 5), 3, False, ('dummy', 3), 1, ('j', 7), 2, ('x', 14), ('k', 10), 4, 7, True, ('z', 0), 8]
# i = 1
# j = 2
# x = 8
# k = 4
# z = 0
# Garbage list - [3, False, 7, True]

# [0, ('i', 5), 3, False, ('dummy', 12), 1, ('j', 7), 2, ('x', 14), ('k', 10), 4, 7, True, ('z', 0), 8]
# i = 1
# j = 2
# x = 8
# k = 4
# z = 0
# Garbage list - [3, False, 7, True]

# [0, ('i', 7), 3, False, ('dummy', 12), 1, ('j', 7), 2, ('x', 14), ('k', 10), 4, 7, True, ('z', 0), 8]
# i = 2
# j = 2
# x = 8
# k = 4
# z = 0

# Final iteration
# [0, ('i', 2), 3, False, ('dummy', 12), 1, ('j', 7), 2, ('x', 16), ('k', 10), 4, 7, True, ('z', 0), 8, 5, 9, ('y', 0)]
# i = 3
# j = 2
# x = 9
# k = 4
# z = 0
# y = 0
# Garbage list - [False, 1, 7, True, 8, 5]