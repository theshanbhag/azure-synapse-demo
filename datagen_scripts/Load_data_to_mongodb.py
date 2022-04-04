import csv
import pymongo

srv = "mongodb+srv://venkatesh:ashwin123@cluster1.2wqno.mongodb.net"
client = pymongo.MongoClient(srv, tlsAllowInvalidCertificates=True)
mydb = client["BigStore"]
mycol = mydb["Product"]

with open('retail-product-catalog.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    for row in csv_reader:
        product = {}
        if i != 0:
            product["ProductID"] = row[0]
            product["ProductName"] = row[1]
            product["Price"] = row[2]
            product["AlternateProductNumber"] = row[3]
            product["Affinity"] = row[4]
            product["GenderID"] = row[5]
            print(row)
            print(product)
            mycol.insert_one(product)
        else:
            pass
        i = i + 1
