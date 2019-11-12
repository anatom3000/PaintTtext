def just8bits(binstr):
    while len(binstr) < 8:
        binstr = "0" + binstr[0:]
    return binstr
    
def encoder(string):
    string = "\x02" + string[0:] + "\x03"
    val_final = str()
    for i in string:
        val_final += just8bits(bin(ord(i))[2:])
    return val_final
    
i = encoder(input("Texte... "))
print(i)

#nb 7/11/2019: c a adapter pour l'interface graphique
