import mysql.connector


def save(predicteddata, Module):
    user = 'cresta' # your username
    passwd = 'cresta' # your password
    host = '10.248.3.91' # your host
    db = 'cresta' # database where your table is stored
    table = 'cresta.save_func' # table you want to save
    table1 = 'cresta.account' # table you want to save
    cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta')
    print Module
    query1 = "update save_func set COUNT="+str(predicteddata)+" where MODULE='"+Module+"'"
      
    try:
        cursor = cnx.cursor()
        cursor.execute(query1)
        cnx.commit()
    finally:
        cnx.close()

