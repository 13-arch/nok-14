'''Требуется написать программу, определяющую наименьшее общее кратное (НОК) чисел a и b.

Входные данные
В единственной строке входного файла INPUT.TXT записаны два натуральных числа А и В через пробел, не превышающих 46340.

Выходные данные
В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — НОК чисел А и В.'''
from math import gcd
input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
data = data.split()
a= int(data[0])
b= int(data[1])
#nok = a*b/nod 
output_data.write(str(a*b//gcd(a,b)))
output_data.close()
input_data.close()