<h2>Log Filtering Automation Script — Shell Scripting Project</h2>

This project is a Linux shell script designed to help developers extract relevant log entries from a noisy system log file. It prompts the user for a keyword, checks whether that keyword exists in the log, and saves the filtered output to a clean text file.
<br>
<br>
<br>


<h3>📝 Problem Statement</h3>

Developers often work with very large and noisy log files containing thousands of lines. Manually searching for specific events or errors becomes time-consuming and error-prone.
<br>
<br>
<br>


            GNU nano 6.2                                                                            log_filter.sh *
                  
                    
                    #!/bin/bash
                    
                    # Define the log files
                    
                    INPUT_LOG="system_events.log"
                    OUTPUT_LOG="filtered_logs_s1_q5.txt"
                    
                    # Demonstrate System Credentials
                    
                    echo "=========================================="
                    echo "System Credentials: "
                    echo "User: $(whoami)"
                    echo "Host: $(hostname)"
                    echo "=========================================="
                    echo ""
                    
                    # Ask for the filtering parameter
                    
                    read -r -p "Enter the keyword to filter the logs (e.g., 'DB_CONN', 'ModuleA', 'ERROR'): " FILTER_KEYWORD
                    
                    # Check if the keyword is empty
                    
                    if [ -z "$FILTER_KEYWORD" ]; then
                        echo "No filter keyword provided. Exiting."
                        exit 1
                    fi
                    
                    # Check if keyword exists in the file
                    
                    if ! grep -q "$FILTER_KEYWORD" "$INPUT_LOG"; then
                        echo "No matching logs found for keyword: '$FILTER_KEYWORD'"
                        echo "Exiting..."
                        exit 1
                    fi
                    
                    # Perform the filtering
                    
                    echo "Filtering '$INPUT_LOG' for keyword: '$FILTER_KEYWORD'"
                    grep "$FILTER_KEYWORD" "$INPUT_LOG" > "$OUTPUT_LOG"
                    echo ""
                    
                    # Display success message
                    
                    echo "Done! $(wc -l < "$OUTPUT_LOG") matching log lines extracted."
                    echo "Results saved to: $OUTPUT_LOG"
                    
<br>
<br>
<br>
<img width="1919" height="1108" alt="image" src="https://github.com/user-attachments/assets/203b2a11-44c1-49f3-af16-b5657958259c" />




