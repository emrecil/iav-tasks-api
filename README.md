# iav-tasks-api
A containerized REST api that lets users manage tasks.

## Task Model
Entries will be saved in a local sqlite3 database called "Tasks". The Table has the following columns:

| <ins>id</ins> | title | done |
|---------------|----|----|
|               |    |    |

## API Endpoints
API will be implemented using flask and will consist of the following Endpoints:

### /tasks
#### GET
Get all tasks.

Response:
```json
[
  {
    "id": 0,
    "title": "Task 1",
    "done": false
  },
  {
    "id": 1,
    "title": "Task 2",
    "done": true
  }
]
```

#### POST
Add a new task.

Body:
```json
{ "title" : "Task 3" }
```

Response:
```json
{
    "id": 2,
    "title": "Task 3",
    "done": false
}
```

### /task/{id}
#### GET
Get task with given id.

Response:
```json
{
    "id": 2,
    "title": "Task 3",
    "done": false
}
```

#### POST
Update task with given id.

Body:
```json
{
    "id": 2,
    "title": "Task 3",
    "done": true
}
```

Response:
```json
{
    "id": 2,
    "title": "Task 3",
    "done": true
}
```
