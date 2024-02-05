import sys, os

class wc_tool:
    
    def __init__(self, command_name: str, file_name: str) -> None:

        #Safely opening the file with UTF-8 encoding
        with open(file_name, "r", encoding='utf-8') as reader:
            
            if (command_name.removeprefix('-') == 'c'):
                # From offset "0" we move our file cursor to the end of the file.
                reader.seek(0, os.SEEK_END)
                # reader.tell() tells the position (in bytes) of the cursor, 
                # and since it's the end of the file, it'll tell us the size of the file.
                print(f"The size of {file_name} is {reader.tell()} bytes.")

            elif (command_name.removeprefix('-') == 'l'):
                # Outputs the number of lines in a file
                lines = reader.readlines()
                print(f"File: {file_name} contains {len(lines)} lines.")

            elif (command_name.removeprefix('-') == 'w'):
                raw_data = reader.read()
                # split all words in the file by a comma to a list, so we can get the length of the list!
                lines = raw_data.split()
                print(f"File: {file_name} have {len(lines)} words.")
                
            
def main():
    command_name = sys.argv[1]
    file_name = sys.argv[2]
    print(command_name, ' ', file_name, ' ')
    wc_reader = wc_tool(command_name, file_name)

if __name__=="__main__":
    main()
