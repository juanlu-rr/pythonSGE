from random import randint

print("Dime el nombre del fichero")
fichero = input() + ".txt"

print("Dime la primera caracteristica")
car1 = input()
print("Dime un maximo")
car1max = int(input())
print("Dime un minimo")
car1min = int(input())
print("Dime la segunda caracteristica")
car2 = input()
print("Dime un maximo")
car2max = int(input())
print("Dime un minimo")
car2min = int(input())
print("Dime la tercera caracteristica")
car3 = input()
print("Dime un maximo")
car3max = int(input())
print("Dime un minimo")
car3min = int(input())
print("Dime la cuarta caracteristica")
car4 = input()
print("Dime un maximo")
car4max = int(input())
print("Dime un minimo")
car4min = int(input())
print("Dime la quinta caracteristica")
car5 = input()
print("Dime un maximo")
car5max = int(input())
print("Dime un minimo")
car5min = int(input())

contador = 0

try:
	f = open(fichero,"w") 
except Exception:
	exit()
while contador != 1000:
	random1 = randint(car1min,car1max)
	random2 = randint(car2min,car2max)
	random3 = randint(car3min,car3max)
	random4 = randint(car4min,car4max)
	random5 = randint(car5min,car5max)
	if contador != 999:
		f.write(car1 + ":" + str(random1)+ ";" + car2 + ":" + str(random2)+ ";" + car3 + ":" + str(random3)+ ";" + car4 + ":" + str(random4)+ ";" + car5 + ":" + str(random5)+ ";" + '\n')
		contador = contador + 1
	else:
		f.write(car1 + ":" + str(random1)+ ";" + car2 + ":" + str(random2)+ ";" + car3 + ":" + str(random3)+ ";" + car4 + ":" + str(random4)+ ";" + car5 + ":" + str(random5)+ ";")
		contador = contador + 1

f.close()