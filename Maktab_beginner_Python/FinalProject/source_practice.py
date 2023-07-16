import hashlib
import csv
import collections
from typing import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    name_pass=OrderedDict()
    Pass=OrderedDict()
    HashPool=OrderedDict()
    with open( input_file_name,'r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            name=row[0]
            hashCode = row [1]
            name_pass[name]=hashCode
    for num in range(1000,9999):
        m = hashlib.sha256((str(num)).encode())
        m=m.hexdigest()
        HashPool[m]=num
    for k, v in list(name_pass.items()):
        key=HashPool.get(v)
        Pass[k]=key
    with open(output_file_name, 'w', newline='') as outfile:
            writer=csv.writer(outfile)
            for u,v in Pass.items():
                writer.writerow([u,v])                    
#hash_password_hack('D:\\Python\\MakPractices\\Final\\name_pass.csv','D:\\Python\\MakPractices\\Final\\pass.csv')