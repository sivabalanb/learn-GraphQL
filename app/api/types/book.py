import graphene

class Book(graphene.ObjectType):
    title = graphene.String()
    author = graphene.Field('app.api.types.author.Author')
