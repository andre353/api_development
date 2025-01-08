# from typing import List
# from typing import Optional
# from sqlalchemy import ForeignKey
# from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declared_attr
# from sqlalchemy.orm import relationship

# базовый класс необходим для описания работы моделей базы данных
class Base(DeclarativeBase):
    # данная модель не должна быть создана в базе данных - abstract - такой таблицы в базе данных быть не должно
    __abstract__ = True

    # имя таблицы будет создано на основе класса
    @declared_attr.directive
    def __tablename__(cls) -> str:
        # return cls.__name__.lower()
        # если с префиксом и во мн ч
        return f"shop_app__{cls.__name__.lower()}s"


    id: Mapped[int] = mapped_column(primary_key=True)

