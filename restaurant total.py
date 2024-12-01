# Andrew Keller
# 11/26/2024

subtotal = input('Enter the subtotal. ')
while isinstance(subtotal, str):
    if subtotal.replace('.','').isdigit():
        subtotal = float(subtotal)
    else:
        subtotal = input('Subtotal should be a decimal number. Enter the subtotal. ')

tip = subtotal * .18
tax = subtotal * .07
total = subtotal + tip + tax
print(f'Subtotal:      ${subtotal:.2f}')
print(f'Tip:            ${tip:.2f}')
print(f'Tax:            ${tax:.2f}')
print(f'Total:         ${total:.2f}')
