# Content-Based AI Recommendation Engine

An algorithmic recommendation engine that maps user profiles to specific item attributes through feature normalization, token alignment, and mathematical similarity metrics.

## Project Overview

In modern information systems, users frequently encounter choice overload. While collaborative filtering relies heavily on community behavior and historical user-item interactions, it suffers from severe limitations such as the cold-start problem for new items or users. 

This project implements a pure Content-Based Filtering engine developed as part of the DecodeLabs Industrial Training framework. It bypasses community dependency by evaluating the intrinsic properties of items against an explicit user preference state. By mapping both items and user inputs into a unified feature space, the system establishes a deterministic recommendation pipeline driven by mathematical overlap rather than behavioral heuristics.

## System Architecture and Workflow

The recommendation framework operates as a structured three-phase pipeline: Input, Process, and Output.

### 1. Input Phase (Data Acquisition and Profiling)
* **Item Representation:** The catalog consists of discrete items containing descriptive metadata and standardized attribute tags.
* **User Profile Vector:** The user provides text-based inputs representing specialized skills or areas of interest. 

### 2. Process Phase (Feature Mapping and Similarity Scoring)
* **Vocabulary Standardization:** Raw text strings are parsed, stripped of whitespace, and converted to a uniform lower-case format to prevent token mismatches (e.g., ensuring "Web Design" and "frontend development" do not fail due to casing or naming conventions).
* **Mathematical Vectorization:** The system extracts unique vocabulary across the data attributes to represent items as set boundaries.
* **Jaccard Similarity Coefficient:** To evaluate pattern alignment without complex neural architectures, the engine calculates the Jaccard similarity coefficient between the user interest set ($A$) and each item feature set ($B$). The metric computes the ratio of the size of the intersection to the size of the union of the sets:

$$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$

### 3. Output Phase (Ranking and Top-N Selection)
* **Score Sorting:** The entire item collection is scored sequentially against the user profile. Items are sorted in descending order based on their computed Jaccard coefficient.
* **Truncation and Filtering:** The system applies a Top-N truncation filter to isolate the highest-scoring recommendations. Items with a similarity score of zero are explicitly discarded to maintain strict contextual relevance.

## Tech Stack

* Python 3.x (Standard Library)

## File Structure

* `dataset.py`: Contains the structured catalog items and their normalized attribute tags.
* `recommendation_engine.py`: Contains the Jaccard similarity matrix calculations, the sorting pipeline logic, and the command-line interface execution framework.
* `README.md`: System documentation and architectural specifications.

## How to Run

To run the recommendation engine locally, execute the main script from your terminal or command prompt:

```bash
python recommendation_engine.py