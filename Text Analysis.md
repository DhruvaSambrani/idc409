# Keyword counting

Frequency  of words give a sense of which words are key words for summarizing the document/data. 

then, 

$$f_{i,j} = \frac{n_{i,j}}{\sum_k n_{k, i, j}}$$

But often, some words are over represented in a particular paper, but is NOT a key word. Hence, it is also important to multiply it with 

$$\log\left(\frac{\text{\# documents which have that word}{\text{\# documents}}}\right)$$

## Co-occurrance 

Words often come together. Co-occurence looks at how often n words come together. It can be directed or undirected. This is a natural extension of ngrams for letters.

## Random, off-topic concepts

- Adjacency matrix
- Directed-ness
- Centrality - $x_i = \sum_j A_{ij} x_j \Rightarrow \vec{x} = \mathbb{A}\vec{x}$
- 
