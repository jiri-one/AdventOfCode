from operator import itemgetter


# result of test_input.txt file have to be 61229 and for input.txt it is 1007675
with open("input.txt", "r") as file:
	lines_list = file.read().splitlines()

#line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

class SignalDecoder:
	def __init__(self, signals):
		self.signals = signals.split()
		self.segments = {1: "",
						 2: "",
						 3: "",
						 4: "",
						 5: "",
						 6: "",
						 7: ""}

		self.zero = None
		self.one = None
		self.two = None
		self.three = None
		self.four = None
		self.five = None
		self.six = None
		self.seven = None
		self.eight = None
		self.nine = None

		for signal in self.signals:
			if len(signal) == 2:
				self.one = "".join(sorted(signal))
			elif len(signal) == 4:
				self.four = "".join(sorted(signal))
			elif len(signal) == 3:
				self.seven = "".join(sorted(signal))
			elif len(signal) == 7:
				self.eight = "".join(sorted(signal))

		self.segments[1] = [char for char in self.seven if not char in self.one][0] # we know, one and seven, so the first segnem will be letter which is not in number one
		self.segments[7] = self.segment_seven()
		self.segments[5] = self.segment_five()
		self.segments[2] = self.segment_two()
		self.segments[4] = self.segment_four()
		self.segments[3] = self.segment_three()
		self.segments[6] = [char for char in self.one if char != self.segments[3]][0] # we know chars in number one and we know segment three, so the difference will be segment six
		self.rest_signals()

	def segment_seven(self):
		# we know first segment and letters in number four, so the segment seven will be number, which is not combination of number four and first segment
		for signal in self.signals:
			if len(signal) == 6:
				result = [char for char in signal if char not in self.four+self.segments[1]]
				if result and len(result) == 1:
					return result[0]
	
	def segment_five(self):
		# we know segment seven and one and number four, and the last letter will give as nine
		for signal in self.signals:
			if len(signal) == 5:
				result = [char for char in signal if char not in self.four+self.segments[1]+self.segments[7]]
				if result and len(result) == 1:
					return result[0]
	
	def segment_two(self):
		# we know number seven and segments 5 and 7, and the last letter will give as zero
		for signal in self.signals:
			if len(signal) == 6:
				result = [char for char in signal if char not in self.seven+self.segments[5]+self.segments[7]]
				if result and len(result) == 1:
					return result[0]
	
	def segment_four(self):
		# we know number one and segments 1 and 7, and the last letter will give as three
		for signal in self.signals:
			if len(signal) == 5:
				result = [char for char in signal if char not in self.one+self.segments[1]+self.segments[7]]
				if result and len(result) == 1:
					return result[0]
	
	def segment_three(self):
		# we know segments 1,4,5 and 7, and the last letter will give as two
		for signal in self.signals:
			if len(signal) == 5:
				result = [char for char in signal if char not in self.segments[1]+self.segments[4]+self.segments[5]+self.segments[7]]
				if result and len(result) == 1:
					return result[0]
	
	def rest_signals(self):
		self.zero = "".join(sorted(list(itemgetter(1, 2, 3, 5, 6, 7)(self.segments))))
		self.two = "".join(sorted(list(itemgetter(1, 3, 4, 5, 7)(self.segments))))
		self.three = "".join(sorted(list(itemgetter(1, 3, 4, 6, 7)(self.segments))))
		self.five = "".join(sorted(list(itemgetter(1, 2, 4, 6, 7)(self.segments))))
		self.six = "".join(sorted(list(itemgetter(1, 2, 4, 5, 6, 7)(self.segments))))
		self.nine = "".join(sorted(list(itemgetter(1, 2, 3, 4, 6, 7)(self.segments))))
		
def count_one_line(line):
	sd = SignalDecoder(line.split(" | ")[0])
	digits = line.split(" | ")[1]
	number = ""
	for digit in digits.split():
		digit = "".join(sorted(digit))
		if digit == sd.zero:
			number += "0"
		elif digit == sd.one:
			number += "1"
		elif digit == sd.two:
			number += "2"
		elif digit == sd.three:
			number += "3"
		elif digit == sd.four:
			number += "4"
		elif digit == sd.five:
			number += "5"
		elif digit == sd.six:
			number += "6"
		elif digit == sd.seven:
			number += "7"
		elif digit == sd.eight:
			number += "8"
		elif digit == sd.nine:
			number += "9"
	else:
		return int(number)


sum_number = 0

for line in lines_list:
	number_from_one_line = count_one_line(line)
	sum_number += number_from_one_line

print(sum_number)