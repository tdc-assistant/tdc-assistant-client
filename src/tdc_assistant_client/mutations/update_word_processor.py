from gql import gql

update_word_processor_mutation = gql(
    """
mutation UpdateWordProcessor($input: UpdateWordProcessorInput) {
  updateWordProcessor(input: $input) {
    id
    createdAt
    updatedAt
    deletedAt
    type
    number
    content
  }
}
"""
)
