import os
from flask import Flask, request, jsonify
from opensearchpy import OpenSearch, NotFoundError
import urllib3

# Disable SSL warnings for self-signed certs (safe for dev only)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# OpenSearch client configuration
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'Str0ng@Passw0rd!'),  # Replace with your actual password
    use_ssl=True,
    verify_certs=False,
    ssl_show_warn=False
)

INDEX_NAME = "student_records"