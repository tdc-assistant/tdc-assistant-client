from gql import gql

create_word_processor_mutation = gql(
    """
mutation CreateWordProcessor($input: CreateWordProcessorInput) {
  createWordProcessor(input: $input) {
    id
    createdAt
    updatedAt
    deletedAt
    number
    content
  }
}
"""
)
