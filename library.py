class Books:

    def __init__(self,title,author,ISBN) -> None:
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.isborrowed=True
    
    def book(self):
        print(f"Title:\tAuthor:\tISBN:\tIsavailable:\n{self.title}\t{self.author}\t{self.ISBN}\t{self.isborrowed}")
    


Books.book()