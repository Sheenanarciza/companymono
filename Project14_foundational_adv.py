#!/usr/bin/env python3.7

# Assigns the current working directory to the variable 'cd'
cd = os.getcwd()

# Create an empty list to store file information
file_list = []

# Create an empty dictionary to store file path and size information
file_dict = {}

# Define a function to get all files in a directory
def get_dir_file(current_directory):
    # Use os.walk() function to get directory tree information
    dir_tree_info= os.walk(current_directory)
    # Call the look_through_directory function to process directory information
    look_through_directory(dir_tree_info)

# Define a function to look through the directory and get all files and their sizes
def look_through_directory(dir_info):
    # Use a for loop to iterate through the directory information
    for root, sub_dir_names, file_names in dir_info:
        # Check if there are any subdirectories in the current directory
        if len(sub_dir_names) != 0:
            # Use another for loop to iterate through all subdirectories
            for sub_dir_name in sub_dir_names:
                # Use another for loop to iterate through all files in the current subdirectory
                for each_file in file_names:
                    # Check if the current file is a file and not a directory
                    if os.path.isfile(each_file) == True:
                        # Print the file information to the console
                        print(f"{os.path.isfile(each_file)}, 'path' : {root}, {sub_dir_name}, {each_file}, 'size' : {os.path.getsize(each_file)}")
                        # Get the file path and size
                        file_path = os.path.join(root, each_file)
                        file_size = os.path.getsize(each_file)
                        # Add the file path and size to the file dictionary
                        file_dict[file_path] = file_size
                        # Append an empty dictionary to the file list
                        file_list.append({''})

# Get the user input for the directory pathway
current_directory = input("Enter your directory pathway (your current working directory is set by default): ")
# Check if the user input is empty
if len(current_directory) == 0:
    # Set the current directory to the current working directory
    current_directory = os.getcwd() 
# Call the get_dir_file function to get all files in the directory
get_dir_file(current_directory)
print(*<variable_name>, sep="\n")