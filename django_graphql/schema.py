import graphene
import apps.core.schema
from apps.simple_app.schema import Query as simple_query


class Query(
    apps.core.schema.Query,
    simple_query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(apps.core.schema.Mutation, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)