import graphene

class Book(graphene.ObjectType):
    title = graphene.String()
    author = graphene.String()
