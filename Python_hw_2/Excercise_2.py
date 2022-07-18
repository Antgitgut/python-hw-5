def transformStr(str):
    if len(str) > 5:
        print(str[:5] + "...")
    elif str[0] in ["L", "l"]:
        print(str.lower())
    elif str[0] in ["U", "u"]:
        print(str.upper())
    else:
        print(str[:5])





transformStr("posds")
