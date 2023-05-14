#FOUNDATIONAL####

#!/usr/bin/env python3.7

#import os

#def get_file_info(path=None):
#    """
#    """
    
#    if path is None:
#        path = os.getcwd()  
#    file_list = []  

#    for dirpath, dirnames, filenames in os.walk(path):
#        for filename in filenames:
#            file_path = os.path.join(dirpath, filename)
#            file_stat = os.stat(file_path)

            
#            file_info = {
#                'filename': filename,
#                'path': file_path,
#                'size': file_stat.st_size,
#            }

#            file_list.append(file_info)  

#    return file_list


#file_list = get_file_info()

#for file_dict in file_list:
#    print(file_dict)
    
    
#ADVANCED####
#!/usr/bin/env python3.7

import os

def get_file_info(path=None):
    """
    Given a path, returns a list of dictionaries, each containing information about a file in the directory and its subdirectories.
    """
    
    if path is None:
        path = os.getcwd()  # If no path is provided, use the current working directory.
    file_list = []  # Initialize an empty list to hold the file information dictionaries.

   # Walk through the directory tree and iterate over each file in the directory and its subdirectories.
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
        # Join the directory path and the file name to create the file's full path.
            file_path = os.path.join(dirpath, filename)
        # Get the file's statistics, including its size.
            file_stat = os.stat(file_path)

        # Create a dictionary with the file's name, full path, and size.
            file_info = {
            'filename': filename,
            'path': file_path,
            'size': file_stat.st_size,
            }

            file_list.append(file_info)  # Add the file information dictionary to the list.
    return file_list


file_list = get_file_info()  # Call the function to get a list of file information dictionaries.

for file_dict in file_list:
    print(file_dict)  # Print each file information dictionary in the list.