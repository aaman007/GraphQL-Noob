import graphene
from graphene_django import DjangoObjectType

from books.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ['id', 'title', 'content']


class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    @staticmethod
    def resolve_books(root, info):
        return Book.objects.all()


schema = graphene.Schema(query=Query)
