from llama_index.core import SimpleDirectoryReader, GPTVectorStoreIndex

# Load all documents from a "data" folder
documents = SimpleDirectoryReader("data").load_data()

# Create an index from these documents
index = GPTVectorStoreIndex.from_documents(documents)

# Save the index for future use
index.storage_context.persist(persist_dir="./index_storage")


