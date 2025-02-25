# Discussion

## Problem Statement

The task is to extract log entries from a large log file (~1TB) based on a given date (`YYYY-MM-DD`). Each log entry follows the format:
Example:

## Approaches Considered

### 1. Streaming Approach
- **Method:** Read the file line-by-line and write out entries matching the target date.
- **Pros:** 
  - Low memory usage since the file is processed one line at a time.
  - Simple and effective for one-off queries.
- **Cons:** 
  - May be slow for repeated queries since the entire file is scanned each time.

### 2. Indexing Approach
- **Method:** Build an index mapping dates to file offsets for fast lookups.
- **Pros:** 
  - Fast retrieval for repeated queries.
- **Cons:** 
  - Index creation is time-consuming and adds extra complexity.
  - Requires additional storage for the index.

## Final Solution

We chose the **streaming approach** due to its simplicity and minimal memory footprint, which is acceptable for occasional queries.

## How to Run the Solution

1. **Prerequisites:**  
   - Python 3.x must be installed.
   - Place your large log file (`large_log.txt`) in the repository root.

2. **Execution:**  
   Run the following command in the terminal:
   ```bash
   python src/extract_logs.py 2024-12-01
