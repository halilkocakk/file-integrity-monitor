from scanner import scan_folder
from hasher import calculate_sha256
from storage import save_baseline, load_baseline
from pathlib import Path
from comparator import compare_baselines

def create_current_baseline(folder_path):
    files = scan_folder(folder_path)
    baseline = {}

    for file in files:
        hash_value = calculate_sha256(file)
        baseline[str(file)] = hash_value

    return baseline

def print_report(results):
    print("\n===== INTEGRITY REPORT =====")

    for status, files in results.items():
        print(f"\n {status.upper()} ({len(files)})")
        print("-" * 30)

        if not files:
            print("No files.")
        else:
            for file in files:
                print(file)


folder_path = input("Enter folder path: ")

current_baseline = create_current_baseline(folder_path)

if not Path("baseline.json").exists():
    save_baseline(current_baseline)
    print("Baseline created successfully.")

else:
    old_baseline = load_baseline()
    results = compare_baselines(old_baseline, current_baseline)
    print_report(results)
    save_baseline(current_baseline)
    print("\nBaseline updated successfully.")
