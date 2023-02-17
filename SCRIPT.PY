

def DESICION():
    while True:
        print("\nINPUT Application by Jared and Mou \n")
        print("1. SALES")
        print("2. PRODUCTS")
        print("3. REPORT")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            SALES()
        elif choice == 2:
            PRODUCTS()
        elif choice == 3:
            next()
        else:
            print("Invalid option. Please try again.")

def SALES():
    ID = [] 
    SKU = []
    while True:
        id = input("Ingrese un ID : ")
        sku = input("Ingrese un ID : ")
        END = input("Input the word END (if you want to end introducing products): ")
        if END == 'fin':
            break 
        ID.append(id) 
        SKU.append(sku)
        
