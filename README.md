# Big data Text Mining and Search using TF-IDF

Project Report: Wikipedia Dataset Analysis
1. Introduction:
This report presents the analysis of a subset of the English Wikipedia dataset obtained from Wikimedia. The dataset comprises approximately 5 million Wikipedia articles, each identified by a unique ARTICLE_ID. Each article contains various subsections denoted by SECTION_TITLE and SECTION_TEXT fields. The goal of this project is to analyze the dataset, perform indexing and retrieval tasks, and provide insights into information retrieval from large-scale text corpora.

2. Team Members:
Mohid Munir (Roll No: 21I-1719) - Worked on the first 5000 rows.
Moiz Sajjad (Roll No: 21I-2691) - Worked on rows 5001 to 10000.
Abdullah Iftikhar (Roll No: 21I-1687) - Worked on rows 10001 to 15000.
3. Data Preprocessing:
The dataset underwent extensive preprocessing to ensure data quality and consistency. Preprocessing steps included:

Cleaning and normalization of text data.
Tokenization of text into words or phrases.
Removal of stop words, punctuation, and special characters.
Lemmatization or stemming to reduce words to their base form.
Encoding categorical variables if applicable.
4. Task Description:
The main tasks performed on the dataset include indexing and retrieval:

Indexing: Construction of a vector representation for each document using TF-IDF (Term Frequency-Inverse Document Frequency) values. This vector representation allows efficient storage and retrieval of documents.
Retrieval: Searching for relevant documents based on user queries using cosine similarity or other similarity metrics. The TF-IDF representation facilitates the comparison of query vectors with document vectors.
5. Implementation Details:
Programming Language: Python was used for implementation due to its extensive libraries and tools for data analysis and natural language processing.
Libraries: Key libraries utilized include pandas, scikit-learn, numpy, and nltk (Natural Language Toolkit).
Algorithm: The TF-IDF (Term Frequency-Inverse Document Frequency) algorithm was employed for indexing and retrieval tasks.
Tools: Jupyter Notebook or Google Colab was used as the development environment for code execution and documentation.
6. Methodology:
6.1. Indexing:
Each team member implemented indexing for their respective segment of the dataset.
The TF-IDF values were computed for each term in each document.
Document vectors were constructed based on the TF-IDF scores.
Document vectors were normalized to mitigate the effect of document length on similarity calculations.
6.2. Retrieval:
User queries were tokenized and converted into TF-IDF representations using precomputed IDF values.
Cosine similarity or another similarity metric was used to compare query vectors with document vectors.
Relevant documents were ranked based on their similarity to the query.
7. Results:
The indexing and retrieval tasks were successfully implemented for the dataset subset.
Relevant documents were retrieved based on user queries with satisfactory accuracy.
Evaluation metrics such as precision, recall, and F1-score were calculated to assess the performance of the retrieval system.
8. Conclusion:
The project provided valuable insights into the analysis of large-scale text datasets such as Wikipedia. Key conclusions include:

The TF-IDF algorithm is effective for indexing and retrieving relevant information from text corpora.
Preprocessing plays a crucial role in improving the quality and accuracy of information retrieval systems.
Collaboration among team members facilitated the efficient completion of tasks and the exchange of knowledge and expertise.
9. Future Work:
Potential areas for future work and enhancements include:

Experimenting with advanced natural language processing techniques such as word embeddings and deep learning models.
Scaling the analysis to handle larger portions of the Wikipedia dataset.
Incorporating user feedback and iterative improvements to enhance the retrieval system's performance.
10. References:
Link to Wikipedia Dataset
Additional references, papers, and resources consulted during the project implementation.
11. Appendix:
Additional details, code snippets, visualizations, and evaluation metrics can be found in the accompanying code repository or provided upon request.
