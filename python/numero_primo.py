# This program search  prime numers 



def f(a):
    c = [2, 3]
    g = a-1
    for i in range(g):
        i=i+1
#        print ("######")   
#        print (i)
#        print ("======")    
        for j in range(g): 
            j = j + 1
#            print (j)
            if i > 3 and j >1:
                b = i / j
                d = b - int(b)
                if d == 0.0:
                    break
                elif d !=  0.0:
                    if j==i-1:
                        c.append(i)
                    else:
                        continue
                    #continue
            else:
                continue
    return c


a = 100000
#b = 2.5-2
d = f(a)
b = len(d)

print (d)

print (b)


with open("Lista.txt","w") as file:
    for i in range(b):
        j = i+1
        file.write('%d  , ' %j )
        file.write(' %d \n' %d[i])
    file.close()






