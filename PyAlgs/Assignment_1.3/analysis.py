import os
import pandas as pd
import statistics

def main():
    print("=================================================================")
    print("         GENESIS DATASET: DESCRIPTIVE STATISTICS REPORT          ")
    print("=================================================================\n")
    
    # Load the processed dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    processed_path = os.path.join(script_dir, 'genesis_processed.csv')
    df = pd.read_csv(processed_path)
    word_counts = df['Word_Count'].tolist()
    
    # Task 1: Calculate the mean word count per verse
    mean_val = statistics.mean(word_counts)
    print(f"Task 1: Mean Word Count Per Verse: {mean_val:.2f} words")
    
    # Task 2: Calculate the median number of words per verse
    median_val = statistics.median(word_counts)
    print(f"Task 2: Median Word Count Per Verse: {median_val:.1f} words")
    
    # Task 3: Find the mode (most frequent word count per verse)
    mode_val = statistics.mode(word_counts)
    print(f"Task 3: Mode (Most Frequent Word Count): {mode_val} words")
    
    # Task 4: Measure the standard deviation of word counts
    stdev_val = statistics.stdev(word_counts)
    print(f"Task 4: Standard Deviation of Word Counts: {stdev_val:.2f} words")
    
    # Task 5: Identify the shortest and longest verses by word count
    min_wc = min(word_counts)
    max_wc = max(word_counts)
    
    shortest_verses = df[df['Word_Count'] == min_wc]
    longest_verses = df[df['Word_Count'] == max_wc]
    
    print("\nTask 5: Shortest and Longest Verses:")
    print(f"  - Shortest Word Count: {min_wc} words")
    for _, row in shortest_verses.iterrows():
        print(f"    Reference: Genesis {row['Chapter']}:{row['Verse']}")
        print(f"    Text: \"{row['Text'].strip()}\"")
        
    print(f"\n  - Longest Word Count: {max_wc} words")
    for _, row in longest_verses.iterrows():
        print(f"    Reference: Genesis {row['Chapter']}:{row['Verse']}")
        print(f"    Text: \"{row['Text'].strip()}\"")
        
    # Task 6: Count how many verses have a word count above the average
    above_avg_count = sum(1 for count in word_counts if count > mean_val)
    percentage_above = (above_avg_count / len(word_counts)) * 100
    print(f"\nTask 6: Verses Above Average Word Count:")
    print(f"  - Count: {above_avg_count} out of {len(word_counts)} verses ({percentage_above:.2f}%)")
    
    # Task 7: Compare the word count spread in the first 10 chapters vs. the last 10 chapters of Genesis
    # Find the maximum chapter number in the dataset (Genesis has 50 chapters)
    max_chapter = df['Chapter'].max()
    first_10_df = df[df['Chapter'] <= 10]
    last_10_df = df[df['Chapter'] > (max_chapter - 10)]
    
    first_counts = first_10_df['Word_Count'].tolist()
    last_counts = last_10_df['Word_Count'].tolist()
    
    print(f"\nTask 7: Compare Word Count Spread (First 10 vs. Last 10 Chapters):")
    print(f"  - First 10 Chapters (Chapters 1 to 10, total verses: {len(first_counts)}):")
    print(f"    Mean:   {statistics.mean(first_counts):.2f} words")
    print(f"    Median: {statistics.median(first_counts):.1f} words")
    print(f"    Mode:   {statistics.mode(first_counts)} words")
    print(f"    StDev:  {statistics.stdev(first_counts):.2f} words")
    print(f"    Min:    {min(first_counts)} words")
    print(f"    Max:    {max(first_counts)} words")
    
    print(f"\n  - Last 10 Chapters (Chapters {max_chapter-9} to {max_chapter}, total verses: {len(last_counts)}):")
    print(f"    Mean:   {statistics.mean(last_counts):.2f} words")
    print(f"    Median: {statistics.median(last_counts):.1f} words")
    print(f"    Mode:   {statistics.mode(last_counts)} words")
    print(f"    StDev:  {statistics.stdev(last_counts):.2f} words")
    print(f"    Min:    {min(last_counts)} words")
    print(f"    Max:    {max(last_counts)} words")
    
    print("\n=================================================================")

if __name__ == "__main__":
    main()
