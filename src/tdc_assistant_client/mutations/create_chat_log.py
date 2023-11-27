from gql import gql

create_chat_log_mutation = gql(
    """
mutation CreateChatLog($input: CreateChatLogInput) {
  createChatLog(input: $input) {
    createdAt
    customerName
    rawText
    deletedAt
    id
    messages {
      id
      createdAt
      updatedAt
      deletedAt
      content
      role
      annotations {
        ... on ResponseAnnotation {
          id
          createdAt
          updatedAt
          deletedAt
          type
          content
          messageId
        }
        ... on WorkspaceAnnotation {
          id
          createdAt
          updatedAt
          deletedAt
          messageId
          type
          content
          boardNumber
        }
        ... on ChatCompletionAnnotation {
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
        ... on ImageCaptureAnnotation {
          id
          createdAt
          updatedAt
          deletedAt
          type
          imageCapture {
            id
            createdAt
            updatedAt
            deletedAt
            imageUrl
          }
        }
      }
    }
    updatedAt
    workspaces {
      ... on CodeEditor {
        id
        createdAt
        updatedAt
        deletedAt
        programmingLanguage
        editorNumber
        content
        type
      }
      ... on WordProcessor {
        id
        createdAt
        updatedAt
        deletedAt
        number
        content
        type
      }
    }
  }
}
"""
)
