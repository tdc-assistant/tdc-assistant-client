from gql import gql

update_chat_completion_annotation_mutation = gql(
    """
    mutation Mutation($input: UpdateChatCompletionAnnotationInput) {
        updateChatCompletionAnnotation(input: $input) {
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
