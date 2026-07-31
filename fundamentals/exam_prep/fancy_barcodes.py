import re

def barcode_validator(barcode:str):
    pattern = '^@#+(.*)@#+$'
    match = re.search(pattern, barcode)

    if match:
        real_code = match.group(1)
        if not real_code.isalnum():
            return "Invalid barcode"
        if len(real_code) < 6:
            return 'Invalid barcode'
        if not real_code[0].isupper():
            return 'Invalid barcode'
        if not real_code[-1].isupper():
            return "Invalid barcode"
        return real_code
    else:
        return "Invalid barcode"



number_of_barcodes = int(input())
codes = []

for _ in range(number_of_barcodes):
    current_barcode = input()
    code = barcode_validator(current_barcode)

    if code != "Invalid barcode":
        product_code = ""
        for i in code:
            if i.isdigit():
                product_code += i
        if len(product_code) >= 1:
            print(f'Product group: {product_code}')
        else:
            print(f'Product group: 00')
    else:
        print(code)
