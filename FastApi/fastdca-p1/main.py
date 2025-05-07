# def main():
#     print("Hello from fastdca-p1!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello from Anum"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}