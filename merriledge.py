import csv
brokerage = 0
with open("input.csv",'r') as r:
    reader = csv.reader(r)

    for row in reader:
        print(brokerage)
        number = int(row[0])
        price = int(row[1])
        cost = number*(price/10000)
        broker = 0
        if cost-1500<0:
            broker+= cost * 5/100
            brokerage+=broker
            continue
        broker += 1500 * 5 / 100
        cost = cost - 1500

        if cost-3500<0:
            broker+= cost * 2.25/100
            brokerage+=broker
            continue
        broker += 3500 * 2.25 / 100
        cost = cost - 3500

        if cost-15000<0:
            broker+= cost * 1.75/100
            brokerage+=broker
            continue
        broker += 15000 * 5 / 100
        cost = cost - 15000

        if cost-30000<0:
            broker+= cost * 1.5/100
            brokerage+=broker
            continue
        broker += 30000 * 1.5 / 100
        cost = cost - 30000

        if cost-50000<0:
            broker+= cost * 1/100
            brokerage+=broker
            continue
        broker += 50000 * 1 / 100
        cost = cost - 50000

        if cost-400000<0:
            broker+= cost * 0.75/100
            brokerage+=broker
            continue
        broker += 400000 * 0.75 / 100
        cost = cost - 400000

        if cost>=500000:
            broker+= cost * 0.5/100
            brokerage+=broker
            continue

print("Final")
print(brokerage)