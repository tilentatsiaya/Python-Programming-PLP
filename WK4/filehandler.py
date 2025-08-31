# Open a file in write mode ('w')
file_out= open('newFile.pdf', 'w')
content_out = "Hello World, this is amazing!\n"
file_out.write(content_out)
file_out.write("This is a second line.\n")
file_out.close()

# Now, let's read the content from the file.
file_in = open('newFile.pdf', 'r')
content_in = file_in.read()
print("Content read from the file:")
print(content_in)
file_in.close()

try:
    # Ask the user for the filename
    input_file = input("Please enter the filename to read from: ")
    output_file = input("Please enter the filename to write to: ")  
except FileNotFoundError:
    # This block runs if the open() call fails because the file doesn't exist.
    print(f"Error: The file '{input_file}' was not found.")
    print("Please make sure the file exists and try again.")
    print(f"Error: The file '{output_file}' was not found.")
    print("Please make sure the file exists and try again.")
except Exception as e:
    # This is a general error handler for any other unexpected issues
    print(f"An unexpected error occurred: {e}")