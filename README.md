# RAG-Simplified: A DIY Approach to Retrieval-Augmented Generation 

## Introduction

This repository contains a simple and customizable implementation of Retrieval-Augmented Generation (RAG) 
using SQLModel, PostgreSQL with PGVector, and Cohere's embedding model. 
It accompanies the Medium blog post "Search with RAG: A Simple DIY Approach" 
offering a step-by-step guide to building your own RAG system. 

## Requirements

- Python 3.7 or higher
- PostgreSQL with PGVector extension
- Cohere API key (sign up at [Cohere](https://cohere.com/) to obtain one)

## Setup Instructions

1. Clone the repository:

   ```
   git clone git@github.com:helmanofer/simple_rag.git
   ```

2. Install the required Python packages:

   ```
   cd simple_rag
   pip install -r requirements.txt
   ```

3. Set up your local PostgreSQL database using docker compose:

   ```
   docker compose up -d
   ```

4. Update the `.env` file with your Cohere API key:

   ```.dotenv
   COHERE_KEY=Your_Cohere_Key
   ```

5. You're all set! Now you can start experimenting with the provided code and adapting it to your specific use case.

## Usage

The repository includes the following key components:

- `db_models.py`: Defines the DTO models using SQLModel, including the `Document` class for storing text data and embeddings.
- `embeddings.py`: Contains the `co_embed` function, which utilizes Cohere's multilingual embedding model to generate embeddings for a list of texts.
- `search.py`: Implements the search functionality, allowing you to query the database and retrieve relevant documents based on cosine distance.
- `index.py`: Implements the indexing functionality, allowing you to store documents in the database

## Customization

The beauty of this DIY approach is its simplicity and flexibility. You can easily adapt the code to your specific needs:

- Adjust the embedding model used in the `co_embed` function to match your requirements.
- Modify the `Document` class in `document.py` to include additional fields or adjust the embedding dimension.
- Experiment with different tokenization approaches or text preprocessing techniques to suit your data.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open a pull request or create an issue. Please ensure that your contributions adhere to the project's code style and include appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 

Happy searching, and stay tuned for more exciting NLP adventures!