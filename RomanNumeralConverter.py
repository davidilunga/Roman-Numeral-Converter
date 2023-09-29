def roman_to_int(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman)):
        if i > 0 and roman_numerals[roman[i]] > roman_numerals[roman[i - 1]]:
            result += roman_numerals[roman[i]] - 2 * roman_numerals[roman[i - 1]]
        else:
            result += roman_numerals[roman[i]]

    return result

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0

    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1

    return roman_num

# Example usage:

while True:
	user_input = input("Enter a Roman numeral or an integer: ")

	if user_input.isnumeric():
		result_roman = int_to_roman(int(user_input))
		print(f"{user_input} as a Roman numeral: {result_roman}")
	else:
		result_int = roman_to_int(user_input.upper())
		print(f"{user_input} as an integer: {result_int}")
