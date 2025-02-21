



def func1(sir):    #eliminare semne de punctuatie
    semne_de_punctuatie = [".", ",", "!", "?", ":", ";", "-", "(", ")", '”', '“']
    for i in range(0, len(semne_de_punctuatie)):
        sir = sir.replace(semne_de_punctuatie[i], "")
    return sir



def func2(sir):     #Eliminca cifrele din sir
    str=""
    for char in sir:
        if not char.isdigit():
            str = str + char
    return str

def func3(sir):     #SWAPCASE
    str=""
    str=sir.swapcase()
    return str


def main():

    str=""

    f = open("file.txt", "r" )

    sir = f.read()
    str = func1(sir)
    str = func2(str)
    str = func3(str)

    print(str)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


