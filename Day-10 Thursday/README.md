**TASK - Case Task**

                          read -p "Enter Choice: " choice
                          case $choice in
                          1) echo "This is new file" >> Ntext.txt ;;
                          2) read -p "Creating new Dir" NewDir mkdir NewDir;;
                          3) ls;;
                          *) echo "Invalid" ;;
                          esac



<img width="1195" height="319" alt="Screenshot from 2025-11-20 14-57-38" src="https://github.com/user-attachments/assets/45b08125-ae24-4a47-8bc7-40d117592d41" />

**TASK - Name Task**

                          read -p "Enter your name: " name
                          echo $name
                          
                          read -p "Enter your age: " age
                          echo $age
                          
                          if [[ $name =~ [a-zA-Z/_]+$ ]] && (( age > 0 && age < 100 )); then
                                  echo "Correct"
                          else
                                  echo "Not Correct"
                          fi


<img width="779" height="290" alt="Screenshot from 2025-11-20 15-33-59" src="https://github.com/user-attachments/assets/6da0cf6d-a2f1-4d26-b85d-765bc0b5cb68" />


**TASK - System Stats**


                          read -p "Do you need system stats: " t
                          if t==cpu; then
                                  lscpu
                          elif t==memory; then
                                  free -h
                          elif t==disc; then
                                  df -h
                          elif t==network; then
                                  ip -a
                          else
                                  echo "Bye Bye"
                          fi







<img width="1280" height="795" alt="Screenshot from 2025-11-20 15-43-13" src="https://github.com/user-attachments/assets/c25ec946-4e3a-4dcc-a1d7-f3b3aad2564f" />

<img width="1280" height="795" alt="Screenshot from 2025-11-20 15-44-05" src="https://github.com/user-attachments/assets/3ae5647e-0e3f-4d5a-a64c-a95afdb72077" />

<img width="1280" height="795" alt="Screenshot from 2025-11-20 15-44-43" src="https://github.com/user-attachments/assets/299dd952-9d4e-4fee-9c7c-51ecf2563179" />

<img width="1280" height="795" alt="Screenshot from 2025-11-20 15-45-30" src="https://github.com/user-attachments/assets/81aee809-caf3-4baa-9c23-ebe809b5d52d" />



**TASK - File Management Script**

#!/bin/bash

                                                    # --- Main Menu Display ---
                                                    echo "--- Simple File Operations ---"
                                                    echo "U@sys: Do you wish to create(1), delete(2) or move(3) file?"
                                                    read -p "Enter choice (1/2/3): " CHOICE
                                                    
                                                    # --- Input Validation and Execution ---
                                                    
                                                    case $CHOICE in
                                                        1)
                                                            # Create Operation
                                                            read -p "Enter the file name to create: " FILENAME
                                                            if touch "$FILENAME"; then
                                                                echo "** $FILENAME created.**"
                                                            else
                                                                echo "Error: Could not create file $FILENAME."
                                                            fi
                                                            ;;
                                                    
                                                        2)
                                                            # Delete Operation
                                                            read -p "Enter file/dir name to delete (file or dir): " TYPE
                                                            read -p "Enter the name of the item to delete: " ITEM_NAME
                                                    
                                                            if [[ "$TYPE" == "file" ]]; then
                                                                if [[ -f "$ITEM_NAME" ]]; then
                                                                    rm "$ITEM_NAME"
                                                                    echo "** File deleted.**"
                                                                else
                                                                    echo "File not found."
                                                                fi
                                                            elif [[ "$TYPE" == "dir" ]]; then
                                                                if [[ -d "$ITEM_NAME" ]]; then
                                                                    rm -r "$ITEM_NAME" # -r needed for directories
                                                                    echo "** Directory deleted.**"
                                                                else
                                                                    echo "Dir not found."
                                                                fi
                                                            else
                                                                echo "Error: Invalid type. Please enter 'file' or 'dir'."
                                                            fi
                                                            ;;
                                                    
                                                        3)
                                                            # Move Operation
                                                            read -p "Which item do you wish to move (file or dir)? " TYPE
                                                            read -p "Enter the source item name: " SOURCE
                                                            read -p "Enter the destination directory: " DEST
                                                    
                                                            if [[ -f "$SOURCE" || -d "$SOURCE" ]]; then # Checks if source exists (file or dir)
                                                                if [[ -d "$DEST" ]]; then # Checks if destination is a valid directory
                                                                    mv "$SOURCE" "$DEST"
                                                                    echo "** Item found, moving.**"
                                                                else
                                                                    echo "Dir not found."
                                                                fi
                                                            else
                                                                echo "File/Dir not found."
                                                            fi
                                                            ;;
                                                    
                                                        *)
                                                            # Default case for invalid input
                                                            echo "Error: Invalid operation ($CHOICE). Please enter 1, 2, or 3."
                                                            ;;
                                                    esac
                                                    
                                                    echo "--- Operation complete. ---"



