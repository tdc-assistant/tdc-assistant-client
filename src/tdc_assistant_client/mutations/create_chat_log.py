from gql import gql

create_chat_log_mutation = gql(
    """
mutation Mutation {
  createChatLog {
    createdAt
    deletedAt
    id
    customerName
    messages {
      deletedAt
      content
      createdAt
      id
      role
      updatedAt
      annotations {
        ... on ResponseAnnotation {
          content
          createdAt
          deletedAt
          id
          type
          updatedAt
        }
      }
    }
    updatedAt
  }
}
"""
)
