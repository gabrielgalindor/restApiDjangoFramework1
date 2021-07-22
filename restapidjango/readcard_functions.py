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