total = 0
totmil =0
minor = 0
cont = 0
cheap = ' '
while True:
    product = str(input('name of the product :'))
    price = int(input('Price: $'))
    cont += 1
    total+= price
    if price>1000:
      totmil = price
    if cont ==1 and minor<price:
        cheap=product
        minor=price
    ans = ' '
    while ans not in 'Y/N':
        ans =str(input('Want to continue?: Y/N')).strip().upper()
    if ans == 'N':
        break
print(f'''The total of sales is ${total} , we have ${totmil} products above $1000 and the cheapest of them is
{cheap} which is ${minor}''')


