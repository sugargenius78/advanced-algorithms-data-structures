# Algorithms and Advanced Data Structures (Python & UML)

## Overview
A comprehensive suite of data processing algorithms, regex-driven extraction pipelines, and structural data modeling developed for Big Data processing and data warehousing. Built for the Algorithms and Data Structures module (SEN5003) under the Cardiff Metropolitan University curriculum. Grade Achieved: 70% (First-Class Honours / Distinction).

## System Architecture & Implemented Modules

### 1. Data Access & Authentication Layer (`group1_access.py`)
- **Credential Validation & Password Policy:** Algorithmic complexity enforcement checking length, numeric, and character constraints via regular expressions (`re`).
- **Duplicate Prevention:** In-memory traversal preventing duplicate entity registration across user databases.
- **Search & Retrieval:** Sequential ID and username lookup logic with formatted terminal table presentation.

### 2. Entity Extraction & Security Classification (`group2_extraction.py`)
- **Automated Regex Extraction:** Extracts unstructured contact records (emails), currency amounts (prices), and brand entities from raw text (`social_media_data.txt`).
- **Tiered Security Storage:** Segregates extracted data into multi-level categories:
  - `HIGH_SECURITY`: Confidential personal information (emails).
  - `LOW_SECURITY`: Public commercial entities (brands and price points).
- **Formatted Persistence:** Serializes categorized records into formatted hierarchical JSON (`classified_results.json`).

### 3. Structural Data Modeling & Complex Architectures (UML)
- **Time-Based Dictionary Sorting:** Algorithmic activity model sorting key-value records by timestamps.
- **Sequential Array Sorting:** Bubble sort state-flow model for alphabetic character sequences.
- **Hierarchical Search Trees:** Structured tree models for domain/email resolution (`TLD -> Domain -> User`) and geographic drill-down (`Country -> State -> City -> ZIP`).
- **Multi-Relational Business Graphs:** Network models connecting commercial entities (Company, Product, Brand, Location) with directed relational edges.

## Technology Stack
- **Language:** Python 3 (`re`, `json`, `time`)
- **Data Interchange:** JSON (`classified_results.json`), Text parsing (`social_media_data.txt`)
- **Modeling & Design:** UML Activity Diagrams, Object Trees, and Graph Models

## Repository Structure
- `group1_access.py` - Core access control, password security, and retrieval algorithms
- `group2_extraction.py` - Pattern-based extraction and security classification engine
- `social_media_data.txt` - Raw unstructured dataset source
- `classified_results.json` - Serialized multi-tier classified output
- `st20320120 SEN5003 WRIT1 (2).pdf` - Complete coursework research paper, UML diagrams, and documentation

## How to Run
```bash
# Execute access and authentication routines
python group1_access.py

# Execute extraction and classification pipeline
python group2_extraction.py
