#Analyzing Book Store Sales
books=[]
dict={}

num=int(input("Enter number of books you want to store :"))
for i in range(num):
 book=input("Enter name of the book :")
 author=input("Enter name of the author : ")
 year=int(input("Enter in which year it was published :"))
 price=float(input("Enter price of the book :"))


 dict.update({"book_title":book})
 dict.update({"author_name": author})
 dict.update({"b_year": year})
 dict.update({"b_price": price})

 books.append(dict)
print(books)
