from os import walk

def walker(root_path):
    # example: root_path = "/Users/dchen2/Desktop/db/"
    with open("paths.txt", 'w') as fp:  
        for (dirpath, dirnames, filenames) in walk(root_path):
                for j in filenames:
                    fp.writelines(dirpath+j+'\n')

def walker_arr(root_path):
    # example: root_path = "/Users/dchen2/Desktop/db/"
    output = [] 
    for (dirpath, dirnames, filenames) in walk(root_path):
            for j in filenames:
                output.append(dirpath+j)
    return output
