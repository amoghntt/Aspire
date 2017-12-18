import xlrd    #import xlrd module to read Excel Files
import string
import readrequirement
from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
from string import digits
import nltk
nltk.data.path.append("/home/aspire/nltk_data/nltk_data");
from nltk.corpus import stopwords

testCaseId = []
stop_words = set(stopwords.words("english"))

def preProcessString( sentence ):
   "This function returns the preprocessed string"
   processed_sentence = [j for j in sentence.lower().split() if j not in stop_words]
   untokenized_sentence =   "".join([" "+j if not j.startswith("'") and j not in string.punctuation else j for j in processed_sentence]).strip()
   untokenized_sentence1 = untokenized_sentence.translate(None, digits)
   return untokenized_sentence1



def readTestCasesFromExcelFile():
        print ("$$$$$$")
	"This function reads testcases from excel file and writes it to text file"
	workbook = xlrd.open_workbook('/home/aspire/client/juniper/juniper/media/test-case.xlsm')  #open workbook or Excel file
        pointSheets = workbook.sheet_names()
        listTestSheetNames = ['test_case', 'Test_Cases', 'test-cases','test-case','Test-Cases','Test_Case','Test Cases']
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
	offsetRowIndex = None      #set offset from where you can start reading. Set offset = 1 to skip headers
	testStepColumnIndex = None #index value of test step column
        testCaseColumnIndex = None
        testCaseIDColumnIndex = None
        testCaseDescriptionColumnIndex = None
        listValuesToBeSearched = ['Test Scenario','Test Case Description','Test Description','Test Case','Description','Test Step','Expected Results','Actual Results']
	count = 0
	rowNumberHeader = None
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
            
      	listTestSteps =['Test Steps', 'Steps', 'Test Step']
        listTestCase = ['Test Case', 'Test Cases']
        listTestDescription = ['Test Description', 'Test Case Description', 'Description']
        listTestCaseId = ['Test ID', 'Test Reference ID', 'Test Case Number','Test Case Reference ID']
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

    
	for rownum in range(offsetRowIndex,num_rows): 
		if sheet.cell(rownum, testStepColumnIndex).value == 1:    #check if test case step is equal to 1, if yes then create a new list and append values to it.
                        i = i + 1
			g['depth_{0}'.format(i)] = []
			
			for colnum1 in range(num_cols) :
				if sheet.cell_type(rownum, colnum1) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK): #check if cell is empty, if not then append it to list
                                    if (colnum1 == testCaseIDColumnIndex):
                                       sentence = int(sheet.cell(rownum, colnum1).value.strip('TC'))
                                       #stringSentence = sentence.encode('ascii','ignore')
                                       global testCaseId
                                       testCaseId.append(sentence)
                                   
                                    elif (colnum1 == testCaseColumnIndex) or (colnum1 == testCaseDescriptionColumnIndex):
                                       sentence = sheet.cell(rownum, colnum1).value
				       stringSentence = sentence.encode('ascii','ignore')
				       punctuation_sentence = stringSentence.translate(None, string.punctuation)
                                       preprocessed_sentence = preProcessString( punctuation_sentence)
                                       g['depth_{0}'.format(i)].append(preprocessed_sentence)

                                       
				    
		elif sheet.cell(rownum, testStepColumnIndex).value > 1:
                        for colnum1 in range(num_cols) :
				if sheet.cell_type(rownum, colnum1) not in (xlrd.XL_CELL_EMPTY, xlrd.XL_CELL_BLANK): #check if cell is empty, if not then append it to list
                                       if (colnum1 == testCaseColumnIndex)or (colnum1 == testCaseDescriptionColumnIndex):
                                          sentence = sheet.cell(rownum, colnum1).value
					  stringSentence = sentence.encode('ascii','ignore')
					  punctuation_sentence = stringSentence.translate(None, string.punctuation)
                                          preprocessed_sentence = preProcessString( punctuation_sentence)
                                          g['depth_{0}'.format(i)].append(preprocessed_sentence)		

										 

	#Loop to write all dynamically created Lists to text file
	thefile = open('/home/aspire/client/juniper/juniper/media/textrequirementprocessed.txt', 'a')
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
		
        return testCaseId

