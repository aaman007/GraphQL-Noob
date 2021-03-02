import graphene
from graphene_django import DjangoObjectType, DjangoListField

from quiz.models import Category, Quiz, Question, Option


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['id', 'name', 'quizzes']


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'category', 'questions', 'created_date']


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = [
            'id', 'quiz', 'title', 'question_type', 'difficulty', 'quiz', 'is_active', 'options', 'created_date'
        ]


class OptionType(DjangoObjectType):
    class Meta:
        model = Option
        fields = ['id', 'question', 'answer', 'is_correct']


class Query(graphene.ObjectType):
    categories = DjangoListField(CategoryType)
    quizzes = DjangoListField(QuizType)
    questions = DjangoListField(QuestionType)

    @staticmethod
    def resolve_categories(root, info):
        return Category.objects.all()

    @staticmethod
    def resolve_quizzes(root, info):
        return Quiz.objects.all()

    @staticmethod
    def resolve_questions(root, info):
        return Question.objects.all()


schema = graphene.Schema(query=Query)


"""
Query1:
query{
  categories{
    name,
    quizzes{
      title
    }
  }
  quizzes{
    title,
    questions {
      id,
      title
    }
  }
  questions{
    title,
    options{
      answer,
      isCorrect
    }
  }
}

Query2:

"""