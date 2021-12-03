gamma_rate = ""
epsilon_rate = ""

# result of test_input.txt file have to be 198
with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()
    number_of_bits = len(lines_list[0])
    bit_counter_zero = {}
    bit_counter_one = {}
    for bit_index in range(number_of_bits):
        bit_counter_zero[bit_index] = 0
        bit_counter_one[bit_index] = 0
    for line in lines_list:
        bit_index = 0
        for char in line:
            if char == "0":
                bit_counter_zero[bit_index] += 1
            elif char == "1":
                bit_counter_one[bit_index] += 1
            bit_index += 1
    for bit_index in range(number_of_bits):
        if bit_counter_zero[bit_index] > bit_counter_one[bit_index]:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"
        elif bit_counter_zero[bit_index] < bit_counter_one[bit_index]:
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate + "0"            

gamma_rate_decimal = int(gamma_rate, 2)
epsilon_rate_decimal = int(epsilon_rate, 2)
print(gamma_rate_decimal * epsilon_rate_decimal)


