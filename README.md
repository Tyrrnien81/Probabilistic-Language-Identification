# Probabilistic-Language-Identification

Introduction to Artificial Intelligence - HW2

This project is an implementation of a probabilistic language identifier that determines whether a shredded letter is written in English or Spanish. It uses Bayesian inference to compute the conditional probabilities based on the letter's character frequencies and predefined language models.

## Table of Contents

-   [Project Overview](#project-overview)
-   [How It Works](#how-it-works)
-   [Program Structure](#program-structure)
    -   [1. Character Shredder](#1-character-shredder)
    -   [2. Language Identification via Bayes Rule](#2-language-identification-via-bayes-rule)
    -   [3. Computational Considerations](#3-computational-considerations)
    -   [4. Output Specifications](#4-output-specifications)
-   [Prerequisites](#prerequisites)
-   [Running the Program](#running-the-program)
-   [File Descriptions](#file-descriptions)
-   [Sample Output](#sample-output)
-   [References](#references)

## Project Overview

This project is inspired by a scenario in which detectives recover a shredded business letter. The objective is to estimate whether the letter is written in English or Spanish by analyzing the frequency of alphabetic characters (A-Z) in the letter. The project employs a probabilistic approach using Bayes' rule to identify the source language.

## How It Works

The program counts the occurrence of letters from A to Z in the shredded document (ignoring case and non-alphabetic characters) and computes the probability that the letter is either in English or Spanish. It leverages two pre-supplied probability distributions for English and Spanish character frequencies, stored in `e.txt` and `s.txt`, respectively.

### Bayes Rule Formula:

We use the following Bayes rule to compute the probability \( P(Y = y | X) \):

\[
P(Y = y | X) = \frac{P(X | Y = y) P(Y = y)}{\sum\_{y' \in \{English, Spanish\}} P(X | Y = y') P(Y = y')}
\]

Where:

-   \( X \) is the observed vector of character counts.
-   \( Y \) is the language (either English or Spanish).
-   \( P(Y = y) \) is the prior probability of the language.

## Program Structure

### 1. Character Shredder

The function `shred(filename)` reads the provided text file and counts the occurrences of each letter (A-Z) in the document. This process is case-insensitive, and non-alphabetic characters are ignored. The output is a dictionary with each letter's count.

```python
def shred(filename):
    # Function implementation that reads the file and counts letters
```

### 2. Language Identification via Bayes Rule

Once the letter is shredded and the character frequencies are computed, the program applies Bayes rule to calculate the posterior probability of the letter being in English or Spanish. This is done using preloaded probability distributions for English and Spanish stored in `e.txt` and `s.txt`.

### 3. Computational Considerations

To avoid underflow issues that can arise from multiplying many small probabilities, the program performs the computations in the logarithmic domain. This ensures numerical stability, especially for longer texts.

The following logic is used to compute the log probabilities:

-   \( F(y) = \log P(Y = y) + \sum\_{i=1}^{26} X_i \log p_i \)

Where \( X_i \) is the count of the letter, and \( p_i \) is the probability of that letter in the corresponding language.

### 4. Output Specifications

The program generates four distinct outputs as described in the assignment:

-   **Q1**: A count of each letter in the shredded text.
-   **Q2**: Computed values of \( X_1 \log e_1 \) and \( X_1 \log s_1 \).
-   **Q3**: The log probabilities for English and Spanish.
-   **Q4**: The final posterior probability that the letter is in English.

## Prerequisites

-   Python 3.x
-   Required text files: `e.txt` (English character probabilities) and `s.txt` (Spanish character probabilities).

## Running the Program

To execute the program, use the following command:

```bash
python3 hw2.py [letter file] [english prior] [spanish prior]
```

-   `letter file`: The file containing the shredded letter text.
-   `english prior`: The prior probability that the letter is in English (e.g., 0.6).
-   `spanish prior`: The prior probability that the letter is in Spanish (e.g., 0.4).

### Example:

```bash
python3 hw2.py letter.txt 0.6 0.4
```

## File Descriptions

-   `hw2.py`: The main Python script containing the logic for shredding, calculating letter frequencies, and applying Bayes rule.
-   `e.txt`: Contains the 26-dimensional multinomial probability vector for English characters.
-   `s.txt`: Contains the 26-dimensional multinomial probability vector for Spanish characters.
-   `samples/`: Directory containing sample letter files and their expected outputs for testing.

## Sample Output

Here is an example of the output for the four questions:

**Q1 Output:**

```
Q1
A 2
B 1
...
Z 0
```

**Q2 Output:**

```
Q2
-0.1234
-0.5678
```

**Q3 Output:**

```
Q3
-12.3456
-13.5678
```

**Q4 Output:**

```
Q4
0.9234
```

The output should match the format described in the project specification to ensure compatibility with the autograder.

## References

-   [Python Documentation - sys module](https://docs.python.org/3/library/sys.html)
-   [Probabilistic Language Identification - Project Guidelines](CS_540_Fall_2024_HW2.pdf)
