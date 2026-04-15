from pdf_loader import load_pdf
from vector_store import create_vector_store
from rag_pipeline import ask_resume

# Load resume
docs = load_pdf()

# Create vector DB
vectorstore = create_vector_store(docs)


while True:
    query = input("\nAsk something about your resume (type 'exit'): ")

    if query.lower() == "exit":
        break

    answer = ask_resume(vectorstore, query)

    print("\nAI Answer:\n")
    print(answer)