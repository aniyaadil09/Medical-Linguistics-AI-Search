# Medical Linguistics AI Search

-[Project Title](#project-title)
  
- [Medical Linguistics AI Search](#medical-linguistics-ai-search)
  - [Project Title](#project-title)
  - [Introduction](#introduction)
  - [Objectives](#objectives)
  - [Tools and Technologies Used](#tools-and-technologies-used)
    - [Python](#python)
    - [FAISS](#faiss)
    - [JSON / Pickle](#json--pickle)
  - [Project Structure](#project-structure)
  - [Modules / Functionalities](#modules--functionalities)
  - [Create Index](#create-index)
  - [Main Program](#main-program)
  - [Implementation](#implementation)
  - [FAISS Index](#faiss-index)
  - [Backend Files and Environment](#backend-files-and-environment)
  - [Contains all required Python packages](#contains-all-required-python-packages)
    - [venv](#venv)
    - [Testing / Sample Output](#testing--sample-output)
  - [Search Medical Term](#search-medical-term)
  - [Conclusion](#conclusion)

## Project Title

Medical Linguistics AI Search
## Large Files Notice
Some large files such as datasets, model files, and other heavy project resources are not uploaded to GitHub because of file size limitations.

## Download Large Files
[Click here to access the Google Drive folder containing all large project files](https://drive.google.com/drive/folders/16aV5pHtAlYDuoettErABVXX_Kmd6vupy?usp=sharing)

## Important Note
After downloading the large files, place them in the correct project folders before running the project.



An AI-powered system to search medical terms, diseases, and symptoms using semantic vector search. Instead of traditional keyword search, it converts medical text into high-dimensional vectors, stores them in a FAISS index, and retrieves the most semantically similar results along with metadata such as Verified/Unverified status.

## Introduction

Medical language is complex, with many terms, synonyms, and variations. This project implements a semantic search system for medical terms using Python and FAISS:

Converts medical terms into vector embeddings (384-dimensional).

Stores embeddings in a FAISS index for fast similarity search.

Allows user queries to find top similar diseases, symptoms, or terms.

Returns metadata including name, description, and verification status.

This approach provides faster and smarter search than simple keyword matching.

## Objectives

Efficiently search medical terms and diseases using semantic similarity.

Build a vector-based search system with FAISS.

Store and manage metadata in JSON and Pickle files.

Display top search results with verification status.

Lay foundation for AI-powered medical language processing.

## Tools and Technologies Used

### Python

Backend programming language for handling embeddings, vectors, and metadata.

Provides simple file I/O to load and save indices and metadata.

### FAISS

Facebook AI Similarity Search for fast vector similarity search.

Handles large datasets and high-dimensional embeddings efficiently.

### JSON / Pickle

JSON → human-readable format for metadata.

Pickle → Python-native serialization format for fast loading and saving.

## Project Structure

AI Theory/
│
├─ app/
│   ├─ __pycache__/
│   ├─ main.py                     # Main program     interface
│   ├─ search.py                   # Search functions
│   ├─ create_index.py             # Build FAISS index from dataset
│   ├─ vector_db.py                # VectorDB class: add/load/search vectors
│   ├─ metadata.json               # Human-readable metadata
│   ├─ metadata.pkl                # Pickled metadata for fast loading
│   ├─ vector.index                # FAISS vector index
│   └─ faiss_index.index           # Alternate FAISS index file
│
├─ data/
│   └─ processed/
│       └─ chapter1-22.json        # Raw dataset of medical terms
│
├─ .venv/                          # Python virtual environment
├─ README.md                        # Project documentation
└─ requirements.txt                 # Python dependencies

## Modules / Functionalities

## Create Index

Reads the medical dataset (chapter1-22.json).

Converts each medical term into a 384-dimensional vector.

Stores vectors in a FAISS index for fast similarity search.

Saves both the FAISS index (vector.index) and metadata (metadata.pkl) for later use.

Search Medical Terms

Accepts user input of a disease, symptom, or medical term.

Converts query into vector embedding.

Searches the FAISS index for top-k closest terms.

Returns results with metadata and Verified/Unverified status.

## Main Program

Loads FAISS index and metadata.

Runs an interactive loop for the user to search terms.

Displays search results in JSON format.

Allows exiting with "exit" command.

## Implementation

Vector Embeddings

Each medical term is converted into a 384-dimensional vector.

Embeddings represent semantic meaning, not just literal keywords.

Random vectors are used for testing; real embeddings can come from AI models.

## FAISS Index

Stores vectors efficiently for nearest neighbor search.

Supports fast searches even with large datasets.

Index is saved to disk for future use.

Search and Ranking

Searches FAISS index for closest vectors to query.

Returns top results along with metadata, e.g.:

{
  "name": "Fever",
  "description": "Elevated body temperature",
  "status": "Verified"
}

ensure_ascii=False is used in json.dumps() to keep non-English characters readable.

## Backend Files and Environment

File = Description

vector_db.py = Handles vector embeddings, adding/searching metadata, saving/loading index

create_index.py= Builds FAISS index from the dataset

search.py= Helper functions for searching medical terms

main.py= Interactive main program interface

.venv/= Python virtual environment

requirements.txt= List of Python packages

metadata.json= Human-readable metadata for diseases/symptoms

metadata.pkl= Pickled metadata for fast loading

vector.index= FAISS vector index storing embeddings

faiss_index.index= Alternate FAISS index file
requirements.txt

## Contains all required Python packages

faiss

numpy

pickle-mixin

Install with:

pip install -r requirements.txt

### venv

Python virtual environment to manage dependencies and avoid conflicts.

Keeps project isolated from system Python packages.

### Testing / Sample Output

Load Database

vector_db.load("vector.index", "metadata.pkl")

Loads FAISS index and metadata.

Prints the number of items loaded.

## Search Medical Term

Enter a disease or symptom (or 'exit' to quit):
> fever

Finds top 5 similar terms.

Displays results in JSON format.

Sample JSON Output

> {
  "name": "Fever",
  "description": "Elevated body temperature",
  "status": "Verified"
}

Random vectors used for testing; can be replaced with real medical embeddings.

## Conclusion

Demonstrates semantic search for medical language.

Combines Python, FAISS, and metadata for fast AI-based search.

Scalable for larger datasets and integration with real medical embeddings.

Provides a foundation for AI-driven medical language tools.
