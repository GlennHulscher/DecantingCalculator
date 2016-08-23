##############################
#      Decanting calculator  #
#      Runescape OS          #
#      23-8-2016             #
#      Glenn Hulscher        #
##############################

a=float(input("Inkoop (4) potion: "))
b=float(input("Verkoop (3) potion: "))
c=float(input("Inkoop (3) potion: "))
d=float(a*0.75)
e=float(d-b)
print("Koop voor: " + str(c))
print("Verkoop voor: "+ str(a))
print("Marge is: " + str(e))