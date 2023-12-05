from fastapi import FastAPI
import auth
from posting import Posting
import posting

app=FastAPI()


@app.get("/api")
async def root():
    return {"message":"yubin server"}

@app.get("/linkedin")
async def renew_access_token(code:str):
    res= await auth.get_access_token(code)
    return res

@app.post("/api/post")
async def request_posting(posting:Posting):
    posting.post_to_linkedin(posting)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)


