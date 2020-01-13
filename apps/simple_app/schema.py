import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Messages, Tenant
from django.contrib.auth.models import User


class MessageType(DjangoObjectType):
    class Meta:
        model = Messages

class TenantType(DjangoObjectType):
    class Meta:
        model = Tenant

class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(ObjectType):
    all_messages = graphene.List(MessageType)
    all_tenants = graphene.List(TenantType)
    all_users = graphene.List(UserType)


    def resolve_all_messages(self, info, **kwargs):
        return Messages.objects.all()
    
    def resolve_all_tenants(self, info, **kwargs):
        return Tenant.objects.all()

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()



schema = graphene.Schema(query=Query)