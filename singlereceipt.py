import requests
# id = "7619cd53-f9b2-4244-53e2-363b82426948"
# URL = "https://u0crtzygx1-u0pjswn6co-connect.us0-aws.kaleido.io/reply/" + id
#
# AUTH = ('u0fm1uuvgk','uegeOUJqKDHA4-3UfXg2wKvLs1VEUBzQ4nfwezg_2_Y')
# r = requests.get(url=URL, auth=AUTH)
# data = r.json()
# print(data)
# print(data['gasUsed'])
# print(data['headers']['timeElapsed'])


import requests
import csv
with open("single_id_seller.csv",'r') as r , open("single_output_seller.csv","a") as w:
    reader = csv.reader(r)
    writer = csv.writer(w,lineterminator='\n')
    c = 1
    for row in reader:
        id = row[0]

        URL = "https://u0crtzygx1-u0pjswn6co-connect.us0-aws.kaleido.io/reply/" + id

        AUTH = ('u0fm1uuvgk', 'uegeOUJqKDHA4-3UfXg2wKvLs1VEUBzQ4nfwezg_2_Y')
        r = requests.get(url = URL,auth=AUTH)
        data = r.json()
        print(data)
        print(data['gasUsed'])
        print(data['headers']['timeElapsed'])

    # creating a csv writer object
        row = []
        row.append(c)
        row.append(data['gasUsed'])
        row.append(data['cumulativeGasUsed'])
        row.append(data['headers']['timeElapsed'])
        # writing the fields
        writer.writerow(row)
        c=c+1
        print(c)


with open("single_id_buyer.csv",'r') as r , open("single_output_buyer.csv","a") as w:
    reader = csv.reader(r)
    writer = csv.writer(w,lineterminator='\n')
    c = 1
    for row in reader:
        id = row[0]

        URL = "https://u0crtzygx1-u0pjswn6co-connect.us0-aws.kaleido.io/reply/" + id

        AUTH = ('u0fm1uuvgk', 'uegeOUJqKDHA4-3UfXg2wKvLs1VEUBzQ4nfwezg_2_Y')
        r = requests.get(url = URL,auth=AUTH)
        data = r.json()
        print(data)
        if 'gasUsed' in data.keys():
            print(data['gasUsed'])
            print(data['headers']['timeElapsed'])

        # creating a csv writer object
            row = []
            row.append(c)
            row.append(data['gasUsed'])
            row.append(data['cumulativeGasUsed'])
            row.append(data['headers']['timeElapsed'])
            # writing the fields
            writer.writerow(row)
            c=c+1
            print(c)