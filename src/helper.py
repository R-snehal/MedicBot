from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings

def load_pdf_file(data):
    loader = DirectoryLoader(data, glob="*.pdf", 
                             loader_cls=PyMuPDFLoader)
    documents=loader.load()
    return documents

# loader = PyMuPDFLoader("Data/2016 Gale Encyclopedia of Medicine - 5E.pdf")
# documents = loader.load()

#Split the Data into Text Chunks
def text_split(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks

#Download the Embeddings from Hugging Face
def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings