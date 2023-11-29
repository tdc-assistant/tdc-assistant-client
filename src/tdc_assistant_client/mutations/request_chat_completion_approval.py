from gql import gql

request_chat_completion_approval_mutation = gql(
    """
mutation RequestChatCompletionApproval($requestChatCompletionApprovalId: ID!) {
  requestChatCompletionApproval(id: $requestChatCompletionApprovalId) {
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
