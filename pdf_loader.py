from langchain_community.document_loaders import PyPDFLoader

def load_pdf():
    return PyPDFLoader("temp_resume.pdf").load()