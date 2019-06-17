from itertools import islice
import csv
import codecs
import os

dictionary = {}
columnDictionary={}
fname_in = '/Users/suman.das/Downloads/EXP_ASSETS.txt'
fname_out = '/Users/suman.das/Downloads/EXP_ASSETS_OUT.csv'

# This method is used to read each line of master file an create a dictionary out of it
def process(line):
    fields = line.rstrip('\n').split()
    if fields[0] not in dictionary:
        dictionary[fields[0]] = [fields]
    elif type(dictionary[fields[0]]) == list:
        dictionary[fields[0]].append(fields)
    else:
        dictionary[fields[0]] = [dictionary[fields[0]], fields]



with open("/Users/suman.das/Downloads/Master_Data_Listing_20190515180330.txt", "r") as source:
    array = []
    for line in islice(source, 1, None):
        process(line)
    for key,value in dictionary.items() :
        #print(key)
        cols = []
        for idx, val in enumerate(value):
            if(idx==0):
                cols.append(val[4])
            else:
                cols.append(int(cols[idx-1]) + int(val[4]))
        columnDictionary[key.upper()]=cols;


    #print(columnDictionary)

with codecs.open(fname_in,'r', encoding='utf8') as fin, codecs.open(fname_out, 'wb', encoding='utf8') as fout:
    # for the csv file, must be open in binary mode
    writer = csv.writer(fout)
    #print(os.path.basename(fin.name).split(".")[0])
    cols=columnDictionary.get(os.path.basename(fin.name).split(".")[0])
    for line in fin:
        line = line.rstrip()  # removing the '\n' and other trailing whitespaces

        # Get the row (the list) of the column values.
        row = []  # init -- empty list
        pos1 = 0
        for pos2 in cols[0:]:
            value = line[int(pos1):int(pos2)]  # slice the column value
            value = value.rstrip()  # if you want to remove trailing whitespaces
            row.append(value)  # append to the row of values
            pos1 = int(pos2)  # get ready for the next column

        value = line[int(pos1):]  # last column value
        value = value.rstrip()  # if you want to remove trailing whitespaces
        row.append(value)  # append to the row of values

        # Process the row -- here print and writing to the CSV file.
        print(row)
        writer.writerow(row)






