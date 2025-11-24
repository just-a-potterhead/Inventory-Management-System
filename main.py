import csv
import time
try :
    invent = open("inventory.csv","a")
    invent.close()
except FileNotFoundError:
    invent = open("inventory.csv",'w')
    invent.close()

def project():
    try:
        invent = open("inventory.csv",'r')
    except FileNotFoundError :
        return FileNotFoundError
    fileReader = csv.reader(invent)
    for i in fileReader:
        print(f"\n{i[2]} {i[0].upper()} left of brand {i[1].upper()}\nPer piece price of {i[0].upper()} is {i[3]}\n")
    
    print("\n\n")
    
    
def write(inventory):
    invent = open("inventory.csv",'a')
    writer = csv.writer(invent)
    writer.writerow(inventory)
    invent.close
    return "FLAG_SUCCESS"

def insert():
    print("Adding new item")
    item_name = input("Enter the item name : ")
    item_brand = input("Enter the item brand : ")
    item_stock = int(input("Enter the stock left : "))
    if item_stock < 1:
        print("Minimum stock quantity to be added is 1")
        return 0
    cost = float(input("Enter the item cost : "))
    inventory = [item_name.lower(), item_brand.lower(), item_stock, cost]
    x = write(inventory)
    if x.lower() == "flag_success":
        print("Data successfully inserted")
        return 1

def stockextend(reader, i, index):
    x = int(input("Enter the new quantity : "))  
    if len(i) < 0 :
        print("Invalid value for stock.")
        stockextend(i)
    i[2] = x
    j = 0
    vallist = list()
    value = list()
    for z in reader:
        if j == index:
            vallist.append(i)
        else:
            vallist.append(z)
        value.append(vallist)

        j += 1
    print(vallist)
    print("Success")
    return vallist

def update():
    item_name = input("Enter the item name : ")
    item_brand = input("Enter the item brand : ")
    flag = False
    index = 0
    file_path = 'inventory.csv'
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        vallist = list(row for row in csv_reader)  
        for row in vallist:
            if row[0] == item_name.lower() and item_brand.lower() == row[1]:
                print(j for j in row)
                flag = True
                break
            index += 1
    if flag == True:
        print("Current Stock : ", row[2])
        value = stockextend(vallist, row, index)
        csvfile.close()
        invent = open("inventory.csv",'w')
        writer = csv.writer(invent)
        writer.writerows(value)
        print("Write success")
    else:
        print("Item not found!")

def menu():
    print("MENU\n\n\n")
    print("1 : INSERT AN ITEM")
    print("2 : UPDATE THE QUANTITY")
    print("3 : SHOW THE REMAINING QUANTITY")
    print("0 : Exit")
    print("9 : View this menu")
    print("\n\n\n")

def choice():
    x = int(input("Enter your choice [0/1/2/3/4/9]: "))
    if x == 0:
        print("Thank you for using our software")
        exit()
    elif x == 1:
        insert()
        time.sleep(1)
        print("\n\n\n")
        choice()
    elif x == 2:
        update()
    elif x == 3 :
        project()
    elif x == 9:
        menu()
    else :
        print("The choice you entered does not exist. Re-enter your choice")
        choice()

if "__main__" :
    while True:
        menu()
        choice()