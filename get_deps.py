import os
import re
import subprocess

dir = os.listdir()
def print_lists(list, title):
    print(title)
    for i in list:
        print(i)
    print()

def lines_containing_import(filename):
    importModules = []
    importInstalls = []
    fromModules = []
    fromInstalls = []
    filename = filename+".py"
    with open(filename, 'r') as file:
        # Loop through each line in the file
        for line in file:
            # Print the line to the console
            if "import" in line:
                module = re.sub('\s+', ' ', line.strip())
                if line.startswith("import"):
                    moduleName = module.split(' ')[1]
                    if moduleName + ".py" in dir:
                        importModules.append(module)
                    else:
                        importInstalls.append(module)

                else:
                    moduleName = module.split(' ')[1]
                    if moduleName + ".py" in dir:
                        fromModules.append(module)
                    else:
                        fromInstalls.append(module)
    return importInstalls, importModules, fromInstalls, fromModules

imports_first = []
global_file_list = ['post_log_process']
file_queue = ['post_log_process']
global_import_list=[]
count_imports = 0
while len(file_queue)!=0:
    curr_file = file_queue[0]
    importInstalls, importModules, fromInstalls, fromModules = lines_containing_import(curr_file)
    global_import_list.extend(importInstalls)
    global_import_list.extend(importModules)
    global_import_list.extend(fromInstalls)
    global_import_list.extend(fromModules)
    imports_first.extend(importInstalls)
    imports_first.extend(fromInstalls)
    print("Processing " + curr_file)
    print_lists(importInstalls, "Import Installs")
    print_lists(importModules, "Import Modules")
    print_lists(fromInstalls, "From Installs")
    print_lists(fromModules, "From Modules")
    count_imports+= len(importInstalls) + len(importModules) + len(fromInstalls) + len(fromModules)
    for module in importModules:
        module = module.split(' ')[1]
        if module + ".py" in dir:
            if module not in global_file_list:
                global_file_list.append(module)
                file_queue.append(module)
        else:
            print(module + " is somewhere else. Please check")

    for module in fromModules:
        module = module.split(' ')[1]
        if module + ".py" in dir:
            if module not in global_file_list:
                global_file_list.append(module)
                file_queue.append(module)
        else:
            print(module + " is somewhere else. Please check")
    file_queue.pop(0)
    print()
    print()

print(global_file_list)

print(global_import_list)
print(len(global_import_list), count_imports)
import_set=set(global_import_list)
print(import_set)
print(len(import_set))
print(list(import_set))

print(imports_first)
print(len(imports_first))
imports_first_set = set(imports_first)
print(list(imports_first_set))
