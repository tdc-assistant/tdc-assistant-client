from gql import gql

create_image_capture_annotation_mutation = gql(
    """
mutation CreateImageCaptureAnnotation($messageId: ID!, $imageUrl: String!) {
  createImageCaptureAnnotation(messageId: $messageId, imageUrl: $imageUrl) {
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
"""
)
