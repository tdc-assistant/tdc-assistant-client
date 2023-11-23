from gql import gql

update_code_editor_mutation = gql(
    """
mutation UpdateCodeEditor($input: UpdateCodeEditorInput) {
  updateCodeEditor(input: $input) {
    id
    createdAt
    updatedAt
    deletedAt
    type
    programmingLanguage
    editorNumber
    content
  }
}
"""
)
