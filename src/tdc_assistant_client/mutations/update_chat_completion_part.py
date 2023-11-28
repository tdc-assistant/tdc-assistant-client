from gql import gql

update_chat_completion_part_mutation = gql(
    """
mutation UpdateChatCompletionPart {
  updateChatCompletionPart {
    id
    createdAt
    updatedAt
    deletedAt
    content
    type
    programmingLanguage
    shouldOmit
    sentAt
  }
}
"""
)
