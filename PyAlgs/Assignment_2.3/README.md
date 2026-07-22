# Assignment 2.3: Exploring Genesis — Word Frequency Analysis

This directory contains Python programs and a dynamically compiled APA-formatted MS Word report for the word frequency analysis and visualization of the Genesis dataset.

---

## Files

1. **[Genesis_Data.csv](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.3/Genesis_Data.csv)**: The raw dataset containing all verses of the book of Genesis.
2. **[analysis.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.3/analysis.py)**: Performs text cleaning, tokenization, word counting (using `list.count()`), Pandas operations, and generates/saves data visualizations using Seaborn and Matplotlib.
3. **[generate_doc.py](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.3/generate_doc.py)**: Programmatically constructs the final APA-formatted report.
4. **[top_words_overall.png](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.3/top_words_overall.png)**: Visual horizontal bar chart of the top 10 most frequent words overall.
5. **[top_content_words.png](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.3/top_content_words.png)**: Visual horizontal bar chart of the top 10 content-carrying words.
6. **[Jason_Nathaniel_Assignment_2_3.docx](file:///Users/nate/Development/Python/PyAlgs/Assignment_2.3/Jason_Nathaniel_Assignment_2_3.docx)**: The final generated APA-formatted Word report with embedded code, output logs, reflections, and charts.

---

## Execution Steps

### Prerequisites
Make sure you run using the project virtual environment (which has the correct packages pre-installed):
```bash
# Path to python environment with seaborn, matplotlib, pandas, and python-docx
/Users/nate/Development/Python/venc/bin/python3
```

### Running Analysis & Visualizations
To execute the analysis script and export the bar charts, run:
```bash
/Users/nate/Development/Python/venc/bin/python3 analysis.py
```
This output logs word statistics and creates the PNG files in the same directory.

### Generating the MS Word Report
To compile the final report (which dynamically reads `analysis.py` code and embeds the generated charts), execute:
```bash
/Users/nate/Development/Python/venc/bin/python3 generate_doc.py
```
This creates or updates `Jason_Nathaniel_Assignment_2_3.docx` in the directory.
