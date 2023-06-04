import json
import models

def read_json(file_path, session):
    with open(file_path, 'r') as f:
        data = json.load(f)
        publishers, books, shops, stocks, sales = [], [], [], [], []
        for piece in data:
            if piece['model'] == 'publisher':
                publishers.append(models.Publisher(id=piece['pk'], **piece['fields']))
            elif piece['model'] == 'book':
                books.append(models.Book(id=piece['pk'], **piece['fields']))
            elif piece['model'] == 'shop':
                shops.append(models.Shop(id=piece['pk'], **piece['fields']))
            elif piece['model'] == 'stock':
                 stocks.append(models.Stock(id=piece['pk'], **piece['fields']))
            elif piece['model'] == 'sale':
                 sales.append(models.Sale(id=piece['pk'], **piece['fields']))
        session.add_all(publishers + shops + books + stocks + sales)
        session.commit()
