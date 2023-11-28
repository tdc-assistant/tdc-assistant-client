from gql import gql

create_image_capture_mutation = gql(
    """
mutation CreateImageCapture($input: CreateImageCaptureInput!) {
  createImageCapture(input: $input) {
    id
    createdAt
    updatedAt
    deletedAt
    chatLogId
    type
    imageUrl
  }
}
"""
)
