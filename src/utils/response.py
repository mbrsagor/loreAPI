import re


from src.utils.status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST

def created(data):
    return{
        data: "Data created successfully",
        "status": HTTP_200_OK,
    }

def error(data):
    return{
        data: "Error",
        "status": HTTP_400_BAD_REQUEST,
    }
