from llm import get_llm

def ask_resume(vectorstore, query):
    llm = get_llm()

    # Step 1: Get relevant chunks
    docs = vectorstore.similarity_search(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    # Step 2: Create prompt
    prompt = f"""
    You are an AI Resume Analyzer.

    Use the following resume data to answer the question.

    Resume:
    {context}

    Question:
    {query}

    Answer:
    """

    # Step 3: LLM response
    response = llm.invoke(prompt)

    return response.content