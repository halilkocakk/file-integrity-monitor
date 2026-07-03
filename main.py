from enum import nonmember
from logger import write_log
from scanner import scan_folder
from hasher import calculate_sha256
from storage import save_baseline, load_baseline
from pathlib import Path
from comparator import compare_baselines
import time
from colorama import Fore, Style, init
init(autoreset=True)

def create_current_baseline(folder_path):
    files = scan_folder(folder_path)
    baseline = {}

    if not files:
        print("Folder is empty.")
        print("Nothing to scan.")
        return None

    for file in files:
        hash_value = calculate_sha256(file)
        baseline[str(file)] = hash_value

    return baseline

def print_report(results):

    statuses = ["new", "modified", "unchanged", "deleted"]
    new_count = len(results["new"])
    modified_count = len(results["modified"])
    unchanged_count = len(results["unchanged"])
    deleted_count = len(results["deleted"])

    total_files = new_count + modified_count + deleted_count + unchanged_count
    print("\n" + "=" * 45)
    print("            FILE INTEGRITY REPORT")
    print("=" * 45)
    print(f"Total files: {total_files}")
    print(Fore.GREEN + f"new files: {new_count}")
    print(Fore.YELLOW + f"Modified files: {modified_count}")
    print(Fore.BLUE + f"Unchanged files: {unchanged_count}")
    print(Fore.RED + f"Deleted files: {deleted_count}")


    for status, files in results.items():
        print(f"\n {status.upper()} ({len(files)})")
        print("-" * 30)

        if not files:
            print("No files.")
        else:
            for file in files:
                print(file)

start_time = time.time()

folder_path = input("Enter folder path: ")

folder = Path(folder_path)

if not folder.exists():
    print("Folder does not exist..")
    exit()

if not folder.is_dir():
    print("This path is not a folder.")
    exit()

current_baseline = create_current_baseline(folder)

if current_baseline is None:
    exit()

if not Path("baseline.json").exists():
    results = {
        "new": list(current_baseline.keys()),
        "modified": [],
        "deleted": [],
        "unchanged": []
    }

    print_report(results)
    save_baseline(current_baseline)
    print("Baseline created successfully.")

else:
    old_baseline = load_baseline()
    results = compare_baselines(old_baseline, current_baseline)
    print_report(results)
    save_baseline(current_baseline)
    print("\nBaseline updated successfully.")

end_time = time.time()
duration = end_time - start_time
print(f"\nScan completed in {duration:.2f} seconds.")
write_log(results, duration, folder_path)
print("Log saved to scan.log")
