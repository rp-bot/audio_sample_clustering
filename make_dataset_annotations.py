import os
import pandas as pd
import librosa

def analyze_wav_files(directory):
    result = []

    for subdir, _, files in os.walk(directory):
        wav_files = [f for f in files if f.endswith('.wav')]
        for wav_file in wav_files:
            file_path = os.path.join(subdir, wav_file)

            # Get the length of the .wav file using librosa
            try:
                duration = librosa.get_duration(path=file_path)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                continue

            # Extract subdirectory name
            subdirectory_name = os.path.basename(subdir)

            # Append data to result
            result.append({
                'file_path':file_path,
                'Subdirectory': subdirectory_name,
                'File Name': wav_file,
                'Length (seconds)': round(duration, 2)
            })

    return result

def save_results_to_csv(results, output_file):
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)

def print_results(results):
    print(f"{'Subdirectory':<20}{'File Name':<30}{'Length (seconds)':<15}")
    print('-' * 65)
    for entry in results:
        print(f"{entry['Subdirectory']:<20}{entry['File Name']:<30}{entry['Length (seconds)']:<15}")

if __name__ == "__main__":
    directory_to_analyze = "data/Drum_Kit_Sound_Samples"
    output_csv_file = "data/Drum_Kit_Sound_Samples/annotations.csv"

    if os.path.isdir(directory_to_analyze):
        results = analyze_wav_files(directory_to_analyze)
        save_results_to_csv(results, output_csv_file)
        print(f"Results saved to {output_csv_file}")
    else:
        print("The provided directory does not exist.")
