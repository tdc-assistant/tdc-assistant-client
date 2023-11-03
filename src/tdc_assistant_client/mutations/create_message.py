from gql import gql

create_message_mutation = gql(
    """
mutation CreateMessage($chatLogId: ID!, $content: String!, $role: MessageRoleType!) {
  createMessage(chatLogId: $chatLogId, content: $content, role: $role) {
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
    content
    createdAt
    deletedAt
    id
    role
    updatedAt
  }
}
"""
)
