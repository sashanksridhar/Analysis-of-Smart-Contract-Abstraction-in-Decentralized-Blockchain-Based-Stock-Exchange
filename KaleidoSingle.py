import csv
import requests
with open("input.csv",'r') as r:
    reader = csv.reader(r)

    for row in reader:
        print(row)
        if(row[2]=='-1'):
            URL = "https://u0crtzygx1-u0pjswn6co-connect.us0-aws.kaleido.io/contracts/4654613af40fd5f160ea137bc1089c0868a4c0f8/placeOrder"
            PARAMS = {'kld-from':'0xE01cA9f8DB66e67c3aF8eC93F6E777E9D7B997B6'}
            AUTH = ('u0fm1uuvgk','uegeOUJqKDHA4-3UfXg2wKvLs1VEUBzQ4nfwezg_2_Y')
            DATA = {
              "_orderSide": 1,
              "_quantity": row[0],
              "_stockPrice": row[1]
            }

            r = requests.post(url = URL,params=PARAMS,auth=AUTH, data = DATA)
            data = r.json()
            print(r.json())
            id = data['id']
            print(id)
            with open("single_id_seller.csv", 'a') as csvfile:
                # creating a csv writer object
                row = []
                csvwriter = csv.writer(csvfile, lineterminator='\n')
                row.append(id)
                # writing the fields
                csvwriter.writerow(row)
        elif(row[2]=='1'):
            URL = "https://u0crtzygx1-u0pjswn6co-connect.us0-aws.kaleido.io/contracts/4654613af40fd5f160ea137bc1089c0868a4c0f8/placeOrder"
            PARAMS = {'kld-from':'0x16A8B0B7A1b4aB18263033c553969433Fd8f3682',
                      'kld-ethvalue': int(row[0])*int(row[1])
                      }
            AUTH = ('u0fm1uuvgk','uegeOUJqKDHA4-3UfXg2wKvLs1VEUBzQ4nfwezg_2_Y')
            DATA = {
              "_orderSide": 0,
              "_quantity": row[0],
              "_stockPrice": row[1]
            }

            r = requests.post(url = URL,params=PARAMS,auth=AUTH, data = DATA)
            data = r.json()
            print(r.json())
            id = data['id']
            print(id)
            with open("single_id_buyer.csv", 'a') as csvfile:
                # creating a csv writer object
                row = []
                csvwriter = csv.writer(csvfile, lineterminator='\n')
                row.append(id)
                # writing the fields
                csvwriter.writerow(row)
