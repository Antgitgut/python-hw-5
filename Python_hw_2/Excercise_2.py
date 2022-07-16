def transformStr(str):
    if len(str) > 5:
        print(str[:5] + "...")
    elif str[:0] == "U" or "u":
        print(str.upper())
    elif str[:0] == "L" or "l":
        print(str.lower())



transformStr("loq")
