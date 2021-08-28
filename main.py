# My custom functions
import Util.functions

#Scelta dell'azione
AutomaticFollow = str(input("Automatic follow Y o N: "))
RemoveFollow = str(input("Remove follow Y o N: "))

#Followers Automatici
if(AutomaticFollow == "Y" or AutomaticFollow == "y"):
    NumberofNew = str(input("Quante persone vuoi seguire ?: "))
    numberInt = int(NumberofNew)
    Util.functions.AutFollow(round(numberInt/5) + 1, numberInt)
if(RemoveFollow == "Y" or RemoveFollow == "y"): 
    NumberofRem = str(input("Quante persone vuoi rimuovere ?: "))
    numberrem = int(NumberofRem)
    Util.functions.RemoveFollow(round(numberrem/5) + 1 , numberrem)
