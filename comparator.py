def compare_baselines(old_baseline, new_baseline):
    results = {
        "new": [],
        "modified": [],
        "deleted": [],
        "unchanged": [],
    }

    for file_path, new_hash in new_baseline.items():
        if file_path not in old_baseline:
            results["new"].append(file_path)
        elif old_baseline[file_path] != new_hash:
            results["modified"].append(file_path)
        else:
            results["unchanged"].append(file_path)
        for file_path in old_baseline[file_path]:
            if file_path not in new_baseline:
                results["deleted"].append(file_path)

        return results
