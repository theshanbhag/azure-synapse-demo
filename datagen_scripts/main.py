import csv
import string
import random
import time

import pycountry
import pymongo

srv = "mongodb+srv://venkatesh:ashwin123@cluster1.2wqno.mongodb.net"
client = pymongo.MongoClient(srv,tlsAllowInvalidCertificates=True)
mydb = client["BigStore"]
mycol = mydb["Orders"]

# VOWELS = "aeiou"
# CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
#
#
# def generate_word(length):
#     word = ""
#     for i in range(length):
#         if i % 2 == 0:
#             word += random.choice(CONSONANTS)
#         else:
#             word += random.choice(VOWELS)
#     return word


def random_date(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


with open('retail-product-catalog.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    retail_data = {}
    i = 1
    x = 0
    product_id = []

    for row in csv_reader:
        if line_count!= 0:
            product_id.append(row[0])
        line_count = line_count+1

    for j in range(0, 300):
        i = i + 1
        retail_data = {}
        ProductID = random.choice(product_id)
        retail_data["RowID"] = j
        retail_data["OrderID"] = ProductID + "-" + str(j)
        retail_data["OrderDate"] = random_date("1/1/2021 1:30 PM", "1/3/2021 4:50 AM", '%m/%d/%Y %I:%M %p',random.random()).split(" ")[0]
        retail_data["ShipDate"] = random_date("2/3/2021 1:30 PM", "1/6/2021 4:50 AM", '%m/%d/%Y %I:%M %p',random.random()).split(" ")[0]
        retail_data["ShipMode"] = random.choice(["Fright", "Container", "By Road", "flight"])
        retail_data["CustomerID"] = random.randint(0,1000)
        retail_data["CustomerName"] = random.choice(["Jack", "Jhon", "Gabe", "Max", "Phill", "Jane", "Alan", "Olly"]) + " " + random.choice(["Smith", "Doe", "Watts", "Raynods", "Ryan", "Dunn", "King"])
        retail_data["Segment"] = random.choice(["Consumer", "Corporate"])
        retail_data["ProductID"] = ProductID
        retail_data["Price"] = random.randint(100,1000)
        retail_data["Sales"] = random.randint(1, 1000)
        retail_data["Region"] = random.choice(["North", "East", "South", "West"])
        retail_data["State"] = random.choice(["Florida", "California", "North Carolina", "Utah", "Texas", "Alaska", "Hawaii", "Verginia", "NY"])
        retail_data["State"] = "USA"
        retail_data["Profit"] = random.randint(1,100)

        print(retail_data)
        mycol.insert_one(retail_data)