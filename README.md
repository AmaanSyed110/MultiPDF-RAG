# MultiPDF-RAG

## Overview
The **MultiPDF-RAG** project is a Python-based application designed to facilitate interactive querying across multiple PDF documents. By leveraging advanced language models, it enables users to input natural language questions and receive accurate, contextually relevant answers derived from the content of the loaded PDFs. This functionality is particularly beneficial for researchers, students, and professionals who need to efficiently extract and synthesize information from extensive document collections.

## How it works
![MultiPDF RAG](https://github.com/user-attachments/assets/6b013dbf-a138-4ae4-b809-0923331768bc)


## Demo Video


## Features

- **PDF Loading**: The app reads multiple PDF documents and extracts their text content.

- **Text Chunking**: The extracted text is divided into smaller chunks that can be processed effectively.

- **Language Model**: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

- **Similarity Matching**: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

- **Response Generation**: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.


## Tech Stack
- **Python** - The core programming language used to develop the application, enabling robust and efficient processing.

- **Streamlit** - A lightweight framework for building the user interface, providing an interactive platform to query PDF documents.
  
- **PyPDF2** - A Python library used to extract and manage text content from PDF files for analysis.
  
- **LangChain** - A framework for integrating language models, facilitating the app’s ability to generate contextual answers.
  
- **OpenAI API** - Powers the natural language processing capabilities, enabling accurate responses to user queries based on PDF content.
