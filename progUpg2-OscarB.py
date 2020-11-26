import math
from fractions import Fraction

#Här lägger du in första talet
A = input("Täljare: [pi/4]: \n")

#Definerar a
a = math.pi/4

#Gör så att inputen till b är decimaltal
b = float(input("Nämnare: [0]: \n"))

#Gör att inputen för N är heltal
N = int(input("Delintervaller: [10, 100 eller 1000]:\n"))

#Detta gör så att du kan skriva "pi/4", som ett float (decimaltal)
if A == "pi/4": 
  A = a
else:
  A = float(A)

#Integral sats, kan ändras om man vill göra om programmet till en kalkylator
def intergral(N, A, b):
  
  number1 = 0
  number2 = 0

#Gör så att F ger tillbaka den mattematiska satsen under
  def f(x):
    return math.sin(x)*math.cos(x)

#Hämtar talen och lägger de i formeln under
  for n in range(1, N + 1):
    number1 += f(A+((n - (1 / 2)) * ((b - A) / N))) 

  number2 = ((b - A) / N * number1)
  return number2

#Definerar svaret så du kan printa det med precision
svar = intergral (N, A, b) * (-1) 

#Printar båda talen, andra svaret är i en "/", avrundar också till 2 decimaler med "round"
print("Ta ditt svar och gå:", round(svar, 2), round(Fraction(svar), 2)) 

#Oscar.B TEK 18
