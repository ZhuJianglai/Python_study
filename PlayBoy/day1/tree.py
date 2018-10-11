# author：zhu


def f_d(filepath,forname):
    f=open(filepath,'r')
    lines=f.readline()
    while lines:
        line = lines.split(',')
        pro = line[0]
        city = line[1]
        park = line[2].strip()
        if pro == forname:
            print('city:',city,'park:',park)
        elif city == forname:
            print('park:',park)
        elif park == forname:
            print('prc:',pro,'city:',city)
        lines = f.readline()







    # while lines:
    #     line=lines.split(',')
    #     pro=line[0]
    #     city=line[1]
    #     park=line[2].strip()
    #     if pro==forname:
    #         print(city,park)
    #     elif city==forname:
    #         print(park)
    #     else:
    #         print(pro,city)
    #     lines=f.readline()
    # f.close()






name =input("please input name:")
f_d('tree.txt',name)
