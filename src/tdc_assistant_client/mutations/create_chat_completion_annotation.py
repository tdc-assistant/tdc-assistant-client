from gql import gql

create_chat_completion_annotation_mutation = gql(
    """
    mutation Mutation($messageId: ID!) {
      createChatCompletionAnnotation(messageId: $messageId) {
        id
        createdAt
        updatedAt
        deletedAt
        sentAt
        messageId
        type
        approvalStatus
        responseAnnotationId
        chatCompletion {
          id
          createdAt
          updatedAt
          deletedAt
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
    }
"""
)
