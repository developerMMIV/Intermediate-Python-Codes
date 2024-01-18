frase = str(input('Type a phrase:')).strip().upper()
words = frase.split()
together = ''.join(words)
inverso = ''
for letter in range(len(together)- 1, -1, -1):
    inverso += together[letter]
print('The word {} read backwords is {} '.format(together,inverso))
if inverso == together:
    print('We have a palidrome')
else:
    print('We do not have a palidrome')