import hashlib
import numpy as np

class Crypto4Christmas():
	def __init__(self, matrikel_number):
		self.matrikel_number = matrikel_number
		self.matrikel_hash_hex = hashlib.sha1(matrikel_number.encode()).hexdigest()
		self.k = self.__create_hex_list() # hex representation, strings
		self.x = self.__create_dec_list() # decimal representation, integers

	def __hex2binary(self, hex_string):
		return "{0:04b}".format(int(hex_string,16))

	def __hex2dec(self, hex_string):
		return "{:d}".format(int(hex_string,16))

	def __create_hex_list(self):
		k = [x for x in self.matrikel_hash_hex]
		k.reverse() # reverse the list so that k[0] is the last element of the hash
		return k

	def __create_dec_list(self):
		max = len(self.matrikel_hash_hex)
		x = []
		i = 0
		for i in range (0, max):
			char_at_position = self.k[i]
			dec_char = self.__hex2dec(char_at_position)
			x.append(int(dec_char))
		return x

	# at_position(i) returns details on the ith position of the hash
	def at_position(self, position):
		char_at_position = self.k[position]
		char_at_position_bin = self.__hex2binary(char_at_position)

		formatstring = '# {:30s} {}'
		print("##########################################################################")
		print(formatstring.format("Matrikel", self.matrikel_number))
		print(formatstring.format("SHA-1", self.matrikel_hash_hex))
		print(formatstring.format("Position", position))
		print(formatstring.format("At this position the char is", self.k[position]))
		print(formatstring.format("Binary value for this char is", char_at_position_bin))
		print(formatstring.format("Decimal value for this char is", self.x[position]))
		print("##########################################################################")

	# bin_pos(7,3) returns the 3rd number in the binary representation of the hash's 7th character 
	def bin_pos(self, position_of_character, number_of_binary_position):
		char_at_position = self.k[position_of_character]
		char_at_position_bin = self.__hex2binary(char_at_position)

		calc_position_bin = len(char_at_position_bin) - number_of_binary_position - 1
		binary_value_at_position = char_at_position_bin[calc_position_bin]

		return binary_value_at_position

	def task1(self):
		bitstring = ""
		i = 39
		while (i >= 35):
			bitstring += self.bin_pos(i,3) + self.bin_pos(i,2) + self.bin_pos(i,1) + self.bin_pos(i,0)
			i = i - 1

		a = np.array(
			[[int(self.bin_pos(34,3)), 0, 0, 0, 1],
			[int(self.bin_pos(34,2)), 0, 1, 0, 0],
			[int(self.bin_pos(34,1)), 0, 0, 1, 0],
			[int(self.bin_pos(34,0)), 1, 0, 0, 0],
			[1, 0, 0, 0, 0]
		])

		b = np.array([int(self.bin_pos(33,3)), int(self.bin_pos(33,2)), 1, int(self.bin_pos(33,1)), int(self.bin_pos(33,0))])

		print("\n### Task 1 ###")
		print("Input: " + bitstring)
		print("A = ")
		print(a)
		print("b = ")
		print(b)

	def task2(self):
		vector_k = "( 1 {} {} {} {} {} {} {} )	(mod 11)".format(self.x[32], self.x[31], self.x[30], self.x[29], self.x[28], self.x[27], self.x[26])
		k = "1x⁷ + {}x⁶ + {}x⁵ + {}x⁵ + {}x³ + {}x² + {}x¹ + {}	(mod 11)".format(self.x[32], self.x[31], self.x[30], self.x[29], self.x[28], self.x[27], self.x[26])

		print("\n### Task 2 ###")
		print(vector_k)
		print(k)

	def task3(self):
		key = np.array([
			[self.k[25] + self.k[24], '28','B9', self.k[24] + self.k[25]],
			['7E', self.k[23] + self.k[22], self.k[22] + self.k[23], '00'],
			['15', self.k[20] + self.k[21], self.k[21] + self.k[20], '00'],
			[self.k[18] + self.k[19], 'AD', '63', self.k[19] + self.k[18]]
		])

		print("\n### Task 3 ###")
		print(key)

	def task4(self):
		M = np.array([
			[2396, self.x[17], 6767, self.x[16]],
			[0, 945, 0, 17981],
			[6413, self.x[15], 19746, self.x[14]],
			[0, 377, 0, 31031]
		])
		print("\n### Task 4 ###")
		print(M)

	def task5(self):
		p_dash = (99 - self.x[13]) * (99 - self.x[12])
		e_dash = pow(2,10) + self.x[11]
		m = 999 - self.x[10]

		c_dash_bin_string = ""
		i = 9
		while (i >= 7):
			c_dash_bin_string += self.bin_pos(i,3) + self.bin_pos(i,2) + self.bin_pos(i,1) + self.bin_pos(i,0)
			i = i - 1
		c_dash = int(c_dash_bin_string, 2)

		print("\n### Task 5 ###")
		print("p' = {}".format(p_dash))
		print("e' = {}".format(e_dash))
		print("m = {}".format(m))
		print("c' bitstring = {}".format(c_dash_bin_string))
		print("c' = {}".format(c_dash))

	def task6(self):
		q_dash_bitstring = '110' +  self.bin_pos(6,3) + self.bin_pos(6,2) + self.bin_pos(6,1) + self.bin_pos(6,0)  + '1010' +  self.bin_pos(5,3) + self.bin_pos(5,2) + self.bin_pos(5,1) + self.bin_pos(5,0) + '0101'
		q_dash = int(q_dash_bitstring, 2)
		
		a_bitstring = '1001' + self.bin_pos(4,3) + self.bin_pos(4,2) + self.bin_pos(4,1) + self.bin_pos(4,0)
		a = int(a_bitstring, 2)
		
		B_bitstring = '10' + self.bin_pos(3,3) + self.bin_pos(3,2) + self.bin_pos(3,1) + self.bin_pos(3,0)
		B = int(B_bitstring, 2)
		
		c_bitstring = ""
		i = 2
		while (i >= 0):
			c_bitstring += self.bin_pos(i,3) + self.bin_pos(i,2) + self.bin_pos(i,1) + self.bin_pos(i,0)
			i = i - 1
		c = int(c_bitstring, 2)
		
		print("\n### Task 6 ###")		
		print("q' bitstring = {}".format(q_dash_bitstring))		
		print("q' = {}".format(q_dash))
		print("a bitstring = {}".format(a_bitstring))		
		print("a = {}".format(a))
		print("B bitstring = {}".format(B_bitstring))		
		print("B = {}".format(B))		
		print("c bitstring = {}".format(c_bitstring))		
		print("c = {}".format(c))
		
