import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
openai_api_key = os.getenv('OPENAI_API_KEY')

# Function to extract text from PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split text into manageable chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create a vector store from text chunks
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# Function to create a conversation chain
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo")
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# Function to handle user input
def handle_user_input(user_question):
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(f"**User:** {message.content}")
            else:
                st.write(f"**Bot:** {message.content}")

# Main app function
def main():
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
        pdf_docs = st.file_uploader("Upload PDFs here:", accept_multiple_files=True, type="pdf")

        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing your documents..."):
                    # Extract text from PDFs
                    raw_text = get_pdf_text(pdf_docs)

                    # Split text into chunks
                    text_chunks = get_text_chunks(raw_text)

                    # Create vector store
                    vectorstore = get_vectorstore(text_chunks)

                    # Initialize conversation chain
                    st.session_state.conversation = get_conversation_chain(vectorstore)

                st.success("Documents processed successfully! You can now ask questions.")
            else:
                st.warning("Please upload at least one PDF to process.")

if __name__ == "__main__":
    main()
