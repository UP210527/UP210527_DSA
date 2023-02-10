z=input('Dime una palabra: ')
if z==z[::-1]: #para hacer el reverso del string y poder comparar
  print('Es un Palíndromo')
else:
  print('No es un Palíndromo')