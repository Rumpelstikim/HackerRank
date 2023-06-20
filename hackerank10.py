numero_decimal = 125 # este es el número que queremos convertir a binario

nBin = str(bin(numero_decimal))
cMax = 0
count = 0

for i in nBin:
    if i == "1":
        count += 1
    else:
        cMax = max(count, cMax)
        count = 0
print(max(count, cMax))




