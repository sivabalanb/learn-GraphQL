from graphene import ObjectType, String, List, ID, Schema, Field, Mutation

# Define a Book type
class Book(ObjectType):
    title = String()
    author = String()

# Define a Query
class Query(ObjectType):
    books = List(Book)

    def resolve_books(self, info):
        # This resolver returns a list of books
        return [
            Book(title="Book 1", author="Author 1"),
            Book(title="Book 2", author="Author 2"),
            Book(title="Book 3", author="Author 3"),
        ]

# Define a Mutation for adding a book
class AddBook(Mutation):
    class Arguments:
        title = String()
        author = String()

    book = Field(Book)

    def mutate(self, info, title, author):
        # This resolver adds a new book
        new_book = Book(title=title, author=author)
        return AddBook(book=new_book)

# Define a Mutation type
class Mutation(ObjectType):
    add_book = AddBook.Field()

# Create a schema
schema = Schema(query=Query, mutation=Mutation)

if __name__ == "__main__":
    # Example query
    query = """
    {
        books {
            title
            author
        }
    }
    """

    # Execute the query
    result = schema.execute(query)

    # Print the query result
    print(result.data)

    # Example mutation
    mutation = """
    mutation {
        addBook(title: "New Book", author: "Author") {
            book {
                title
                author
            }
        }
    }
    """

    # Execute the mutation
    result = schema.execute(mutation)

    # Print the mutation result
    print(result.data)
