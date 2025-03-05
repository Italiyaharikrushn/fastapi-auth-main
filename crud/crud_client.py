from typing import Any, Dict, List, Optional, Union, TypeVar
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from core.security import get_password_hash
from sqlalchemy import func, or_
from crud.base import CRUDBase
from models.client import Client
from db.base_class import Base
from schemas.client import ClientBase,ClientCreate,ClientUpdate
ModelType = TypeVar("ModelType", bound=Base)

class CRUDClient(CRUDBase[Client, ClientCreate,ClientUpdate]): 
    def get(self, db: Session):
        return db.query(Client).all()


client = CRUDClient(Client)


# File "/home/harikrushn/.local/lib/python3.10/site-packages/fastapi/_compat.py", line 147, in serialize
#     return self._type_adapter.dump_python(
#   File "/usr/local/lib/python3.10/dist-packages/pydantic/type_adapter.py", line 333, in dump_python
#     return self.serializer.to_python(
# pydantic_core._pydantic_core.PydanticSerializationError: Unable to serialize unknown type: <class 'models.client.Client'>