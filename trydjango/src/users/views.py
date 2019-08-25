from django.shortcuts import render
from django.http import HttpResponse
import csv
import os
from .models import User
from django.views import defaults
from random import *
print(os.getcwd())
# Create your views here.
'''
def all_names(request):
    #return HttpResponse("Hello from posts")

    # enter the function that parses the csv and return a list of names

    name_list = []
    with open('names.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            name_list.append(row[1])
    #print(name_list)
    
    #return render(request, 'users/all_names.html')
    return render(request, 'users/all_names.html', {"names": name_list})
    return HttpResponse(names)
'''
columns = ["id","name"]
def get_all_names(request):
    #return HttpResponse("Hello from posts")

    # enter the function that parses the csv and return a list of names
    name_list = []
    with open('names.csv', 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            name_list.append(row['name'])
    
    #return render(request, 'users/all_names.html')
    return render(request, 'users/all_names.html', {"names": name_list})
    #return HttpResponse(names)

def get_name_by_id(request, id=1):

    dict_csv = {}
    with open('names.csv', 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            dict_csv[row['id']] = row['name']

            #if row['id'] == id:
            #    name = row['name']
        if '1' in dict_csv.keys():
            #print(dict_csv)
            name = dict_csv['1']
            return render(request, 'users/name_by_id.html', {'name':name})
        else:
            return defaults.page_not_found(request, '404.html')

def delete_name_by_id(request, id=1):
    dict_csv = {}
    with open('names.csv', 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            dict_csv[row['id']] = row['name']
    if '1' in dict_csv.keys():
        del dict_csv['1']
        with open('del_csv.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns)
            writer.writeheader()
            for key,value in dict_csv.items():
                writer.writerow({"id":key,"name":value})
        return render(request, 'users/delete_name.html')
    else:
        return defaults.page_not_found(request, '404.html')

def post_name(request, name):
    dict_csv = {}
    with open('names.csv', 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            dict_csv[row['id']] = row['name']
    new_id = choice([i for i in range(1,100) if i not in dict_csv.keys()])   

    
    with open('names.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writerow({'id': new_id, 'name': name})
        return HttpResponse('The name {0} with id {1} was inserted'.format(name,new_id))

def put_name(request, id, name):
    dict_csv = {}
    with open('names.csv', 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            dict_csv[row['id']] = row['name']  
    dict_csv[id]=name    
    
    with open('names.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for key,value in dict_csv.items():
            writer.writerow({"id":key,"name":value})
        return HttpResponse('The csv was updated with name {0} and id {1}.'.format(name,id))

    





