import csv
import requests
with open("input.csv",'r') as r:
    reader = csv.reader(r)

    for row in reader:
        print(row)
        if(row[2]=='-1'):
            URL = "https://u0fmwjtwgo-u0paizg9v1-connect.us0-aws.kaleido.io/gateways/u0dvsxwem1/0x105a03ed8c9911a1e3d399e8ce3e50af9d8f9f2f/placeSellOrder"
            PARAMS = {'kld-from':'0x2Df9B603dEc0Cb45AC25cD2A93D0db370439FFb7',
                      'kld-sync':True}
            AUTH = ('u0rf6wzu4m', 'I5jrT_aM0BxkFLKfJ4CK6elxMD_36MLfQJInfoFKTYM')
            DATA = {
              "centralexchange": "0x40fc88ae6b3a3de7f109bc29962798d2cbf92718",
              "noOfStocks": int(row[0]),
              "oprice": int(int(row[1])/1000000)
            }
            print(DATA)

            r = requests.post(url = URL,params=PARAMS,auth=AUTH, data = DATA)
            data = r.json()
            print(r.json())
            id = data['headers']['id']
            print("seller")
            print(id)

            with open("multiple_id_seller.csv", 'a') as csvfile:
                # creating a csv writer object
                row = []
                csvwriter = csv.writer(csvfile, lineterminator='\n')
                row.append(id)
                # writing the fields
                csvwriter.writerow(row)

            with open("multiple_output_seller.csv", 'a') as csvfile:
                # creating a csv writer object
                row = []
                csvwriter = csv.writer(csvfile, lineterminator='\n')
                row.append(data['gasUsed'])
                row.append(data['cumulativeGasUsed'])
                row.append(data['headers']['timeElapsed'])

                # writing the fields
                csvwriter.writerow(row)

        elif(row[2]=='1'):
            URL = "https://u0fmwjtwgo-u0m86q3xii-connect.us0-aws.kaleido.io/gateways/buyer/0xac3f2aad37a200c313c3b749cbac4ad199addff3/placeBuyOrder"
            PARAMS = {'kld-from':'0x3f42f10F9915b7Bd7df792394fE865B130B77D03',
                      'kld-sync': True}
            AUTH = ('u0rf6wzu4m', 'I5jrT_aM0BxkFLKfJ4CK6elxMD_36MLfQJInfoFKTYM')
            DATA = {
              "centralexchange": "0x40fc88ae6b3a3de7f109bc29962798d2cbf92718",
              "company": "0x105a03ed8c9911a1e3d399e8ce3e50af9d8f9f2f",
              "noOfStocks": int(row[0]),
              "oprice": int(int(row[1])/1000000)
            }

            r = requests.post(url = URL,params=PARAMS,auth=AUTH, data = DATA)
            data = r.json()
            print(r.json())
            id = data['headers']['id']
            print("buyer")
            print(id)
            with open("multiple_id_buyer.csv", 'a') as csvfile:
                # creating a csv writer object
                row = []
                csvwriter = csv.writer(csvfile, lineterminator='\n')
                row.append(id)
                # writing the fields
                csvwriter.writerow(row)

            with open("multiple_output_buyer.csv", 'a') as csvfile:
                # creating a csv writer object
                row = []
                csvwriter = csv.writer(csvfile, lineterminator='\n')
                row.append(data['gasUsed'])
                row.append(data['cumulativeGasUsed'])
                row.append(data['headers']['timeElapsed'])

                # writing the fields
                csvwriter.writerow(row)
