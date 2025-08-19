#using a function to create and add content to the file
def create_file():
    filename = "sample.txt"
    content = "This is the original content.\nFeel free to modify me!.\nThis is a fun topic learning about the \\n, r,w and a"
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f"File '{filename}' created and written successfully.")

#using a function to ask user to open the file
def handle_user_file():
    user_file = input("Enter the filename you want to read(include the file extension; .txt, .pdf): ")

    try:
        with open(user_file, 'r') as f:
            data = f.read()
            print("File content:")
            print(data)
    except FileNotFoundError:
        print("Error: That file does not exist.")
    except PermissionError:
        print("Error: File could not be read. You do not have the permission.")

# Run both parts
create_file()
handle_user_file()