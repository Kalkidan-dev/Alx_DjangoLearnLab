
## 2. retrieve.md

```markdown
```python
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
# Output:
# 1984 George Orwell 1949
