oxygen_generator_rating = None
co2_scrubber_rating = None


def filter_by_more_bits_on_position(lines_list: list, bit_position: int = 0) -> list:
    if len(lines_list) == 1:
        global oxygen_generator_rating
        oxygen_generator_rating = lines_list
        return
    ones = 0
    zeroes = 0
    for line in lines_list:
        if line[bit_position] == "1":
            ones += 1
        elif line[bit_position] == "0":
            zeroes += 1
    if ones >= zeroes:
        lines_list = [line for line in lines_list if line[bit_position] == "1"]
    elif ones < zeroes:
        lines_list = [line for line in lines_list if line[bit_position] == "0"]
    bit_position += 1
    filter_by_more_bits_on_position(lines_list, bit_position)


def filter_by_less_bits_on_position(lines_list: list, bit_position: int = 0) -> list:
    if len(lines_list) == 1:
        global co2_scrubber_rating
        co2_scrubber_rating = lines_list
        return
    ones = 0
    zeroes = 0
    for line in lines_list:
        if line[bit_position] == "1":
            ones += 1
        elif line[bit_position] == "0":
            zeroes += 1
    if ones < zeroes:
        lines_list = [line for line in lines_list if line[bit_position] == "1"]
    elif ones >= zeroes:
        lines_list = [line for line in lines_list if line[bit_position] == "0"]
    bit_position += 1
    filter_by_less_bits_on_position(lines_list, bit_position)


# result of test_input.txt file have to be 230
with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()
    filter_by_more_bits_on_position(lines_list)
    filter_by_less_bits_on_position(lines_list)
    oxygen_generator_rating_decimal = int(oxygen_generator_rating[0], 2)
    co2_scrubber_rating_decimal = int(co2_scrubber_rating[0], 2)
    print(oxygen_generator_rating_decimal * co2_scrubber_rating_decimal)
