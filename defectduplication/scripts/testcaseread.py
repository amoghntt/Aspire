import xlrd    #import xlrd module to read Excel Files
import string
#import readrequirement
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import digits
from django.conf import settings
import os


testCaseId = []
DefectId=[]
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
   untokenized_sentence1 = untokenized_sentence.translate(None, digits)
   return untokenized_sentence1



def readTestCasesFromExcelFile( corpora_lan ):
	"This function reads testcases from excel file and writes it to text file"
	workbook = xlrd.open_workbook('/home/aspire/client/juniper/juniper/media/Book2.xlsm')  #open workbook or Excel file
	#workbook = xlrd.open_workbook(os.path.join(settings.PROJECT_ROOT, 'media\\test-case.xlsm'))
	stopwords(corpora_lan)
	print(corpora_lan)
        pointSheets = workbook.sheet_names()
        listTestSheetNames = ['test_case', 'Test_Cases', 'Data','test-case','Test-Cases','Test_Case','Test Cases']
        sheetName = None
        for i in listTestSheetNames:
           if(i in pointSheets):
              sheetName = i
	sheet = workbook.sheet_by_name(sheetName) #open workdsheet by name
	#initialize parameters for reading
	num_rows = sheet.nrows #gets the total number of rows in sheet
	num_cols = sheet.ncols  #gets the total number of columns in sheet
        g = globals()   #declare a global variable to create lists dynamically
	i = 0
	offsetRowIndex = 0     #set offset from where you can start reading. Set offset = 1 to skip headers
	DefectIDColumnIndex = None #index value of test step column
        testCaseColumnIndex = None
        DefectSummaryIDColumnIndex = None
        testCaseDescriptionColumnIndex = None
        listValuesToBeSearched = ['Summary','Test Case','Description']
	count = 0
	rowNumberHeader =0
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
            
      	DefectcolID =['DefectID', 'Steps', 'Test Step']
        listDefectSummary = ['Summary', 'Test Cases']
        listTestDescription = ['Description', 'Test Case Description', ]
        #listTestCaseId = ['Test ID', 'Test Reference ID', 'Test Case Number']
	for colnum in range(num_cols):
           #print rowNumberHeader,colnum
           #print sheet.cell(rowNumberHeader, colnum).value
           if (sheet.cell(rowNumberHeader, colnum).value in listTestDescription):
              testCaseDescriptionColumnIndex = colnum
              #offsetRowIndex = rowNumberHeader + 1
             
           #if sheet.cell(rowNumberHeader, colnum).value in listTestSteps:
           #   testStepColumnIndex = colnum
           if (sheet.cell(rowNumberHeader, colnum).value in listDefectSummary):
              DefectSummaryIDColumnIndex = colnum
              #offsetRowIndex = rowNumberHeader + 1
              
              print offsetRowIndex
           if sheet.cell(rowNumberHeader, colnum).value in DefectcolID:
               DefectIDColumnIndex = colnum
               offsetRowIndex = rowNumberHeader + 1

        print DefectSummaryIDColumnIndex
        print testCaseDescriptionColumnIndex
	for rownum in range(offsetRowIndex,num_rows): 
		#if sheet.cell(rownum, DefectIDColumnIndex).value == 1:    #check if test case step is equal to 1, if yes then create a new list and append values to it.
               i = i + 1
	       g['depth_{0}'.format(i)] = []
			
	       for colnum1 in range(num_cols) :
			   if sheet.cell_type(rownum, colnum1) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK): #check if cell is empty, if not then append it to list
                                 if (colnum1 == DefectIDColumnIndex):
                                       sentence = str(sheet.cell(rownum, colnum1).value)
                                       #print type(sentence)
                                       stringSentence = sentence.encode('ascii','ignore')
                                       global DefectId
                                       DefectId.append(stringSentence)
                                   
                                 elif (colnum1 == testCaseDescriptionColumnIndex) or (colnum1 == testCaseDescriptionColumnIndex):
                                       sentence = sheet.cell(rownum, colnum1).value
                                       print rownum,colnum1
				       stringSentence = sentence.encode('ascii','ignore')
				       punctuation_sentence = stringSentence.translate(None, string.punctuation)
                                       preprocessed_sentence = preProcessString( punctuation_sentence)
                                       g['depth_{0}'.format(i)].append(preprocessed_sentence)
                                       print g['depth_{0}'.format(i)] 
                                       
				    
	       if sheet.cell(rownum, DefectIDColumnIndex).value > 0:
                        g['depth_{0}'.format(i)] = []
                        for colnum1 in range(num_cols) :
				if sheet.cell_type(rownum, colnum1) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK): #check if cell is empty, if not then append it to list
                                       #if (colnum1 == DefectSummaryIDColumnIndex)or (colnum1 == testCaseDescriptionColumnIndex):
                                       if (colnum1 == testCaseDescriptionColumnIndex)or (colnum1 == testCaseDescriptionColumnIndex):   
                                          sentence2 = sheet.cell(rownum, testCaseDescriptionColumnIndex).value
                                          sentence1 = sheet.cell(rownum, DefectSummaryIDColumnIndex).value
                                          sentence=sentence1+sentence2
                                          
                                          print sentence
                                          print colnum1
					  stringSentence = sentence.encode('ascii','ignore')
					  punctuation_sentence = stringSentence.translate(None, string.punctuation)
                                          preprocessed_sentence = preProcessString( punctuation_sentence)
                                          g['depth_{0}'.format(i)].append(preprocessed_sentence)
                                          print g['depth_{0}'.format(i)]

										 
               
              
	#Loop to write all dynamically created Lists to text file
	thefile = open('/home/aspire/client/juniper/juniper/media/textrequirementprocessed.txt', 'w')
	#thefile = open(os.path.join(settings.PROJECT_ROOT, 'media\\textrequirementprocessed.txt'), 'a')
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
	print "yes"
	print DefectId
        return DefectId
