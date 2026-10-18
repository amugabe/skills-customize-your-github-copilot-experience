from fastapi import FastAPI

app = FastAPI(title="Task API")

# In-memory storage for tasks
items = [
    {"id": 1, "title": "Read chapter", "done": False},
    {"id": 2, "title": "Practice Python", "done": True},
]


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
