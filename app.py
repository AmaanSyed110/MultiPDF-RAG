import streamlit as st
import pdfplumber
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate environment variables
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API key.")

# Initialize the embedding model with text-embedding-3-small
embeddings = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY,
    model="text-embedding-3-small"
)

def get_pdf_text(pdf_docs):
    """Extract text from uploaded PDF documents using pdfplumber."""
    text = ""
    for pdf in pdf_docs:
        with pdfplumber.open(pdf) as pdf_reader:
            for page in pdf_reader.pages:
                text += page.extract_text() or ""  # Ensure no error if extract_text returns None
    return text

def get_text_chunks(text):
    """Split text into smaller chunks for processing."""
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1500,  # Set chunk size to 1500 characters for optimal performance
        chunk_overlap=300,  # Overlap of 300 characters for better context retention
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    """Create a FAISS vector store from text chunks."""
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model="gpt-4o",
        temperature=0.7
    )
    
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    
    return conversation_chain

def handle_user_input(user_question):
    """Process user input and get response using the conversation chain."""
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']
        
        # Display the updated chat history
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(f"**User:** {message.content}")
            else:
                st.write(f"**Assistant:** {message.content}")

def main():
    """Main application function."""
    st.set_page_config(page_title="Chat with PDFs", page_icon=":books:")
    st.title("Chat with Your PDFs :books:")

    # Initialize session state variables
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User question input
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_user_input(user_question)

    # Sidebar for PDF upload and processing
    with st.sidebar:
        st.subheader("Upload your PDFs")
        pdf_docs = st.file_uploader(
            "Upload PDFs here:",
            accept_multiple_files=True,
            type="pdf"
        )

        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing your documents..."):
                    try:
                        # Process PDFs and create vector store
                        raw_text = get_pdf_text(pdf_docs)
                        if raw_text.strip() == "":
                            st.error("No readable text found in the uploaded PDFs. Please check the PDFs.")
                        else:
                            text_chunks = get_text_chunks(raw_text)
                            vectorstore = get_vectorstore(text_chunks)
                            # Create conversation chain
                            st.session_state.conversation = get_conversation_chain(vectorstore)
                            st.success("Documents processed successfully! You can now ask questions.")
                    except Exception as e:
                        st.error(f"Error processing documents: {str(e)}")
            else:
                st.warning("Please upload at least one PDF to process.")

if __name__ == "__main__":
    main()