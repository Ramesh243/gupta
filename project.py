import math
import random 
import sys

print(u"\u001b[31m")
print("\t\t\t\t       ******     ")
print("\t\t\t\t     **********   ") 
print("\t\t\t\t    **        **  ")
print("\t\t\t\t   **          ** ")          
print("\t\t\t\t   **          ** ")    
print("\t\t\t\t   **          ** ")
print("\t\t\t\t ******************")    
print("\t\t\t\t ******************")
print("\t\t\t\t ******************")
print("\t\t\t\t *******    *******")
print("\t\t\t\t ********  ********")
print("\t\t\t\t ********  ********")
print("\t\t\t\t ******************")
print("\t\t\t\t ******************")

print(u"\u001b[0m")
choice = int(input("Enter 1 for encryption and 2 for decryption: "))

if choice == 1:

	familiars = {
		'a':50,'b':31,'c':32,'d':33,'e':34,'f':35,'g':36,'h':37,'i':38,'j': 39, 'k': 40, 'l': 41, 'm': 42, 'n': 43, 'o': 44, 'p': 45, 'q': 46, 'r': 47, 's': 48, 't': 49, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
		'z': 26, ' ': 27, '  ': 28, ',': 29, '.': 30

	}

	message = input("enter the message: ")

	array = []

	length_of_message = len(message)

	for i in range(length_of_message):

		array.append(message[i])


	replace = [familiars[letter] for letter in array]

	new = [int(item) for item in replace]

	randy = int(input("enter a number (a number between 5000000000 and 1000000000): "))

	sr_randi = str(randy)

	multiplied_list = [element * randy for element in new]
	
	output = [str(x) for x in multiplied_list]

	mes_len = len(output[1])

	sr_len = str(mes_len)

	sec_key = sr_randi + sr_len

	joined = ''.join(map(str, multiplied_list))

	print("Your encrypted message is :  ",joined)

	print("secret key:   ",sec_key)

elif choice == 2:

	a_message = input("Enter the message for decryption: ")

	secret_mes_str = input("enter the secret key :  ")

	print("decrypting.......")

	first_last = secret_mes_str[-2] + secret_mes_str[-1]

	div = int(first_last)

	secret_mes_int = int(secret_mes_str[:-2])

	new_List = []
	for i in range(0, len(a_message), div):

	    new_List.append(a_message[i : i + div])

	map_object = map(int,new_List)

	list_of_integers = list(map_object)

	divided_list = [math.floor(elem / secret_mes_int) for elem in list_of_integers]


	familiars1 = {

	    50:'a',31:'b',32:'c',33:'d',34:'e',35:'f',36:'g',37:'h',38:'i',39:'j',40:'k',41:'l', 42:'m',43:'n',44:'o', 45:'p', 46:'q',47:'r',48:'s',  49:'t', 21:'u',22:'v',23:'w', 24:'x', 25:'y',
	    26:'z', 27:' ',28:'  ', 29:',', 30:'.'

	}

	replace1 = [familiars1[letter1] for letter1 in divided_list]

	
	listtostr = "".join(replace1)

	print("the secret message is:", listtostr)

else:

	print("choose a correct option")































