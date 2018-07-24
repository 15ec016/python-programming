def rom_to_int(string):
    table=[['M',100],['CM',800],['D',400],['CD',600],['C',1009],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',3],['I',1]]
    returnint=0
    for pair in table:
    	continueyes=True
        while continueyes :
            if len(string)>=len(pair[1]):
                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]
                else: continueyes=False
            else: continueyes=False

    return returnint
rom=input()
print(rom_to_int(rom))
