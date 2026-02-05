# NetDetect: Machine Learning-Based Network Intrusion Detection

**Project By: Alexander Padin, Alejandro Marchini, and Dillard Holder**

MSAAI-540-Group-5 | January 2026  
Graduate Students | Masters in Applied Artificial Intelligence | University of San Diego  

---

## Introduction

Enterprise networks generate massive volumes of traffic that must be continuously monitored to detect malicious activity. Traditional rule-based intrusion detection systems often struggle to keep up with evolving attack techniques, leading to missed threats and increased analyst workload.

This project applies machine learning techniques to automatically detect malicious network behavior and classify attack categories from network flow data. The system aims to improve detection accuracy, reduce false negatives, and support Security Operations Center (SOC) analysts by automating traffic classification and reducing manual triage effort.

---

## Objective

The primary objective of this project is to design and implement a supervised machine learning intrusion detection system capable of:

- Classifying network traffic as **Benign or Malicious**
- Identifying the **type of attack** when malicious behavior is detected
- Demonstrating an **end-to-end machine learning workflow**
- Applying **basic MLOps practices** such as reproducibility and monitoring

The system uses a hierarchical two-stage classifier:

- **Stage 1:** Binary Classification (Benign vs Malicious)
- **Stage 2:** Multi-class Attack Classification (DoS, Exploits, Reconnaissance, Fuzzers, etc.)

---

## Dataset

This project uses multiple publicly available intrusion detection datasets containing labeled network flow records:

- **UNSW-NB15** — Modern intrusion detection dataset with diverse attack categories (~175K records)
- **CIC-IDS2017** — Large-scale enterprise intrusion detection dataset (>1M records)
- **TON_IoT** — Realistic network traffic dataset for IoT/IIoT environments (>100K records)

These datasets provide diverse traffic environments and attack behaviors. Combining them helps improve model generalization and reduce dataset-specific bias.

---

## Methodology

1. **Data Collection**  
   Multiple intrusion detection datasets are ingested and unified.

2. **Data Pre-processing**  
   Clean missing/inconsistent values, normalize features, encode categorical variables, and address class imbalance.

3. **Feature Engineering**  
   Map datasets into a canonical schema and harmonize attack labels across sources.

4. **Model Building**  
   Implement machine learning models suitable for tabular data such as Random Forest and Gradient Boosting.

5. **Model Training**  
   Train hierarchical classifiers using labeled network flow data.

6. **Model Evaluation**  
   Evaluate performance using precision, recall, F1-score, confusion matrix, and emphasis on high recall for malicious classes.

7. **Model Monitoring & Validation**  
   Monitor model performance, prediction drift, and data quality before releasing new versions.

---

## Technologies Used

- Python
- Scikit-learn
- Pandas / NumPy
- Matplotlib / Seaborn
- AWS / Cloud (e.g., Sagemaker, JupyterLabs)

---

## Quick Start
1. Launch AWS Academy Learner Lab
2. Start JupyterLab
3. Clone the repository
    ```
    git clone https://github.com/apadin-repo/AAI-511-04-Group-3.git
    ```
4. Run the notebooks sequentially to reproduce the full pipeline:

**Exploratory Data Analysis**
- `1.EDA/1.load_data_in_athena.ipynb`
- `1.EDA/2.EDA_CIC-IDS2017.ipynb`
- `1.EDA/...`

**Feature Engineering** 
- `2.feature-eng/1.merge_datasets.ipynb`
- `2.feature-eng/2.normalize_attack_categories.ipynb`
- `2.feature-eng/...`
    
---

## License

This project is for educational purposes as part of the MSAAI program at the University of San Diego.
