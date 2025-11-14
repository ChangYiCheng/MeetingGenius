# MeetingGenius

## 🧠 Introduction
This project is an intuitive web application that allows users to upload meeting audio. It leverages **LLM model** to perform **real-time speech-to-text transcription** and **content summarization**, presenting high-quality textual results on the front end and effectively enhancing meeting information management efficiency.

## 🚀 Key Features
- Utilizes the **Whisper-Medium** model for high-accuracy speech-to-text transcription
- Leverages the **Llama-3.2-3B-Instruct** model for automated summary generation
- Backend built with **FastAPI** to create a high-performance API and integrate frontend and backend
- Frontend developed with **HTML/CSS/JavaScript**, featuring a clean and intuitive interface
- Implements **real-time audio upload and analysis**, with automatic storage and backup of relevant files

## ⭐ Usage Workflow
### Step 1. Open the web interface
Prepare the audio file you want to convert into meeting notes and open the web interface.
![Web Interface](screenshot/1_web_interface.png)<br><br>
### Step 2. Select language
Select your preferred language. Currently, Traditional Chinese, English, Japanese, and German are supported. The meeting summary will be generated in your chosen language.
![Select an Audio File](screenshot/2_select_language.png)<br><br>
### Step 3. Select an audio file
Click the "Select Audio File" button and choose a file from your device. The file name will be displayed immediately, confirming your selection.
![Upload and Analyze](screenshot/3_2_select_an_audio_file_English.png)<br><br>
### Step 4. Upload and analyze
Click the "Upload and Analyze" button. The status will display a "Uploading, please wait..." message, and the system will immediately perform transcription and generate the summary.
![Upload and Analyze](screenshot/4_2_upload_and_analyze_English.png)<br><br>
### Step 5. View results
The transcribed text and automatically generated summary are displayed, enabling quick understanding of the meeting content.
![Upload and Analyze](screenshot/5_2_view_results_English.png)<br><br>

## 📚 Reference
- Whisper-Medium: [Hugging Face](https://huggingface.co/openai/whisper-medium)
- Llama-3.2-3B-Instruct: [Hugging Face](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)




