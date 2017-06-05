import json
from apiclient.discovery import build

print ("starting")

def createService():
    #Specifiy which api, version and API key
	service = (build('translate', 'v2', 
		developerKey='AIzaSyCBkuLV3-zuPSXJM7HFISLgYwtOJFfmem8'))
	return service

def translate_me(text, language):
	collection = createService().translations()
	request = collection.list(q=text, target=language)
	response = request.execute()
	return response['translations'][0]['translatedText']

inputText = input("Enter some text:")
translatedWord = translate_me(inputText, "el")
backToEnglish = translate_me(translatedWord, "en")
print ("Greek > " + translatedWord)
print ("English > " + backToEnglish)