import MySQLdb

ip_adressS = 'localhost'
usernameS = 'root'
passwordS = 'xxmaster'
db_nameS = 'products'

# Connection to Database.
db = MySQLdb.connect(ip_adressS, usernameS, passwordS, db_nameS)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM product_list"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        item = row[1]
        amount = row[2]
        minamount = row[3]
        # Now print fetched result
        print( "ID=%s, Item=%s, Amount=%s, MinAmount=%s" % \
        (id,item,amount,minamount))

except:
    print("Error: unable to fecth data")

# disconnect from server
db.close()