metn=input()
luget=dict()
for herf in metn:
    if herf in luget:
        luget[herf]+=1
    else:
        luget[herf]=1
for herf,say in luget.items():
    print(herf,say)
