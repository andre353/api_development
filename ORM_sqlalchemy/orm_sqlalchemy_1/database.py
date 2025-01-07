from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.connect() as connection:
    result = connection.execute(text("select 'hello, World'"))
    # print(result.all())
    # print(result.scalars().one_or_none())
    # print(result.scalar_one_or_none()) # scalar закрывает соединение result, поэтому через генератор возращаем:
    for entry in result.scalars():
        print(entry)
