import csv
from operator import itemgetter
from optparse import Values
# For the average
from statistics import mean 
import collections
from typing import Counter, OrderedDict
def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        with open(output_file_name, 'w', newline='') as outfile:
            writer=csv.writer(outfile)
            for row in reader:
                name = row[0]
                grade_mean = (float(grade) for grade in row [1:])
                writer.writerow([row[0],mean(grade_mean)])
def calculate_sorted_averages(input_file_name, output_file_name):
    name_scores=dict()
    name_scores_sorted=OrderedDict()
    with open( input_file_name,'r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            name=row[0]
            score = mean(float(grade) for grade in row [1:])
            name_scores[name]=score
           #sort_scores=sorted(name_scores.values(),reverse=True)
        sort_scores=sorted(name_scores.items(), key=itemgetter(1,0),reverse=False)
        with open(output_file_name, 'w', newline='') as outfile:
            writer=csv.writer(outfile)
            for u,v in sort_scores:
                writer.writerow([u,v])     
def calculate_three_best(input_file_name, output_file_name):
    name_scores=OrderedDict()
    s=list()
    name_scores=dict()
    name_scores_sorted=OrderedDict()
    with open( input_file_name,'r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            name=row[0]
            score = mean(float(grade) for grade in row [1:])
            name_scores[name]=score
           #sort_scores=sorted(name_scores.values(),reverse=True)
        sort_scores=sorted(name_scores.items(), key=itemgetter(1,0),reverse=False)
        Value_list=[v for v in name_scores.values()]
        Value_sorted=sorted(Value_list, reverse=True)
        counter=0
        name_sorted_reversed={v: k for k , v in name_scores.items()}
        Top_three=OrderedDict()
        keys=Tops=list()
        for i in range (0,3):
            for k , v in name_scores.items():
                if v==Value_sorted[i]:
                    keys.append(k)
                    Top_three[k]=v
    #print(Top_three)
    with open(output_file_name, 'w', newline='') as outfile:
        writer=csv.writer(outfile)
        for u,v in Top_three.items():
            #print(u,v)
            writer.writerow([u,v])    
def calculate_three_worst(input_file_name, output_file_name):
    name_scores=OrderedDict()
    s=list()
    name_scores=dict()
    name_scores_sorted=OrderedDict()
    with open( input_file_name,'r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            name=row[0]
            score = mean(float(grade) for grade in row [1:])
            name_scores[name]=score
           #sort_scores=sorted(name_scores.values(),reverse=True)
        sort_scores=sorted(name_scores.items(), key=itemgetter(1,0),reverse=False)
        Value_list=[v for v in name_scores.values()]
        Value_sorted=sorted(Value_list, reverse=False)
        counter=0
        name_sorted_reversed={v: k for k , v in name_scores.items()}
        worst_three=OrderedDict()
        keys=Tops=list()
        for i in range (0,3):
            for k , v in name_scores.items():
                if v==Value_sorted[i]:
                    keys.append(k)
                    worst_three[k]=v
    #print(Top_three)
    with open(output_file_name, 'w', newline='') as outfile:
        writer=csv.writer(outfile)
        for u,v in worst_three.items():
            #print(u,v)
            writer.writerow([v])      
def calculate_average_of_averages(input_file_name, output_file_name):
    name_scores=dict()
    name_scores_sorted=OrderedDict()
    count=0
    score=0
    name_scores=dict()
    name_scores_sorted=OrderedDict()
    with open( input_file_name,'r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            name=row[0]
            score = mean(float(grade) for grade in row [1:])
            name_scores[name]=score
           #sort_scores=sorted(name_scores.values(),reverse=True)
        Total_Average=mean([k for k in name_scores.values()])
        with open(output_file_name, 'w', newline='') as outfile:
            writer=csv.writer(outfile)
            writer.writerow([Total_Average])
