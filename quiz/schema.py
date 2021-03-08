import graphene
from graphene_django import DjangoObjectType, DjangoListField

from quiz.models import Category, Quiz, Question, Option


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['id', 'name', 'quizzes']


class CategoryCreateMutation(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryCreateMutation(category=category)


class CategoryUpdateMutation(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, id, name):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryUpdateMutation(category)


class CategoryDeleteMutation(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return


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
    # List
    categories = DjangoListField(CategoryType)
    quizzes = DjangoListField(QuizType)
    questions = DjangoListField(QuestionType)
    options = DjangoListField(OptionType)
    question_options = graphene.List(OptionType, id=graphene.Int())

    # Single Objects
    quiz = graphene.Field(QuizType, id=graphene.Int())
    question = graphene.Field(QuestionType, id=graphene.Int())
    option = graphene.Field(OptionType, id=graphene.Int())

    @staticmethod
    def resolve_categories(root, info):
        return Category.objects.all()

    @staticmethod
    def resolve_quizzes(root, info):
        return Quiz.objects.all()

    @staticmethod
    def resolve_quiz(root, info, id):
        return Quiz.objects.get(pk=id)

    @staticmethod
    def resolve_questions(root, info):
        return Question.objects.all()

    @staticmethod
    def resolve_question(root, info, id):
        return Question.objects.get(pk=id)

    @staticmethod
    def resolve_options(root, info):
        return Option.objects.all()

    @staticmethod
    def resolve_question_options(root, info, id):
        return Option.objects.filter(question_id=id)

    @staticmethod
    def resolve_option(root, info, id):
        return Option.objects.get(pk=id)


class Mutation(graphene.ObjectType):
    add_category = CategoryCreateMutation.Field()
    update_category = CategoryUpdateMutation.Field()
    delete_category = CategoryDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


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
query{
  quiz(id:2){
    title
  }
}

Query3:
query{
  question(id:1){
    title
  }
  questionOptions(id:1){
    answer
  }
}

Query4:
query GetQuestion($id: Int = 2){
  question(id:$id){
    title
  }
  questionOptions(id:$id){
    answer
  }
}


Query5:
mutation AddCategory {
  addCategory (name: "Category Title") {
    category {
      name
    }
  }
}


Query6:
mutation UpdateCategory {
  updateCategory (id: 3, name: "Updated+ Category") {
    category {
      id,
      name
    }
  }
}

Query7:
mutation DeleteCategory {
  deleteCategory (id: 2) {
    category {
      id
    }
  }
}

"""