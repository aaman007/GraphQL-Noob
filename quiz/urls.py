from django.urls import path
from graphene_django.views import GraphQLView

from quiz.schema import schema


app_name = 'quiz'

urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema))
]
