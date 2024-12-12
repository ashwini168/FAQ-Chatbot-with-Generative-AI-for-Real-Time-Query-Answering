import chardet

# Detect the encoding of the file
file_path = "/content/code.csv"

try:
    with open(file_path, "rb") as file:
        result = chardet.detect(file.read())
        encoding = result['encoding']
        print(f"Detected encoding: {encoding}")

    # Load the file using the detected encoding
    import pandas as pd
    df = pd.read_csv(file_path, encoding=encoding)
    print("File loaded successfully!")
    print(df.head())  # Display the first few rows of the data
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")


    # Preprocess the data (stripping spaces and removing duplicates)
df['prompt'] = df['prompt'].str.strip()
df['response'] = df['response'].str.strip()
df.drop_duplicates(subset='prompt', inplace=True)

