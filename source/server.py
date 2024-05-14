from fastapi import FastAPI
import auth

app=FastAPI()

@app.get("/linkedin")
async def renew_access_token(code:str):
    res= await auth.get_access_token(code)
    return res

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)


