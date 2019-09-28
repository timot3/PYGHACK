import torch

def extract_data_from_file(file, num_rows):
    list_data = []
    with open(file, 'r') as fin:
        line = fin.readline()
        counter = 1
        while line:
            list_data.append(list(map(float, line.split(',')[1:])))
            if counter % 100000 == 0:
                print("%.2f%% Finished" % (counter / num_rows * 100))
            
            line = fin.readline()
            counter = counter + 1
    raw_data = torch.as_tensor(list_data).float()
    
    labels = raw_data[:,-1]
    features = raw_data[:,:-1]

    return (labels, features)

def normalize(x):
    return (x - x.mean()) / x.std()
            
        