from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
import os
import shutil

app = Flask(__name__)
CORS(app)

# Global variables
retriever = None
chain = None

def read_csv_file():
    """Read and return data from CSV file"""
    try:
        df = pd.read_csv("me.csv")
        return df["paragraph"].dropna().tolist()
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

def create_documents(paragraphs):
    """Create document objects from paragraphs"""
    documents = []
    for i, para in enumerate(paragraphs):
        doc = Document(
            page_content=para,
            metadata={"source": "me.csv", "paragraph": i+1}
        )
        documents.append(doc)
    return documents

def delete_old_database():
    """Delete existing database if it exists"""
    db_path = "./chroma_me_db"
    if os.path.exists(db_path):
        try:
            shutil.rmtree(db_path)
            print("🗑️  Old database deleted")
        except Exception as e:
            print(f"⚠️  Could not delete database: {e}")

def create_vector_store(documents):
    """Create and return vector store"""
    embedding = OllamaEmbeddings(model="mxbai-embed-large")
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding,
        persist_directory="./chroma_me_db",
        collection_name="me_info"
    )
    return vector_store

def create_llm_chain():
    """Create and return LLM chain"""
    llm = OllamaLLM(model="llama3")
    prompt = ChatPromptTemplate.from_template("""
You are Siddharth Vishwakarma. Use only the given information below to answer about yourself.

Information:
{details}

Question: {question}

If the answer is not in the information, say "I don't know that."
Be friendly and helpful. Keep answers concise but informative.
Capitalize the keywords of the answer.
no need to print "i am siddharth vishwakarma" everytime                                             

""")
    return prompt | llm

def setup_chatbot():
    """Setup the complete chatbot"""
    global retriever, chain
    
    # Load data
    paragraphs = read_csv_file()
    if not paragraphs:
        print("❌ No data found in CSV!")
        return False
    
    # Create documents
    documents = create_documents(paragraphs)
    
    # Setup database
    delete_old_database()
    vector_store = create_vector_store(documents)
    retriever = vector_store.as_retriever(search_kwargs={"k": 6})
    
    # Setup LLM
    chain = create_llm_chain()
    
    print(f"✅ Loaded {len(paragraphs)} paragraphs")
    return True

def get_relevant_docs(question):
    """Get relevant documents for a question"""
    docs = retriever.invoke(question)
    return docs

def format_context(docs):
    """Format documents into context string"""
    context_parts = []
    for i, doc in enumerate(docs):
        context_parts.append(f"Paragraph {i+1}: {doc.page_content}")
    return "\n\n".join(context_parts)

def generate_response(question, context):
    """Generate response using LLM"""
    response = chain.invoke({"details": context, "question": question})
    return str(response)

def ask_question(question):
    """Main function to ask a question and get answer"""
    try:
        # Check if chatbot is ready
        if not retriever or not chain:
            return "Chatbot is not ready. Please restart the server."
        
        # Get relevant documents
        docs = get_relevant_docs(question)
        
        # Format context
        context = format_context(docs)
        
        # Generate response
        answer = generate_response(question, context)
        
        return answer
        
    except Exception as e:
        print(f"Error processing question: {e}")
        return "Sorry, I encountered an error. Please try again."

def validate_request(data):
    """Validate incoming request data"""
    if not data:
        return False, "No data provided"
    
    question = data.get('question', '').strip()
    if not question:
        return False, "Question is required"
    
    return True, question

@app.route('/')
def home():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    """Handle question requests"""
    try:
        # Validate request
        is_valid, result = validate_request(request.get_json())
        if not is_valid:
            return jsonify({'error': result}), 400
        
        # Get answer
        answer = ask_question(result)
        return jsonify({'answer': answer})
        
    except Exception as e:
        print(f"API Error: {e}")
        return jsonify({'error': 'Server error'}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    status = {
        'status': 'ok',
        'chatbot_ready': retriever is not None and chain is not None
    }
    return jsonify(status)

def start_server():
    """Start the Flask server"""
    print("🌐 Starting web server at http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    print("🚀 Setting up chatbot...")
    if setup_chatbot():
        print("✅ Chatbot ready!")
        start_server()
    else:
        print("❌ Failed to setup chatbot!") 