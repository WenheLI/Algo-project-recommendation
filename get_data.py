import pandas as pd

HOST = './data'

def get_netflix():
    data = pd.read_csv('../input/combined_data_1.txt', header = None, names = ['Cust_Id', 'Rating'], usecols = [0,1])
    print(data)

if __name__ == '__main__':
    get_netflix()
