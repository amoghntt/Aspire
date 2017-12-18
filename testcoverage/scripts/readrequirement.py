import io
import string
import testcaseread
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def readRequirementFromTextFile():
	"This function read requirement from text file and preprocesses it"
	#with open('/opt/apache-tomcat-8.0.36/webapps/resources1/textrequirement.txt', 'r') as myfile:
	with open('/home/aspire/client/juniper/juniper/media/textrequirement.txt', 'r') as myfile:
		d=myfile.read().replace('\n', '')
		data=d.encode('utf-8').strip()
					  

	preprocessed_sentence = testcaseread.preProcessString(data.translate(None, string.punctuation))

	#text_file = open("/opt/apache-tomcat-8.0.36/webapps/resources1/textrequirementprocessed.txt", "w")
	text_file = open("/home/aspire/client/juniper/juniper/media/textrequirementprocessed.txt", "w")
	text_file.write(preprocessed_sentence+"\n")
	text_file.flush()
	text_file.close()

