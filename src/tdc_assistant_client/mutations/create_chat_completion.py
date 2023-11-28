from gql import gql

create_chat_completion_mutation = gql(
    """
mutation CreateChatCompletion($chatLogId: ID!) {
  createChatCompletion(chatLogId: $chatLogId) {
    id
    createdAt
    updatedAt
    deletedAt
    sentAt
    parts {
      id
      createdAt
      updatedAt
      deletedAt
      content
      type
      programmingLanguage
      shouldOmit
    }
  }
}
"""
)
