from gql import gql

update_workspace_mutation = gql(
    """
    mutation Mutation($input: UpdateWorkspaceInput) {
        updateWorkspace(input: $input) {
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
