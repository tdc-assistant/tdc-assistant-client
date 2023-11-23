from gql import gql

create_code_editor_mutation = gql(
    """
mutation CreateCodeEditor($input: CreateCodeEditorInput) {
  createCodeEditor(input: $input) {
    id
    createdAt
    updatedAt
    deletedAt
    chatLogId
    programmingLanguage
    editorNumber
    content
  }
}
"""
)
