maks = 0
while True:
    a = int(input("masukan bilangan = "))
    if maks < a:
        maks = a
    if a == 0:
         break
print("bilangan terbesarnya adalah = ", maks)