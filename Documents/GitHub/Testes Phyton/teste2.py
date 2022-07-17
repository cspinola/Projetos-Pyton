
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

max_num = lista[0]
min_num = lista[0]
neg_sum = 0
list_even = []
mean_numbers = 0

for num in lista:
    mean_numbers = + num
    if max_num < num:
        max_num = num
    if min_num > num:
        min_num = num
    if num < 0:
        neg_sum = + num
    if num % 2 == 0:
        list_even.append(num)


print('O maior elemento é: {}'.format(max_num))
print('O menor elemento é: {}'.format(min_num))
print('A média dos elemento é: {}'.format(mean_numbers/len(lista)))
print('A soma dos elementos negativos é: {}'.format(neg_sum))
print('Os números pares são: {}'.format(list_even))
