import os
import pandas as pd

def main():
    print("--- STEP 1: LOADING DATA ---")
    # Load dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'Genesis_Data.csv')
    print(f"Loading dataset from '{csv_path}'...")
    df = pd.read_csv(csv_path)
    
    print("\n--- STEP 2: CREATING WORD COUNT COLUMN ---")
    # Compute Word_Count column
    df['Word_Count'] = df['Text'].apply(lambda x: len(str(x).split()))
    
    # Save the processed dataset
    processed_path = os.path.join(script_dir, 'genesis_processed.csv')
    print(f"Saving processed dataset with Word_Count to '{processed_path}'...")
    df.to_csv(processed_path, index=False)
    
    # Output quick confirmation statistics
    print("\n--- SETUP SUCCESSFUL ---")
    print(f"Total verses processed: {len(df)}")
    print(f"Processed columns: {list(df.columns)}")
    print("\nFirst 3 rows sample:")
    print(df[['Chapter', 'Verse', 'Word_Count', 'Text']].head(3).to_string(index=False))

if __name__ == "__main__":
    main()
