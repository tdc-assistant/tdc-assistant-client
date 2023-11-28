from gql import gql

create_chat_completion_mutation = gql(
    """
mutation CreateChatCompletion($chatLogId: ID!) {
  createChatCompletion(chatLogId: $chatLogId) {
    id
    createdAt
    updatedAt
    deletedAt
    parts {
      id
      createdAt
      updatedAt
      deletedAt
      sentAt
      content
      type
      programmingLanguage
      shouldOmit
    }
  }
}
"""
)
