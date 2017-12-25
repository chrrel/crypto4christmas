import hashlib
import numpy as np

class Crypto4Christmas():
	def __init__(self, matrikel_number):
		self.matrikel_number = matrikel_number
		self.matrikel_hash_hex = hashlib.sha1(matrikel_number.encode()).hexdigest()
		self.matrikel_hash_bin = self.__hex2binary(self.matrikel_hash_hex)

	def __get_char_at_position(self, position):
		calc_position = len(self.matrikel_hash_hex) - position - 1
		return self.matrikel_hash_hex[calc_position]

	def __hex2binary(self, hex_string):
		return "{0:04b}".format(int(hex_string,16))

	def __hex2dec(self, hex_string):
		return "{:d}".format(int(hex_string,16))

	def at_position(self, position):
		char_at_position = self.__get_char_at_position(position)
		char_at_position_bin = self.__hex2binary(char_at_position)
		char_at_position_dec = self.__hex2dec(char_at_position)

		formatstring = '# {:30s} {}'
		print("##########################################################################")
		print(formatstring.format("Matrikel", self.matrikel_number))
		print(formatstring.format("SHA-1", self.matrikel_hash_hex))
		print(formatstring.format("Position", position))
		print(formatstring.format("At this position the char is", char_at_position))
		print(formatstring.format("Binary value for this char is", char_at_position_bin))
		print(formatstring.format("Decimal value for this char is", char_at_position_dec))

		print("##########################################################################")

	# get_binary_position
	def bin_pos(self, position_of_character, number_of_binary_position):
		char_at_position = self.__get_char_at_position(position_of_character)
		char_at_position_bin = self.__hex2binary(char_at_position)

		calc_position_bin = len(char_at_position_bin) - number_of_binary_position - 1
		binary_value_at_position = char_at_position_bin[calc_position_bin]

		# print("At position {} the character is {} which in binary is {}. At position {} of the binary representation there is a {}.".format(position_of_character, char_at_position, char_at_position_bin, number_of_binary_position, binary_value_at_position) )
		return binary_value_at_position

	# get decimal at position
	def dec_pos(self, position):
		char_at_position = self.__get_char_at_position(position)
		return self.__hex2dec(char_at_position)

	# get hex at position
	def hex_pos(self, position):
		return self.__get_char_at_position(position)

	def task1(self):
		bitstring = ""
		i = 39
		while (i >= 35):
			bitstring += self.bin_pos(i,3) + self.bin_pos(i,2) + self.bin_pos(i,1) + self.bin_pos(i,0)
			i = i - 1

		a = np.array([[int(self.bin_pos(34,3)), 0, 0, 0, 1],
					[int(self.bin_pos(34,2)), 0, 1, 0, 0],
					[int(self.bin_pos(34,1)), 0, 0, 1, 0],
					[int(self.bin_pos(34,0)), 1, 0, 0, 0],
					[1, 0, 0, 0, 0]]
					)

		b = np.array([int(self.bin_pos(33,3)), int(self.bin_pos(33,2)), 1, int(self.bin_pos(33,1)), int(self.bin_pos(33,0))])

		print("\n### Task 1 ###")
		print("Input: " + bitstring)
		print("A = ")
		print(a)
		print("b = ")
		print(b)

	def task2(self):
		vector_k = "( 1 {} {} {} {} {} {} {} )	(mod 11)".format(self.dec_pos(32), self.dec_pos(31), self.dec_pos(30), self.dec_pos(29), self.dec_pos(28), self.dec_pos(27), self.dec_pos(26) )
		k = "1x⁷ + {}x⁶ + {}x⁵ + {}x⁵ + {}x³ + {}x² + {}x¹ + {}	(mod 11)".format(self.dec_pos(32), self.dec_pos(31), self.dec_pos(30), self.dec_pos(29), self.dec_pos(28), self.dec_pos(27), self.dec_pos(26) )

		print("\n### Task 2 ###")
		print(vector_k)
		print(k)

	def task3(self):
		key = np.array([[self.hex_pos(25) + self.hex_pos(24), '28','B9', self.hex_pos(24) + self.hex_pos(25)],
			['7E', self.hex_pos(23) + self.hex_pos(22), self.hex_pos(22) + self.hex_pos(23), '00'],
			['15', self.hex_pos(20) + self.hex_pos(21), self.hex_pos(21) + self.hex_pos(20), '00'],
			[self.hex_pos(18) + self.hex_pos(19), 'AD', '63', self.hex_pos(19) + self.hex_pos(18)]
		])

		print("\n### Task 3 ###")
		print(key)

	def task4(self):
		M = np.array([
			[2396, int(self.dec_pos(17)), 6767, int(self.dec_pos(16))],
			[0, 945, 0, 17981],
			[6413, int(self.dec_pos(15)), 19746, int(self.dec_pos(14))],
			[0, 377, 0, 31031]
		])
		print("\n### Task 4 ###")
		print(M)

	def task5(self):
		p_dash = (99 - int(self.dec_pos(13))) * (99 - int(self.dec_pos(12)))
		e_dash = pow(2,10) + int(self.dec_pos(11))
		m = 999 - int(self.dec_pos(10))

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



matrikel_number = "1231023" # Todo: Correct number
c = Crypto4Christmas(matrikel_number)


c.at_position(1)

c.bin_pos(7,2)

c.task1()
c.task2()
c.task3()
c.task4()
c.task5()
