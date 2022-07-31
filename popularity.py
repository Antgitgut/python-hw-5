def popularity(text):
    S = str(text)
    Lo = S.lower()
    Sp = Lo.split()


    De = sorted(set(Sp), key=lambda i: Sp.count(i), reverse=True)


    #Ss = sorted(set(Sp), key=lambda i: Sp.count(i), reverse=True)

    #Ns = sorted(set(Sp), key=lambda i: Sp.count(i), reverse=True)


    #res = sorted(set(Sp), key=lambda i: Sp.count(i), reverse=True)
    #print(res)


popularity('ana ana y lodz lodz y y y')
