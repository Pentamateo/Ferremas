import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()


class PostgreConnectionManager:

    def __init__(
        self,
        connection_string: str = os.getenv("POSTGRESQL_CONNECTION_STRING"),
        max_size: int = 10
    ):
        self.connection_string = connection_string
        self.max_size = max_size
        self.engine = create_engine(self.connection_string)
        self.session = Session(bind=self.engine)