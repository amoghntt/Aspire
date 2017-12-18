import xlrd    #import xlrd module to read Excel Files
import string
#import readrequirement
from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
from string import digits
from django.conf import settings
import os
import nltk
nltk.data.path.append("/home/aspire/nltk_data/nltk_data");
from nltk.corpus import stopwords



testCaseId = []
stop_words = set(stopwords.words("english"))
def stopwords(corpora_lan):
   from nltk.corpus import stopwords
   if( corpora_lan==1 ):
      stop_words = set(stopwords.words("english"))
      print('english')
   elif( corpora_lan==2 ):
      stop_words = set(stopwords.words("german"))
      print('german')
   elif( corpora_lan==3 ):
      stop_words = set(stopwords.words("spanish"))
      print('spanish')

def preProcessString( sentence ):
   "This function returns the preprocessed string"
   processed_sentence = [j for j in sentence.lower().split() if j not in stop_words]
   untokenized_sentence =   "".join([" "+j if not j.startswith("'") and j not in string.punctuation else j for j in processed_sentence]).strip()
   untokenized_sentence1 = untokenized_sentence.translate(None)
   return untokenized_sentence1



def readTestCasesFromExcelFile(file_name):
	"This function reads testcases from excel file and writes it to text file"
	#workbook = xlrd.open_workbook('TestData1.xlsx')  #open workbook or Excel file
	test_ref=[]
	workbook = xlrd.open_workbook(os.path.join(settings.PROJECT_ROOT, 'media/testcases/'+file_name))
	#stopwords("english")
	#stop_words = set(stopwords.words("english"))
	print("english")
        pointSheets = workbook.sheet_names()
        print("english")
        listTestSheetNames = ['test_case', 'Test_Cases', 'test-cases','test-case','Test-Cases','Test_Case','Test Cases']
        sheetName = None
        print("english")
        for i in listTestSheetNames:
           if(i in pointSheets):

              sheetName = i

        #print(corpora_lan)      
	sheet = workbook.sheet_by_name(sheetName) #open workdsheet by name
	#initialize parameters for reading
	num_rows = sheet.nrows #gets the total number of rows in sheet
	num_cols = sheet.ncols  #gets the total number of columns in sheet
        g = globals()   #declare a global variable to create lists dynamically
	i = 0
	offsetRowIndex = None      #set offset from where you can start reading. Set offset = 1 to skip headers
	testStepColumnIndex = None #index value of test step column
        testCaseColumnIndex = None
        testCaseIDColumnIndex = None
        testCaseDescriptionColumnIndex = None
        testRefColumnIndex=None
        listValuesToBeSearched = ['Test Scenario','Test Case Description','Test Description','Test Case','Description','Test Step','Expected Results','Actual Results']
	count = 0
	rowNumberHeader = None
#	print(corpora_lan)
	for rownum1 in range(num_rows):
           row =  sheet.row(rownum1)
           for colnum1 in range(num_cols):
              if(row[colnum1].value in listValuesToBeSearched):
                 count = count + 1
              if(count >=3):
                 rowNumberHeader = rownum1
                 break
	   else:
              continue
           break
#        print(corpora_lan)    
      	listTestSteps =['Test Steps', 'Steps', 'Test Step']
        listTestCase = ['Test Case', 'Test Cases']
        listTestDescription = ['Test Description', 'Test Case Description', 'Description']
        listTestCaseId = ['Test ID', 'Test Reference ID', 'Test Case Number']
        listTestRef=['Test Case Reference ID']
        print 1
	for colnum in range(num_cols):
           if sheet.cell(rowNumberHeader, colnum).value in listTestDescription:
              testCaseDescriptionColumnIndex = colnum
           if sheet.cell(rowNumberHeader, colnum).value in listTestSteps:
              testStepColumnIndex = colnum
           if sheet.cell(rowNumberHeader, colnum).value in listTestCaseId:
              testCaseIDColumnIndex = colnum
           if sheet.cell(rowNumberHeader, colnum).value in listTestCase:
              testCaseColumnIndex = colnum
              offsetRowIndex = rowNumberHeader + 1
           if sheet.cell(rowNumberHeader, colnum).value in listTestRef:
              testRefColumnIndex = colnum
              print('haiiiii')
              offsetRowIndex = rowNumberHeader + 1

    
	for rownum in range(offsetRowIndex,num_rows): 
		if sheet.cell(rownum, testStepColumnIndex).value == 1:    #check if test case step is equal to 1, if yes then create a new list and append values to it.
                        i = i + 1
			g['depth_{0}'.format(i)] = []
			
			for colnum1 in range(num_cols) :
				if sheet.cell_type(rownum, colnum1) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK): #check if cell is empty, if not then append it to list
                                    if (colnum1 == testCaseIDColumnIndex):
                                       sentence = sheet.cell(rownum, colnum1).value
                                       stringSentence = sentence.encode('ascii','ignore')
                                       global testCaseId
                                       print 1
                                       testCaseId.append(stringSentence)
                                   
                                    elif (colnum1 == testCaseColumnIndex) or (colnum1 == testCaseDescriptionColumnIndex):
                                       sentence = sheet.cell(rownum, colnum1).value
				       stringSentence = sentence.encode('ascii','ignore')
				       punctuation_sentence = stringSentence.translate(None, string.punctuation)
                                       preprocessed_sentence = preProcessString( punctuation_sentence)
                                       g['depth_{0}'.format(i)].append(preprocessed_sentence)
				       #g['depth_{0}'.format(i)].append(punctuation_sentence)

                                    if (colnum1 == testRefColumnIndex ):
                                       sentence = sheet.cell(rownum, colnum1).value
				       #stringSentence = sentence.encode('ascii','ignore')
				       #punctuation_sentence = stringSentence.translate(None, string.punctuation)
                                       print 'hello'    #preprocessed_sentence = preProcessString( punctuation_sentence)
                                       test_ref.append(sentence)
				       #g['depth_{0}'.format(i)].append(sentence )

                                       
				    
		elif sheet.cell(rownum, testStepColumnIndex).value > 1:
                        for colnum1 in range(num_cols) :
				if sheet.cell_type(rownum, colnum1) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK): #check if cell is empty, if not then append it to list
                                       if (colnum1 == testCaseColumnIndex)or (colnum1 == testCaseDescriptionColumnIndex):
                                          sentence = sheet.cell(rownum, colnum1).value
					  stringSentence = sentence.encode('ascii','ignore')
					  punctuation_sentence = stringSentence.translate(None, string.punctuation)
                                          preprocessed_sentence = preProcessString( punctuation_sentence)
                                          g['depth_{0}'.format(i)].append(preprocessed_sentence)
					  #g['depth_{0}'.format(i)].append(punctuation_sentence)

										 

	#Loop to write all dynamically created Lists to text file
	thefile = open('/home/aspire/client/juniper/juniper1/static/juniper/documents/opt/textrequirementprocessed.txt', 'w')
	#thefile = open(os.path.join(settings.PROJECT_ROOT, 'media/opt/textrequirementprocessed.txt'), 'a')
	thefile.truncate()
	k = i
	index = 1
	list_string = "List_"
	while index <= k :
		#thefile.write("\n ")
		for item in g['depth_{0}'.format(index)]:
			thefile.write(item)
			thefile.write(" ")
		index = index + 1
		if(index <= k):
                   thefile.write("\n ")
		
        return test_ref

#print readTestCasesFromExcelFile()
