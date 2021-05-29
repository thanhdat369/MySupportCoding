def get_list_label(path_label_file):
    names = []
    with open(path_label_file,'r') as f:
        for line in f:
            names.append(line.strip())
    return names

def write_labels_file(path,list_label):
    with open(path,'w') as f:
        for line in list_label:
            f.writelines(f'{line}\n')
    print(f"Write success {path}")