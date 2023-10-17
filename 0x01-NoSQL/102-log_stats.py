#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
improve by adding top 10 most present IPs in collection nginx
database logs
"""
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace 'localhost:27017' with your MongoDB server address
db = client['logs']  # Connect to the 'logs' database
collection = db['nginx']  # Connect to the 'nginx' collection

# Get number of documents in the collection
total_logs = collection.count_documents({})

# Get methods count
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = [collection.count_documents({"method": method}) for method in methods]

# Get count of logs with method=GET and path=/status
special_logs_count = collection.count_documents({"method": "GET", "path": "/status"})

# Print the statistics
print(f"{total_logs} logs")
print("\t" + "\n\t".join([f"{count} {method}" for method, count in zip(methods, method_counts)]))
print(f"\t{special_logs_count} method=GET path=/status")
