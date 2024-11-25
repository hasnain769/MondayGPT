2023-10 changes from 2023-07

Breaking changes:

1. Removed the deprecated items field on boards queries, replaced it with items_page (https://developer.monday.com/api-reference/changelog/removing-the-deprecated-items-field-on-boards-queries-replace-with-items-page)

2. New column values fields and typed column values (https://developer.monday.com/api-reference/changelog/new-column-values-fields-and-typed-column-values)

3. Removed the deprecated items_by_column_values and items_by_multiple_column_values objects, replaced them with items_page_by_column_values (https://developer.monday.com/api-reference/changelog/deprecating-items_by_column_values-and-items_by_multiple_column_values)

4. The column_type field on the create_column mutation is now a required field (https://developer.monday.com/api-reference/changelog/required-column_type-argument-for-create_column-mutation)

5. Empty parentheses are no longer supported (https://developer.monday.com/api-reference/changelog/empty-parentheses-no-longer-supported)

6. Quotation marks for strings are now required (https://developer.monday.com/api-reference/changelog/quotation-marks-for-strings-required)

7. Removed the deprecated pos fields on boards and columns queries (https://developer.monday.com/api-reference/changelog/removing-deprecated-pos-fields)

8. The type field on columns queries has changed from String! to ColumnType! (https://developer.monday.com/api-reference/changelog/type-change-for-type-field-on-columns-queries)

9. Deprecated the newest_first argument on boards queries (https://developer.monday.com/api-reference/changelog/deprecating-the-newest_first-argument)

10. Many of the ID arguments and fields have changed from Int to ID type (https://developer.monday.com/api-reference/changelog/type-change-for-id-arguments-and-fields)

11. Text field returns empty results for mirror, dependency, and connect boards columns (https://developer.monday.com/api-reference/changelog/text-field-empty-value-for-mirror-dependency-and-connect-boards-columns)

Non-breaking changes:

1. New move_item_to_board mutation (https://developer.monday.com/api-reference/changelog/new-move_item_to_board-mutation)

2. New linked_items field on items queries (https://developer.monday.com/api-reference/changelog/new-linked_items-field)

3. New edit_update and delete_update webhooks (https://developer.monday.com/api-reference/changelog/new-edit_update-and-delete-update-webhooks)

4. The value argument in the change_simple_column_value mutation is now nullable (https://developer.monday.com/api-reference/changelog/nullable-value-argument-in-change-simple-column-value-mutation)

5. The complexity of the text field for mirror, link, and dependency columns increased (https://developer.monday.com/api-reference/changelog/increased-complexity-for-text-field)


Here's the updated document with a response template included for each operation. You can use these templates to copy and paste responses from Postman into the document.

---

## Monday.com GraphQL CRUD Operation Examples

### 1. **Check Complexity Points Usage**

This query checks the complexity points of your API requests, helping you monitor rate limits.

#### Query
```graphql
query {
  complexity {
    before
    query
    after
    reset_in_x_seconds
  }
  boards(ids: 1614669298) {
    id
    name
  }
}
```

#### Response Template
```json
{
  "data": {
    "complexity": {
      "before": 4999805,
      "query": 12,
      "after": 4999793,
      "reset_in_x_seconds": 23
    },
    "boards": [
      {
        "id": "1614669298",
        "name": "Sample project"
      }
    ]
  },
  "account_id": 25228442
}
```

---

### 2. **Update Simple Column Value**

This mutation updates a simple text-based column value for a specific item on a board.

#### Mutation
```graphql
mutation {
  change_simple_column_value(
    item_id: 1655422739,
    board_id: 1614669298,
    column_id: "text__1",
    value: "Some text"
  ) {
    id
  }
}
```

#### Response Template
```json
{
  "data": {
    "change_simple_column_value": {
      "id": "1655422739"
    }
  },
  "account_id": 25228442
}
```

---

### 3. **Update Complex Column Value**

This mutation changes the value of a more complex column, such as an email, which requires a structured JSON input.

#### Mutation
```graphql
mutation {
  change_column_value(
    item_id: 1655422739,
    board_id: 1614669298,
    column_id: "email",
    value: "{\"text\":\"test@gmail.com\",\"email\":\"test@gmail.com\"}"
  ) {
    id
  }
}
```

#### Response Template
```json
{
  "data": {
    "change_column_value": {
      "id": "1655422739"
    }
  },
  "account_id": 25228442
}
```

### 4. **Upload a File to a Files Column**

This mutation uploads a file to a specific files column within an item.

#### Mutation
```graphql
mutation add_file($file: File!) {
  add_file_to_column(item_id: 1234567890, column_id: "files", file: $file) {
    id
  }
}
```

#### Form Data (for file upload)
| Key  | Value                           |
|------|---------------------------------|
| map  | {"image": "variables.file"}     |
| image| [Upload your file here]         |

---

#### Response Template
```json
{
  "data": {
    "add_file_to_column": {
      "id": "1234567890"
    }
  }
}
```


### 5. **Upload a File to an Update**

This mutation uploads a file to a specific update, which can be used for attachments in communication threads.

#### Mutation
```graphql
mutation ($file: File!) {
  add_file_to_update(file: $file, update_id: 1234567890) {
    id
  }
}
```

#### Form Data (for file upload)
| Key  | Value                           |
|------|---------------------------------|
| map  | {"image": "variables.file"}     |
| image| [Upload your file here]         |

---

#### Response Template
```json
{
  "data": {
    "add_file_to_update": {
      "id": "1234567890"
    }
  }
}

```
### 6. **Create a Notification**

This mutation creates a notification targeted to a specific user or board/project.

#### Mutation
```graphql
mutation {
  create_notification(
    user_id: 65548265,
    target_id: 1655422739,
    text: "This is a notification",
    target_type: Project
  ) {
    text
  }
}
```

#### Response Template
```json
{
  "data": {
    "create_notification": {
      "text": "This is a notification"
    }
  },
  "account_id": 25228442
}
```

---

### 7. **Create an Item**

This mutation creates a new item on a board within a specified group.

#### Mutation
```graphql
mutation {
  create_item(board_id: 1614669298, group_id: "topics", item_name: "new item") {
    id
  }
}
```

#### Response Template
```json
{
  "data": {
    "create_item": {
      "id": "1710752117"
    }
  },
  "account_id": 25228442
}
```
---

### 8. **Create an Item (Using Variables)**

This example shows how to use variables to create an item, which is especially useful in dynamic requests.

#### Mutation
```graphql
mutation createItem($boardId: Int!, $groupId: String!, $itemName: String!) {
  create_item(board_id: $boardId, group_id: $groupId, item_name: $itemName) {
    id
  }
}
```

#### Variables
```json
{
  "boardId": "1937184631",
  "groupId": "mvp_release__1",
  "itemName": "Code Review"
}

```
#### Response Template
```json
{
  "data": {
    "create_item": {
      "id": "1939643213"
    }
  },
  "account_id": 26381028
}
```
---

### 9. **Create an Item with Column Values**

This mutation creates an item and sets column values such as status or text at creation.

#### Mutation
```graphql
mutation {
  create_item(
    board_id: 1614669298,
    group_id: "topics",
    item_name: "new item",
    column_values: "{\"status\":\"Done\", \"text\":\"My Text\"}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_item": {
      "id": "1710782705"
    }
  },
  "account_id": 25228442
}
```
---


### 10. **Retrieve Account Details**

This query retrieves information about the Monday.com account, such as active members, country, and account name.

#### Query
```graphql
query {
  account {
    id
    name
    country_code
    active_members_count
    plan {
      name
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "account": {
      "id": "25228442",
      "name": "Example Company",
      "country_code": "US",
      "active_members_count": 25,
      "plan": {
        "name": "Pro"
      }
    }
  }
}

```
---

### 11. **List Board Details**

Using the `Board` schema, this query fetches board information, including the name, description, columns, and item count.

#### Query
```graphql
query {
  boards(ids: [1234567890]) {
    id
    name
    description
    items_count
    columns {
      id
      title
      type
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "boards": [
      {
        "id": "1614669298",
        "name": "Sample project",
        "description": "Add your board's description here",
        "items_count": 5,
        "columns": [
          {
            "id": "name",
            "title": "Name",
            "type": "name"
          },
          {
            "id": "subitems",
            "title": "Subitems",
            "type": "subtasks"
          },
          {
            "id": "person",
            "title": "assignee",
            "type": "people"
          },
          {
            "id": "status__1",
            "title": "Status",
            "type": "status"
          },
          {
            "id": "text__1",
            "title": "client_name",
            "type": "text"
          },
          {
            "id": "text_1__1",
            "title": "Text 1",
            "type": "text"
          },
          {
            "id": "item_id__1",
            "title": "Item ID",
            "type": "item_id"
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 12. **Create an Item with Detailed Column Values**

To create an item with column values, we can add multiple column types by referencing `ColumnType` in the schema. Here’s an example with a few specific column types.

#### Mutation
```graphql
mutation {
  create_item(
    board_id: 1614669298,
    group_id: "topics",
    item_name: "Task for Project",
    column_values: "{\"status\":\"Working on it\", \"priority\":\"High\", \"date\":\"2023-10-01\"}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_item": {
      "id": "1710794933"
    }
  },
  "account_id": 25228442
}
```
---

Let me know if you'd like to expand on specific fields or entities, and I can customize further based on the schema.

### 13. **Create a Board**

This mutation creates a new board with a specified name and visibility kind (`public`, `private`, or `share`). The `BoardKind` enum in the schema allows for these options.

#### Mutation
```graphql
mutation {
  create_board(board_name: "my board", board_kind: public) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_board": {
      "id": "1710799453"
    }
  },
  "account_id": 25228442
}
```
---

### 14. **Create a Column**

This mutation creates a new column on an existing board, with options for specifying the column title, description, and type. Referencing the `ColumnType` enum allows types such as `status`, `text`, `number`, etc.

#### Mutation
```graphql
mutation {
  create_column(
    board_id: 1614669298,
    title: "Work Status",
    description: "This is my work status column",
    column_type: status
  ) {
    id
    title
    description
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_column": {
      "id": "work_status__1",
      "title": "Work Status",
      "description": "This is my work status column"
    }
  },
  "account_id": 25228442
}
```
---

### 15. **Create a Group**

This mutation adds a new group to a specific board. A group in Monday.com can help organize items, allowing multiple categories or phases within a board.

#### Mutation
```graphql
mutation {
  create_group(board_id: 1614669298, group_name: "new group") {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_group": {
      "id": "new_group__1"
    }
  },
  "account_id": 25228442
}
```
---

### 16. **Create a Subitem**

This mutation creates a subitem under a specified parent item. Subitems allow for more granular task organization within a primary item on a board.

#### Mutation
```graphql
mutation {
  create_subitem(parent_item_id: 1655422739, item_name: "new subitem") {
    id
    board {
      id
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_subitem": {
      "id": "1710911835",
      "board": {
        "id": "1614669310"
      }
    }
  },
  "account_id": 25228442
}
```
---


### 17. **Create a Subitem (Using Variables)**

This mutation achieves the same functionality as above, but it uses variables to enhance flexibility in dynamic requests.

#### Mutation
```graphql
mutation createSubitem($parentId: Int!, $name: String!) {
  create_subitem(parent_item_id: $parentId, item_name: $name) {
    id
    board {
      id
    }
  }
}
```

#### Variables
```json
{
  "parentId": 1234567,
  "name": "new subitem"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
#### Response Template
```json
{
  "data": {
    "create_subitem": {
      "id": "9876543",
      "board": {
        "id": "1234567890"
      }
    }
  }
}

```




### 18. **Create a Workspace**

This mutation creates a workspace with a specific name, kind (`open` or `closed`), and description. Workspaces help organize boards and streamline collaboration.

#### Mutation
```graphql
mutation {
  create_workspace(
    name: "New Cool Workspace",
    kind: open,
    description: "This is a cool description"
  ) {
    id
    description
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_workspace": {
      "id": "3107802",
      "description": "This is a cool description"
    }
  },
  "account_id": 25228442
}
```
---

### 19. **Check a Checkbox**

This mutation sets a checkbox column value to checked (`true`). Using `change_multiple_column_values` allows modifying multiple columns simultaneously.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1655422739,
    board_id: 1614669298,
    column_values: "{\"checkbox\": {\"checked\": \"true\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1655422739"
    }
  },
  "account_id": 25228442
}
```
---

### 20. **Uncheck a Checkbox**

This mutation unchecks a checkbox by setting its value to `null`, effectively removing the checkmark.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1655422739,
    board_id: 1614669298,
    column_values: "{\"checkbox\": null}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1655422739"
    }
  },
  "account_id": 25228442
}
```
---


### 21. **Change a Connect Boards Column**

This mutation updates a "Connect Boards" column by linking items from other boards. This is useful for creating cross-board relationships.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1234567890,
    board_id: 1122334455,
    column_values: "{\"connect_boards\": {\"item_ids\": [123123123, 456456456]}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1234567890"
    }
  }
}

```
---

### 22. **Change a Country Column**

This mutation updates a country column with a specific country code and name, following the `CountryColumn` schema.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 11111,
    board_id: 22222,
    column_values: "{\"country__1\": {\"countryCode\": \"US\", \"countryName\": \"United States\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1655422739"
    }
  },
  "account_id": 25228442
}
```
---

### 23. **Change a Date Column**

This mutation updates a date column with a specified date and optional time value.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1655422739,
    board_id: 1614669298,
    column_values: "{\"date__1\": {\"date\": \"1993-08-27\", \"time\": \"18:00:00\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1655422739"
    }
  },
  "account_id": 25228442
}
```
---


### 24. **Change a Dropdown Column**

This mutation updates a dropdown column by selecting specific options, with an option to create new labels if they don’t already exist in the dropdown menu.

#### Mutation
```graphql
mutation {
  change_simple_column_value(
    item_id: 1234567890,
    board_id: 1122334455,
    column_id: "dropdown",
    value: "Cookie, Cupcake",
    create_labels_if_missing: true
  ) {
    id
  }
}
```


#### Response Template
```json
{
  "data": {
    "change_simple_column_value": {
      "id": "1234567890"
    }
  }
}


```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃


### 25. **Change an Email Column**

This mutation updates an email column with a new email address and optional label text.

#### Mutation
```graphql
mutation {
  change_simple_column_value(
    item_id: 1655422739,
    board_id: 1614669298,
    column_id: "email__1",
    value: "example@example.com This is an example email"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_simple_column_value": {
      "id": "1655422739"
    }
  },
  "account_id": 25228442
}
```
---

### 26. **Change an Hour Column**

This mutation sets the hour and minute values for an hour-type column.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"hour__1\": {\"hour\": 16, \"minute\": 42}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 27. **Change an Item's Name**

This mutation changes the name of a specific item.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"text8__1\": \"My Item\"}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 28. **Change a Link Column**

This mutation updates a link column with a URL and display text.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"link__1\": {\"url\": \"http://monday.com\", \"text\": \"go to monday!\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 29. **Change a Location Column**

This mutation updates a location column with latitude, longitude, and address details.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"location__1\": {\"lat\": \"29.9772962\", \"lng\": \"31.1324955\", \"address\": \"Giza Pyramid Complex\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 30. **Change a Long Text Column**

This mutation updates a long text column with new content.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"long_text__1\": {\"text\": \"Sample text\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 31. **Change a Numbers Column**

This mutation updates a numbers column with a new numeric value.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"numbers__1\": \"3\"}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---
##error

### 32. **Change a People Column**

This mutation assigns people or teams to a people column.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 11111,
    board_id: 22222,
    column_values: "{\"people_2\": {\"personsAndTeams\": [{\"id\": 4616627, \"kind\": \"person\"}, {\"id\": 4616666, \"kind\": \"person\"}, {\"id\": 51166, \"kind\": \"team\"}]}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "11111"
    }
  }
}

```
---

### 33. **Change a Phone Column**

This mutation updates a phone column with a new phone number and country code.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"phone__1\": {\"phone\": \"11231234567\", \"countryShortName\": \"US\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 34. **Change a Rating Column**

This mutation updates a rating column with a new rating value.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"rating__1\": {\"rating\": 5}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 35. **Change a Status Column**

This mutation sets a new label for a status column.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"status_1__1\": {\"label\": \"Done\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 36. **Change a Tags Column**

This mutation updates a tags column with specified tag IDs.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"tags__1\": {\"tag_ids\": [295026, 295064]}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 37. **Change a Text Column**

This mutation sets a new value for a text column.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"text8__1\": \"Sample text\"}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 38. **Change a Timeline Column**

This mutation updates a timeline column with start and end dates.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"timeline__1\": {\"from\": \"2019-06-03\", \"to\": \"2019-06-07\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 39. **Change a Week Column**

This mutation sets the start and end dates for a week column.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"week__1\": {\"week\": {\"startDate\": \"2019-06-10\", \"endDate\": \"2019-06-16\"}}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 40. **Change a World Clock Column**

This mutation updates the timezone for a world clock column.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"world_clock__1\": {\"timezone\": \"Europe/London\"}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 41. **Clear a Text Column**

This mutation clears the content of a text column by setting its value to an empty string.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"text8__1\": \"\"}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 42. **Clear a Numbers Column**

This mutation clears the value of a numbers column by setting it to an empty string.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"numbers__1\": \"\"}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 43. **Clear a Files Column**

This mutation clears all files in a files column.

#### Mutation
```graphql
mutation {
  change_column_value(
    item_id: 1711043053,
    board_id: 1614669298,
    column_id: "files__1",
    value: "{\"clear_all\": true}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_column_value": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 44. **Clear a Connect Boards Column**

This mutation clears all connected items in a connect boards column.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"connect_boards__1\": {}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---



### 45. **Clear a Dependency Column**

This mutation clears a dependency column by removing all linked dependencies.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"dependency__1\": {}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 46. **Clear a Status Column**

This mutation clears a status column by removing the assigned label.

#### Mutation
```graphql
mutation {
  change_multiple_column_values(
    item_id: 1711043053,
    board_id: 1614669298,
    column_values: "{\"status_1__1\": {}}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---

### 47. **Clear a People Column**

This mutation clears all people or teams assigned in a people column.

#### Mutation
```graphql
mutation {
  change_column_value(
    item_id: 1711043053,
    board_id: 1614669298,
    column_id: "people__1",
    value: "{\"clear_all\": true}"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_column_value": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---


### 48. **Get Specific Values in Column Values for a Location Column**

This query retrieves specific details within a location column, such as country, street, and street number.

#### Query
```graphql
query {
  items(ids: [1234567890, 9876543210]) {
    column_values {
      ... on LocationValue {
        country
        street
        street_number
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "country": "United States",
            "street": "Broadway",
            "street_number": "123"
          },
          {
            "country": "Canada",
            "street": "King Street",
            "street_number": "456"
          }
        ]
      }
    ]
  }
}

```
---

### 49. **Get Specific Values in Column Values for a Status Column**

This query fetches detailed information in a status column, including label and update ID.

#### Query
```graphql
query {
  items(ids: 1711043053) {
    column_values {
      value
      type
      ... on StatusValue {
        label
        update_id
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "value": null,
            "type": "subtasks"
          },
          {
            "value": null,
            "type": "people"
          },
          {
            "value": null,
            "type": "status",
            "label": null,
            "update_id": null
          },
          {
            "value": null,
            "type": "text"
          },
          {
            "value": null,
            "type": "text"
          },
          {
            "value": "{\"item_id\":\"1711043053\"}",
            "type": "item_id"
          },
          {
            "value": null,
            "type": "status",
            "label": null,
            "update_id": null
          },
          {
            "value": "{\"checked\":false}",
            "type": "checkbox"
          },
          {
            "value": null,
            "type": "board_relation"
          },
          {
            "value": null,
            "type": "country"
          },
          {
            "value": null,
            "type": "date"
          },
          {
            "value": null,
            "type": "dropdown"
          },
          {
            "value": null,
            "type": "email"
          },
          {
            "value": "{\"item_id\":\"1711043053\"}",
            "type": "item_id"
          },
          {
            "value": "{\"hour\":16,\"minute\":42,\"changed_at\":\"2024-11-19T13:35:32.849Z\"}",
            "type": "hour"
          },
          {
            "value": "\"\"",
            "type": "text"
          },
          {
            "value": "{\"url\":\"http://monday.com\",\"text\":\"go to monday!\",\"changed_at\":\"2024-11-19T13:39:48.292Z\"}",
            "type": "link"
          },
          {
            "value": "{\"lat\":\"29.9772962\",\"lng\":\"31.1324955\",\"address\":\"Giza Pyramid Complex\",\"changed_at\":\"2024-11-19T13:41:27.913Z\"}",
            "type": "location"
          },
          {
            "value": "{\"text\":\"Sample text\",\"changed_at\":\"2024-11-19T13:43:36.060Z\"}",
            "type": "long_text"
          },
          {
            "value": "\"\"",
            "type": "numbers"
          },
          {
            "value": null,
            "type": "people"
          },
          {
            "value": "{\"phone\":\"11231234567\",\"changed_at\":\"2024-11-19T13:48:30.138Z\",\"countryShortName\":\"US\"}",
            "type": "phone"
          },
          {
            "value": "{\"rating\":5,\"changed_at\":\"2024-11-19T13:50:47.818Z\"}",
            "type": "rating"
          },
          {
            "value": "{\"changed_at\":\"2024-11-20T05:32:53.428Z\"}",
            "type": "status",
            "label": null,
            "update_id": null
          },
          {
            "value": "{\"tag_ids\":[295026,295064]}",
            "type": "tags"
          },
          {
            "value": "{\"to\":\"2019-06-07\",\"from\":\"2019-06-03\",\"changed_at\":\"2024-11-19T13:58:44.781Z\"}",
            "type": "timeline"
          },
          {
            "value": "{\"week\":{\"endDate\":\"2019-06-16\",\"startDate\":\"2019-06-10\"}}",
            "type": "week"
          },
          {
            "value": "{\"timezone\":\"Europe/London\",\"changed_at\":\"2024-11-20T05:19:30.213Z\"}",
            "type": "world_clock"
          },
          {
            "value": "{\"files\":[]}",
            "type": "file"
          },
          {
            "value": null,
            "type": "dependency"
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---


### 50. **Get Specific Values in Column Values for a Checkbox Column**

This query retrieves the checked status and the last updated time of a checkbox column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1655422739]) {
    column_values {
      ... on CheckboxValue {
        checked
        updated_at
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "checked": false,
            "updated_at": null
          }
        ]
      },
      {
        "column_values": [
          {
            "checked": true,
            "updated_at": "2024-11-24T12:00:00Z"
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---

### 51. **Get Specific Values in Column Values for a Connect Boards Column**

This query fetches details from a connect boards column, such as linked item IDs and the linked items themselves.

#### Query
```graphql
query {
  items(ids: [1234567890, 9876543210]) {
    column_values {
      ... on BoardRelationValue {
        linked_item_ids
        linked_items
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "complexity": {
      "before": 0,
      "query": 0,
      "after": 0,
      "reset_in_x_seconds": 0
    },
    "boards": [
      {
        "id": "1234567890",
        "name": "Board Name"
      }
    ]
  }
}
```
---


### 52. **Get Specific Values in Column Values for a Country Column**

This query retrieves country details and the last update time for a country column.

#### Query
```graphql
query {
  items(ids: [1234567890, 9876543210]) {
    column_values {
      ... on CountryValue {
        country
        updated_at
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "country": "United States",
            "updated_at": "2024-11-25T12:00:00Z"
          }
        ]
      },
      {
        "column_values": [
          {
            "country": "Canada",
            "updated_at": "2024-11-24T15:30:00Z"
          }
        ]
      }
    ]
  }
}

```

### 53. **Get Specific Values in Column Values for a Date Column**

This query retrieves date and time details from a date column.

#### Query
```graphql
query {
  items(ids: [1655422739, 1655422742]) {
    column_values {
      ... on DateValue {
        time
        date
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "time": "23:00",
            "date": "1993-08-27"
          }
        ]
      },
      {
        "column_values": [
          {
            "time": "",
            "date": ""
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---

### 54. **Get Specific Values in Column Values for a Dependency Column**

This query fetches linked item IDs and the last updated time for a dependency column.

#### Query
```graphql
query {
  items(ids: [1655422739, 9876543210]) {
    column_values {
      ... on DependencyValue {
        linked_item_ids
        updated_at
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "linked_item_ids": [987654321, 123456789],
            "updated_at": "2024-11-25T12:00:00Z"
          }
        ]
      },
      {
        "column_values": [
          {
            "linked_item_ids": [1122334455],
            "updated_at": "2024-11-24T15:30:00Z"
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---

### 55. **Get Specific Values in Column Values for a Dropdown Column**

This query retrieves values and column details for a dropdown column.

#### Query
```graphql
query {
  items(ids: [1655422739, 1655422742]) {
    column_values {
      ... on DropdownValue {
        values {
          id
        }
        column {
          id
        }
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "values": [
              {
                "id": "0"
              },
              {
                "id": "1"
              }
            ],
            "column": {
              "id": "dropdown__1"
            }
          }
        ]
      },
      {
        "column_values": [
          {
            "values": [],
            "column": {
              "id": "dropdown__1"
            }
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---

### 56. **Get Specific Values in Column Values for an Email Column**

This query retrieves the email address and last update time for an email column.

#### Query
```graphql
query {
  items(ids: [1655422739, 1711043053]) {
    column_values {
      ... on EmailValue {
        email
        updated_at
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "values": [
              {
                "id": "0"
              },
              {
                "id": "1"
              }
            ],
            "column": {
              "id": "dropdown__1"
            }
          }
        ]
      },
      {
        "column_values": [
          {
            "values": [],
            "column": {
              "id": "dropdown__1"
            }
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---

### 57. **Get Specific Values in Column Values for an Hour Column**

This query fetches the hour and minute values from an hour column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1655422739]) {
    column_values {
      ... on HourValue {
        minute
        hour
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "email": "example@example.com",
            "updated_at": "2024-11-19T13:32:57+00:00"
          }
        ]
      },
      {
        "column_values": [
          {
            "email": null,
            "updated_at": null
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---

### 58. **Get Specific Values in Column Values for a Link Column**

This query retrieves the URL and display text from a link column.

#### Query
```graphql
query {
  items(ids: [1655422739, 1711043053]) {
    column_values {
      ... on LinkValue {
        url
        url_text
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "url": null,
            "url_text": null
          }
        ]
      },
      {
        "column_values": [
          {
            "url": "http://monday.com",
            "url_text": "go to monday!"
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---




### 59. **Get Specific Values in Column Values for a Long Text Column**

This query retrieves the text content and value from a long text column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1655422739]) {
    column_values {
      ... on LongTextValue {
        text
        value
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "text": "",
            "value": null
          }
        ]
      },
      {
        "column_values": [
          {
            "text": "Sample text",
            "value": "{\"text\":\"Sample text\",\"changed_at\":\"2024-11-19T13:43:36.060Z\"}"
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---

### 60. **Get Specific Values in Column Values for a Monday Doc Column**

This query retrieves file information from a Monday Doc column.

#### Query
```graphql
query {
  items(ids: [1655422739, 1711043053]) {
    column_values {
      ... on DocValue {
        file {
          creator_id
          url
        }
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "file": {
              "creator_id": "12345",
              "url": "https://example.com/file.pdf"
            }
          }
        ]
      },
      {
        "column_values": [
          {
            "file": {
              "creator_id": "67890",
              "url": "https://example.com/another_file.pdf"
            }
          }
        ]
      }
    ]
  },
  "account_id": 25228442
}

```
---

### 61. **Get Specific Values in Column Values for a Numbers Column**

This query retrieves the numeric value and ID from a numbers column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1655422739]) {
    column_values {
      ... on NumbersValue {
        number
        id
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "number": null,
            "id": "numbers__1"
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "number": 0,
            "id": "numbers__1"
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 62. **Get Specific Values in Column Values for a People Column**

This query fetches information about persons and teams from a people column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1655422739]) {
    column_values {
      ... on PeopleValue {
        persons_and_teams {
          id
        }
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {
            "persons_and_teams": [
              {
                "id": "65548265"
              }
            ]
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "persons_and_teams": []
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {
            "persons_and_teams": []
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "persons_and_teams": []
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 63. **Get Specific Values in Column Values for a Phone Column**

This query retrieves the phone number and country code from a phone column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1655422739]) {
    column_values {
      ... on PhoneValue {
        country_short_name
        phone
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "country_short_name": null,
            "phone": null
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "country_short_name": "US",
            "phone": "11231234567"
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---


### 64. **Get Specific Values in Column Values for a Status Column**

This query retrieves the index and value of a status column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1655422739]) {
    column_values {
      ... on StatusValue {
        index
        value
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {},
          {
            "index": 3,
            "value": "{\"index\":3}"
          },
          {},
          {},
          {},
          {
            "index": null,
            "value": null
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "index": null,
            "value": null
          },
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {},
          {
            "index": null,
            "value": null
          },
          {},
          {},
          {},
          {
            "index": null,
            "value": null
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "index": 1,
            "value": "{\"index\":1,\"post_id\":null,\"changed_at\":\"2024-11-20T05:38:29.390Z\"}"
          },
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 65. **Using `items_page` with Query Parameters**

This query retrieves items from a board with specific filters on column values. The `query_params` allows applying rules based on column IDs and values.

#### Query
```graphql
query {
  boards(ids: 1614669298) {
    items_page(
      limit: 100,
      query_params: {
        rules: [{column_id: "text__1", compare_value: "task name"}],
        operator: and
      }
    ) {
      cursor
      items {
        id
        name
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "boards": [
      {
        "items_page": {
          "cursor": null,
          "items": []
        }
      }
    ]
  },
  "account_id": 25228442
}
```
---
### error
### 66. **Using `next_items_page`**

This query fetches the next set of items based on a cursor for pagination.

#### Query
```graphql
query {
  next_items_page(
    limit: 50,
    cursor: "MSw5NzI4MDA5MDAsaV9YcmxJb0p1VEdYc1VWeGlxeF9kLDg4MiwzNXw0MTQ1NzU1MTE5"
  ) {
    cursor
    items {
      id
      name
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "complexity": {
      "before": 0,
      "query": 0,
      "after": 0,
      "reset_in_x_seconds": 0
    },
    "boards": [
      {
        "id": "1234567890",
        "name": "Board Name"
      }
    ]
  }
}
```
---

### 67. **Using `items_page`**

This query retrieves a paginated set of items from a board, limited to a specified number of items.

#### Query
```graphql
query {
  boards(ids: 1614669298) {
    items_page(limit: 100) {
      cursor
      items {
        id
        name
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "boards": [
      {
        "items_page": {
          "cursor": null,
          "items": [
            {
              "id": "1711043053",
              "name": "sample"
            },
            {
              "id": "1655422739",
              "name": "chatgpt project"
            },
            {
              "id": "1655422742",
              "name": "make trigger for code"
            },
            {
              "id": "1655423449",
              "name": "update monday.com"
            },
            {
              "id": "1710752117",
              "name": "new item"
            },
            {
              "id": "1710782705",
              "name": "new item"
            },
            {
              "id": "1710794933",
              "name": "Task for Project"
            }
          ]
        }
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 68. **Using `items_page_by_column_values`**

This query retrieves items from a board that match specific column values, allowing filtering by multiple columns.

#### Query
```graphql
query {
  items_page_by_column_values(
    limit: 50,
    board_id: 1614669298,
    columns: [
      {column_id: "text__1", column_values: ["Some text"]},
      {column_id: "country__1", column_values: ["US", "IL"]}
    ]
  ) {
    cursor
    items {
      id
      name
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items_page_by_column_values": {
      "cursor": null,
      "items": [
        {
          "id": "1655422739",
          "name": "chatgpt project"
        }
      ]
    }
  },
  "account_id": 25228442
}
```
---

### 69. **Move an Item to a Different Board**

This mutation moves an item to a specified board and group.

#### Mutation
```graphql
mutation {
  move_item_to_board(
    board_id: 1614669298,
    group_id: "topics",
    item_id: 1711043053
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "move_item_to_board": {
      "id": "1711043053"
    }
  },
  "account_id": 25228442
}
```
---
### error
### 70. **Get Items Linked to a Specific Item**

This query retrieves items that are linked to a specified item through a connect boards column.

#### Query
```graphql
query {
  items(ids: 1234567890) {
    linked_items(
      linked_board_id: 1122334455,
      link_to_item_column_id: "connect_boards"
    ) {
      id
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "complexity": {
      "before": 0,
      "query": 0,
      "after": 0,
      "reset_in_x_seconds": 0
    },
    "boards": [
      {
        "id": "1234567890",
        "name": "Board Name"
      }
    ]
  }
}
```
---

### 71. **Clear Column Values**

This mutation clears the value of a specific column by setting it to `null`.

#### Mutation
```graphql
mutation {
  change_simple_column_value(
    board_id: 1614669298,
    item_id: 1655422739,
    column_id: "date__1",
    value: null
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "change_simple_column_value": {
      "id": "1655422739"
    }
  },
  "account_id": 25228442
}
```
---


### 72. **Get Specific Values in Column Values for a Rating Column**

This query retrieves the rating value and last updated time for a rating column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1710794933]) {
    column_values {
      ... on RatingValue {
        rating
        updated_at
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "rating": 2,
            "updated_at": "2024-11-20T16:12:52+00:00"
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "rating": 5,
            "updated_at": "2024-11-19T13:50:47+00:00"
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 73. **Get Specific Values in Column Values for a Tags Column**

This query retrieves tag IDs and associated text from a tags column.

#### Query
```graphql
query {
  items(ids: [1710794933, 1711043053]) {
    column_values {
      ... on TagsValue {
        tag_ids
        text
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "tag_ids": [
              5135281
            ],
            "text": "one"
          },
          {},
          {},
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "tag_ids": [
              295026,
              295064
            ],
            "text": ""
          },
          {},
          {},
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 74. **Get Specific Values in Column Values for a Text Column**

This query retrieves the text content and value from a text column.

#### Query
```graphql
query {
  items(ids: [1711043053, 1655422739]) {
    column_values {
      ... on TextValue {
        text
        value
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {},
          {},
          {
            "text": "Some text",
            "value": "\"Some text\""
          },
          {
            "text": "",
            "value": null
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "text": "",
            "value": null
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {},
          {},
          {
            "text": "",
            "value": null
          },
          {
            "text": "",
            "value": null
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "text": "",
            "value": "\"\""
          },
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 75. **Get Specific Values in Column Values for a Timeline Column**

This query retrieves the start and end dates of a timeline column.

#### Query
```graphql
query {
  items(ids: [1655422739, 1711043053]) {
    column_values {
      ... on TimelineValue {
        from
        to
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "from": null,
            "to": null
          },
          {},
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "from": "2019-06-03T00:00:00+00:00",
            "to": "2019-06-07T00:00:00+00:00"
          },
          {},
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---

### 76. **Get Specific Values in Column Values for a Week Column**

This query retrieves the start and end dates of a week column.

#### Query
```graphql
query {
  items(ids: [1655422739, 1711043053]) {
    column_values {
      ... on WeekValue {
        start_date
        end_date
      }
    }
  }
}
```
#### Response Template
```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "start_date": null,
            "end_date": null
          },
          {},
          {},
          {}
        ]
      },
      {
        "column_values": [
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {},
          {
            "start_date": "2019-06-10T00:00:00+00:00",
            "end_date": "2019-06-16T00:00:00+00:00"
          },
          {},
          {},
          {}
        ]
      }
    ]
  },
  "account_id": 25228442
}
```
---


### 77. **Create a Tag**

This mutation creates a new tag or retrieves an existing tag with the specified name.

#### Mutation
```graphql
mutation {
  create_or_get_tag(tag_name: "one") {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_or_get_tag": {
      "id": "5135281"
    }
  },
  "account_id": 25228442
}
```
---

### 78. **Create an Update**

This mutation creates an update attached to a specified item, allowing you to add notes or status updates.

#### Mutation
```graphql
mutation {
  create_update(
    item_id: 1710794933,
    body: "This update will be added to the item"
  ) {
    id
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_update": {
      "id": "349485151"
    }
  },
  "account_id": 25228442
}
```
---

### 79. **Create a Webhook**

This mutation sets up a webhook to monitor events on a specified board. The example below sets a webhook for status column changes.

#### Mutation
```graphql
mutation {
  create_webhook(
    board_id: 1614669298,
    url: "https://myendpoint.com/webhook",
    event: change_status_column_value,
    config: "{\"columnId\":\"status\", \"columnValue\":{\"$any$\":true}}"
  ) {
    id
    board_id
  }
}
```
#### Response Template
```json
{
  "data": {
    "create_webhook": null
  },
  "account_id": 25228442
}
```
---
