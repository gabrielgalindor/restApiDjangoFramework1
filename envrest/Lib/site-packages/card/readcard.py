#Funcion que devuelve en lista una cadena de caracteres
def splitall(word):
    return [char for char in word]

#Funcion que verifica si un elemento esta duplicado dentro de la lista
def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
#Funcion que no arroja error en caso de no encontrar un elemento dentro de una lista
def checkSecureInList(lista,check):
    try:
        lista.index(check)
        return True
    except:
        return False
#Funcion que retorna unicamente los elementos que se repiten
def notset(lista):
    setlist = list(set(lista))
    for i in setlist:
        if checkSecureInList(lista,i):
            lista.remove(i)
    return lista
#Funcion que compara si una lista esta contenida como sublista de otra
def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

# CLASES 
# Clase Readkeylog permite convertir el archivo en una lista de strings para poder trabajar con ellos

class readkeylog:
    def __init__(self, filename):
        self.filename = filename
        self.line_count = 0
        self.numberlist = []
        self.alreadyread = False

    
    def getlistnumbers(self):
        if self.alreadyread == False:
            file = open(self.filename,'r')
            for line in file:
                if line != "\n":
                    self.line_count +=1
                    self.numberlist.append(line[0:3])
            self.alreadyread = True
        return self.numberlist
    
    def get_alreadyread(self):
        return self.alreadyread
    
    def get_numberlines(self):
        return self.line_count
    
    def get_numberlist(self):
        return self.numberlist

class creditcard:

    def __init__(self):
        #Se busca hacer una lista de diccionarios que permita agregar un digito ej: [{id: 0, antesde: [3,4,5] despuesde: [5,6,7]}, ...]
        self.numbers_disorder = []
        self.numbers_disorder2 = []
        self.numbers_order =[]
        self.number_digit = 0
        self.setlist_numbers = []
        self.befores_list = []
        self.beforesfinded = 0
        self.afters_list = []
        self.aftersfinded = 0
        self.credit_card=[]
    
    def add_number(self,allstring):
        for single_string in allstring:
            list_string = splitall(single_string)
            k = 0
            for knumber in list_string:
                before = []
                after = []
                if k<len(list_string)-1:
                    for i in list_string[k+1::]:
                        after.append(i)
                if k>0:
                    for i in list_string[:k:]:
                        before.append(i)
                #print(f"before ={before} after = {after} number={knumber}")
                itsrepeat = False
                if checkIfDuplicates_1(list_string):
                    check_repeat = notset(list_string)
                    itsrepeat = checkSecureInList(check_repeat,knumber)
                dictinfo = {"id":knumber,"before":before, "after":after, "is_repeat":itsrepeat}
                tuplafinal = (knumber,dictinfo)
                self.numbers_disorder.append(tuplafinal)
                self.numbers_disorder2.append(tuplafinal)
                k +=1
        
    def get_disorderList(self):
        return self.numbers_disorder
    
    def find_afterIsNull(self):
        numberslist = []
        for i in self.numbers_disorder2:
            temp_numbers = i[0]
            numberslist.append(temp_numbers)
        repeatnumbers = list(set(numberslist))
        tuplas_ubications = []
        for i in repeatnumbers:
            ubications = []
            k = 0
            for j in self.numbers_disorder2:
                if i == j[0]:
                    #print(j)
                    ubications.append(k)
                k+=1
            finaltupla = (i,ubications)
            tuplas_ubications.append(finaltupla)
        afters = None
        #print(self.numbers_disorder2)
        #Identify the Ids where after = []
        for i in tuplas_ubications:
            number_string = i[0]
            after_isnull = True
            #print(i)
            for j in i[1]:
                temp_resp = self.numbers_disorder2[j]
                dict_number = temp_resp[1]
                list_after = dict_number['after']
                if len(list_after) != 0:
                    after_isnull = False
            if after_isnull:
                #print(number_string)
                afters = number_string
        #Remove the Id into numbers disorder dictonary 
        k = 0
        for i in self.numbers_disorder2:
            temp_dict = i[1]
            remove_element = self.numbers_disorder2[k]
            if i[0] == afters:
                #self.numbers_disorder2.remove(self.numbers_disorder2[k])
                self.numbers_disorder2.remove(remove_element)
            if checkSecureInList(temp_dict['after'],afters):
                remove_list = temp_dict['after']
                remove_list.remove(afters)
            k+=1
        k = 0
        for i in self.numbers_disorder2:
            temp_dict = i[1]
            remove_element = self.numbers_disorder2[k]
            if i[0] == afters:
                #self.numbers_disorder2.remove(self.numbers_disorder2[k])
                self.numbers_disorder2.remove(remove_element)
            if checkSecureInList(temp_dict['after'],afters):
                remove_list = temp_dict['after']
                remove_list.remove(afters)
            k+=1
        k = 0
        for i in self.numbers_disorder2:
            temp_dict = i[1]
            remove_element = self.numbers_disorder2[k]
            if i[0] == afters:
                #self.numbers_disorder2.remove(self.numbers_disorder2[k])
                self.numbers_disorder2.remove(remove_element)
            if checkSecureInList(temp_dict['after'],afters):
                remove_list = temp_dict['after']
                remove_list.remove(afters)
            k+=1
        
        #print(self.numbers_disorder2)
        self.afters_list.append(afters)
        self.aftersfinded+=1
        #print(self.afters_list)
        if afters == None:
            return False
        else:
            return True

    def find_beforeIsNull(self):
        numberslist = []
        for i in self.numbers_disorder:
            temp_numbers = i[0]
            numberslist.append(temp_numbers)
        repeatnumbers = list(set(numberslist))
        tuplas_ubications = []
        for i in repeatnumbers:
            ubications = []
            k = 0
            for j in self.numbers_disorder:
                if i == j[0]:
                    #print(j)
                    ubications.append(k)
                k+=1
            finaltupla = (i,ubications)
            tuplas_ubications.append(finaltupla)
        befores = None
        #print(self.numbers_disorder)
        #Identify the Ids where before = []
        for i in tuplas_ubications:
            number_string = i[0]
            before_isnull = True
            #print(i)
            for j in i[1]:
                temp_resp = self.numbers_disorder[j]
                dict_number = temp_resp[1]
                list_before = dict_number['before']
                if len(list_before) != 0:
                    before_isnull = False
            if before_isnull:
                #print(number_string)
                befores = number_string
        #Remove the Id into numbers disorder dictonary 
        k = 0
        for i in self.numbers_disorder:
            temp_dict = i[1]
            remove_element = self.numbers_disorder[k]
            if i[0] == befores:
                #self.numbers_disorder.remove(self.numbers_disorder[k])
                self.numbers_disorder.remove(remove_element)
            if checkSecureInList(temp_dict['before'],befores):
                remove_list = temp_dict['before']
                remove_list.remove(befores)
            k+=1
        k = 0
        for i in self.numbers_disorder:
            temp_dict = i[1]
            remove_element = self.numbers_disorder[k]
            if i[0] == befores:
                #self.numbers_disorder.remove(self.numbers_disorder[k])
                self.numbers_disorder.remove(remove_element)
            if checkSecureInList(temp_dict['before'],befores):
                remove_list = temp_dict['before']
                remove_list.remove(befores)
            k+=1
        k = 0
        for i in self.numbers_disorder:
            temp_dict = i[1]
            remove_element = self.numbers_disorder[k]
            if i[0] == befores:
                #self.numbers_disorder.remove(self.numbers_disorder[k])
                self.numbers_disorder.remove(remove_element)
            if checkSecureInList(temp_dict['before'],befores):
                remove_list = temp_dict['before']
                remove_list.remove(befores)
            k+=1
        
        #print(self.numbers_disorder)
        self.befores_list.append(befores)
        self.beforesfinded+=1
        #print(self.befores_list)
        if befores == None:
            return False
        else:
            return True
    def get_creditCard(self):
        l = len(self.afters_list)
        inverse_after = self.afters_list[::-1]
        position = 1
        not_sublist = True
        while not_sublist and position < l:
            compare_list = inverse_after[position:l:]
            not_sublist = is_Sublist(self.befores_list,compare_list)
            position+=1
        compare_list = inverse_after[position:l:]
        self.credit_card += compare_list
        return self.credit_card





keylogfile = readkeylog('keylog.txt')
listnumbers = keylogfile.getlistnumbers()
credit1 = creditcard()
credit1.add_number(listnumbers)
n = 0
itsNone = True
while itsNone:
    itsNone = credit1.find_beforeIsNull()
    n+=1
n = 0
itsNone = True
while itsNone:
    itsNone = credit1.find_afterIsNull()
    n+=1
print(credit1.get_creditCard())



#print(credit1.get_disorderList())



