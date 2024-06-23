#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".



def main() -> None:
    
    
    # Get template
    with open(".\Input\Letters\starting_letter.txt","r") as l:
        letter_content = l.read()
        l.close()
        
    # Get all names
    
    with open(".\Input\\Names\invited_names.txt","r") as n:
        name_list = n.readlines()
        n.close()
        
    for name in name_list:
        tmp_name = name.strip()
        
        with open(f".\Output\ReadyToSend\letter_for_{tmp_name}.txt","w") as f:
            f.write(letter_content.replace("[name]",tmp_name))
            f.close()
    
    
        
    
    
    
    

if __name__ == "__main__":
    main()