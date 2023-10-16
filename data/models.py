from sqlalchemy import create_engine, Column, Integer, String, Sequence, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("ip")
DB_USER = os.getenv('db_user')
DB_PASS = os.getenv('db_pass')
DB_NAME = os.getenv('db_name')
port = os.getenv("port")


DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{port}/{DB_NAME}'

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class UserConversation(Base):
    __tablename__ = 'user_conversations'

    id = Column(Integer, Sequence('user_conversation_id_seq'), primary_key=True)
    user_id = Column(Integer)
    message = Column(String)
    response = Column(String)
    timestamp = Column(DateTime, server_default= text('now()'))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
