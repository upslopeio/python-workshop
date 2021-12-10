import json
import os
from secrets import compare_digest
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Request, Header
from fastapi.params import Depends
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse


class House(BaseModel):
    address: str
    city: str
    state: str
    zip: str
    price: int


class ErrorMessage(BaseModel):
    message: str


class HouseRepository():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./data/houses.json")) as f:
        houses = json.load(f)


app = FastAPI()
security = HTTPBasic()


@app.get("/")
def home(request: Request, x_forwarded_for: Optional[str] = Header(None)):
    base_url = str(request.base_url) if x_forwarded_for is None else f"{request.url.components[0]}://{x_forwarded_for}/"
    return {"_links": {
        "_self": {
            "href": request.url_for("home").replace(str(request.base_url), base_url),
        },
        "houses": {
            "href": request.url_for("houses").replace(str(request.base_url), base_url),
        },
        "profile": {
            "href": request.url_for("profile").replace(str(request.base_url), base_url),
        },
    }}


@app.get("/houses", response_model=List[House])
def houses(zip: Optional[str] = None):
    if zip is not None:
        return [house for house in HouseRepository.houses if house["zip"] == zip]
    else:
        return HouseRepository.houses


@app.get("/houses/{id}", response_model=House, responses={404: {"model": ErrorMessage}})
async def house(id: int):
    if range(1, len(HouseRepository.houses) + 1):
        return HouseRepository.houses[id - 1]
    else:
        return JSONResponse(status_code=404, content={"message": "House not found"})


@app.post("/houses", response_class=RedirectResponse, status_code=201)
async def create_house(house: House):
    HouseRepository.houses.append(house)
    return f"/houses/{len(HouseRepository.houses)}"


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = compare_digest(credentials.username, "super-secure")
    correct_password = compare_digest(credentials.password, "password1234")

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.get("/profile", dependencies=[Depends(authenticate)])
async def profile():
    return {"username": "super-secure", "password": "************", "loggedIn": "true"}
