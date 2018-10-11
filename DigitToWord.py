digitsInWords = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
while True:
    digit = int(input('Enter a digit: '))
    if digit > 9 or digit < 0:
        break
    print('{} in words: {}'.format(digit, digitsInWords[digit]))