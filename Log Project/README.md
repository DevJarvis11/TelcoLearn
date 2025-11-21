**Log Filtering Automation Script — Shell Scripting Project**

This project is a Linux shell script designed to help developers extract relevant log entries from a noisy system log file. It prompts the user for a keyword, checks whether that keyword exists in the log, and saves the filtered output to a clean text file.

**📝 Problem Statement**

Developers often work with very large and noisy log files containing thousands of lines. Manually searching for specific events or errors becomes time-consuming and error-prone.

  **Objective:**
  Create a shell script that:
  
  Accepts a keyword from the user.
  
  Checks if the keyword exists in the log file.
  
  Filters and extracts ONLY matching log lines.
  
  Saves them to a clean output file.

  Displays user credentials (username + hostname) as proof of system execution.

  **🎯 Expected Output**
  
  The script should generate:
  
  ✔ A terminal output that shows:
  
  System username
  
  System hostname
  
  Whether the keyword was found
  
  Total number of matching lines
  
  Output file location
