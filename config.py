
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://atultvarghese:WyFCmcnrkkEQasDM@clueless-mallu.p6zv9hp.mongodb.net/?retryWrites=true&w=majority&appName=clueless-mallu&ssl=true&ssl_cert_reqs=CERT_NONE"

# Create a new client and connect to the server
client = MongoClient(uri, connect=False)

db = client.todo_data
collection = db["todo_data"]