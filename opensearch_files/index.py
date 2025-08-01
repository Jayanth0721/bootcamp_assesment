from opensearchpy import OpenSearch
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to OpenSearch
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'Str0ng@Passw0rd!'),
    use_ssl=True,
    verify_certs=False,
    ssl_show_warn=False
)

# Load mapping
with open('mapping.json') as f:
    mapping = json.load(f)

index_name = "student_records"

# Check if index exists
if not client.indices.exists(index=index_name):
    print(f"Creating index '{index_name}'...")
    client.indices.create(index=index_name, body=mapping)
else:
    print(f"Index '{index_name}' already exists.")

# Sample documents to insert
docs = [
    {"student_id": "S101", "name": "Amit Sharma", "age": 21, "course": "Python", "score": 88.5},
    {"student_id": "S102", "name": "Neha Singh", "age": 22, "course": "Data Science", "score": 92.3},
    {"student_id": "S103", "name": "Ravi Kumar", "age": 20, "course": "Java", "score": 78.0},
]

print("Inserting sample documents...")
for doc in docs:
    client.index(index=index_name, id=doc["student_id"], body=doc)

client.indices.refresh(index=index_name)  # Make sure data is searchable

# Query all documents to verify
response = client.search(index=index_name, body={"query": {"match_all": {}}})

print(f"Found {response['hits']['total']['value']} documents:")
for hit in response['hits']['hits']:
    print(hit["_source"])
