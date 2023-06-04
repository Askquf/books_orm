import sqlalchemy
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from models import Book, Publisher, Sale, Stock, Shop, Base
from settings import DSN
from json_reader import read_json

def find(session, publisher_name = None, publisher_id = None):
    if publisher_id is None and publisher_name is None:
        print("Wrong parameter")
    else:
        for _, book, __, shop, sale in session.query(Publisher, Book, Stock, Shop, Sale).filter(or_(Publisher.name == publisher_name, Publisher.id == publisher_id)).\
            join(Book, Book.id_publisher == Publisher.id).\
            join(Stock, Stock.id_book == Book.id).\
            join(Shop, Shop.id == Stock.id_shop).\
            join(Sale, Sale.id_stock == Stock.id).filter():
            print(f'{book.title} | {shop.name} | {sale.price} | {sale.date_sale}')

def main():
    engine = sqlalchemy.create_engine(DSN)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    read_json('data.json', session)
    filter = input()
    if (filter.isdigit()):
        find(session, publisher_id=filter)
    else:
        find(session, publisher_name=filter)

if __name__ == '__main__':
    main()

