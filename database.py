from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://root:Secret55@localhost/gaming_analytics"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
