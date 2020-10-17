import requests
import json
import os
import string
import codecs


url="http://localhost:8111/api"

absFilePath = os.path.abspath(__file__)                # Absolute Path of the module
print("Current directory: ",absFilePath)
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module

parentDir = os.path.dirname(fileDir)                   # Directory of the Module directory

modelPath = os.path.join(fileDir, 'model')             # Get the directory for model

filePath = os.path.join(fileDir, 'upload')              # Directory of the test file
temp_file = os.path.join(filePath, 'test_file.txt')
test_file = codecs.open(temp_file, encoding='utf-8', errors='ignore').read()

data = json.dumps(test_file)
r=requests.post(url,data)


result = r.json()

print(result)
