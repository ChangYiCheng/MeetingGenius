# MeetingGenius

## Introduction
This project is an intuitive web application that allows users to upload meeting audio. It leverages **LLM model** to perform **real-time speech-to-text transcription** and **content summarization**, presenting high-quality textual results on the front end and effectively enhancing meeting information management efficiency.

## Key Features
- Utilizes the **Whisper-Medium** model for high-accuracy speech-to-text transcription
- Leverages the **Llama-3.2-3B-Instruct** model for automated summary generation
- Backend built with **FastAPI** to create a high-performance API and integrate frontend and backend
- Frontend developed with **HTML/CSS/JavaScript**, featuring a clean and intuitive interface
- Implements **real-time audio upload and analysis**, with automatic storage and backup of relevant files

## Usage Workflow
1. Open the web interface
Prepare the audio file you want to convert into meeting notes and open the web interface.
![image]()
2. Select an audio file
Click the “Select Audio File” button and choose a file from your device. The file name will be displayed immediately, confirming your selection.
![image]()
3. Upload and analyze
Click the “Upload and Analyze” button. The status message will show “Uploading, please wait…”. Within moments, the system will complete transcription and summarization.
![image](screenshot_upload.png)
4. View results
The transcribed text and automatically generated summary are displayed, enabling quick understanding of the meeting content.
![image](screenshot_upload.png)

## Model Source
- Whisper-Medium: [Hugging Face](https://huggingface.co/openai/whisper-medium)
- Llama-3.2-3B-Instruct: [Hugging Face](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)




