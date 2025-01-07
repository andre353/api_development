from sqlalchemy import BigInteger, Column, ForeignKey, Integer, MetaData, String, Table, create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", BigInteger, unique=True),
    Column("fullname", String),
)

user_table = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey('users.user_id')),
    Column("email", String, nullable=False),
)

metadata.create_all(engine)
metadata.drop_all(engine)  # сначала удаляются таблицы зависимые с foreign keys и только после те, на которые ссылаются: сначала addresses, затем users