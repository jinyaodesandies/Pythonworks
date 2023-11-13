
class book:
    def __init__(self,ISBN,Title,Pages,Prince,Genre,Author,Qty):
        self.ISBN = ISBN
        self.title = Title
        self.pages = Pages
        self.price = Prince
        self.genre = Genre
        self.author = Author
        self.qty = Qty
    def add_book(self):
        book = {"title" : self.title,
                "ISBN" : self.ISBN,
                "pages": self.pages,
                "price": self.price,
                "genre": self.genre,
                "author": self.author,
                "quantity": self.qty
                }

        return book
