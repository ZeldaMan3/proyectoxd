
print("Eres gei?")
res= input()
if (res == "no"):
    print("Seguro?")
    res2 =input()
    if (res2 == "si"):
        print("Ya lo sabia")
    while (res2 == "no"):
        print("Vuelve a intentarlo")
        print("Seguro?")
        res2 = input()


if(res == "si" or res2 == "si"):
    print("Ya lo sabia")

