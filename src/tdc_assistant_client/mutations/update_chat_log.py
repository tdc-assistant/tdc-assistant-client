from gql import gql

update_chat_log_mutation = gql(
    """
    mutation Mutation {
        updateChatLog {
            id
            customerName
        }
    }
"""
)
