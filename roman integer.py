def romaninteger(romaninput):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    resultinteger = 0
    
    for i in range(0, len(romaninput)- 1):
        if roman[romaninput[i]] < roman[romaninput[i+1]]:
            resultinteger -= roman[romaninput[i]]
        else:
            resultinteger += roman[romaninput[i]]
    return resultinteger + roman[romaninput[-1]]

roman = input("Enter a Roman numeral: ")
print(f"Integer equivalent : {romaninteger(roman)}")