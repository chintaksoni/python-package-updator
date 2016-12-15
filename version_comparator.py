import sys

current = sys.argv[1]
latest = sys.argv[2]

seperator = '.'

alpha_dict = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':25  }

def get_number(num):
	if num.isdigit():
		return int(num)

	elif num.isalpha():
		digit = alpha_dict[num[0]]
		fraction = 0
		for i in range(1,len(num)):
			alpha_char = alpha_dict[num[i]]
			fraction = fraction*pow(10,len(alpha_char)) + alpha_char
		return ( float(str(digit)+'.'+str(fraction)) )

	elif num.isalnum():
		digit = 0
		if num[0].isalpha():
			digit = alpha_dict[num[0]]
		elif num[0].isdigit():
			digit = num[0]

		fraction = 0
		for i in range(1,len(num)):
			if num[i].isalpha():
				alpha_char = alpha_dict[num[i]]
				fraction = fraction*pow(10,len(alpha_char)) + alpha_char
			else:
				alpha_char = num[i]
				fraction = fraction*pow(10,len(alpha_char)) + int(alpha_char)
		return ( float(str(digit)+'.'+str(fraction)) )

	else:
		return '-1'


def check_update(current, latest):
	current_split = current.split(seperator)
	latest_split = latest.split(seperator)

	length = min( len(current_split), len(latest_split) )

	for i in range(length):
		current_number = get_number(current_split[i])
		latest_number = get_number(latest_split[i])

		if current_number == '-1' or latest_number == '-1':
			return False	

		if current_number > latest_number:
			return False
		elif current_number < latest_number:
			return True
		else:
			continue
	return False


need_update = check_update(current,latest)
print need_update




