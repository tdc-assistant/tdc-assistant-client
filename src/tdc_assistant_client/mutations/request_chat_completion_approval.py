from gql import gql

request_chat_completion_approval_mutation = gql(
    """
mutation RequestChatCompletionApproval($id: ID!) {
  requestChatCompletionApproval(id: $id) {
    id
    createdAt
    updatedAt
    deletedAt
    approvalStatus
    parts {
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
}
"""
)
