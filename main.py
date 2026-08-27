from fastapi import FastAPI

app = FastAPI(title="Первый проект, который, надеюсь, переастёт в склад")


@app.get("/")
def home_page():
    return {"status:": "Работает", "message:": "добро пожаловать на первый проект"}


@app.get("/api/catalog")
def get_test_catalog():
    return [
        {"id": 1, "title": "масло", "price": 4500.0},
        {"id": 2, "title": "коврик", "price": 800.0},
    ]


