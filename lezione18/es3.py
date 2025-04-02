'''
Context Managers for File Handling: Use the with statement and context managers to open and close a file. 
Handle potential IOError within the with block for clean resource management.'''


try:
    with open("hbvhjbu.txt", "r") as file:
        content = file.read()
        print(content)
except IOError as e:
    print(f"An error occurred while handling the file: {e}")