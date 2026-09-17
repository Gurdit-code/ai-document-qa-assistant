from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from rag import load_vector

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
vectorstore = load_vector()
chat_history = []

def needs_rag(question):
    keywords = [
        "machine learning",
        "deep learning",
        "neural network",
        "cnn",
        "rnn",
        "lstm",
        "python",
        "nlp",
        "embedding",
        "llm",
        "rag",
        "agent",
        "overfitting",
        "underfitting",
        "random forest",
        "decision tree",
        "linear regression",
        "logistic regression",
        "cross-validation",
        "cross validation",
        "vector database"
    ]

    question_lower = question.lower()
    if any(keyword in question_lower
        for keyword in keywords ):
        return True

    for user_message, ai_message in chat_history:
        conversation = (user_message + " " + ai_message ).lower()

        if any(keyword in conversation
            for keyword in keywords):
            return True
        
    return False


def get_history():
    if not chat_history:
        return "No previous conversation."
    history_text = ""

    for user_message, ai_message in chat_history[-5:]:
        history_text += f"""
User: {user_message}
Assistant: {ai_message}
"""
    return history_text

def ask_question(question):
    use_rag = needs_rag(question)
    context = ""
    sources = []

    if use_rag:
        print("Searching FAISS...")
        results = vectorstore.similarity_search(question, k=3 )

        context = "\n\n".join(result.page_content 
                              for result in results)

        for result in results:
            source = result.metadata.get( "source","Unknown")
            page = result.metadata.get("page")

            if page is not None:
                sources.append(f"{source} - Page {page + 1}" )
            else:
                sources.append(source)

    history_text = get_history()
    prompt = f"""
You are a helpful AI assistant.

Previous conversation:
{history_text}

Document context:
{context}

Current question:
{question}

Instructions:

- Understand follow-up questions using previous conversation.
- Use document context when available.
- Give a clear and simple answer.
- Do not invent information from the document.
- If the answer is not in the document, say:
"I could not find this information in the document."
"""

    response = llm.invoke(prompt)
    answer = response.content

    if isinstance(answer, list):
        answer = "\n".join(item["text"]
            for item in answer
            if item.get("type") == "text")

    chat_history.append((question, answer))

    return answer, sources