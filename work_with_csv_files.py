import csv

with open('results.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    line_count1 = 0
    summ = 0
    for row in csv_reader:
        line_count+=1
        summ+=int(row['Latency'])
        if int(row['Latency'])>400:
            line_count1+=1
    average=summ/line_count
    print(f'\tAverage value of Latency column is: {average}.')
    print(f'\t{line_count1} times latency reached over 400 ms.')
