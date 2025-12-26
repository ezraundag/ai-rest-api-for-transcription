import requests 
import json

# SET url variable to REST API endpoint for Batch Speech to text. The endpoint can be found in your Azure console.
url = 'https://eastus.api.cognitive.microsoft.com/speechtotext/v3.2/transcriptions'

# SET contentUrl to URL location of audio file for transcription. The file has to be made accessible to the Azure transcription service
contentUrl='https://locationtoaudiofile.test/audiofiletest.m4a'

# SET locale of language as spoken in the audio file
locale = 'en-US'

params = {
    "retina_name":"en_associative",
    "start_index":0,
    "max_results":1,
    "sparsity":1.0,
    "get_fingerprint":False
}

# SET Ocp-Apim-Subscription-Key to the 32-character Private Key, which is required to call Azure Rest API endpoint. This key can be found in your Azure console.
headers={
    "Ocp-Apim-Subscription-Key":"aabbccddeeffgghhiijjkkllmmnnooppqq",
    "Content-Type":"application/json"
    }
data = {
    "displayName": "test_speechtotext",
    "description": "Speech Studio Batch speech to text for test audio file",
    "locale": locale,
    "contentUrls": [
        contentUrl
    ],
    "properties": {
        "wordLevelTimestampsEnabled": False,
        "displayFormWordLevelTimestampsEnabled": True,
        "diarizationEnabled": False,
        "punctuationMode": "DictatedAndAutomatic",
        "profanityFilterMode": "Masked"
    },
    "customProperties": {}
}

# Send a HTTP POST to REST API endpoint for Batch Speech to text, with arguments set to initialized variables: url, paramas, data, headers
res = requests.post(url,params=params, json=data, headers=headers)


# convert response body to json formated string 
jsonres = json.dumps(res.json())

# convert json formated string to python object
data = json.loads(jsonres)

# convert python object back to json formated string 
prettydata = json.dumps(data, indent=2)

# Print the response body, which contains the transcription id needed to fetch the transcription results
print(prettydata)
