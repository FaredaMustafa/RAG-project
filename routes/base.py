#routes

from fastapi import FastAPI, APIRouter
import os 

#decorator is a function that : takes another function adds some additional functionality and returns a new enhanced function
#decorator with base router

base_router = APIRouter(
        prefix="/api/v1",
        tags=["api_v1"]
        

)

#adding a route to access welcome function

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "app_name": app_name,
        "app_version": app_version,
        "message": "Welcome to the FastAPI application!",
        "wanna play a game?": True
        }
