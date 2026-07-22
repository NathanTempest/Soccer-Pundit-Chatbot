# Assignment 1.3: Descriptive Statistics and Scriptural Analysis

This project performs quantitative textual analysis on the book of Genesis from the Bible using python's data analysis library `pandas` and built-in `statistics` module.

---

## Files

1. **[setup.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_1.3/setup.py)**: Loads the raw data, computes the `Word_Count` for each verse, and saves the intermediate preprocessed CSV.
2. **[analysis.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_1.3/analysis.py)**: Performs the descriptive statistical computations on word counts.
3. **[Jason_Nathaniel_Assignment_1_3.docx](file:///Users/nate/Development/Python/PyAlgs/Assignment_1.3/Jason_Nathaniel_Assignment_1_3.docx)**: The assignment submission document containing:
   - Setup and statistical tasks description.
   - Project pseudocodes.
   - Spiritual Reflection on scriptural text analysis and the misuses of "Bible codes".
   - Screenshot placeholder for console output.

---

## Setup and Execution

### Prerequisites
Install pandas library:
```bash
python3 -m pip install pandas --user
```

### Execution Steps
1. **Preprocess the dataset**:
   Run the setup script to load the raw data and generate the processed dataset `genesis_processed.csv`:
   ```bash
   python3 setup.py
   ```

2. **Run statistical analysis**:
   Run the analysis script to execute all descriptive statistics tasks:
   ```bash
   python3 analysis.py
   ```
