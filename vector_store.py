from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(documents):
    
    # Step 1: Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    texts = text_splitter.split_documents(documents)
    
    # Step 2: Create embeddings (FREE)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Step 3: Store in FAISS
    vectorstore = FAISS.from_documents(texts, embeddings)
    
    return vectorstore