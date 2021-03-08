import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


"""
Q1:
query {
  users {
    edges {
      node {
        username,
        email
      }
    }
  }
}


Q2:
query {
  me {
    username,
    email,
    isStaff,
    firstName
  }
}

# pip install django-graphql-jwt==0.3.0
Q3:
mutation {
  register (
    email: "ssjh@shjhf.cashj",
    username: "sahgjgdhj",
    password1: "wegjhwegfyuew732463tgehjgef43tr",
    password2: "wegjhwegfyuew732463tgehjgef43tr"
  ) {
    success
    errors
    token,
    refreshToken
  }
}

Q4:
mutation {
  verifyAccount (
    token: "eyJ1c2VybmFtZSI6InNhaGdqZ2RoaiIsImFjdGlvbiI6ImFjdGl2YXRpb24ifQ:1lJBX1:u69hO1Z0IdUCLcu7W5tVgrHyH-b1nmJMa4S7CTRgNnM"
  ) {
    success
    errors
  }
}

Q5:
mutation {
  tokenAuth(username: "admin", password: "admin") {
    success,
    errors,
    token,
    refreshToken,
    
    user {
      username,
      email
    }
  }
}
"""