def convert_to_decimal(hex_num: str) -> int:
    hex_num = hex_num
    decimal_num = int(hex_num, 16)

    return decimal_num


def reverse_by_pairs(hex_num):
    if hex_num[0] == "#":
        hex_num = hex_num[1:]

    pairs = [hex_num[i:i+2] for i in range(0, len(hex_num), 2)]
    reversed_pairs = pairs[::-1]

    return "".join(reversed_pairs)


if __name__ == "__main__":
    color_code = reverse_by_pairs(input("Please input the color code.\n"))
    result = convert_to_decimal(color_code)
    print(f"color code: {result}")
