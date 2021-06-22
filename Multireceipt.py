import requests
import csv
import csv
with open("multiple_id_seller.csv",'r') as r , open("multiple_output_seller.csv","a") as w:
    reader = csv.reader(r)
    writer = csv.writer(w,lineterminator='\n')
    c = 1
    for row in reader:
        id = row[0]


        URL = "https://u0fmwjtwgo-u0paizg9v1-connect.us0-aws.kaleido.io/replies/"+id

        AUTH = ('u0rf6wzu4m', 'I5jrT_aM0BxkFLKfJ4CK6elxMD_36MLfQJInfoFKTYM')
        r = requests.get(url = URL,auth=AUTH)
        data = r.json()
        print(data)
         print(data['gasUsed'])
         print(data['headers']['timeElapsed'])

      creating a csv writer object
         row = []
         row.append(c)
         row.append(data['gasUsed'])
         row.append(data['cumulativeGasUsed'])
         row.append(data['headers']['timeElapsed'])
          writing the fields
         writer.writerow(row)
         c=c+1
         print(c)

 with open("multiple_id_buyer.csv",'r') as r , open("multiple_output_buyer.csv","a") as w:
     reader = csv.reader(r)
     writer = csv.writer(w,lineterminator='\n')
     c = 1
     for row in reader:
         id = row[0]


         URL = "https://u0fmwjtwgo-u0m86q3xii-connect.us0-aws.kaleido.io/reply/"+id

         AUTH = ('u0rf6wzu4m', 'I5jrT_aM0BxkFLKfJ4CK6elxMD_36MLfQJInfoFKTYM')
         r = requests.get(url = URL,auth=AUTH)
         data = r.json()
         print(data)
         print(data['gasUsed'])
         print(data['headers']['timeElapsed'])

      creating a csv writer object
         row = []
         row.append(c)
         row.append(data['gasUsed'])
         row.append(data['cumulativeGasUsed'])
         row.append(data['headers']['timeElapsed'])
          writing the fields
         writer.writerow(row)
         c=c+1
         print(c)