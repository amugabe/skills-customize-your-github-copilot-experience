# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API in Python using FastAPI. Students will practice creating routes, returning JSON data, and handling requests with a simple in-memory data store.

## 📝 Tasks

### 🛠️ Create the API foundation

#### Description
Set up a FastAPI application and define endpoints for reading and creating records. The goal is to create a working web service that responds to HTTP requests.

#### Requirements
Completed program should:

- create a FastAPI app instance
- define a GET endpoint that returns a list of items or records
- define a POST endpoint that accepts JSON data
- store data in memory for the current session
- return JSON responses using the FastAPI framework

### 🛠️ Add validation and error handling

#### Description
Improve the API by validating input and handling missing or invalid requests more gracefully.

#### Requirements
Completed program should:

- use a Pydantic model to validate request data
- return a 404 response when a requested item does not exist
- return appropriate status codes for create and error cases
- keep the API organized with clear route names and simple function logic

### 🛠️ Test the API locally

#### Description
Run the application and check that the endpoints behave as expected using a browser or a local HTTP client.

#### Requirements
Completed program should:

- start the API using Uvicorn
- successfully call at least one GET endpoint
- successfully submit a POST request with JSON data
- verify that the API returns the expected response structure
