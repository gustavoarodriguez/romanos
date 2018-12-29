#### ROMANOS ####

 ## Define output variable
roman = ''
# Get number
while True:
	try:
		number = int(raw_input('Number: '))
		if number >= 1 and number <= 1000:
			break
		print('Number must be between 1 and 1000.\n Try again.')
	except ValueError:
		print('You must introduce an int number.\n Try again.')
### Convert

while number != 0:
	if number == 1000:
		roman = roman + 'M'
		number = 0
	elif number >=900:
		roman = roman + 'CM'
		number = number - 900
	elif number >= 500:
		roman= roman + 'D'
		number = number - 500
	elif number >= 400:
		roman = roman + 'CD'
		number = number - 400
	elif number >= 100:
		roman = roman + 'C'
		number = number - 100
	elif number >= 90:
		roman = roman + 'XC'
		number = number - 90
	elif number >= 50:
		roman = roman + 'L'
		number = number - 50
	elif number >= 40:
		roman = roman + 'XL'
		number = number - 40
	elif number >= 10:
		roman = roman + 'X'
		number = number - 10
	elif number == 9:
		roman = roman + 'IX'
		number = number - 9
	elif number >= 5:
		roman = roman + 'V'
		number = number - 5
	elif number == 4:
		roman = roman + 'IV'
		number = number - 4
	elif number >= 1:
		roman = roman + 'I'
		number = number - 1

print('The number in roman numerals is: '+roman)

	
