 # programa para verificar cual de los dos numeros es enteros es el mayor 

print("-----------------------------------")
print("------------- MAYOR 2 ENTEROS------")
print("-----------------------------------")

 # imput 
x= int(input("digite el valor de x: "))
y= int(input("digite el valor de y: "))

#processing 
if x == y: 
     # output
    print("los numeros son iguales...")
else: 
    if x > y:
         mayor = x 
    else:
        mayor = y 
# output
print("El mayor entre " + str [x] + " y " + str(mayor))
