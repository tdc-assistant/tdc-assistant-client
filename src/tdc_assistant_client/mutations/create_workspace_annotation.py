from gql import gql

create_workspace_annotation_mutation = gql(
    """
    mutation Mutation($messageId: ID!, $content: String!, $boardNumber: Int!) {
        createWorkspaceAnnotation(messageId: $messageId, content: $content, boardNumber: $boardNumber) {
            id
            createdAt
            updatedAt
            deletedAt
            type
            content
            boardNumber
        }
    }
"""
)
