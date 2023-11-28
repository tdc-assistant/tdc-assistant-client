from gql import gql

create_messages_mutation = gql(
    """
mutation CreateMessages($input: [CreateMessageInput!]!) {
  createMessages(input: $input) {
    updatedAt
    role
    id
    deletedAt
    createdAt
    content
  }
}
"""
)
