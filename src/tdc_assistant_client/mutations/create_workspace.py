from gql import gql

create_workspace_mutation = gql(
    """
    mutation CreateWorkspace($input: CreateWorkspaceInput) {
    createWorkspace(input: $input) {
        id
        createdAt
        updatedAt
        deletedAt
        chatLogId
        boardNumber
        type
        content
    }
    }
"""
)
