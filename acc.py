from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Article(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

articles = [
    {"id": 1, "name": "Coque iPhone", "price": 25.0, "in_stock": True},
    {"id": 2, "name": "Chargeur Samsung", "price": 40.0, "in_stock": True},
    {"id": 3, "name": "Écouteurs Bluetooth", "price": 60.0, "in_stock": False}
]

@app.get("/articles")
def get_articles():
    return articles

@app.get("/articles/{article_id}")
def get_article(article_id: int):
    for article in articles:
        if article["id"] == article_id:
            return article
    return {"error": "Article non trouvé"}

@app.post("/articles")
def add_article(article: Article):
    articles.append(article.dict())
    return {"message": "Article ajouté"}

@app.delete("/articles/{article_id}")
def delete_article(article_id: int):
    for article in articles:
        if article["id"] == article_id:
            articles.remove(article)
            return {"message": "Supprimé"}
    return {"error": "Not found"}