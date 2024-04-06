bit = int(input("Enter number of bits: "))


if bit <= 64:
    print(f"\nMax number in {bit} bits is {'{:,}'.format(2 ** bit)}")
    print(f"from 0 to {'{:,}'.format(2 ** bit - 1)}")
    print("Bits:", bin(2 ** bit - 1).lstrip("0b"))
else:
    print(f"\nMax number in {bit} bits is 2 ^ {bit}")
    print(f"from 0 to 2 ^ {bit} - 1")
    print("Bits:", bit, "Ones")