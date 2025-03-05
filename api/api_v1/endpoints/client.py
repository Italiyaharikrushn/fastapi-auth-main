from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.dependencies import get_db
import crud.base
from schemas.client import ClientCreate
from typing import List, Any
from api import dependencies
from sqlalchemy import func
import crud
from util.user_util import get_current_user
from models.client import Client


router = APIRouter()


@router.post("/create", status_code=201)
def create_client(
    client_in: ClientCreate,
    db: Session = Depends(get_db),
):
    create_client = ClientCreate(
        first_name=client_in.first_name,
        last_name=client_in.last_name,
        email=client_in.email,
        phone=client_in.phone,
        gender=client_in.gender,
    )
    client = crud.client.create(db=db, obj_in=create_client)
    return client

@router.get("/get", status_code=200)
def get_all_clients(db: Session = Depends(get_db)):
    clients = crud.client.get(db=db)
    return clients
