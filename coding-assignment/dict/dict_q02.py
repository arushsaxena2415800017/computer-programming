# Handling missing keys in Python dictionaries
country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))
