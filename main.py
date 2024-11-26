import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from pydantic import BaseModel

# import requests

# from util_oauth2 import create_oauth2, getAuthorizationURL, getToken
from util_oauth1 import create_client

load_dotenv()

app = FastAPI()

class Tweet(BaseModel):
    text: str

SCOPE = ["tweet.read", "tweet.write", "users.read"]

# oauth2 = create_oauth2(client_id=os.getenv("CLIENT_ID"), redirect_uri=os.getenv("REDIRECT_URI"), scope=SCOPE)
client = create_client(
    consumer_key=os.getenv("CONSUMER_KEY"), 
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

# @app.get("/auth")
# async def get_auth():
#     auth_url = "https://twitter.com/i/oauth2/authorize"
#     authorization_url = getAuthorizationURL(oauth2, auth_url)
#     return {"authorization_url": authorization_url}

# @app.get("/callback")
# async def callback(request: Request):
#     code = request.query_params.get("code")
#     print("code")
#     headers = {
#         "Authorization": f"Basic {os.getenv("BEARER_TOKEN")}",
#     }
#     token_url = "https://api.x.com/2/oauth2/token"
#     access_token = getToken(oauth2, token_url, os.getenv("CLIENT_SECRET"), code, headers)
#     print(access_token)
#     return {"access_token": code}


@app.post("/tweet")
async def tweet(tweet: Tweet):
    response = client.create_tweet(text=tweet.text)
    return {"response": response}