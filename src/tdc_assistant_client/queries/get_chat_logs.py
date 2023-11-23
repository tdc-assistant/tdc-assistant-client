from gql import gql

get_chat_logs_query = gql(
    """
  query ChatLogs {
  chatLogs {
    id
    createdAt
    updatedAt
    deletedAt
    customerName
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
    workspaces {
      ... on CodeEditor {
        id
        createdAt
        updatedAt
        deletedAt
        programmingLanguage
        editorNumber
        content
      }
    }
  }
}
"""
)
