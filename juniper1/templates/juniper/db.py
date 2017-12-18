#!/usr/bin/python
import MySQL
db=MySQL.connect("10.248.3.91","cresta","cresta","cresta_uat")
cursor=db.cursor
cursor.execute("select version()")
print "Database version :%s" %data
db.close()