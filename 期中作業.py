from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from elasticsearch import Elasticsearch
from typing import List

# 初始化 FastAPI
app = FastAPI()

# 連接 Elasticsearch
es = Elasticsearch("http://localhost:9200")
INDEX_NAME = "webpages"

# 定義資料結構
class Page(BaseModel):
    url: str
    title: str
    content: str

@app.on_event("startup")
def setup_index():
    # 若不存在 index 就建立
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME)

# 新增一頁網站資料
@app.post("/index/")
async def index_page(page: Page):
    doc = page.dict()
    res = es.index(index=INDEX_NAME, document=doc)
    return {"result": res["result"], "id": res["_id"]}

# 搜尋網站內容
@app.get("/search/")
async def search(q: str = Query(..., min_length=1)):
    res = es.search(index=INDEX_NAME, query={
        "multi_match": {
            "query": q,
            "fields": ["title", "content"]
        }
    })
    hits = res["hits"]["hits"]
    return [{"url": hit["_source"]["url"], "title": hit["_source"]["title"]} for hit in hits]
