import random


# gets user input for each row
def user_input():
    validation = True
    # check to see if its 10 chars long
    while validation:
        user_input_for_nums = input("Please enter 10 1's and 0's: ")
        if len(user_input_for_nums) != 10:
            user_fixed_input_for_len = input("Sorry, you need to enter EXACTLY 10 1's and 0's: ")
            user_input_for_nums = user_fixed_input_for_len
        else:
            validation = False
        # checks to see if each char is either a 1 or 0
        for char in user_input_for_nums:
            if char != "1" and char != "0":
                user_input_wrong_chars = input("Sorry, you can ONLY enter 10 1's or 0's: ")
                user_input_for_nums = user_input_wrong_chars
                break
            else:
                validation = False

    return user_input_for_nums


# turns the string of 10 to 10 separate chars
def single_row_chars():
    user_nums_of_single_row = user_input()
    row = []
    row[:] = user_nums_of_single_row

    return row


# converts the 1's and 0's to symbols
def convert_and_stores_row(user_symbol):
    one_row_of_nums = single_row_chars()
    converted_row = [convert.replace("1", user_symbol).replace("0", " ") for convert in one_row_of_nums]

    return converted_row


# converts 1's and 0's to symbols and scales it
def convert_and_scale_store_rows(scaled_sym, scaled_space):
    unscaled_row = single_row_chars()
    scaled_row = [convert.replace("1", scaled_sym).replace("0", scaled_space) for convert in unscaled_row]

    return scaled_row


# replaces the characters with symbols but inverts the 1's and 0's
def convert_store_invert_rows(user_symbol):
    row_of_nums = single_row_chars()
    convert_invert_row = [convert.replace("1", " ").replace("0", user_symbol) for convert in row_of_nums]

    return convert_invert_row


# replaces the characters with symbols, scales it and inverts the 1's and 0's
def convert_store_scale_invert_row(user_symbol, scaled_space):
    row_of_nums = single_row_chars()
    convert_invert_scale_row = [convert.replace("1", scaled_space).replace("0", user_symbol) for convert in row_of_nums]

    return convert_invert_scale_row


# creates a random row of 1's and 0's then converts it to symbols
def random_row(user_symbol):
    random_list_nums = []
    for i in range(10):
        random_list_nums.append(str(random.randint(0, 1)))
    converted_rand_row = [convert.replace("1", user_symbol).replace("0", " ") for convert in random_list_nums]
    print(*converted_rand_row, sep=" ")


# creates a random row of 1's and 0's then converts it to symbols and scales it
def random_row_scale(scaled_sym, scaled_space):
    random_list_nums_scaled = []
    for i in range(10):
        random_list_nums_scaled.append(str(random.randint(0, 1)))
    converted_rand_row = [convert.replace("1", scaled_sym).replace("0", scaled_space) for convert in random_list_nums_scaled]
    print(*converted_rand_row, sep=" ")


# creates a random row then converts and inverts it
def random_row_invert(user_symbol):
    random_list_nums = []
    for i in range(10):
        random_list_nums.append(str(random.randint(0, 1)))
    converted_rand_row = [convert.replace("1", " ").replace("0", user_symbol) for convert in random_list_nums]
    print(*converted_rand_row, sep=" ")


# creates a random row then converts it, scales it then inverts it
def random_row_scale_invert(scaled_sym, scaled_space):
    random_list_nums_scaled = []
    for i in range(10):
        random_list_nums_scaled.append(str(random.randint(0, 1)))
    converted_rand_row_invert = [convert.replace("1", scaled_space).replace("0", scaled_sym) for convert in random_list_nums_scaled]
    print(*converted_rand_row_invert, sep=" ")


# creates a normal grid
def unscaled_to_grid(user_symbol_input):
    unscaled_grid = []
    user_scale_size = 1
    for i in range(10):
        unscaled_grid.append(convert_and_stores_row(user_symbol_input))
    for i in range(10 * user_scale_size):
        print(*unscaled_grid[i], sep=" ")


# creates a scaled grid
def scaled_to_grid(user_scale_size, scaled_sym, scaled_space):
    scaled_grid = []
    scaled_grid_square = []
    for i in range(10):
        scaled_grid.append(convert_and_scale_store_rows(scaled_sym, scaled_space))
    for i in range(10):
        for j in range(user_scale_size):
            scaled_grid_square.append(scaled_grid[i])
    for i in range(10 * user_scale_size):
        print(*scaled_grid_square[i], sep=" ")


# creates a inverted grid
def invert_to_grid(user_symbol_input):
    invert_grid = []
    user_scale_size = 1
    for i in range(10):
        invert_grid.append(convert_store_invert_rows(user_symbol_input))
    for i in range(10 * user_scale_size):
        print(*invert_grid[i], sep=" ")


# creates a scaled inverted grid
def scaled_invert_to_grid(user_scale_size, scaled_sym, scaled_space):
    invert_grid = []
    invert_scale_grid = []
    for i in range(10):
        invert_grid.append(convert_store_scale_invert_row(scaled_sym, scaled_space))
    for i in range(10):
        for j in range(user_scale_size):
            invert_scale_grid.append(invert_grid[i])
    for i in range(10 * user_scale_size):
        print(*invert_scale_grid[i], sep=" ")


def main():
    # welcome display
    print()
    print("                         Welcome to the Icon Creator")
    print()
    print("You will be asked to enter 1's and 0's or I can make you a random icon")
    print()
    print("A 1 will print a symbol, a 0 will print a blank space (Unless you invert it)")
    print("----------------------------------------------------------------------------")
    # asks for symbol input
    repeat = True
    user_symbol_input = str(input("Enter a symbol you would like to make the icon out of: "))
    while len(user_symbol_input) != 1:
        wrong_input = input("Sorry, you can only enter One symbol. Please enter a symbol")
        user_symbol_input = wrong_input

    # asks if grid should be random
    user_input_rand = str(input("Would you like me to make you a random icon? (Enter Yes or No): ")).lower()
    while user_input_rand != "yes" and user_input_rand != "no":
        wrong_input = input("Sorry, I only understand Yes and No: ")
        user_input_rand = wrong_input

    # asks if user wants to scale the grid
    user_scale = str(input("Would you like to scale the icon? (Enter Yes or No): ")).lower()
    while user_scale != "yes" and user_scale != "no":
        wrong_input = input("Sorry, I only understand Yes and No")
        user_scale = wrong_input
    if user_scale == "yes":
        # asks user how much they want to scale the grid
        while repeat:
            try:
                user_scale_size = int(input("How much would you like to scale the icon? (Enter a number): "))
                repeat = False
            except ValueError:
                print("Sorry, ONLY enter a number please")
    else:
        user_scale_size = 1

    # asks user to invert the grid
    user_invert = str(input("Would you like the invert the icon? (Enter Yes or No): ")).lower()
    while user_invert != "yes" and user_invert != "no":
        wrong_input = input("Sorry, I only understand Yes or No")
        user_invert = wrong_input
       
    # aesthetic display
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                     Making Icon...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    # scaled variables
    scaled_sym = user_scale_size * user_symbol_input
    scaled_space = user_scale_size * " "
    # creates icon for scale and invert
    if user_scale == "yes" and user_invert == "yes" and user_input_rand != "yes":
        scaled_invert_to_grid(user_scale_size, scaled_sym, scaled_space)
    # creates icon for scaled icon
    elif user_scale == "yes" and user_invert != "yes" and user_input_rand != "yes":
        scaled_to_grid(user_scale_size, scaled_sym, scaled_space)
    # creates icon for inverted icon
    elif user_invert == "yes" and user_scale != "yes" and user_input_rand != "yes":
        invert_to_grid(user_symbol_input)
    # creates random icon
    elif user_input_rand == "yes" and user_invert != "yes" and user_scale != "yes":
        for i in range(10):
            random_row(user_symbol_input)
    # creates a scaled random icon
    elif user_input_rand == "yes" and user_scale == "yes" and user_invert != "yes":
        for i in range(10 * user_scale_size):
            random_row_scale(scaled_sym, scaled_space)
    # creates a random inverted scaled icon
    elif user_input_rand == "yes" and user_scale == "yes" and user_invert == "yes":
        for i in range(10 * user_scale_size):
            random_row_scale_invert(scaled_sym, scaled_space)
    # creates a random inverted icon
    elif user_input_rand == "yes" and user_scale != "yes" and user_invert == "yes":
        for i in range(10):
            random_row_invert(user_symbol_input)
    else:
        # creates a normal 10x10 grid
        unscaled_to_grid(user_symbol_input)


if __name__ == '__main__':
    main()
