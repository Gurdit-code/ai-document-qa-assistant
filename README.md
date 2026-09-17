# AI-Powered Document Q&A Assistant

An AI-powered document question-answering application built with Python, Streamlit, LangChain, Google Gemini, and FAISS. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded PDF documents and generate contextual answers.

## Features

- Upload PDF documents through the Streamlit interface
- Extract and split document text into smaller chunks
- Generate embeddings for semantic document search
- Store and retrieve document chunks using FAISS
- Generate answers using Google Gemini
- Support conversation history for follow-up questions


## How It Works

```text
PDF Upload
    ↓
Text Extraction
    ↓
Document Chunking
    ↓
Gemini Embeddings
    ↓
FAISS Vector Search
    ↓
Relevant Context
    ↓
Google Gemini
    ↓
Context-Aware Answer
```

## Project Structure

```text
AI-Powered-Document-QA-Assistant/
│
├── app.py              # Streamlit user interface
├── agent.py            # RAG and conversation logic
├── rag.py              # PDF processing and vector store
├── requirements.txt    # Project dependencies
├── .env                # API key configuration
└── README.md           # Project documentation
```

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini
- FAISS
- PyPDF
- Python-dotenv




### 4. Configure Gemini API

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

## Usage

1. Open the application.
2. Upload one or more PDF documents.
3. Wait for the documents to be processed.
4. Ask a question about the uploaded documents.
5. Ask follow-up questions using the conversation history.
6. Check the source section to see the document and page used for the answer.

## Example

```text
User: What is overfitting?

Assistant: Overfitting occurs when a machine learning model learns
the training data too closely and performs poorly on unseen data.

User: How can it be reduced?

Assistant: It can be reduced using techniques such as regularization,
cross-validation, simpler models, more training data, and appropriate
feature selection.
```

## Environment Variables

The project requires:

```text
GEMINI_API_KEY
```

## Future Improvements

- Support DOCX, TXT, CSV, and other document formats
- Add document management and deletion
- Improve conversational query rewriting
- Add authentication
- Add persistent vector databases

## Author

Gurditta
