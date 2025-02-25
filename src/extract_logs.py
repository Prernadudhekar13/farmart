#!/usr/bin/env python3
import sys
import os
import datetime

def main():
    # Check for the correct usage
    if len(sys.argv) < 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    target_date = sys.argv[1]

    # Validate date format
    try:
        datetime.datetime.strptime(target_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    # Define the log file path (modify if needed)
    log_file_path = "large_log.txt"

    # Create output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(log_file_path, "r", encoding="utf-8") as log_file, \
             open(output_file_path, "w", encoding="utf-8") as out_file:
            for line in log_file:
                # Ensure the line is long enough to contain a date
                if len(line) < 10:
                    continue
                line_date = line[:10]
                if line_date == target_date:
                    out_file.write(line)
    except FileNotFoundError:
        print(f"Log file '{log_file_path}' not found.")
        sys.exit(1)

    print(f"Logs for {target_date} have been extracted to: {output_file_path}")

if __name__ == "__main__":
    main()
