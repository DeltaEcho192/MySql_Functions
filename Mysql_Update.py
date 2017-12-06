import MySQLdb

def Get_Var_Names():
    condition1 = str(raw_input("Please enter the column name of what you want to change. "))
    condition2 = "='"
    condition3 = str(raw_input("Please enter the new value. "))
    condition4 = "'"
    condition5 = str(raw_input("Please enter the name of the Product you want to change. "))
    condition6 = str(raw_input("Please enter the Value of which product you want to change."))

    finalstring1 = condition1 + condition2 + condition3 + condition4
    finalstring2 = condition5 + condition2 + condition6 + condition4

    return finalstring1,finalstring2



def Mysql_Update(condition1, condition2):
    ip_adressS = 'localhost'
    usernameS = 'root'
    passwordS = 'xxmaster'
    db_nameS = 'Products'
    tablename = 'product_list'
    # Connection to Database.
    db = MySQLdb.connect(ip_adressS, usernameS, passwordS, db_nameS)

    cursor = db.cursor()


    print(condition1,condition2)
    # The SQL Code Needed.
    sql = "UPDATE {0} SET {1} WHERE {2}".format(tablename,condition1,condition2)

    print(sql)

    try:
        cursor.execute(sql)
        db.commit()
        print("Command has been executed")
    except:
        print("The Command did not go through.")

    db.close()


varnames = Get_Var_Names()
condition1 = varnames[0]
condition2 = varnames[1]

Mysql_Update(condition1,condition2)