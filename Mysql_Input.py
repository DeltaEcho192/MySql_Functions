import MySQLdb

def get_ID():
    idL = []
    db = MySQLdb.connect("localhost", "root", "xxmaster", "products")
    cursor = db.cursor()

    sql = "SELECT id FROM product_list"
    try:
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            idL.append(id)

    except:
        print("Error: unable to fecth data")

    print (idL)
    if idL == []:
        idmax1I = 1
    else:
        idmaxI = max(idL)
        idmax1I = idmaxI + 1
        #print(idmaxI)
    db.close()
    return idmax1I

get_ID()


def mysql_input(idI):
    itemS = raw_input("Please enter the Name of the Item.")
    amountS = raw_input("Please enter the Amount")
    minamountS = raw_input("Please enter the minimum Amount")

    db = MySQLdb.connect("localhost", "root", "xxmaster", "Products")

    cursor = db.cursor()

    sql = 'insert into product_list (id, item, amount, minamount) VALUES ("%s","%s","%s", "%s")'% (idI, itemS, amountS, minamountS)

    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print('Data has been Entered into the DataBase')
    except:
        db.rollback()
        print("There has been an error with entering the data.")

    db.close()

id1I = get_ID()
print(id1I)
#print(get_ID())
mysql_input(id1I)
