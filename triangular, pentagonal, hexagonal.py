same = False
x = 40757
while same == False:
    for i in range(40756,x):
        triangular = (i*(i+1))//2
        print(triangular)
        for j in range(1,triangular):
            if (j*((3*j)-1))//2 == triangular:
                for k in range(1,triangular):
                    if k*((2*k)-1) == triangular:
                        same = True
        x += 1