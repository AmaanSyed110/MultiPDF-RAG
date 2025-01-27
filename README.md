# MultiPDF-RAG

## Overview
The **MultiPDF-RAG** project is a Python-based application designed to facilitate interactive querying across multiple PDF documents. By leveraging advanced language models, it enables users to input natural language questions and receive accurate, contextually relevant answers derived from the content of the loaded PDFs. This functionality is particularly beneficial for researchers, students, and professionals who need to efficiently extract and synthesize information from extensive document collections.

## How it works
![MultiPDF RAG](https://github.com/user-attachments/assets/6b013dbf-a138-4ae4-b809-0923331768bc)


## Demo Video
[MultiPDF-RAG.webm](https://github.com/user-attachments/assets/85eeb026-3b83-4bba-bcf7-890a3dad4d88)


## Features

- **Upload PDFs**: Supports uploading multiple PDFs simultaneously for processing..

- **Smart Text Extraction**: Uses ```pdfplumber``` to extract readable content from uploaded PDFs.

- **Embeddings**: Create vector embeddings with OpenAI's ```text-embedding-3-small```

- **Efficient Search**: Leverages FAISS for fast similarity search and retrieval of relevant information.

- **Interactive Q&A**: Powered by OpenAI's ```gpt-4o``` model to provide insightful, context-aware answers to user questions.

- **Chat History**: Maintains a conversation buffer for seamless interactions.


## Tech Stack
- **Python** - The core programming language used to develop the application, enabling robust and efficient processing.

- **Streamlit** - A lightweight framework for building the user interface, providing an interactive platform to query PDF documents.
  
- **pdfplumber** - A Python library used to extract readable text from PDFs.
  
- **LangChain** - A framework for integrating language models, facilitating the app’s ability to generate contextual answers.

- **FAISS** - High-performance similarity search for vector embeddings.
  
- **OpenAI API** - Powers the natural language processing capabilities, enabling accurate responses to user queries based on PDF content.

## Steps to Run the MultiPDF-RAG Project on Your Local Machine:
- ### Clone the Repository
Open a terminal and run the following command to clone the repository:

```
git clone https://github.com/AmaanSyed110/MultiPDF-RAG.git
```
- ### Set Up a Virtual Environment
It is recommended to use a virtual environment for managing dependencies:

```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
- ### Install Dependencies
Install the required packages listed in the ```requirements.txt``` file
```
pip install -r requirements.txt
```
- ### Add Your OpenAI API Key
Create a ```.env``` file in the project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```
- ### Run the Application
Launch the Streamlit app by running the following command:
```
streamlit run app.py
```
- ### Upload PDF Documents
Use the web interface to upload PDF files and start querying their content.

- ### Interact with the Application
Ask questions related to the PDFs, and the app will provide relevant responses based on the document content.

## Contributions
Contributions are welcome! Please fork the repository and create a pull request for any feature enhancements or bug fixes.


