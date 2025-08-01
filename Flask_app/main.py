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

@app.route('/')
def home():
    return "Welcome to the Student Records API. Use /student endpoints."

@app.route('/student', methods=['POST'])
def add_student():
    data = request.json
    student_id = data.get("student_id")
    if not student_id:
        return jsonify({"error": "student_id is required"}), 400
    # Index the document
    client.index(index=INDEX_NAME, id=student_id, body=data)
    return jsonify({"message": "Student added", "student_id": student_id}), 201

@app.route('/student/<student_id>', methods=['GET'])
def get_student(student_id):
    try:
        response = client.get(index=INDEX_NAME, id=student_id)
        return jsonify(response['_source']), 200
    except NotFoundError:
        return jsonify({"error": "Student not found"}), 404

@app.route('/student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        client.delete(index=INDEX_NAME, id=student_id)
        return jsonify({"message": "Student deleted", "student_id": student_id}), 200
    except NotFoundError:
        return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
