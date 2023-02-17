OrderNumber = []
Date = []
Products = []
Amount  = []
Subtotal = []
Total = []
TypeOfPayment = []
BILL = []


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
    while True:
        print("\nSales Application by Jared and Mou \n")
        print("1. Add products")
        print("2. See stock")
        print("3. Create Sale")
        print("4. View Sale")
        print("5.Go to sales")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ID = input("Enter id roduct : ")
            SKU = (input("Enter de sku"))
            ProductName = (input("Enter the product name :"))
            ProductPresentation = (input("Enter the product presentation: "))
            Laboratory  = (input("Enter the product Laboratory: "))
            Stock = (input("Enter de # : "))

            
            add_product(product, price, stock_level)
        elif choice == 2:
            see_stock()
        elif choice == 3:
            product = input("Enter the product name: ")
            quantity = int(input("Enter the quantity: "))
            create_sale(product, quantity)
        elif choice == 4:
            view_sale()
        elif choice == 5:
            exit_program()
        else:
            print("Invalid option. Please try again.")            
def PRODUCTS():
    while True:
        print("\nINPUT Application by Jared and Mou \n")
        print("1. Add products")
        print("2. See stock")
        print("3. Create Sale")
        print("4. View Sale")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ID = input("Enter id roduct : ")
            SKU = (input("Enter de sku"))
            ProductName = (input("Enter the product name :"))
            ProductPresentation = (input("Enter the product presentation: "))
            Laboratory  = (input("Enter the product Laboratory: "))
            Stock = (input("Enter de # : "))

            
            add_product(product, price, stock_level)
        elif choice == 2:
            see_stock()
        elif choice == 3:
            product = input("Enter the product name: ")
            quantity = int(input("Enter the quantity: "))
            create_sale(product, quantity)
        elif choice == 4:
            view_sale()
        elif choice == 5:
            exit_program()
        else:
            print("Invalid option. Please try again.")

def NEXT():
    while True:
        print("\nINPUT Application by Jared and Mou \n")
        print("1. Add products")
        print("2. See stock")
        print("3. Create Sale")
        print("4. View Sale")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ID = input("Enter id roduct : ")
            SKU = (input("Enter de sku"))
            ProductName = (input("Enter the product name :"))
            ProductPresentation = (input("Enter the product presentation: "))
            Laboratory  = (input("Enter the product Laboratory: "))
            Stock = (input("Enter de # : "))

            
            add_product(product, price, stock_level)
        elif choice == 2:
            see_stock()
        elif choice == 3:
            product = input("Enter the product name: ")
            quantity = int(input("Enter the quantity: "))
            create_sale(product, quantity)
        elif choice == 4:
            view_sale()
        elif choice == 5:
            exit_program()
        else:
            print("Invalid option. Please try again.")