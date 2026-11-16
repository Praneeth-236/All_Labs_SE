
def clean_pan(pan):
    """
    Removes spaces from a PAN and upper-cases it.
    Validates that the input is a string.
    """
    if not isinstance(pan, str):
        raise ValueError("PAN must be a string")

    pan = pan.strip()

    if not pan:
        raise ValueError("PAN cannot be empty")

    return pan.replace(' ', '').upper()


def parse_amount(text):
    """
    Converts an amount such as 'Rs 12,50,000' into an integer.
    Validates the input before conversion.
    """
    if not isinstance(text, str):
        raise ValueError("Amount must be a string")

    text = text.replace('Rs', '').replace(',', '').strip()

    if not text:
        raise ValueError("Amount cannot be empty")

    try:
        amount = int(text)
    except ValueError:
        raise ValueError("Amount must contain a valid integer")

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    return amount


def parse_tax_slab(line):
    """
    Parses 'LOW-HIGH:RATE' into a (low, high, rate) tuple.
    Validates the format and numeric values.
    """
    if not isinstance(line, str):
        raise ValueError("Tax slab must be a string")

    line = line.strip()

    if not line:
        raise ValueError("Tax slab cannot be empty")

    try:
        limits, rate = line.split(':')
        low, high = limits.split('-')

        low = int(low)
        high = int(high)
        rate = int(rate)

    except ValueError:
        raise ValueError("Tax slab must follow LOW-HIGH:RATE format")

    if low < 0 or high < low or rate < 0:
        raise ValueError("Invalid tax slab values")

    return low, high, rate


def main():
    print("==== Running clean_pan ====")
    value = input("Enter a PAN (e.g. abcde 1234f): ")
    print("Cleaned PAN:", clean_pan(value))

    print("\n==== Running parse_amount ====")
    value = input("Enter an amount (e.g. Rs 12,50,000): ")
    print("Amount in rupees:", parse_amount(value))

    print("\n==== Running parse_tax_slab ====")
    value = input("Enter a tax slab as LOW-HIGH:RATE (e.g. 250000-500000:5): ")
    print("Tax slab (low, high, rate):", parse_tax_slab(value))


if __name__ == "__main__":
    main()
