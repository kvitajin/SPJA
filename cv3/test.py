#ZDE DOPLNTE FUNKCE

def add_line_numbers(name):
    file=open(name, "r")
    line=file.readlines()
    file.close()
    jmeno='n_'+name
    pis=None
    try:
        pis=open(jmeno, "wt")
    except:
        print("nejde to")
    finally:
        if pis is not None:
            for i, radek in enumerate(line):
                go=str(i)+ ' '+radek
                pis.write(go)

def my_map(func, seq):
    ret = []
    for item in seq:
        ret.append(func(item))
    return ret

def my_filtered_map(list, x, **kw):
    tmp=[i for i in list if (type(i) == float) or (type(i) == int)]

def bank_account(*kw):
    accouns={}
    for i in kw:
        file=open(i,"rt")
        lines=file.readlines()
        for j in lines:
            tmp=j.split()
            if (tmp[1]=='D'):
                accouns[tmp[0]]
                accouns[tmp[0]]+=int(tmp[2])
            elif(tmp[1]=='W'):
                accouns[tmp[0]]
                accouns[tmp[0]]-=int(tmp[2])
        # print(accouns)

        file.close()
    # print(accouns)
    return accouns





#ZDE ODKOMENTUJTE FUNKCE A DOPLNTE LAMBDA FUNKCI

add_line_numbers("text.txt")

#print(my_filtered_map([1,2,3,"x",5,8,13], your_lambda_function, min=5, max=20))
#print(my_filtered_map([True,-2.2,-1,0,1,2], your_lambda_function, max=0))

print(bank_account("bank_01.txt", "bank_02.txt"))
