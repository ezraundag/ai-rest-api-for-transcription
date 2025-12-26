**Transcribing audio files using Microsoft Azure Cognitize Service - Foundry Tools**

This repo contains two python files that transcribe an audio file and save the transcription to a word document. These scripts can be useful if you need to batch-transcribe multiple large audio files from long interviews. 

I wrote these scripts to transcribe and code collected interviews for qualitative research.

**(1) batchspeechtotext.py**

This python script uses Microsoft Azure Cognitize Service - Foundry Tools for Batch Speech to Text processing. Using batch processing is useful for very large audio files, allowing for asynchronous processing. An important output of this script is the Transcription Id, which is found in the response body. It is specifically found in the top-level self property as part of the transcription's URI. 

For example: Transcription Id is "88a1f24-f980-4809-8978-e5cf41f77b35" from "self": "https://eastus.api.cognitive.microsoft.com/speechtotext/transcriptions/788a1f24-f980-4809-8978-e5cf41f77b35"


See example response body in REST API documentation: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/batch-transcription-create?pivots=rest-api

**(2) savetranscriptiontodoc.py** 

This python script asynchronously checks the status of the transcription process then saves the transcription to a word document upon completion. The Transcription Id from batchspeechtotext.py is used in savetranscriptiontodoc.py.
