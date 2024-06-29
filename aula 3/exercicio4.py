A = int(input('digite primeiro lado do triangulo: '))
B = int(input('digite segundo lado do triangulo: '))
C = int(input('digite terceiro lado do triangulo: '))

if (( A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
  if ( A != B and A != C and B != C):
    print('triangulo escaleno')
  else:
     if ( A == B and B == C ):
       print('triangulo equilatero')
     else:
       print('triangulo esosceles')

