from langchain_community.vectorstores import FAISS
import os


class Memory:
    def __init__(self, embedding_provider, **kwargs):

        _embeddings = None
        match embedding_provider:
            case "ollama":
                from langchain_community.embeddings import OllamaEmbeddings
                _embeddings = OllamaEmbeddings(model="mxbai-embed-large")
                #_embeddings = OllamaEmbeddings(model="llama2")
            case "openai":
                from langchain_openai import OpenAIEmbeddings
                _embeddings = OpenAIEmbeddings()
            case "azureopenai":
                from langchain_openai import AzureOpenAIEmbeddings
                _embeddings = AzureOpenAIEmbeddings(deployment=os.environ["AZURE_EMBEDDING_MODEL"], chunk_size=16)
            case "huggingface":
                from langchain_community.embeddings import HuggingFaceEmbeddings
                _embeddings = HuggingFaceEmbeddings(model_name=os.environ["HUGGINGFACE_EMBEDDING_MODEL"],model_kwargs = {'device': 'cpu'}, encode_kwargs = {'normalize_embeddings': False})

            case _:
                raise Exception("Embedding provider not found.")

        self._embeddings = _embeddings

    def get_embeddings(self):
        return self._embeddings
