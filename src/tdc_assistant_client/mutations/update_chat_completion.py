from gql import gql

update_chat_completion_mutation = gql(
    """
mutation UpdateChatCompletion($input: UpdateChatCompletionInput) {
  updateChatCompletion(input: $input) {
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
