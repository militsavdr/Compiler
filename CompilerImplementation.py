# KALIOPI OIKONOMOU 5099
# MILITSA VOUDOURI 5104

import sys # anoigma arxeioy
import os

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0','1','2','3','4','5','6','7','8','9']


file=open(str(sys.argv[1]),'r')     #DIORTHWSH 

#LEKTIKES MONADES
tab_space_return=0

letter = 1                          #ABC...abc...

number=2                            # 0123...

plus_symbol=3                       # +

minus_symbol=4                      # -

multiply_symbol=5                   # *

slash_symbol=6                     # need // divide

percent_symbol=7                    # %

less_symbol=8                       # <

greater_symbol=9                    # >

equal_symbol=10                     # = (= assign == equal)

exclamation_mark_symbol=11           # ! needs =

comma_symbol=12                     # ,

colon_symbol=13                     # :

left_parenthesis_symbol=14          # (

right_parenthesis_symbol=15         # )

hashtag_symbol=16                   # ## 

left_bracket_symbol=17              # {

right_bracket_symbol=18             # } 

newLine = 19 

eof=20

unknown_symbol=21


#DESMEUMENES LEKSEIS      
keywords=['main','#def','def','#int','global','elif','if','else','while','print','return','input','int','and','or','not']


#TOKENS GIA LEKTIKES MONADES 
tab_space_return_token=30

identifier_token = 31                          #ABC...abc...123 

number_token=32                            # 0123...

plus_symbol_token=33                       # +

minus_symbol_token=34                      # -

multiply_symbol_token=35                   # *

divide_symbol_token=36                     # //

percent_symbol_token=37                    # %

less_symbol_token=38                       # <

greater_symbol_token=39                    # >

equal_symbol_token=40                      # ==

less_or_equal_symbol_token=41             # <=

greater_or_equal_symbol_token=42          # >=

not_equal_symbol_token=43                 # !=

assign_symbol_token=44                    # =

comma_symbol_token=45                     # ,

colon_symbol_token=46                     # :

left_parenthesis_symbol_token=47          # (

right_parenthesis_symbol_token=48         # )

hashtag_left_symbol_token = 49            # #{

hashtag_right_symbol_token = 50           # #}

comment_symbol_token=  51                 # ## ... ## 

eof_token = 52

newLine_token=53

unknown_symbol_token=54

hashtag_symbol_token=55

#TOKENS GIA DESMEUMENES LEKSEIS 

main_token=60

def_token=61

hashtag_def_token=62

hashtag_int_token = 63

global_token = 64

if_token = 65

elif_token = 66

else_token = 67

while_token = 68

print_token = 69

return_token = 70

input_token = 71

int_token = 72

and_token = 73

or_token  = 74

not_token  = 75


# dictionary - tokens
keyword_tokens = {
    "main": main_token,
    "#def": hashtag_def_token,
    "def": def_token,
    "#int": hashtag_int_token,
    "global": global_token,
    "if": if_token,
    "elif": elif_token,
    "else": else_token,
    "while": while_token,
    "print": print_token,
    "return": return_token,
    "input": input_token,
    "int": int_token,
    "and": and_token,
    "or": or_token,
    "not": not_token
}

# KATASTASEIS

initial_state = 0
identifier_state = 1       # letter or number or nothing ?
numbers_state = 2          # number or nothing
less_state = 3             # <= or  <
greater_state = 4          # >= or  >
is_state = 5               # ==  or  =
not_equal_state = 6        # != [always]            
hashtag_state = 7          #  #{ or #}


#ERRORS

identifier_length_error=-1      #over 30
comment_closed_error=-2         #otan anoigei na kleinei 
exclamation_mark_error=-3       #! xwris = 
unknown_symbol_error=-4         #den to anagnwrizei 
number_out_of_range_error=-5    #-32767 ews 32767



def characters(character, line) :

    if (character=="\n"):
        current_character=newLine 
    elif (character == ' ' or character == '\t'): 
        current_character = tab_space_return
    elif (character in letters):
        current_character = letter 
    elif (character in numbers):
        current_character = number
    elif (character == '+'):
        current_character = plus_symbol
    elif (character == '-'):
        current_character = minus_symbol
    elif (character == '*'):
        current_character = multiply_symbol
    elif (character == '/'):
        current_character = slash_symbol  # needs 2 - // 
    elif (character == '%'):
        current_character = percent_symbol
    elif (character == '<'):
        current_character = less_symbol
    elif (character == '>'):
        current_character = greater_symbol
    elif (character == '='):
        current_character = equal_symbol # needs 2 - ==
    elif (character == '!'):
       current_character = exclamation_mark_symbol # needs 2 - !=
    elif (character == ','):
        current_character = comma_symbol
    elif (character == ':'):
        current_character = colon_symbol
    elif (character == '('):
        current_character = left_parenthesis_symbol
    elif (character == ')'):
        current_character = right_parenthesis_symbol
    elif (character == '#'):
        current_character = hashtag_symbol 
    elif (character == '{'):
        current_character = left_bracket_symbol
    elif (character == '}'):
        current_character = right_bracket_symbol
    elif (character == ''):
        current_character = eof 
    else:
        current_character=unknown_symbol
    return current_character

def lexer():

    words = ""                                   
    current_state = initial_state    # arxikopoihsh 
    line_counter = 1 #line
    token_list=[]
    token=""
    lastTokenSeen = -1 # arxikopoihsh
    fairy_dust = ""
    fairy_granted = False
    num = ''
    content = file.read()
    i = 0
    inside_comment=False


    while i < len(content):
        current_char = content[i]
        if i + 1 < len(content):
            next_char = content[i + 1]
        else:
             next_char = None
        if i !=0:
            previous_char = content[i-1]
        else:
            previous_char = None
        previous_symbol = characters(previous_char, line_counter)
        symbol = characters(current_char, line_counter)
        next_symbol= characters(next_char,line_counter)
        


        if current_state==initial_state:

            if symbol == letter:
       
                current_state = identifier_state
                
            elif symbol == number:
                if lastTokenSeen == identifier_token:    
                    current_state = identifier_state
                else:
                    current_state = numbers_state
            else:
                fairy_dust = current_char
                fairy_granted = True

                if symbol==plus_symbol:
                    token=plus_symbol_token 
                    
                elif symbol==minus_symbol:
                    token=minus_symbol_token
                   
                elif symbol==multiply_symbol:
                    token=multiply_symbol_token
                   
                elif symbol==slash_symbol:
                    if next_symbol== slash_symbol:
                        token=divide_symbol_token
                        i+=1   
                        fairy_dust += next_char
                        
                    else:
                        token = unknown_symbol_error             
                        
                elif symbol==percent_symbol:
                    token=percent_symbol_token
                    
                elif symbol==equal_symbol:
                    current_state=is_state

                elif symbol == less_symbol:
                    current_state=less_state
                elif symbol == greater_symbol:
                    current_state=greater_state
                    
                elif symbol==exclamation_mark_symbol:          
                    current_state=not_equal_state
                elif symbol==comma_symbol:
                    token=comma_symbol_token
                elif symbol==colon_symbol:
                    token=colon_symbol_token
                elif symbol==left_parenthesis_symbol:
                    token=left_parenthesis_symbol_token
                elif symbol==right_parenthesis_symbol:
                    token=right_parenthesis_symbol_token
                elif symbol==hashtag_symbol:
                    if next_symbol == hashtag_symbol:
                        inside_comment = True
                        i += 1 
                        continue 
                    else:
                
                        token = hashtag_symbol_token
                        current_state=hashtag_state
                elif symbol==newLine:
                    token=newLine_token
                    fairy_granted = False
                    line_counter+=1                 
                elif symbol==eof:
                    token=eof_token
                elif symbol==tab_space_return:
                    token=tab_space_return_token
                    fairy_granted = False

                else:                               
                    token = unknown_symbol_error
                    
        if inside_comment:
            if current_char == '#' and next_char == '#':
                # brike to telos ##
                inside_comment = False
                i += 2  # Skip to next_char
                current_state=initial_state
                continue  
            else:
                # mesa sta comment 
                i += 1
                continue  # Skip se epomeno loop gia na agnoisei tous xarakthres mesa sta sxolia 

        if current_state==hashtag_state:
    
            if next_symbol==left_bracket_symbol: #{
                token=hashtag_left_symbol_token
                fairy_dust += next_char
                i+=1
                
            elif next_symbol==right_bracket_symbol:
                token=hashtag_right_symbol_token
                fairy_dust += next_char
                i+=1
                                       
            else:
                fairy_granted = False
                words+=current_char   # words ++ '#'
                #seperate error
            current_state=initial_state
        

        if current_state==not_equal_state:  # !
            if next_symbol==equal_symbol:
                token=not_equal_symbol_token
                fairy_dust += next_char # '!' -> '!='
                i += 1
                
            else:
                token=exclamation_mark_error
            current_state=initial_state
            
        if current_state==less_state:
            if next_symbol==equal_symbol:
                token=less_or_equal_symbol_token
                fairy_dust+=next_char     # '<' -> '<='
                i += 1
            else:
                token=less_symbol_token
            current_state=initial_state

        if current_state==greater_state:
            if next_symbol==equal_symbol:
                token=greater_or_equal_symbol_token
                fairy_dust+=next_char     # '>' -> '>='
                i += 1
            else:
                token=greater_symbol_token
            current_state=initial_state

        if current_state==is_state:
            if next_symbol==equal_symbol:
                token=equal_symbol_token
                fairy_dust+=next_char     # '=' -> '=='
                i += 1
            else:
                token=assign_symbol_token
            current_state=initial_state

        if current_state==identifier_state:
            #symbol==letter or symbol==number:
            token = identifier_token  
            words+=current_char    
            hasFoundKey = False
            for key in keywords:
                if key in words:
                    hasFoundKey = True
                    token = keyword_tokens.get(key) # gets the key of the keyword
                    fairy_dust = key 
                    fairy_granted = True

                    words = "" # reseting words
                    
            current_state = initial_state   
            if hasFoundKey== False:
                if next_symbol==letter or next_symbol==number:
                    fairy_granted = False
                if next_symbol!=letter and next_symbol!=number:
                    if len(words)<30:
                        #stamataei o identifier
                        fairy_dust = words
                        
                    else:
                        fairy_dust=words
                        token=identifier_length_error

                    fairy_granted = True
                    words = ""


        if current_state==numbers_state:    
            token=number_token
            current_state=initial_state                         
            num+=current_char
            if next_symbol == number :            
                fairy_granted = False
                
            else:
                if int(num)<32767:
                    fairy_dust = num
                
                else:
                    fairy_dust=num
                    token=number_out_of_range_error

                fairy_granted=True
                num=""

        lastTokenSeen = token
        if fairy_granted:
            if current_char =='\n':
                token_list.append((fairy_dust, token, line_counter-1))

            else:
                token_list.append((fairy_dust, token, line_counter))
            fairy_granted = False
    
        i+=1    # next loop 
    if inside_comment==True:
        return comment_closed_error
    else:
        return token_list

#----------------------------------------------- INTERMEDIATE - SYNTAX ANALYSIS -----------------------------------------------------------#

global totalQuadsList
totalQuadsList=[]

quadId=1
T_i=1
totalTempList=[]

def nextQuad():
    global quadId
    return quadId

def generateQuad(operator,operand1,operand2,target):
    global quadId
    global totalQuadsList

    #temp=[]                            
    temp=[nextQuad()]                    #resets for each quad

    temp += [operator] + [operand1] + [operand2] + [target]

    quadId+=1
    totalQuadsList+=[temp]                #[[quad1],[quad1][..]]
    return temp

def newTemp():
    global T_i
    global totalTempList

    temp=['T_']
    temp.append(str(T_i))
    tempVar="".join(temp)
    T_i+=1

    totalTempList+=[tempVar]
    return tempVar

def emptyList():

    emptyList=[]

    return emptyList

def makeList(x):    #takes only one label and puts it in a list each time

    makeList=[x]

    return makeList

def merge(listA,listB):

    #temp=[]
    temp= listA + listB 

    return temp

def backpatch(list,z):
    
    global totalQuadsList

    #[100,200] [[100,<,2,3,_],[101,>,2,3,_]]

    for i in range(len(list)):                                              #loops through the true list with ids
        for j in range(len(totalQuadsList)):                                #loops through the total Quads
            if list[i]==totalQuadsList[j][0] and totalQuadsList[j][4]=="_": #checks if the ids are the same and if target="_"
                totalQuadsList[j][4]=z
                break

    return 
#----------------------------------------------- SYMBOL TABLE CLASSES -----------------------------------------------------------#

class Entity:
    def __init__(self,name):
        self.name=name

class Scope:
    def __init__(self):
        self.offset=12  #the first 3 places are taken by the following 3 (4 bytes each)
        self.return_addr=Entity("return_addr")
        self.link=Entity("link")
        self.return_val=Entity("return_val")
        self.entities=[self.return_addr,self.link,self.return_val]

    def nextOffset(self):
        val=self.offset
        self.offset+=4
        return val
    
    def addEntity(self,entity):
        self.entities.append(entity)

    def __str__(self):
        scope_str = "\t---------------------------------------------------\n"
        scope_str += "\tENTER ENTITIES :\n"
        for entity in self.entities[3:]:
            scope_str += f"\tName of Entity: {entity.name}\n"
            if isinstance(entity, Variable):
                scope_str += f"\t  Data Type: {entity.datatype}\n"
                scope_str += f"\t  Offset: {entity.name}/{entity.offset}\n"
            elif isinstance(entity, Parameter):
                scope_str += f"\t  Data Type: {entity.datatype}\n"
                scope_str += f"\t  Offset: {entity.name}/{entity.offset}\n"
                scope_str += f"\t  Mode: {entity.name}/{entity.offset}/{entity.mode}\n"
            elif isinstance(entity, TemporaryVariable):
                scope_str += f"\t  Data Type: {entity.datatype}\n"
                scope_str += f"\t  Offset: {entity.name}/{entity.offset}\n"
            elif isinstance(entity, Function):
                scope_str += f"\t  Data Type: {entity.datatype}\n"
                if entity.startingQuad is not None:
                    scope_str += f"\t  Starting Quad:{entity.name}/{entity.startingQuad}\n"
                if entity.framelength is not None:
                    scope_str += f"\t  Frame Length: {entity.name}/{entity.startingQuad}/{entity.framelength}\n"
                if entity.formalParameters is not None:
                    scope_str += "\t  Formal Parameters:\n"
                    for formal_param in entity.formalParameters:
                        scope_str += f"\t-Name: {formal_param.name}\n\tData Type: {formal_param.datatype}\n\tMode: {formal_param.name}/{formal_param.mode}\n"
            scope_str += "\t---------------------------------------------------\n"
        scope_str += "\tOUT OF ENTITIES\n"
        return scope_str

class Variable(Entity): #subclass of Entity 
    def __init__(self, name,datatype,offset):
        super().__init__(name)  #super : arxikopoihsh koinwn xarakthristikwn 
        self.datatype=datatype
        self.offset=offset

    #def __str__(self):
    #    return (str(self.name)+ "/"+str(self.offset))

class FormalParameter(Entity):  # DEF KELLY(X,Y)
    def __init__(self,name,datatype,mode):
        super().__init__(name)  # gia logous aplothtas to theloume alla den xreiazetai 
        self.datatype=datatype
        self.mode=mode

    #def __str__(self):
    #    return str(self.name)+ "/" +str(self.offset)+ "/" +str(self.mode)


class Parameter(FormalParameter): #KELLY(2,4)
        def __init__(self, name, datatype, mode, offset):
            super().__init__(name, datatype, mode)  
            self.offset = offset

class TemporaryVariable(Variable):
    def __init__(self, name, datatype, offset):
        super().__init__(name, datatype, offset)

class Function(Entity):
    def __init__(self, name, datatype, startingQuad, formalParameters, framelength):
        super().__init__(name)
        self.datatype = datatype
        self.startingQuad = startingQuad
        self.formalParameters = formalParameters    #list of formal parameters
        self.framelength = framelength     

    def addFormalParameters(self,formalParameters):
        self.formalParameters=formalParameters

    def updateQuad(self,startingQuad):
        self.startingQuad = startingQuad

    def updateFramelength(self,framelength):
        self.framelength=framelength

    def __str__(self):
        if self.framelength != 0:   #to framelength tha simplirwthei sto telos ths metafrashs
            return str(self.name) + "/" + str(self.framelength)
        else:
            return str(self.name)

class SymbolTable:
    def __init__(self):
        self.table=[]
    
    def addScope(self,scope):
        self.table.append(scope)

    def removeScope(self):
        if self.table:
            self.table.pop()

    def getCurrentScope(self):
        if self.table:
            return self.table[-1]
        else:
            return None
    
    def search(self, name):
        global_mentioned = False
        scopeLevel = 0
        #print(len(self.table))
        for scope in reversed(self.table):
            scopeLevel += 1
            #print(len(scope.entities))
            for entity in reversed(scope.entities):
                if entity!=None:
                    if entity.name == name:
                        if isinstance (entity, Variable):
                            if entity.offset == None:
                                global_mentioned = True
                                if isinstance (entity, Variable):
                                    if entity.offset == None:
                                        global_mentioned = True
                                        continue
                                    
                        return scopeLevel, entity , global_mentioned
        return 
    
    def __str__(self):
        level=0
        str="======================== TABLE ========================\n"
        for scope in self.table:
            str+=f"LEVEL {level}\n"
            level+=1
            str+=scope.__str__()
        return str
#-------------------------------------------------------------FINAL CODE-----------------------------#

class FinalCode:
    def __init__(self,table):
        self.table=table    #takes the symbol table and generates the output file
        self.res=[]     #res=code
        self.outputFinal="final.asm"
        self.label=0
        
        fd=open(self.outputFinal,"w")
        fd.close()

        self.produce(".data")
        self.produce('newline: .asciz "\\n"')   #for new line
        self.produce('.text')   #arxh enothtas kwdika
        self.produce('Lstart:')  
        self.produceL()
        self.produce('j Lmain') #entoli gia jump sthn main
        self.parameters = []    #apothikeusi parametrwn sunarthshs
        self.processed_functions=set()

    def produce(self, command):     #prosthiki grammwn ston teliko kwdika
        self.res.append(command)
        with open(self.outputFinal, 'a') as f:
           if command=="Lmain:":
               f.write(f'{command}\n')
           else:
               f.write(f'\t{command}\n')
        #print("\t", command)

    def produceL(self):
        self.res.append(f'L{self.label}:')
        with open(self.outputFinal, 'a') as f:
            f.write(f'L{self.label}:\n')
        #print(f'L{self.labelCounter}:')
        self.label+= 1

    def gnlvcode(self,v):   #anaktisi dieuthinsis metablitis
        result = self.table.search(v)
        #EDW HTAN SCOPE==1
        if result is None:
            print(f"Entity {v} not found")
            return
        scopeNum, entity ,global_mentioned = result
        if scopeNum==1:    #ama h metablhth einai topiki denxreiazetai paragwgh kwdika
            return
        for i in range(scopeNum-1):    #apo trexon epipedo ews epipedo metablhths
            if i==0:
                self.produce("lw t0,-4(sp)")        #ama einai sto prwto tote kanei apeutheias apo korufh stoibas
            else:
                self.produce("lw t0,-4(t0)")    #alliws fortwnei thn dieuthunsy tou prohgoumenou
        if isinstance(entity,Function):
            return       
        self.produce(f'addi t0, t0, -{entity.offset}')  #prosthiki offset na ftasei sthn metablhth

    def loadvr(self,v,reg):   #fortwsh timhs metablhths , h arithmou se enan reg
        result = self.table.search(v)
        
        if v.isdigit() or (v.startswith('-') and v[1:].isdigit()):
            if v.startswith('-'):
                v = v[1:]
                self.produce(f"li {reg},-{v}")
                return
            self.produce(f"li {reg},{v}")
            return
        if result is None:
            print(f"Entity {v} not found")
            return
        scope, entity , global_mentioned = result
        if scope==1:    #local
            self.produce(f'lw {reg}, -{entity.offset}(sp)')     #fortwnei thn timh apo thn stoiba mesw tou offset ths metablhths
        elif global_mentioned == True:
            self.produce(f"lw {reg},-{entity.offset}(gp)")
        elif scope!=1:
            self.gnlvcode(v)    #an den einai local anakta thn dieuthinsi ths v kai thn apothikeuei t0
            self.produce(f"lw {reg},(t0)")

    def storevr(self,reg,v):    #kwdika gia apothikeusi timhs kataxwriti se metabliti
        result = self.table.search(v)
        if result is None:
            print(f"Entity {v} not found")
            return
        scope, entity , global_mentioned = result

        if scope==1:    #local
            self.produce(f'sw {reg}, -{entity.offset}(sp)')

        elif global_mentioned == True:
            self.produce(f"sw {reg},-{entity.offset}(gp)")
            self.produce(entity.name)
            self.produce(f'sw {reg}, -{entity.offset}(sp)')
        
        elif scope !=1:
           
            self.produce(entity.name)
            self.produce(f'sw {reg}, -{entity.offset}(sp)')
            self.gnlvcode(v)    #fortwnei dieuthynsh sto t0
            self.produce(f'sw {reg}, (t0)')

    def generateFinal(self, quadruples , name_of_function):
        print("=================NEW==============")
        index = 0
        start_fucntion = False
        for quad in quadruples:

            if quad[1] == 'begin_block' and  quad[2] == name_of_function:
                name = quad[2]
                if name == "main":
    
                    self.produce("Lmain:")
                    self.produceL()
                    self.produce(f"addi,sp,sp,")
                    self.produce("mv gp,sp")
                    start_fucntion = True
                else:
                    self.produceL()
                    self.produce("sw ra, 0(sp)")  #store return address
                    start_fucntion = True
                continue
            if quad[1] == 'end_block' and  quad[2] == name_of_function:
                self.produceL()
                self.produce("lw ra, 0(sp)")  
                self.produce("jr ra")  
                start_fucntion = False

                
            if start_fucntion == True: #100: < 2 3 10
                operator = quad[1]
                nameOfentity = quad[2]
                nameOfother = quad[3]

                if operator == 'par':
                    self.parameters.append(nameOfentity)
                    index += 1
                    continue
                if operator == 'call':
                    result = self.table.search(nameOfentity)
                    if result != None:
                        scopeNum, entity , global_mentioned = result
                        startingQuad = entity.startingQuad  #gia na kanoume meta j 
                        framelength = entity.framelength  #poso tha xreiastei na aukshsw deikth stoivas
                        formalParameters = entity.formalParameters  #an oi parametroi kata thn klhsh tairiazoun me ton orismo 

                    if len(formalParameters) != len(self.parameters) - 1:
                        print("Invalid number of parameters")

                    is_first = True
                    for parameter in self.parameters:  
                        self.produceL()
                        if is_first:  #theloume 1h parametro
                            #sp koryfh stoivas 
                            #fp gia na prospelasoume parametrous
                            self.produce(f"addi fp, sp, {framelength}")  #bazoume fp sthn thesh 1hs parametrou sthn stoiba
                            is_first = False

                        if parameter == "CV":
                            self.loadvr(nameOfentity, "t0")  #fortwse thn timh ston t0
                            pos = 12
                            for p in self.parameters:
                                if p == parameter:
                                    break  #ama brei idia parametro stamataei
                                pos += 4  #apostash apo arxh plaisiou ews to pos pou apothikeuthke h par
                            self.produce(f'sw t0, -{pos}(fp)')
                        elif parameter == "RET":
                            result = self.table.search(nameOfentity)
                            if result is None:
                                print(f"Entity {nameOfentity} not found")
                            scopeNum, entity,global_mentioned = result
                            if scopeNum != 1:
                                print("Non local")
                            if isinstance(entity, Function):
                                return
                            self.produce(f'addi t0, sp, -{entity.offset}')  # store return value address to t0
                            self.produce('sw t0, -8(fp)')  # Store t0 to the reserved address in the stack

                    # Access link
                    self.produceL()
                    if nameOfentity != "main":
                        result = self.table.search(nameOfentity)
                        if result != None:
                            scopeNum, entity ,global_mentioned = result
                            scope = len(self.table.table) - scopeNum + 1  #upologizei scope trexousas synarthshs  (+1 gia to katholiko scope)
                        if scope == self.table.getCurrentScope():  #ama einai adelfia exoun idio goneo ara idio scope
                            self.produce('lw t0, -4(sp)')  #metafora sp sthn arxh tou frame ths sunarthshs
                            self.produce('sw t0, -4(fp)')
                            
                        elif scope != self.table.getCurrentScope():
                            self.produce("sw sp, -4(fp)")
                        else:
                            sys.exit("Not accessible")

                    self.produce(f'addi sp, sp, {framelength}')  #auksanei sp kata megethos frame gia na dhmioyrghsoume xwro gia local var
                    self.produce(f'jal L{startingQuad}')

                    if nameOfentity != "main":
                        self.parameters = []
                    index += 1
                    continue  # next loop step

                self.produceL()
                if operator == "=":
                    self.loadvr(nameOfentity, "t1")
                    self.storevr("t1", quad[4])
                elif operator == "+":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce("add t1, t1, t2")
                    self.storevr("t1", quad[4])
                elif operator == "-":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce("sub t1, t1, t2")
                    self.storevr("t1", quad[4])
                elif operator == "*":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce("mul t1, t1, t2")
                    self.storevr("t1", quad[4])
                elif operator == "//":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce("div t1, t1, t2")
                    self.storevr("t1", quad[4])
                elif operator == "%":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce("div t3, t1, t2")
                    self.produce("mul t3, t3, t2")
                    self.produce("sub t1, t1, t3")
                    self.storevr("t1", quad[4])
                elif operator == "==":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce(f"beq t1, t2, L{quad[4]}")
                elif operator == "!=":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce(f"bne t1, t2, L{quad[4]}")
                elif operator == ">":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce(f"bgt t1, t2, L{quad[4]}")
                elif operator == "<":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce(f"blt t1, t2, L{quad[4]}")
                elif operator == ">=":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce(f"bge t1, t2, L{quad[4]}")
                elif operator == "<=":
                    self.loadvr(nameOfentity, "t1")
                    self.loadvr(nameOfother, "t2")
                    self.produce(f"ble t1, t2, L{quad[4]}")
                elif operator == "jump":
                    self.produce(f"j L{quad[4]}")
                elif operator == "inp":
                    self.produce("li a7, 5")
                    self.produce("ecall")
                    self.storevr("a0", nameOfentity)
                elif operator == "out":
                    self.loadvr(nameOfentity, "a0")
                    self.produce("li a7, 1")
                    self.produce("la a0, newline")
                    self.produce("li a7, 4")
                    self.produce("ecall")
                elif operator == "ret":
                    self.loadvr(nameOfentity, "t1")
                    self.produce("sw t1, (t0)")
                    self.produce("lw ra, (sp)")  # Load return address
                    self.produce("jr ra")  
                elif operator == "halt":
                    self.produce('li a0, 0')
                    self.produce('li a7, 93')
                    self.produce('ecall')
        return self.res

#----------------------------------------------- SYNTAX ANALYSIS -----------------------------------------------------------#
finals= []
def syn():
    global res 
    global line 
    global round
    global table
    table=SymbolTable()
    
    global scope
    global code
    #global call_name
    res = lexer()
    round=0
    func_names=[]

    if res==comment_closed_error:
        print("LexerError -2: Comment Closed Error ")  
        exit(-1)

    
    def checkLexerError(errorChar,errorTok,errorLine):
        if errorTok==-1:
            print("LexerError -1: ",errorChar ," Identifier Length Over 30 in line: ",errorLine)
            exit(-1)

        if errorTok==-3:
            print("LexerError -3: ",errorChar ," Exclamation Mark Error in line: ",errorLine)  
            exit(-1)

        if errorTok==-4:
            print("LexerError -4: Unknown Symbol Error : ",errorLine)  
            exit(-1)

        if errorTok==-5:
            print("LexerError -5:",errorChar," Number Out Of Range Error : ",errorLine)  
            exit(-1)


    def update(round):

        if round==len(res)-1:
            return round
        
        else:
            return round+1
        
    
    def startRule():
        with open("symbolTable.sym","w") as f:

            def_main_part(f)     #o upoloipos kwdikas ews main
            call_main_part(f)    #def main 
        #print(table.__str__())


    def def_main_part(f):
        global round
        global line
        global scope
        global table
        outputFinal="final.asm"

        variables=[]
        newScope=Scope()    #before declarations
        scope=newScope
        table.addScope(newScope)
        checkLexerError(res[round][0],res[round][1],res[round][2])
        variables=declarations() #store them in a list 
        checkLexerError(res[round][0],res[round][1],res[round][2])
        #print(variables)
        for i in variables: #for each variable create an entity
            newEntity=Variable(i,"Integer",newScope.nextOffset())
            newScope.addEntity(newEntity)
    
        while res[round][1]==def_token:
            checkLexerError(res[round][0],res[round][1],res[round][2])
            scope=newScope
            def_function(f)
            f.write(table.__str__())
            table.removeScope()
            f.write(table.__str__())
        scope=newScope

    def def_function(f):
        global round
        global line
        global scope
        global table
        global code

        parameters=[]
        variables=[]
        variables_global=[]
        if res[round][1]==def_token:
            round=update(round)
            line=res[round][2]

            checkLexerError(res[round][0],res[round][1],res[round][2])
            if res[round][1]==identifier_token:
                func_entity=Function(res[round][0],"Integer",None,None,None)
                                                     ## consider the error -1
                
                scope.addEntity(func_entity)
                #print(table.__str__())

                newScope=Scope()
                scope=newScope
                table.addScope(newScope)

                func_names.append(res[round][0])
                round=update(round)
                line=res[round][2]
                

                if res[round][1]==left_parenthesis_symbol_token:
                    round=update(round)
                    line=res[round][2]

                    parameters=id_list()
                    entities=[]

                    for i in parameters:
                        entity=FormalParameter(i,"Integer","CV")
                        entities.append(entity)

                        entity=Parameter(i,"Integer","CV",scope.nextOffset())
                        scope.addEntity(entity)
                    
                    func_entity.addFormalParameters(entities)

                    if res[round][1]==right_parenthesis_symbol_token:
                        round=update(round)
                        line=res[round][2]

                        if res[round][1]==colon_symbol_token:
                            round=update(round)
                            line=res[round][2]

                            if res[round][1]==hashtag_left_symbol_token:
                                round=update(round)
                                line=res[round][2]

                                checkLexerError(res[round][0],res[round][1],res[round][2])

                                variables=declarations()
                                for i in variables:
                                    entity=Variable(i,"Integer",scope.nextOffset())
                                    scope.addEntity(entity)
                                    
                                name_of_function = func_names[-1]
                                
                                while(res[round][1]==def_token):
                                    
                                    def_function(f)
                                    f.write(table.__str__())
                                    table.removeScope()
                                    f.write(table.__str__())
                                
                                variables_global=declarations_global()
                                for i in variables_global:
                                    entity=Variable(i,"Integer",None)
                                    scope.addEntity(entity)
                                
                                
                                firstQuad=int(nextQuad())+1
                                checkLexerError(res[round][0],res[round][1],res[round][2])
                                func_entity.updateQuad(firstQuad)
                                generateQuad('begin_block',name_of_function,'_','_')
                                
                                checkLexerError(res[round][0],res[round][1],res[round][2])
                                scope=newScope

                                statements()
                            
                                if res[round][1]==hashtag_right_symbol_token:

                                    framelength=len(scope.entities)*4
                                    func_entity.updateFramelength(framelength)
                                    generateQuad('end_block',name_of_function,'_','_')

                                    code=FinalCode(table)
                                    finals = code.generateFinal(totalQuadsList , name_of_function)
                            
                                    for result in finals :

                                        print(result)

                                    round=update(round)
                                    line=res[round][2]

                                else:
                                    checkLexerError(res[round][0],res[round][1],res[round][2])

                                    print("SyntaxError: '#}' was not found after function's declaration in line: ",line)
                                    exit(-1)
                                        

                            else:
                                checkLexerError(res[round][0],res[round][1],res[round][2])

                                print("SyntaxError: '#{' was not found before function's declaration in line: ",line)
                                exit(-1)


                        else:
                            checkLexerError(res[round][0],res[round][1],res[round][2])

                            print("SyntaxError: ':' was not found after the definiton of function in line: ",line)
                            exit(-1)

                    else:
                        checkLexerError(res[round][0],res[round][1],res[round][2])

                        print("SyntaxError: ')' was not found after list of parameters in line: ",line)
                        exit(-1)


                    
                else:
                    checkLexerError(res[round][0],res[round][1],res[round][2])

                    print("SyntaxError: '(' was not found after 'identifier' statement in line: ",line)
                    exit(-1)
                    
            else:
                checkLexerError(res[round][0],res[round][1],res[round][2])

                print("SyntaxError: 'identifier' was not found after 'def' statement in line: ",line)
                exit(-1)
        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: 'def' was not found: ")
            exit(-1)

    def declarations_global():
        global round
        global line
        checkLexerError(res[round][0],res[round][1],res[round][2])

        variables=[]
        while(res[round][1]==global_token):
            restOfVar=declaration_line_global() 
            variables=variables+restOfVar
        return variables

    def declarations():
        global round
        global line
        checkLexerError(res[round][0],res[round][1],res[round][2])

        variables=[]
        while(res[round][1]==hashtag_int_token):
            restOfVar=declaration_line()
            variables=variables+restOfVar
        return variables
    
    def declaration_line_global():
        global round
        global line

        variable=[]
        if res[round][1]==global_token:
            round=update(round)
            line=res[round][2]
            checkLexerError(res[round][0],res[round][1],res[round][2])

            variable=id_list()

        return variable

    def declaration_line():
        global round
        global line

        variable=[]
        if res[round][1]==hashtag_int_token:
            round=update(round)
            line=res[round][2]
            checkLexerError(res[round][0],res[round][1],res[round][2])

            variable=id_list()
        return variable
    
    def id_list():
        global round
        global line

        variables=[]
        checkLexerError(res[round][0],res[round][1],res[round][2])

        if res[round][1]==identifier_token:
            variables.append(res[round][0])
            round=update(round)
            line=res[round][2]

            while(res[round][1]==comma_symbol_token):
                round=update(round)
                line=res[round][2]

                if res[round][1]==identifier_token:
                    variables.append(res[round][0])

                    round=update(round)
                    line=res[round][2]

                else:
                    checkLexerError(res[round][0],res[round][1],res[round][2])

                    print("SyntaxError: 'identifier' was not found after ',' statement in line: ",line)
                    exit(-1)
            checkLexerError(res[round][0],res[round][1],res[round][2])
        return variables

    def statement():
        global round
        global line  

        checkLexerError(res[round][0],res[round][1],res[round][2])

        if res[round][1]==identifier_token or res[round][1]==print_token or res[round][1]==return_token:
            simple_statement()
        elif res[round][1]==if_token or res[round][1]==while_token:
            structured_statement()
        else:
            print("SyntaxError: Statement was not found in line: ",line)
            exit(-1)
            

    def statements():
        global round
        global line

        
        statement()
        while(res[round][1]==identifier_token or res[round][1]==print_token or res[round][1]==return_token or res[round][1]==if_token or res[round][1]==while_token):
            statement()
    
    def simple_statement():
        global round
        global line 

        if res[round][1]==identifier_token:
            assignment_stat()
        elif res[round][1]==print_token:
            print_stat()
        elif res[round][1]==return_token: #else ?
            return_stat()

        
    def structured_statement():
        global round
        global line 

        if res[round][1]== if_token:
            if_stat()
        elif res[round][1]==while_token:
            while_stat()

    def assignment_stat():
        global round
        global line 

        eliflist=emptyList()
        checkLexerError(res[round][0],res[round][1],res[round][2])

        if res[round][1]==identifier_token:
            var_name=res[round][0]  # character 
            #print(var_name)
            round=update(round)
            line=res[round][2]

            if res[round][1]==assign_symbol_token:
                round=update(round)
                line=res[round][2]

                if res[round][1]==int_token:
                    round=update(round)
                    line=res[round][2]

                    if res[round][1]==left_parenthesis_symbol_token:
                        round=update(round)
                        line=res[round][2]

                        if res[round][1]==input_token:
                            round=update(round)
                            line=res[round][2]

                            if res[round][1]==left_parenthesis_symbol_token:
                                round=update(round)
                                line=res[round][2]
                                
                                #int(input(w))
                                w=newTemp()
                                generateQuad("inp",w,"_",var_name)

                                if res[round][1]==right_parenthesis_symbol_token:
                                    round=update(round)
                                    line=res[round][2]

                                    if res[round][1]==right_parenthesis_symbol_token:
                                        round=update(round)
                                        line=res[round][2]

                                        checkLexerError(res[round][0],res[round][1],res[round][2])

                                    else:
                                        checkLexerError(res[round][0],res[round][1],res[round][2])

                                        print("SyntaxError: ')' was not found in line: ",line)
                                        exit(-1)

                                else:
                                    checkLexerError(res[round][0],res[round][1],res[round][2])

                                    print("SyntaxError: ')' was not found in line: ",line)
                                    exit(-1)

                            else:
                                checkLexerError(res[round][0],res[round][1],res[round][2])

                                print("SyntaxError: '(' was not found in line: ",line)
                                exit(-1)
                        else:
                            checkLexerError(res[round][0],res[round][1],res[round][2])

                            print("SyntaxError: 'input' was not found in line: ",line)
                            exit(-1)
                    else:
                        checkLexerError(res[round][0],res[round][1],res[round][2])

                        print("SyntaxError: '(' was not found in line: ",line)
                        exit(-1)
                else:
                    checkLexerError(res[round][0],res[round][1],res[round][2])
                    
                    Eplace=expression()
                    generateQuad('=',Eplace,'_',var_name)
                    #if not int(input()) then expression 
            else:
                checkLexerError(res[round][0],res[round][1],res[round][2])

                print("SyntaxError: '=' was not found in line: ",line)
                exit(-1)


        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: 'identifier' was not found in line: ",line)
            exit(-1)

    def print_stat():
        global round
        global line 
        
        if res[round][1]==print_token:
            round=update(round)
            line=res[round][2]
            
            if res[round][1]==left_parenthesis_symbol_token:
                
                round=update(round)
                line=res[round][2]

                checkLexerError(res[round][0],res[round][1],res[round][2])
                Eplace=expression()


                generateQuad('out',Eplace,'_','_')

                if res[round][1]==right_parenthesis_symbol_token:
                    round=update(round)
                    line=res[round][2]
    
                else:
                    checkLexerError(res[round][0],res[round][1],res[round][2])

                    print("SyntaxError: ')' was not found after 'print' in line: ",line)
                    exit(-1)

            else:
                checkLexerError(res[round][0],res[round][1],res[round][2])

                print("SyntaxError: '(' was not found after 'print' in line: ",line)
                exit(-1)

        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: 'print' was not found in line: ",line)
            exit(-1)
        

    def return_stat():
        global round
        global line

        if res[round][1]==return_token:
            round=update(round)
            line=res[round][2]

            checkLexerError(res[round][0],res[round][1],res[round][2])


            Eplace=expression()
            generateQuad('ret',Eplace,'_','_')

        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: 'return' was not found in line: ",line)
            exit(-1)

    def if_stat():
        global round
        global line

        iflist=emptyList()  # error prin 
        eliflist=emptyList()
        
        if res[round][1]==if_token:
            round=update(round)
            line=res[round][2]

            checkLexerError(res[round][0],res[round][1],res[round][2])

            cond1=condition() # p1 
            backpatch(cond1[0],nextQuad()) #TRUE 


            if res[round][1]==colon_symbol_token:
                round=update(round)
                line=res[round][2]
            
                if res[round][1]==hashtag_left_symbol_token:
                    round=update(round)
                    line=res[round][2]
                    
                    checkLexerError(res[round][0],res[round][1],res[round][2])

                    statements() 
                    # P2
                    iflist=makeList(nextQuad())
                    generateQuad('jump','_','_','_')
                    backpatch(cond1[1],nextQuad()) #FALSE 
                    
                    if res[round][1]==hashtag_right_symbol_token:
                        round=update(round)
                        line=res[round][2]

                    else:
                        checkLexerError(res[round][0],res[round][1],res[round][2])

                        print("SyntaxError: '#}' was not found in line: ",line)
                        exit(-1)
                else:
                    checkLexerError(res[round][0],res[round][1],res[round][2])

                    statement()
                    # P2                           # NOT S U R E
                    iflist=makeList(nextQuad())
                    generateQuad('jump','_','_','_')
                    backpatch(cond1[1],nextQuad()) #FALSE 

                while (res[round][1]==elif_token):                                  ##### while or if ??
                    round=update(round)
                    line=res[round][2]

                    checkLexerError(res[round][0],res[round][1],res[round][2])

                    cond2=condition() # P1
                    backpatch(cond2[0],nextQuad()) #TRUE 

        
                    if res[round][1]==colon_symbol_token:
                        round=update(round)
                        line=res[round][2]

                        if res[round][1]==hashtag_left_symbol_token:
                            round=update(round)
                            line=res[round][2]
                            
                            checkLexerError(res[round][0],res[round][1],res[round][2])

                            statements()
                            # P2 
                            eliflist=makeList(nextQuad())
                            generateQuad('jump','_','_','_')
                            backpatch(cond2[1],nextQuad())
                            
                            if res[round][1]==hashtag_right_symbol_token:
                                round=update(round)
                                line=res[round][2]

                            else:
                                checkLexerError(res[round][0],res[round][1],res[round][2])

                                print("SyntaxError: '#}' was not found in line: ",line)
                                exit(-1)                 
                        else:
                            checkLexerError(res[round][0],res[round][1],res[round][2])

                            statement()
                            # P2
                            eliflist=makeList(nextQuad())
                            generateQuad('jump','_','_','_')
                            backpatch(cond2[1],nextQuad())
                    else:
                        checkLexerError(res[round][0],res[round][1],res[round][2])

                        print("SyntaxError: ':' was not found after 'elif' in line: ",line)
                        exit(-1)

                if res[round][1]==else_token:                                               
                    round=update(round)
                    line=res[round][2]

                    if res[round][1]==colon_symbol_token:
                        round=update(round)
                        line=res[round][2]

                        if res[round][1]==hashtag_left_symbol_token:
                            round=update(round)
                            line=res[round][2]

                            checkLexerError(res[round][0],res[round][1],res[round][2])
                            
                            statements()
                            
                            if res[round][1]==hashtag_right_symbol_token:
                                round=update(round)
                                line=res[round][2]


                            else:
                                checkLexerError(res[round][0],res[round][1],res[round][2])

                                print("SyntaxError: '#}' was not found in line: ",line)
                                exit(-1)

                        else:
                            checkLexerError(res[round][0],res[round][1],res[round][2])

                            statement()

                    else:
                        checkLexerError(res[round][0],res[round][1],res[round][2])

                        print("SyntaxError: ':' was not found after 'else' in line: ",line)
                        exit(-1)
                # den einai upoxrewtiko to else->no error
                # P3
                iflist=merge(iflist,eliflist)   #synolika apotelesmata gia na mas steilei sto else

                backpatch(iflist,nextQuad())    
            else:
                checkLexerError(res[round][0],res[round][1],res[round][2])

                print("SyntaxError: ':' was not found after 'if' in line: ",line)
                exit(-1)

        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: 'if' was not found in line: ",line)
            exit(-1)
    
    def while_stat():
        global round
        global line

        if res[round][1]==while_token:
            round=update(round)
            line=res[round][2]
            checkLexerError(res[round][0],res[round][1],res[round][2])

            # P1
            firstquad=nextQuad()    #gia na kanei jump pisw 
            
            cond=condition()

            backpatch(cond[0],nextQuad())   # TRUE -> STATEMENTS

            if res[round][1]==colon_symbol_token:
                round=update(round)
                line=res[round][2]

                if res[round][1]==hashtag_left_symbol_token:
                    round=update(round)
                    line=res[round][2]
                    checkLexerError(res[round][0],res[round][1],res[round][2])
                    
                    statements()
                    # P3
                    
                    generateQuad("jump","_","_",firstquad)  #TRUE -> LOOP
                    backpatch(cond[1],nextQuad())   #FALSE -> EKTOS WHILE
                    
                    if res[round][1]==hashtag_right_symbol_token:
                        round=update(round)
                        line=res[round][2]

                    else:
                        checkLexerError(res[round][0],res[round][1],res[round][2])

                        print("SyntaxError: '#}' was not found in line: ",line)
                        exit(-1)

                else:
                    checkLexerError(res[round][0],res[round][1],res[round][2])

                    statement()

            else:
                checkLexerError(res[round][0],res[round][1],res[round][2])

                print("SyntaxError: ':' was not found after 'else' in line: ",line)
                exit(-1)

        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: 'while' was not found in line: ",line)
            exit(-1)

    def expression():
        global round
        global line 
        global scope
        sign = None

        sign = optional_sign()
        #------------PROTERAIOTHTA------------#
        #print(sign)
        T1place=term()
        #print(T1place)
        if sign != None:
            T1place = sign + T1place
            #print(T1place)

        while(res[round][1]==plus_symbol_token or res[round][1]==minus_symbol_token):
            operator = None
            operator=ADD_OP()   # ADD or MINUS operator
            T2place=term()

            w=newTemp()
            newTempvar=TemporaryVariable(w,"Integer",scope.nextOffset())
            scope.addEntity(newTempvar)
            generateQuad(operator,T1place,T2place,w)
            T1place=w

        # P2
        Eplace=T1place
        #print(Eplace)
        return Eplace 
    
    def term():
        global round
        global line 
        global scope

        F1place=factor()

        while(res[round][1]==multiply_symbol_token or res[round][1]==divide_symbol_token or res[round][1]==percent_symbol_token):
            operator=MUL_OP()   # MUL or DIV or PERCENT
            F2place=factor()

            w=newTemp()
            newTempvar=TemporaryVariable(w,"Integer",scope.nextOffset())
            scope.addEntity(newTempvar)
            generateQuad(operator,F1place,F2place,w)
            F1place=w

        Tplace=F1place
        return Tplace


    def factor():
        global round
        global line 
        #global call_name

        checkLexerError(res[round][0],res[round][1],res[round][2])

        if res[round][1]==number_token:
            Fplace=res[round][0]
            round=update(round)
            line=res[round][2]


        elif res[round][1]==left_parenthesis_symbol_token:
            round=update(round)
            line=res[round][2]
            
            checkLexerError(res[round][0],res[round][1],res[round][2])

            Eplace=expression()
            Fplace=Eplace

            if res[round][1]==right_parenthesis_symbol_token:
                round=update(round)
                line=res[round][2]
            else:
                checkLexerError(res[round][0],res[round][1],res[round][2])

                print("SyntaxError: ')' was not found in line: ",line)
                exit(-1)

        elif res[round][1]==identifier_token:
            Fplace=res[round][0] #new 
            
            round=update(round)
            w=idtail() # 1: name or 2:temp var 
            if w!=Fplace:   #if w is name then return Fplace else return Temp var
                return w 
            line=res[round][2]
            checkLexerError(res[round][0],res[round][1],res[round][2])
        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: Expression was not found in line: ",line)           #expression ??
            exit(-1)

        return Fplace
    
    def idtail():
        global round
        global line
        global scope
        #global call_name

        name=res[round-1][0]
        parameters=[]
        if res[round][1]==left_parenthesis_symbol_token:
            #print("inside left parenthesis:")
            round=update(round)
            #name=res[round+1][0]
            line=res[round][2]
            #print(name)
            checkLexerError(res[round][0],res[round][1],res[round][2])
            #print("*")
            actual_par_list()
            w=newTemp()
            newTempVar=TemporaryVariable(w,"Integer",scope.nextOffset())
            scope.addEntity(newTempVar)
            generateQuad('par',w,'RET','_')
            generateQuad('call',name,'_','_')   # klisi sunarthshs
            #print("before right parenthesis")
            if res[round][1]==right_parenthesis_symbol_token:
                round=update(round)
                line=res[round][2]
                return w   

            else:
                checkLexerError(res[round][0],res[round][1],res[round][2])

                print("SyntaxError: ')' was not found in line: ",line)          # DEN EINAI UPOXREWTIKO ) ????
                exit(-1)
        else:
            
            return name

    def actual_par_list():
        global round
        global line 
        global scope

        if res[round][1]==number_token or res[round][1]==left_parenthesis_symbol_token or res[round][1]==identifier_token:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            expr=expression()
            generateQuad('par',expr,'CV','_')

            
            while(res[round][1]==comma_symbol_token):
                round=update(round)
                line=res[round][2]
                checkLexerError(res[round][0],res[round][1],res[round][2])

                expr=expression()
                generateQuad('par',expr,'CV','_')
        return 

    
    def optional_sign():
        global round
        global line

        if res[round][1]==plus_symbol_token or res[round][1]==minus_symbol_token:
            return ADD_OP()

        return

    def ADD_OP():
        global round
        global line


        if res[round][1]==plus_symbol_token:
            operator=res[round][0]  #isws ektos
            round=update(round)
            line=res[round][2]
        
        elif res[round][1]==minus_symbol_token:
            operator=res[round][0]
            round=update(round)
            line=res[round][2]
        checkLexerError(res[round][0],res[round][1],res[round][2])
        return operator
        

    def MUL_OP():
        global round
        global line

        if res[round][1]==multiply_symbol_token:
            operator=res[round][0]

            round=update(round)
            line=res[round][2]
        
        elif res[round][1]==divide_symbol_token:
            operator=res[round][0]

            round=update(round)
            line=res[round][2]

        elif res[round][1]==percent_symbol_token:
            operator=res[round][0]

            round=update(round)
            line=res[round][2]
        checkLexerError(res[round][0],res[round][1],res[round][2])
        
        return operator

    def condition():
        global round
        global line

        checkLexerError(res[round][0],res[round][1],res[round][2])

        condTrue=[]
        condFalse=[]

        BT1=bool_term()
        
        condTrue=BT1[0]
        condFalse=BT1[1]

        while(res[round][1]==or_token):                    ## teleutaio se proteraiothta 
            round=update(round)
            line=res[round][2]
            checkLexerError(res[round][0],res[round][1],res[round][2])

            backpatch(condFalse,nextQuad())
            BT2 = bool_term()

            condTrue = merge(condTrue,BT2[0])
            condFalse= BT2[1] 
        
        return condTrue , condFalse


    def bool_term():
        global round
        global line 

        btTrue=[]
        btFalse=[]

        BF1=bool_factor()
        btTrue=BF1[0]
        btFalse=BF1[1]

        while(res[round][1]==and_token):
            round=update(round)
            line=res[round][2]
            checkLexerError(res[round][0],res[round][1],res[round][2])

            backpatch(btTrue,nextQuad())
            BF2=bool_factor()
            
            btFalse=merge(btFalse,BF2[1])
            btTrue=BF2[0]

        return btTrue , btFalse


    def bool_factor():
        global round
        global line

        bfTrue=[]
        bfFalse=[]
        #print("HERE BOOL FACTOR",res[round][0])

        if res[round][1]==not_token:
            round=update(round)
            line=res[round][2]
            checkLexerError(res[round][0],res[round][1],res[round][2])

            cond=condition()
            bfTrue=cond[1]  #not-> antistrefei gia auto cond[1] kai oxi cond[0]
            bfFalse=cond[0]

        ## elegxos gia sketo condition
        else:

            E1place=expression()
            relop=REL_OP()            
            E2place=expression()

            bfTrue=makeList(nextQuad())
            generateQuad(relop,E1place,E2place,'_')
            bfFalse=makeList(nextQuad())
            generateQuad('jump','_','_','_')
        
        return bfTrue,bfFalse

        #bfFalse=[100,101,102]
    
    def REL_OP():
        global round
        global line
        
        #print(relop)
        if res[round][1]==equal_symbol_token:
            relop=res[round][0]
            round=update(round)
            line=res[round][2]
        
        elif res[round][1]==less_symbol_token:
            relop=res[round][0]
            round=update(round)
            line=res[round][2]

        elif res[round][1]==less_or_equal_symbol_token:
            relop=res[round][0]
            round=update(round)
            line=res[round][2]

        elif res[round][1]==not_equal_symbol_token:
            relop=res[round][0]
            round=update(round)
            line=res[round][2]

        elif res[round][1]==greater_symbol_token:
            relop=res[round][0]
            round=update(round)
            line=res[round][2]

        elif res[round][1]==greater_or_equal_symbol_token:
            relop=res[round][0]
            round=update(round)
            line=res[round][2]
        
        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: Operator was not found in line: ",line)
            exit(-1)
            
        return relop


    def call_main_part(f):
        global round
        global line
        checkLexerError(res[round][0],res[round][1],res[round][2])
        main_function_call(f)          # declarations edw or both ??
        

    def main_function_call(f):
        global round
        global line
        global scope
        global table
        global code

        variables=[]
        variables_global=[]
        if res[round][1]==hashtag_def_token:
            round=update(round)
            line=res[round][2]

            if res[round][1]==main_token:
                round=update(round)
                line=res[round][2]

                checkLexerError(res[round][0],res[round][1],res[round][2])
                variables=declarations()   
                table.addScope(scope)
                checkLexerError(res[round][0],res[round][1],res[round][2])
                variables_global=declarations_global()
                for i in variables:
                    entity=Variable(i,"Integer",scope.nextOffset())
                    scope.addEntity(entity)
                
                for i in variables_global:
                    entity=Variable(i,"Integer",None)
                    scope.addEntity(entity)
                
                generateQuad('begin_block','main','_','_')
                table.removeScope()
                f.write(table.__str__())

                checkLexerError(res[round][0],res[round][1],res[round][2])

                statements()

                checkLexerError(res[round][0],res[round][1],res[round][2])

                generateQuad('halt','_','_','_')
                generateQuad('end_block','main','_','_')
                
                code.generateFinal(totalQuadsList,'main')
            else:
                checkLexerError(res[round][0],res[round][1],res[round][2])

                print("SyntaxError: 'main' was not found after '#def' statement in line: ",line)
                exit(-1)
        else:
            checkLexerError(res[round][0],res[round][1],res[round][2])

            print("SyntaxError: '#def' was not found ")
            exit(-1)

    startRule()

syn()
output="intCode.int"
with open(output, "w") as f:
    for sublist in totalQuadsList:
        f.write(f"{sublist[0]}: {' '.join(str(x) for x in sublist[1:])}\n")
print()
print("========== Compilation completed successfully! ==============")



