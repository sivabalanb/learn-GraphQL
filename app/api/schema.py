import graphene
from .mutations import Mutation
from .resolvers import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
