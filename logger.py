from datetime import datetime

def write_log(results, duration, folder_path):
    with open("scan.log", "a") as log_file:

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write("=" * 50 + "\n")
        log_file.write(f"Scan Date: {current_time}\n")
        log_file.write(f"Folder: {folder_path}\n")
        log_file.write(f"Scan Duration: {duration:.2f} seconds\n\n")

        for status, files in results.items():
            log_file.write(f"\n{status.upper()} ({len(files)})\n")

            if not files:
                log_file.write("No files.\n")
            else:
                for file in files:
                    log_file.write(f"- {file}\n")

        log_file.write(f"New: {len(results['new'])}\n")
        log_file.write(f"Modified: {len(results['modified'])}\n")
        log_file.write(f"Deleted: {len(results['deleted'])}\n")
        log_file.write(f"Unchanged: {len(results['unchanged'])}\n")

        log_file.write("=" * 50 + "\n\n")
