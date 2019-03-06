# coding: utf-8
'''
Created on 5 mar. 2019

@author: Juanlu-PC
'''
import statistics as ss
print("Dime el nombre del fichero")
fichero = input() + ".txt"
f = open(fichero,"r") 

fin = False # Variable para controlar fin del bucle
car1 = ""
car2 = ""
car3 = ""
car4 = ""
car5 = ""
listc1 = []
listc2 = []
listc3 = []
listc4 = []
listc5 = []
contador = 0
while contador != 1000: # Bucle para recorrer fichero
    linea = f.readline() # Lectura de una línea
    campo = linea.split(";")
    
    split = campo[0].split(":")
    car1 = split[0]
    listc1.append(int(split[1]))
    
    split = campo[1].split(":")
    car2 = split[0]
    listc2.append(int(split[1]))
    
    split = campo[2].split(":")
    car3 = split[0]
    listc3.append(int(split[1]))
    
    split = campo[3].split(":")
    car4 = split[0]
    listc4.append(int(split[1]))
    
    split = campo[4].split(":")
    car5 = split[0]
    listc5.append(int(split[1]))
    
    contador = contador +1
f.close() # Cerrar

n = 1000

#Medias 
mediaCar1 = round(sum(listc1)*1.0/1000,2)
mediaCar2 = round(sum(listc2)*1.0/1000,2)
mediaCar3 = round(sum(listc3)*1.0/1000,2)
mediaCar4 = round(sum(listc4)*1.0/1000,2)
mediaCar5 = round(sum(listc5)*1.0/1000,2)

#Modas

repetir = 0                                                                         
for i in listc1:                                                                              
    aparece = listc1.count(i)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                                                                                                          
moda = []                                                                               
for i in listc1:                                                                              
    aparece = listc1.count(i)                                                             
    if aparece == repetir and i not in moda:                                   
        moda.append(i) 
        
repetir = 0                                                                         
for i2 in listc2:                                                                              
    aparece = listc2.count(i2)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                                                                                                          
moda = []                                                                               
for i2 in listc2:                                                                              
    aparece = listc2.count(i2)                                                             
    if aparece == repetir and i2 not in moda:                                   
        moda.append(i2) 

repetir = 0                                                                         
for i3 in listc3:                                                                              
    aparece = listc3.count(i3)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                                                                                                          
moda = []                                                                               
for i3 in listc3:                                                                              
    aparece = listc3.count(i3)                                                             
    if aparece == repetir and i3 not in moda:                                   
        moda.append(i3) 

repetir = 0                                                                         
for i4 in listc4:                                                                              
    aparece = listc4.count(i4)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                                                                                                          
moda = []                                                                               
for i4 in listc4:                                                                              
    aparece = listc4.count(i4)                                                             
    if aparece == repetir and i4 not in moda:                                   
        moda.append(i4) 

repetir = 0                                                                         
for i5 in listc5:                                                                              
    aparece = listc5.count(i5)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                                                                                                          
moda = []                                                                               
for i5 in listc5:                                                                              
    aparece = listc5.count(i5)                                                             
    if aparece == repetir and i5 not in moda:                                   
        moda.append(i5) 

modaCar1 = i
modaCar2 = i2
modaCar3 = i3
modaCar4 = i4
modaCar5 = i5

#Varianzas
varCar1 = ss.variance(listc1)
varCar2 = ss.variance(listc2)
varCar3 = ss.variance(listc3)
varCar4 = ss.variance(listc4)
varCar5 = ss.variance(listc5)

#Maximos
maxCar1 = max(listc1)
maxCar2 = max(listc2)
maxCar3 = max(listc3)
maxCar4 = max(listc4)
maxCar5 = max(listc5)

#Minimos

minCar1 = min(listc1)
minCar2 = min(listc2)
minCar3 = min(listc3)
minCar4 = min(listc4)
minCar5 = min(listc5)

print("----------" + car1 + " , " + car2 + " , " + car3 + " , " + car4 + " , " + car5)
print(" Media: " + str(mediaCar1) + " , " + str(mediaCar2) + " , " +  str(mediaCar3) + " , " +  str(mediaCar4) + " , " +  str(mediaCar5))
print(" Moda: " + str(modaCar1) + " , " + str(modaCar2) + " , " +  str(modaCar3) + " , " +  str(modaCar4) + " , " +  str(modaCar5))
print(" Máximos: " + str(maxCar1) + " , " +  str(maxCar2) + " , " +  str(maxCar3) + " , " +  str(maxCar4) + " , " +  str(maxCar5))
print(" Mínimos: " + str(minCar1) + " , " +  str(minCar2) + " , " +  str(minCar3) + " , " +  str(minCar4) + " , " +  str(minCar5))
print(" Varianza: " + str(varCar1) + " , " +  str(varCar2) + " , " +  str(varCar3) + " , " +  str(varCar4) + " , " +  str(varCar5))