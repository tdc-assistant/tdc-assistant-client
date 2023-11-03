from gql import gql

create_response_annotation_mutation = gql(
    """
mutation CreateResponseAnnotation($messageId: ID!, $content: String!) {
  createResponseAnnotation(messageId: $messageId, content: $content) {
    content
    createdAt
    deletedAt
    id
    type
    updatedAt
  }
}
"""
)
