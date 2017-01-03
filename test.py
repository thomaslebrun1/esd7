ma_liste = ["-","2","3",".","2","1"]
print (ma_liste)
var = ""
for elt in ma_liste:
    print elt
    var=var+elt
    print var
    calc= eval(var)
    print calc
    calc= calc*2
    print calc