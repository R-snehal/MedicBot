from flask import Flask, render_template, jsonify, request

from src.helper import download_hugging_face_embeddings

from langchain_qdrant import QdrantVectorStore

from langchain_huggingface import (
    HuggingFaceEmbeddings,
    HuggingFaceEndpoint,
    ChatHuggingFace,
)

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
from src.prompt import *
import os



app = Flask(__name__)

print("__file__:", __file__)
print("Current Working Directory:", os.getcwd())
print("App root:", app.root_path)
print("Template folder:", app.template_folder)
print("Template exists:", os.path.exists(os.path.join(app.root_path, app.template_folder)))
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# os.environ["QDRANT_API_KEY"] = None
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

embeddings = download_hugging_face_embeddings()

docsearch = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    collection_name="MedicBot",
    prefer_grpc=True,
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

llm_endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    temperature=0.4,
    max_new_tokens=500,
)

llm = ChatHuggingFace(llm=llm_endpoint)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(
    llm,
    prompt,
)
rag_chain = create_retrieval_chain(
    retriever,
    question_answer_chain,
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input=msg
    print(input)
    response= rag_chain.invoke({"input": msg})
    print("Response:", response["answer"])
    return str(response["answer"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug=True)

