from sqlalchemy import create_engine, Integer, Column
from sqlalchemy.orm import registry, declarative_base

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# mapper_registry = registry()
# print(mapper_registry)  # <sqlalchemy.orm.decl_api.registry object at 0x000001E1AC25D1F0>
# print(mapper_registry.metadata) # MetaData()

# вместо 2х строк теперь одна с declarative_base()
# mapper_registry = registry()
# Base = mapper_registry.generate_base()

Base = declarative_base()

class AbstractModel(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)

class UserModel(AbstractModel):
    ...
    
class AddressModel(AbstractModel):
    ...
