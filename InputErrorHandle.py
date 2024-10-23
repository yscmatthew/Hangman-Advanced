def ctype(var,type): #can it be convertted into that type?
    if type == 'int':
        try:
            temp = int(var)
            return True
        except ValueError:
            return False
        
print(ctype('0.5','int'))

def boundary(hi,lo,val,inclusive):
    if inclusive == 'incl':
        if (lo<=val<=hi):
            return True
        else:
            return False
    elif inclusive == 'excl':
        if (lo<val<hi):
            return True
        else:
            return False

proceed2 = False
proceed2 = (boundary(5,1,int('4'),'incl'))
print(proceed2)
