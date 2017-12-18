from xlsxwriter.workbook import Workbook
#import MySQLdb
import os
from django.conf import settings
import mysql.connector 

def export_users_xlsx(request):
    #workbook = Workbook(os.path.join(settings.PROJECT_ROOT, 'media\\Saved_Results.xlsx'))
    workbook = Workbook("/home/aspire/client/juniper/juniper1/static/juniper/documents/Saved_Results.xlsx")
    worksheet = workbook.add_worksheet('test')
    
    
    format1 = workbook.add_format()
    format1.set_font_size(14)
    format1.set_pattern(1) 
    format1.set_bg_color('green')
    format1.set_bold()
    
    format2 = workbook.add_format()
    format2.set_border(1)
    format2.set_font_size(12)
    format2.set_bg_color('red')
    format2.set_bold()
    
    format3 = workbook.add_format()
    format3.set_border(1)
    
    
    
    user = 'cresta' # your username
    passwd = 'cresta' # your password
    host = '10.248.3.91' # your host
    db = 'cresta' # database where your table is stored
    table = 'cresta.save_func' # table you want to save
    table1 = 'cresta.account' # table you want to save

    con = mysql.connector.connect(user=user, passwd=passwd, host=host, db=db)
    cursor = con.cursor()
    query = "SELECT * FROM save_func"
    cursor.execute(query)
    data=list(cursor.fetchall())
    print data
    length=len(data)
    worksheet.set_column('B:B', 20)
    worksheet.merge_range('B7:C7','PREDICTION ANALYSIS',format1)
    worksheet.write('B8','MODULE', format2)
    worksheet.write('C8','VALUE', format2)
    i=8
    j=1
    k=2
    for module,value in data:
        worksheet.write(i, j, module,format3)
        worksheet.write(i, k, value,format3)
        i=i+1
        
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({'categories': '=test!$B$9:$B$13', 'values': '=test!$C$9:$C$13'})
    chart.set_title({'name': 'Prediction count'})
    worksheet.insert_chart('F4', chart)


    
    worksheet1 = workbook.add_worksheet('account')
    con1 = mysql.connector.connect(user=user, passwd=passwd, host=host, db=db)
    cursor = con1.cursor()
    query1 = "SELECT * FROM account"
    cursor.execute(query1)
    data1=list(cursor.fetchall())
    print data1
    length=len(data1)

    worksheet1.set_column('B:B', 16)
    worksheet1.merge_range('B7:C7','QUALITY PREDICTION',format1)
    worksheet1.write('B8','PROJECT', format2)
    worksheet1.write('C8','COUNT', format2)
    i1=8
    j1=1
    k1=2
    for project,count in data1:
        worksheet1.write(i1, j1, project,format3)
        worksheet1.write(i1, k1, count,format3)
        i1=i1+1



    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({'categories': '=account!$B$9:$B$13', 'values': '=account!$C$9:$C$13'})
    worksheet1.insert_chart('F3', chart1, {'x_offset': 35, 'y_offset': 15})
    chart1.set_title({'name': 'Quality Prediction project wise'})

    workbook.close()
    
#export_users_xlsx('hi')

