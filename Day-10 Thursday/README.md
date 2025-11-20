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
                            
                            echo "Choose an option:"
                            echo "1) Create File"
                            echo "2) Delete File"
                            echo "3) Copy File"
                            read -p "Enter your choice (1/2/3): " choice
                            
                            case $choice in
                            
                            1)
                                read -p "Enter the filename to create: " filename
                                touch "$filename"
                                echo "File '$filename' created successfully."
                                ;;
                            
                            2)
                                read -p "Enter the filename to delete: " filename
                                if [ -f "$filename" ]; then
                                    rm "$filename"
                                    echo "File '$filename' deleted."
                                else
                                    echo "File not found!"
                                fi
                                ;;
                            
                            3)
                                read -p "Enter source file: " src
                                read -p "Enter destination file: " dest
                                if [ -f "$src" ]; then
                                    cp "$src" "$dest"
                                    echo "File copied from '$src' to '$dest'."
                                else
                                    echo "Source file not found!"
                                fi
                                ;;
                            
                            *)
                                echo "Invalid option"
                                ;;
                            
                            esac


<img width="817" height="573" alt="Screenshot from 2025-11-20 19-42-03" src="https://github.com/user-attachments/assets/79046358-d6a7-413d-957c-000ed70c8b6d" />

<img width="817" height="573" alt="Screenshot from 2025-11-20 19-52-46" src="https://github.com/user-attachments/assets/e0f60f29-6969-486d-83f9-c10734e9f954" />

<img width="817" height="573" alt="Screenshot from 2025-11-20 20-20-11" src="https://github.com/user-attachments/assets/afe0a242-0af4-41f3-bd19-a86170473138" />
