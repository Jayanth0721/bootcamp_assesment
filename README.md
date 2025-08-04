# OpenSearch + Flask + Git Mini Project



## Step 1:
- use Docker/Podman, here i have used Podman. Most of the Podman Commands are same as Docker commands.

- I have Installed & run docker compose file by running **podman compose up -d** (to stop - podman compose down)

- After executing that command, Opensearch & Opensearch Dashboard starts running in the port 9200 = data API, 9600 = metrics/monitoring, 5601 = GUI (Dashboards). 

- Username:admin, Password:Str0ng@Passw0rd!

![Login for opensearch](image-5.png)

![Login for opensearch-dashboard](image-10.png)

[!![localhost:9200](image-4.png)]


## Step 2:
- Create Index and Insert Sample Data for that i have used mapping.json for define schema, index.py for creating index & insert sample data.

[!![inserted data](image-6.png)]



## Step 3: 
- Create Flask API and added end points to perform POST, GET, DELETE operations (I'm using flask locally & installed required packages).

![flask endpoint](image-8.png)


## Step 4: Git Version Control
- Here i have created 2 feature banches: 
    1. feature/opensearch for opensearch index mapping & script to load sample data
    2. feature/flask_api for Implemented Flask API for student records

- Images of Git Commits

![Commits](image.png)

[!![Commit done by master](image-1.png)]

[!![Commit done by feature/flask_api](image-2.png)]

[!![Commit done by feature/opensearch](image-3.png)]


- GET:
    `curl http://localhost:5000/student/S102`
<img width="1919" height="279" alt="image" src="https://github.com/user-attachments/assets/70af53a2-579c-4a92-95e0-974d7a320ce4" />



- POST:
    `curl -X POST http://127.0.0.1:5000/student \
-H "Content-Type: application/json" \
-d '{"student_id":"S105", "name":"Rahul Mehta", "age":22, "course":"Flask", "score":91.2}'`

![Sample data inserted](image-9.png)


- PUT:
    `curl -X PUT http://localhost:5000/student/S106 \
-H "Content-Type: application/json" \
-d '{
  "student_id": "S106",
  "name": "AB",
  "age": 24,
  "course": "Data Engineering",
  "score": 92.7
}'
`

<img width="1827" height="479" alt="image" src="https://github.com/user-attachments/assets/d0e64d1a-d6e9-4b68-b1bd-985768fc8d90" />

- To list all data for the student index:
  ` curl -X GET http://127.0.0.1:5000/student`

<img width="1477" height="695" alt="image" src="https://github.com/user-attachments/assets/64369cb8-28f8-46bc-9a49-6873d7e64e5b" />

