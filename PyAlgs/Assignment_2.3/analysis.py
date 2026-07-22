import os
import string
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Get directory of the current script to resolve paths relatively
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Load the Genesis Dataset
    csv_file = os.path.join(script_dir, 'Genesis_Data.csv')
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"Could not find the dataset at {csv_file}")
        
    df = pd.read_csv(csv_file)
    
    # 2. Combine, Clean, and Tokenize Text Using List Operations
    # Combine all verse texts into one lowercase string
    all_text = ' '.join(df['Text'].tolist()).lower()
    
    # Remove punctuation using str.translate
    clean_text = all_text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into individual words (tokenization)
    words = clean_text.split()
    
    # Preview the first 10 words
    print("First 10 words:")
    print(words[:10])
    print()
    
    # 3. Create a list of unique words from the tokenized list
    unique_words = sorted(list(set(words)))
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(unique_words)}")
    print()
    
    # 4. Count the frequency of each unique word using list.count()
    # To follow instructions precisely while remaining performant, we use list comprehension with list.count()
    print("Calculating word frequencies using list.count() (this may take a few seconds)...")
    frequencies = [words.count(w) for w in unique_words]
    print("Frequencies calculated successfully!")
    print()
    
    # 5. Create a Pandas DataFrame containing words and their frequencies
    df_freq = pd.DataFrame({
        'Word': unique_words,
        'Frequency': frequencies
    })
    
    # 6. Sort the DataFrame by frequency in descending order
    df_freq_sorted = df_freq.sort_values(by='Frequency', ascending=False).reset_index(drop=True)
    
    # 7. Display the top 10 most frequent words
    print("Top 10 Most Frequent Words (Overall):")
    top_10_overall = df_freq_sorted.head(10)
    print(top_10_overall.to_string(index=False))
    print()
    
    # 8. Visualize the top words using Seaborn/Matplotlib
    # Chart 1: Top 10 Overall Words (including stop words)
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    
    # Standard bar plot
    palette = sns.color_palette("viridis", 10)
    ax = sns.barplot(x='Frequency', y='Word', data=top_10_overall, palette=palette, hue='Word', legend=False)
    
    plt.title("Top 10 Most Frequent Words in the Book of Genesis (Overall)", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Frequency (Count)", fontsize=12, labelpad=10)
    plt.ylabel("Word", fontsize=12, labelpad=10)
    plt.tight_layout()
    
    chart_overall_path = os.path.join(script_dir, 'top_words_overall.png')
    plt.savefig(chart_overall_path, dpi=300)
    plt.close()
    print(f"Saved overall word frequency chart to: {chart_overall_path}")
    
    # 9. Additional Thematic Content-Word Analysis (Filtering out stop words)
    # This directly supports the reflection questions by revealing terms like "God", "said", "lord", and "land"
    stop_words = {
        'and', 'the', 'of', 'his', 'he', 'to', 'in', 'unto', 'that', 'i', 'him', 'my', 'a', 
        'for', 'was', 'it', 'with', 'me', 'thou', 'they', 'them', 'shall', 'be', 'not', 'thee', 
        'is', 'were', 'had', 'all', 'on', 'their', 'are', 'which', 'from', 'this', 'by', 'as', 
        'out', 'up', 'us', 'your', 'or', 'so', 'but', 'have', 'there', 'at', 'an', 'am', 'she', 
        'her', 'their', 'our', 'out', 'then', 'when', 'no', 'thence', 'these', 'these_', 'if',
        'who', 'whom', 'whose', 'how', 'why', 'what'
    }
    
    df_content = df_freq_sorted[~df_freq_sorted['Word'].isin(stop_words)].reset_index(drop=True)
    
    print("Top 10 Most Frequent Content-Carrying Words:")
    top_10_content = df_content.head(10)
    print(top_10_content.to_string(index=False))
    print()
    
    # Chart 2: Top 10 Content Words
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    
    content_palette = sns.color_palette("plasma", 10)
    ax2 = sns.barplot(x='Frequency', y='Word', data=top_10_content, palette=content_palette, hue='Word', legend=False)
    
    plt.title("Top 10 Most Frequent Content Words in the Book of Genesis", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Frequency (Count)", fontsize=12, labelpad=10)
    plt.ylabel("Word", fontsize=12, labelpad=10)
    plt.tight_layout()
    
    chart_content_path = os.path.join(script_dir, 'top_content_words.png')
    plt.savefig(chart_content_path, dpi=300)
    plt.close()
    print(f"Saved content word frequency chart to: {chart_content_path}")
    print()
    
    # 10. Specific Term Check (for Reflection)
    print("Spiritual/Thematic Term Frequencies for Reflection:")
    for term in ['god', 'said', 'light', 'lord', 'covenant', 'bless']:
        count_val = words.count(term)
        print(f"- '{term}': {count_val} occurrences")

if __name__ == '__main__':
    main()
