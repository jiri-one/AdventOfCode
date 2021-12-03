co2_scrubber_rating = None

def filter_by_more_bits_on_position(lines_list: list, bit_position: int = 0) -> list:
    print("len", len(lines_list))
    print("na vstupu", lines_list)
    if len(lines_list) == 1:
        print("znovu", lines_list)
        return 'vykuř'
    #if len(lines_list) == 2:
        #pass
    #if bit_position == len(lines_list)-1:
        #pass
    # settings again to zero before next iteration
    ones = 0
    zeroes = 0
    for line in lines_list:
        if line[bit_position] == "1":
            ones += 1
        elif line[bit_position] == "0":
            zeroes += 1
    print(ones, zeroes)
    if ones >= zeroes:
        lines_list = [line for line in lines_list if line[bit_position] == "1"]
        print(lines_list)
    elif ones < zeroes:
        lines_list = [line for line in lines_list if line[bit_position] == "0"]
    bit_position += 1
    print("position", bit_position)
    filter_by_more_bits_on_position(lines_list, bit_position)
        

# result of test_input.txt file have to be 198
with open("test_input.txt", "r") as file:
    lines_list = file.read().splitlines()
    print(filter_by_more_bits_on_position(lines_list))
   