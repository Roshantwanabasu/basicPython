import  csv
with open("New.csv","w", newline='') as csvfile:
    filewriter = csv.writer(csvfile )
    data = [['ID','Date'],
            ['1','2017-01-02'],
            ['2','2017-02-13'],
            ['3','2017-03-16'],
            ['4','2018-04-13'],
            ['5','2018-05-10'],
            ['6','2018-06-11'],
            ['7','2018-07-12']]
    filewriter.writerows(data)
data1 = [['22'],['23'],['16'],['18'],['25'],['24'],['21']]

with open('New.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('new1.csv', 'w') as csvfile1:
        writer = csv.writer(csvfile1)
        writer.writerow(next(reader) + ['Age'])
        for x in data1:
            writer.writerow(next(reader) + x)

with open('New.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('date.csv', 'w') as csvfile1:
        writer = csv.writer(csvfile1, delimiter = ' ')
        for row in reader:
            writer.writerow(row[1])

with open('New.csv', 'r', newline='') as csvfile:
    with open('id.csv', 'w', ) as csvfile1:
        reader = csv.reader(csvfile)
        writer = csv.writer(csvfile1, delimiter = ' ')
        for row in reader:
            writer.writerow(row[0])


