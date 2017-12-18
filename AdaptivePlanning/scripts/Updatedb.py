import xlrd



def fun1 ():

 file=r'E:\Aspire\New folder\juniper\juniper\AdaptivePlanning\scripts\UC4_Data.xlsx'
 book = xlrd.open_workbook(file)
 sheet = book.sheet_by_name("UC4_Data")
 SR_ID=[]
 for r in range(1, sheet.nrows):

  SR_ID.append(sheet.cell(r,0).value)
  USER_ID = sheet.cell(r,1).value
 PRED_CODE = sheet.cell(r,2).value
 DEFECT_COUNT = sheet.cell(r,3).value
 TEST_CASE_COUNT = sheet.cell(r,4).value
 APPLICATION_COMPLEXITY = sheet.cell(r,5).value
 DOMAIN_KNOWLEDGE = sheet.cell(r,6).value
 TECHNICAL_SKILLS = sheet.cell(r,7).value
 REQUIREMENTS_QUERY_COUNTS = sheet.cell(r,8).value
 REL_ID = sheet.cell(r,9).value
 SEVERITY = sheet.cell(r,10).value
 MODULE_NAME = sheet.cell(r,11).value
 
 values = (SR_ID,USER_ID,PRED_CODE,DEFECT_COUNT,TEST_CASE_COUNT,APPLICATION_COMPLEXITY,DOMAIN_KNOWLEDGE,TECHNICAL_SKILLS,REQUIREMENTS_QUERY_COUNTS,REL_ID,SEVERITY,MODULE_NAME)
 
 print (SR_ID)
 return SR_ID







