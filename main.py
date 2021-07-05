#Created by Khalid Al Shuaib on 5/7/21
# Text to binary translator
def string_to_binary(string):
	total_binary = ''


	for x in range(0,len(string)):	
		binary = ''
		string_ord = ord(string[x : x + 1])
		
		
		while string_ord > 0:
			i = string_ord % 2
			string_ord = string_ord//2
			binary = str(i) + str(binary)


			
		if len(total_binary) + len(binary) < 64:
			required_bits = 64 - len(total_binary)
			for i in range(required_bits):
				total_binary = '0' + total_binary


		total_binary += binary + ' '



	print(total_binary)


string_to_binary('Khalid Al Shuaib')
