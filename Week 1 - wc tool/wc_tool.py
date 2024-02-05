import sys, os, io

class wc_tool:
    
    def __init__(self, file_name: str, command_name: str = '') -> None:

        #Safely opening the file with UTF-8 encoding
        with open(file_name, "r", encoding='utf-8') as reader:
            
            #Handle the edge case first of not getting an input! (Fail Fast)
            if (command_name == ''):
                lines_count = self.get_number_of_lines(reader, file_name)
                words_count = self.get_number_of_words(reader, file_name)
                characters_count = self.get_number_of_bytes(reader, file_name)
                print(f'This file have {lines_count} lines, {words_count} words, {characters_count} characters.')
            elif (command_name.removeprefix('-') == 'c'):
                self.get_number_of_bytes(reader, file_name)
            elif (command_name.removeprefix('-') == 'l'):
                self.get_number_of_lines(reader,file_name)
            elif (command_name.removeprefix('-') == 'w'):
                self.get_number_of_words(reader, file_name)
            elif (command_name.removeprefix('-') == 'm'):
                self.get_number_of_multilines_char(reader, file_name) 
    
    def get_number_of_bytes(self, reader: io.TextIOWrapper, file_name: str) -> int:
        # From offset "0" we move our file cursor to the end of the file.
        reader.seek(0, os.SEEK_END)
        # reader.tell() tells the position (in bytes) of the cursor, 
        # and since it's the end of the file, it'll tell us the size of the file.
        number_of_bytes = reader.tell()
        print(f"The size of {file_name} is {number_of_bytes} bytes.")
        return number_of_bytes

    def get_number_of_lines(self, reader: io.TextIOWrapper, file_name: str) -> int:
        # Outputs the number of lines in a file
        lines = reader.readlines()
        print(f"File: {file_name} contains {len(lines)} lines.")
        return len(lines)
    
    def get_number_of_words(self, reader: io.TextIOWrapper, file_name: str) -> int:
        #Reseting the seek pointer, since readlines() changes the seek index
        reader.seek(0)
        raw_data = reader.read()
        # split all words in the file by a comma to a list, so we can get the length of the list!
        lines = raw_data.split()
        num_of_words = len(lines)
        print('text: ', num_of_words)
        print(f"File: {file_name} have {num_of_words} words.")
        return num_of_words
    
    def get_number_of_multilines_char(self, reader: io.TextIOWrapper, file_name: str) -> int:
        raw_data = reader.read()
        # split all words in the file by a comma to a list, so we can get the length of the list!
        lines = raw_data.split()
        characters_count = sum(len(word) for word in lines)
        print(f"File: {file_name} have {characters_count} characters.")  
        return characters_count
            
def main():
    if  len(sys.argv) < 2:
        print('File name is not provided!') 
        exit(0)
    elif len(sys.argv) == 2:
        file_name = sys.argv[1]
        command_name = ''
        print(file_name, ' ')
    else:
        command_name = sys.argv[1] 
        file_name = sys.argv[2]
        print(command_name, ' ', file_name, ' ')

    wc_tool(file_name, command_name)

if __name__=="__main__":
    main()
