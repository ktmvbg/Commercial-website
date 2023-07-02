from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import *
import re


def init_db():
    engine = create_engine(
        # "mysql+pymysql://usdxmdmf_meocon:shy*}xgkySOf@45.252.251.44/usdxmdmf_ecom?charset=utf8mb4")
        "postgresql://postgres:123456@localhost/ecom")
    Base.metadata.bind = engine
    # Base.metadata.create_all()
    
    # NewsComment.__table__.drop(engine)
    # News.__table__.drop(engine)
    # News.__table__.create(engine)
    # NewsComment.__table__.create(engine)

def drop_db():
    engine = create_engine(
        # "mysql+pymysql://usdxmdmf_meocon:shy*}xgkySOf@45.252.251.44/usdxmdmf_ecom?charset=utf8mb4")
        "postgresql://postgres:123456@localhost/ecom")
    Base.metadata.bind = engine
    Base.metadata.drop_all()

    

def get_session():
    engine = create_engine(
        # "mysql+pymysql://usdxmdmf_meocon:shy*}xgkySOf@45.252.251.44/usdxmdmf_ecom?charset=utf8mb4")
        "postgresql://postgres:123456@localhost/ecom")
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    return DBSession()


init_db()
# drop_db()
