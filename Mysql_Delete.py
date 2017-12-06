import MySQLdb


def Mysql_Delete():
    ip_adressS = 'localhost'
    usernameS = 'root'
    passwordS = 'xxmaster'
    db_nameS = 'Products'

    #Connection to Database.
    db = MySQLdb.connect(ip_adressS,usernameS,passwordS,db_nameS)

    cursor = db.cursor()

    condition1 = str(raw_input("Please Enter Column."))
    condition2 = "='"
    condition3 = str(raw_input("Please Enter the Parameter."))
    condition4 = "'"
    condition5 = condition1 + condition2 + condition3 + condition4

    #The SQL Code Needed.
    sql = "DELETE FROM product_list WHERE %s" % (condition5)

    try:
        cursor.execute(sql)
        db.commit()
        print("Command has been executed")
    except:
        print("The Command did not go through.")

    db.close()

Mysql_Delete()