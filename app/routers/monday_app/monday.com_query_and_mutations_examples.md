# RAG Document for Monday.com GraphQL CRUD Operations

This document provides templates and guidelines for performing CRUD operations using Monday.com's GraphQL API. Variables that need to be customized are enclosed in double curly braces `{{ }}` for easy identification and modification.

---

## Table of Contents

1. [Check Complexity Points Usage](#1-check-complexity-points-usage)
2. [Update Simple Column Value](#2-update-simple-column-value)
3. [Update Complex Column Value](#3-update-complex-column-value)
4. [Upload a File to a Files Column](#4-upload-a-file-to-a-files-column)
5. [Upload a File to an Update](#5-upload-a-file-to-an-update)
6. [Create a Notification](#6-create-a-notification)
7. [Create an Item](#7-create-an-item)
8. [Create an Item (Using Variables)](#8-create-an-item-using-variables)
9. [Create an Item with Column Values](#9-create-an-item-with-column-values)
10. [Retrieve Account Details](#10-retrieve-account-details)
11. [List Board Details](#11-list-board-details)
12. [Create an Item with Detailed Column Values](#12-create-an-item-with-detailed-column-values)
13. [Create a Board](#13-create-a-board)
14. [Create a Column](#14-create-a-column)
15. [Create a Group](#15-create-a-group)
16. [Create a Subitem](#16-create-a-subitem)
17. [Create a Subitem (Using Variables)](#17-create-a-subitem-using-variables)
18. [Create a Workspace](#18-create-a-workspace)
19. [Check a Checkbox](#19-check-a-checkbox)
20. [Uncheck a Checkbox](#20-uncheck-a-checkbox)
21. [Change a Connect Boards Column](#21-change-a-connect-boards-column)
22. [Change a Country Column](#22-change-a-country-column)
23. [Change a Date Column](#23-change-a-date-column)
24. [Change a Dropdown Column](#24-change-a-dropdown-column)
25. [Change an Email Column](#25-change-an-email-column)
26. [Change an Hour Column](#26-change-an-hour-column)
27. [Change an Item's Name](#27-change-an-items-name)
28. [Change a Link Column](#28-change-a-link-column)
29. [Change a Location Column](#29-change-a-location-column)
30. [Change a Long Text Column](#30-change-a-long-text-column)
31. [Change a Numbers Column](#31-change-a-numbers-column)
32. [Change a People Column](#32-change-a-people-column)
33. [Change a Phone Column](#33-change-a-phone-column)
34. [Change a Rating Column](#34-change-a-rating-column)
35. [Change a Status Column](#35-change-a-status-column)
36. [Change a Tags Column](#36-change-a-tags-column)
37. [Change a Text Column](#37-change-a-text-column)
38. [Change a Timeline Column](#38-change-a-timeline-column)
39. [Change a Week Column](#39-change-a-week-column)
40. [Change a World Clock Column](#40-change-a-world-clock-column)
41. [Clear a Text Column](#41-clear-a-text-column)
42. [Clear a Numbers Column](#42-clear-a-numbers-column)
43. [Clear a Files Column](#43-clear-a-files-column)
44. [Clear a Connect Boards Column](#44-clear-a-connect-boards-column)
45. [Clear a Dependency Column](#45-clear-a-dependency-column)
46. [Clear a Status Column](#46-clear-a-status-column)
47. [Clear a People Column](#47-clear-a-people-column)
48. [Get Specific Values in Column Values for a Location Column](#48-get-specific-values-in-column-values-for-a-location-column)
49. [Get Specific Values in Column Values for a Status Column](#49-get-specific-values-in-column-values-for-a-status-column)
50. [Get Specific Values in Column Values for a Checkbox Column](#50-get-specific-values-in-column-values-for-a-checkbox-column)
51. [Get Specific Values in Column Values for a Connect Boards Column](#51-get-specific-values-in-column-values-for-a-connect-boards-column)
52. [Get Specific Values in Column Values for a Country Column](#52-get-specific-values-in-column-values-for-a-country-column)
53. [Get Specific Values in Column Values for a Date Column](#53-get-specific-values-in-column-values-for-a-date-column)
54. [Get Specific Values in Column Values for a Dependency Column](#54-get-specific-values-in-column-values-for-a-dependency-column)
55. [Get Specific Values in Column Values for a Dropdown Column](#55-get-specific-values-in-column-values-for-a-dropdown-column)
56. [Get Specific Values in Column Values for an Email Column](#56-get-specific-values-in-column-values-for-an-email-column)
57. [Get Specific Values in Column Values for an Hour Column](#57-get-specific-values-in-column-values-for-an-hour-column)
58. [Get Specific Values in Column Values for a Link Column](#58-get-specific-values-in-column-values-for-a-link-column)
59. [Get Specific Values in Column Values for a Long Text Column](#59-get-specific-values-in-column-values-for-a-long-text-column)
60. [Get Specific Values in Column Values for a Monday Doc Column](#60-get-specific-values-in-column-values-for-a-monday-doc-column)
61. [Get Specific Values in Column Values for a Numbers Column](#61-get-specific-values-in-column-values-for-a-numbers-column)
62. [Get Specific Values in Column Values for a People Column](#62-get-specific-values-in-column-values-for-a-people-column)
63. [Get Specific Values in Column Values for a Phone Column](#63-get-specific-values-in-column-values-for-a-phone-column)
64. [Get Specific Values in Column Values for a Status Column](#64-get-specific-values-in-column-values-for-a-status-column)
65. [Using `items_page` with Query Parameters](#65-using-items_page-with-query-parameters)
66. [Using `next_items_page`](#66-using-next_items_page)
67. [Using `items_page`](#67-using-items_page)
68. [Using `items_page_by_column_values`](#68-using-items_page_by_column_values)
69. [Move an Item to a Different Board](#69-move-an-item-to-a-different-board)
70. [Get Items Linked to a Specific Item](#70-get-items-linked-to-a-specific-item)
71. [Clear Column Values](#71-clear-column-values)
72. [Get Specific Values in Column Values for a Rating Column](#72-get-specific-values-in-column-values-for-a-rating-column)
73. [Get Specific Values in Column Values for a Tags Column](#73-get-specific-values-in-column-values-for-a-tags-column)
74. [Get Specific Values in Column Values for a Text Column](#74-get-specific-values-in-column-values-for-a-text-column)
75. [Get Specific Values in Column Values for a Timeline Column](#75-get-specific-values-in-column-values-for-a-timeline-column)
76. [Get Specific Values in Column Values for a Week Column](#76-get-specific-values-in-column-values-for-a-week-column)
77. [Create a Tag](#77-create-a-tag)
78. [Create an Update](#78-create-an-update)
79. [Create a Webhook](#79-create-a-webhook)

---

## Important Updates (October 2023)

**Breaking Changes:**

1. **Removed Deprecated `items` Field on Boards Queries:**
   - The `items` field on boards queries has been removed.
   - Use `items_page` instead.

2. **New Column Values Fields and Typed Column Values:**
   - Column values now have specific types.
   - Use the appropriate typed column values in queries.

3. **Removed Deprecated `items_by_column_values` and `items_by_multiple_column_values`:**
   - Use `items_page_by_column_values` instead.

4. **`column_type` Field on `create_column` Mutation is Now Required:**
   - You must specify `column_type` when creating a column.

5. **Empty Parentheses No Longer Supported:**
   - Avoid using empty parentheses `()` in queries.

6. **Quotation Marks for Strings are Now Required:**
   - All string values must be enclosed in quotation marks.

7. **Removed Deprecated `pos` Fields on Boards and Columns Queries:**
   - The `pos` field is no longer available.

8. **`type` Field on Columns Queries Changed from `String!` to `ColumnType!`:**
   - Adjust your queries accordingly.

9. **Deprecated `newest_first` Argument on Boards Queries:**
   - This argument is no longer supported.

10. **ID Arguments and Fields Changed from `Int` to `ID`:**
    - Update your variable types if necessary.

11. **`text` Field Returns Empty Results for Mirror, Dependency, and Connect Boards Columns:**
    - Use the appropriate fields for these column types.

**Non-Breaking Changes:**

1. **New `move_item_to_board` Mutation:**
   - Allows moving items between boards.

2. **New `linked_items` Field on Items Queries:**
   - Retrieve items linked through connect boards columns.

3. **New `edit_update` and `delete_update` Webhooks:**
   - Monitor when updates are edited or deleted.

4. **`value` Argument in `change_simple_column_value` Mutation is Now Nullable:**
   - You can set `value` to `null` to clear column values.

5. **Increased Complexity of `text` Field for Mirror, Link, and Dependency Columns:**
   - Be mindful of complexity limits when querying these fields.

---


## 1. Check Complexity Points Usage

**Description:** Monitor your API rate limits by checking the complexity points of your requests.

### **Query Template**

```graphql
query {
  complexity {
    before
    query
    after
    reset_in_x_seconds
  }
  boards(ids: {{ board_id }}) {
    id
    name
  }
}
```

**Instructions:**

- **`{{ board_id }}`**: Replace with the ID of the board you want to query.

### **Expected Response Structure**

```json
{
  "data": {
    "complexity": {
      "before": {{ before_points }},
      "query": {{ query_points }},
      "after": {{ after_points }},
      "reset_in_x_seconds": {{ reset_time }}
    },
    "boards": [
      {
        "id": "{{ board_id }}",
        "name": "{{ board_name }}"
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 2. Update Simple Column Value

**Description:** Update a text-based column value for a specific item on a board.

### **Mutation Template**

```graphql
mutation {
  change_simple_column_value(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_id: "{{ column_id }}",
    value: "{{ new_value }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ item_id }}`**: Replace with the ID of the item you want to update.
- **`{{ board_id }}`**: Replace with the ID of the board containing the item.
- **`{{ column_id }}`**: Replace with the ID of the column you want to update.
- **`{{ new_value }}`**: Replace with the new text value for the column.

### **Expected Response Structure**

```json
{
  "data": {
    "change_simple_column_value": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 3. Update Complex Column Value

**Description:** Update a complex column (e.g., email) that requires a JSON-formatted value.

### **Mutation Template**

```graphql
mutation {
  change_column_value(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_id: "{{ column_id }}",
    value: "{{ json_value }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ item_id }}`**: Replace with the ID of the item you want to update.
- **`{{ board_id }}`**: Replace with the ID of the board containing the item.
- **`{{ column_id }}`**: Replace with the ID of the complex column.
- **`{{ json_value }}`**: Replace with the JSON string representing the new value.

**Example JSON Value for Email Column:**

```json
"{\"text\":\"{{ email_text }}\",\"email\":\"{{ email_address }}\"}"
```

- **`{{ email_text }}`**: Display name or label for the email.
- **`{{ email_address }}`**: Actual email address.

### **Expected Response Structure**

```json
{
  "data": {
    "change_column_value": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 4. Upload a File to a Files Column

**Description:** Upload a file to a specific files column within an item.

### **Mutation Template**

```graphql
mutation add_file($file: File!) {
  add_file_to_column(
    item_id: {{ item_id }},
    column_id: "{{ column_id }}",
    file: $file
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ item_id }}`**: Replace with the ID of the item.
- **`{{ column_id }}`**: Replace with the ID of the files column.
- **`$file`**: Represents the file to be uploaded; it should be included in the form data.

### **Form Data for File Upload**

| Key         | Value                                     |
|-------------|-------------------------------------------|
| **query**       | The mutation query above.                 |
| **variables**   | `{"file": null}`                          |
| **map**         | `{"file": ["variables.file"]}`            |
| **file**        | [Attach your file here in the form data] |

### **Expected Response Structure**

```json
{
  "data": {
    "add_file_to_column": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 5. Upload a File to an Update

**Description:** Upload a file to a specific update, useful for attachments in communication threads.

### **Mutation Template**

```graphql
mutation ($file: File!) {
  add_file_to_update(
    file: $file,
    update_id: {{ update_id }}
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ update_id }}`**: Replace with the ID of the update.
- **`$file`**: Represents the file to be uploaded; it should be included in the form data.

### **Form Data for File Upload**

| Key         | Value                                     |
|-------------|-------------------------------------------|
| **query**       | The mutation query above.                 |
| **variables**   | `{"file": null}`                          |
| **map**         | `{"file": ["variables.file"]}`            |
| **file**        | [Attach your file here in the form data] |

### **Expected Response Structure**

```json
{
  "data": {
    "add_file_to_update": {
      "id": "{{ update_id }}"
    }
  }
}
```

---

## 6. Create a Notification

**Description:** Create a notification targeted to a specific user or project.

### **Mutation Template**

```graphql
mutation {
  create_notification(
    user_id: {{ user_id }},
    target_id: {{ target_id }},
    text: "{{ notification_text }}",
    target_type: {{ target_type }}
  ) {
    text
  }
}
```

**Instructions:**

- **`{{ user_id }}`**: Replace with the ID of the user who will receive the notification.
- **`{{ target_id }}`**: Replace with the ID of the target (e.g., item, project).
- **`{{ notification_text }}`**: Replace with the content of the notification.
- **`{{ target_type }}`**: Replace with the target type (e.g., `Project`, `Post`, `Update`).

### **Expected Response Structure**

```json
{
  "data": {
    "create_notification": {
      "text": "{{ notification_text }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 7. Create an Item

**Description:** Create a new item on a board within a specified group.

### **Mutation Template**

```graphql
mutation {
  create_item(
    board_id: {{ board_id }},
    group_id: "{{ group_id }}",
    item_name: "{{ item_name }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ board_id }}`**: Replace with the ID of the board.
- **`{{ group_id }}`**: Replace with the ID of the group.
- **`{{ item_name }}`**: Replace with the name of the new item.

### **Expected Response Structure**

```json
{
  "data": {
    "create_item": {
      "id": "{{ new_item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 8. Create an Item (Using Variables)

**Description:** Use variables to create an item, helpful for dynamic requests.

### **Mutation Template**

```graphql
mutation createItem($boardId: Int!, $groupId: String!, $itemName: String!) {
  create_item(
    board_id: $boardId,
    group_id: $groupId,
    item_name: $itemName
  ) {
    id
  }
}
```

**Variables Template**

```json
{
  "boardId": {{ board_id }},
  "groupId": "{{ group_id }}",
  "itemName": "{{ item_name }}"
}
```

**Instructions:**

- **`$boardId`**: Set to the board ID.
- **`$groupId`**: Set to the group ID.
- **`$itemName`**: Set to the item name.

### **Expected Response Structure**

```json
{
  "data": {
    "create_item": {
      "id": "{{ new_item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 9. Create an Item with Column Values

**Description:** Create an item and set column values such as status or text at creation.

### **Mutation Template**

```graphql
mutation {
  create_item(
    board_id: {{ board_id }},
    group_id: "{{ group_id }}",
    item_name: "{{ item_name }}",
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Replace with a JSON string of column values.

**Example Column Values JSON:**

```json
"{\"status\":\"Done\", \"text\":\"My Text\"}"
```

- **`"status"`**: Column ID for the status column.
- **`"text"`**: Column ID for the text column.

### **Expected Response Structure**

```json
{
  "data": {
    "create_item": {
      "id": "{{ new_item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 10. Retrieve Account Details

**Description:** Retrieve information about the account, such as active members and plan details.

### **Query Template**

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

**Instructions:**

- No variables need to be replaced.

### **Expected Response Structure**

```json
{
  "data": {
    "account": {
      "id": "{{ account_id }}",
      "name": "{{ account_name }}",
      "country_code": "{{ country_code }}",
      "active_members_count": {{ active_members_count }},
      "plan": {
        "name": "{{ plan_name }}"
      }
    }
  }
}
```

---

## 11. List Board Details

**Description:** Fetch board information, including name, description, columns, and item count.

### **Query Template**

```graphql
query {
  boards(ids: [{{ board_id }}]) {
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

**Instructions:**

- **`{{ board_id }}`**: Replace with the board ID.

### **Expected Response Structure**

```json
{
  "data": {
    "boards": [
      {
        "id": "{{ board_id }}",
        "name": "{{ board_name }}",
        "description": "{{ board_description }}",
        "items_count": {{ items_count }},
        "columns": [
          {
            "id": "{{ column_id }}",
            "title": "{{ column_title }}",
            "type": "{{ column_type }}"
          }
          // Additional columns...
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 12. Create an Item with Detailed Column Values

**Description:** Create an item with multiple column types by specifying detailed column values.

### **Mutation Template**

```graphql
mutation {
  create_item(
    board_id: {{ board_id }},
    group_id: "{{ group_id }}",
    item_name: "{{ item_name }}",
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Replace with a JSON string containing the desired column values.

**Example Column Values JSON:**

```json
"{\"status\":\"Working on it\", \"priority\":\"High\", \"date\":\"{{ date_value }}\"}"
```

- **`{{ date_value }}`**: Replace with a date in `YYYY-MM-DD` format.

### **Expected Response Structure**

```json
{
  "data": {
    "create_item": {
      "id": "{{ new_item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 13. Create a Board

**Description:** Create a new board with a specified name and visibility.

### **Mutation Template**

```graphql
mutation {
  create_board(
    board_name: "{{ board_name }}",
    board_kind: {{ board_kind }}
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ board_name }}`**: Replace with the new board's name.
- **`{{ board_kind }}`**: Replace with `public`, `private`, or `share`.

### **Expected Response Structure**

```json
{
  "data": {
    "create_board": {
      "id": "{{ new_board_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 14. Create a Column

**Description:** Create a new column on an existing board.

### **Mutation Template**

```graphql
mutation {
  create_column(
    board_id: {{ board_id }},
    title: "{{ column_title }}",
    description: "{{ column_description }}",
    column_type: {{ column_type }}
  ) {
    id
    title
    description
  }
}
```

**Instructions:**

- **`{{ column_title }}`**: Replace with the column's title.
- **`{{ column_description }}`**: Replace with a description.
- **`{{ column_type }}`**: Replace with the column type (e.g., `status`, `text`, `number`).

### **Expected Response Structure**

```json
{
  "data": {
    "create_column": {
      "id": "{{ new_column_id }}",
      "title": "{{ column_title }}",
      "description": "{{ column_description }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 15. Create a Group

**Description:** Add a new group to a specific board.

### **Mutation Template**

```graphql
mutation {
  create_group(
    board_id: {{ board_id }},
    group_name: "{{ group_name }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ group_name }}`**: Replace with the new group's name.

### **Expected Response Structure**

```json
{
  "data": {
    "create_group": {
      "id": "{{ new_group_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 16. Create a Subitem

**Description:** Create a subitem under a specified parent item.

### **Mutation Template**

```graphql
mutation {
  create_subitem(
    parent_item_id: {{ parent_item_id }},
    item_name: "{{ subitem_name }}"
  ) {
    id
    board {
      id
    }
  }
}
```

**Instructions:**

- **`{{ parent_item_id }}`**: Replace with the parent item ID.
- **`{{ subitem_name }}`**: Replace with the subitem's name.

### **Expected Response Structure**

```json
{
  "data": {
    "create_subitem": {
      "id": "{{ subitem_id }}",
      "board": {
        "id": "{{ subitem_board_id }}"
      }
    }
  }
}
```

---

## 17. Create a Subitem (Using Variables)

**Description:** Create a subitem using variables for dynamic requests.

### **Mutation Template**

```graphql
mutation createSubitem($parentId: Int!, $name: String!) {
  create_subitem(
    parent_item_id: $parentId,
    item_name: $name
  ) {
    id
    board {
      id
    }
  }
}
```

**Variables Template**

```json
{
  "parentId": {{ parent_item_id }},
  "name": "{{ subitem_name }}"
}
```

**Instructions:**

- **`$parentId`**: Set to the parent item ID.
- **`$name`**: Set to the subitem name.

### **Expected Response Structure**

```json
{
  "data": {
    "create_subitem": {
      "id": "{{ subitem_id }}",
      "board": {
        "id": "{{ subitem_board_id }}"
      }
    }
  }
}
```

---

## 18. Create a Workspace

**Description:** Create a workspace with a specific name, kind, and description.

### **Mutation Template**

```graphql
mutation {
  create_workspace(
    name: "{{ workspace_name }}",
    kind: {{ workspace_kind }},
    description: "{{ workspace_description }}"
  ) {
    id
    description
  }
}
```

**Instructions:**

- **`{{ workspace_name }}`**: Replace with the workspace's name.
- **`{{ workspace_kind }}`**: Replace with `open` or `closed`.
- **`{{ workspace_description }}`**: Replace with a description.

### **Expected Response Structure**

```json
{
  "data": {
    "create_workspace": {
      "id": "{{ workspace_id }}",
      "description": "{{ workspace_description }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 19. Check a Checkbox

**Description:** Set a checkbox column value to checked (`true`).

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string to check the checkbox.

**Example Column Values JSON:**

```json
"{\"{{ checkbox_column_id }}\": {\"checked\": \"true\"}}"
```

- **`{{ checkbox_column_id }}`**: Replace with the ID of the checkbox column.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 20. Uncheck a Checkbox

**Description:** Uncheck a checkbox by setting its value to `null`.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string to uncheck the checkbox.

**Example Column Values JSON:**

```json
"{\"{{ checkbox_column_id }}\": null}"
```

- **`{{ checkbox_column_id }}`**: Replace with the ID of the checkbox column.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```


---

## 21. Change a Connect Boards Column

**Description:** Update a "Connect Boards" column by linking items from other boards, useful for creating cross-board relationships.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ item_id }}`**: Replace with the ID of the item to update.
- **`{{ board_id }}`**: Replace with the ID of the board containing the item.
- **`{{ column_values_json }}`**: Replace with a JSON string representing the column values.

**Example Column Values JSON:**

```json
"{\"{{ connect_boards_column_id }}\": {\"item_ids\": [{{ linked_item_id1 }}, {{ linked_item_id2 }}]}}"
```

- **`{{ connect_boards_column_id }}`**: Replace with the ID of the "Connect Boards" column.
- **`{{ linked_item_id1 }}`, `{{ linked_item_id2 }}`**: Replace with the IDs of the items you want to link.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 22. Change a Country Column

**Description:** Update a country column with a specific country code and name.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ country_column_id }}\": {\"countryCode\": \"{{ country_code }}\", \"countryName\": \"{{ country_name }}\"}}"
```

- **`{{ country_column_id }}`**: Replace with the ID of the country column.
- **`{{ country_code }}`**: Replace with the country's ISO code (e.g., "US").
- **`{{ country_name }}`**: Replace with the country's full name (e.g., "United States").

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 23. Change a Date Column

**Description:** Update a date column with a specified date and optional time value.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ date_column_id }}\": {\"date\": \"{{ date_value }}\", \"time\": \"{{ time_value }}\"}}"
```

- **`{{ date_column_id }}`**: Replace with the ID of the date column.
- **`{{ date_value }}`**: Replace with the date in `YYYY-MM-DD` format.
- **`{{ time_value }}`**: (Optional) Replace with the time in `HH:MM:SS` format.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 24. Change a Dropdown Column

**Description:** Update a dropdown column by selecting specific options, with an option to create new labels if they don’t already exist.

### **Mutation Template**

```graphql
mutation {
  change_simple_column_value(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_id: "{{ dropdown_column_id }}",
    value: "{{ options }}",
    create_labels_if_missing: {{ create_labels_if_missing }}
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ dropdown_column_id }}`**: Replace with the ID of the dropdown column.
- **`{{ options }}`**: Replace with a comma-separated list of options (e.g., "Option1, Option2").
- **`{{ create_labels_if_missing }}`**: Replace with `true` or `false`.

### **Expected Response Structure**

```json
{
  "data": {
    "change_simple_column_value": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 25. Change an Email Column

**Description:** Update an email column with a new email address and optional label text.

### **Mutation Template**

```graphql
mutation {
  change_simple_column_value(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_id: "{{ email_column_id }}",
    value: "{{ email_value }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ email_column_id }}`**: Replace with the ID of the email column.
- **`{{ email_value }}`**: Replace with the email address and optional text, separated by a space.

**Example Email Value:**

```
"example@example.com Optional Label"
```

### **Expected Response Structure**

```json
{
  "data": {
    "change_simple_column_value": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 26. Change an Hour Column

**Description:** Set the hour and minute values for an hour-type column.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ hour_column_id }}\": {\"hour\": {{ hour }}, \"minute\": {{ minute }}}}"
```

- **`{{ hour_column_id }}`**: Replace with the ID of the hour column.
- **`{{ hour }}`**: Replace with the hour value (0-23).
- **`{{ minute }}`**: Replace with the minute value (0-59).

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 27. Change an Item's Name

**Description:** Change the name of a specific item.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"name\": \"{{ new_item_name }}\"}"
```

- **`{{ new_item_name }}`**: Replace with the new name for the item.

**Note:** Alternatively, you can use the specific column ID if "name" does not work.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 28. Change a Link Column

**Description:** Update a link column with a URL and display text.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ link_column_id }}\": {\"url\": \"{{ url }}\", \"text\": \"{{ link_text }}\"}}"
```

- **`{{ link_column_id }}`**: Replace with the ID of the link column.
- **`{{ url }}`**: Replace with the URL.
- **`{{ link_text }}`**: Replace with the display text.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 29. Change a Location Column

**Description:** Update a location column with latitude, longitude, and address details.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ location_column_id }}\": {\"lat\": \"{{ latitude }}\", \"lng\": \"{{ longitude }}\", \"address\": \"{{ address }}\"}}"
```

- **`{{ location_column_id }}`**: Replace with the ID of the location column.
- **`{{ latitude }}`**: Replace with the latitude coordinate.
- **`{{ longitude }}`**: Replace with the longitude coordinate.
- **`{{ address }}`**: Replace with the address.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 30. Change a Long Text Column

**Description:** Update a long text column with new content.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ long_text_column_id }}\": {\"text\": \"{{ text_content }}\"}}"
```

- **`{{ long_text_column_id }}`**: Replace with the ID of the long text column.
- **`{{ text_content }}`**: Replace with the new text content.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 31. Change a Numbers Column

**Description:** Update a numbers column with a new numeric value.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ numbers_column_id }}\": \"{{ number_value }}\"}"
```

- **`{{ numbers_column_id }}`**: Replace with the ID of the numbers column.
- **`{{ number_value }}`**: Replace with the numeric value.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 32. Change a People Column

**Description:** Assign people or teams to a people column.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ people_column_id }}\": {\"personsAndTeams\": [{\"id\": {{ person_id1 }}, \"kind\": \"person\"}, {\"id\": {{ person_id2 }}, \"kind\": \"person\"}, {\"id\": {{ team_id }}, \"kind\": \"team\"}]}}"
```

- **`{{ people_column_id }}`**: Replace with the ID of the people column.
- **`{{ person_id1 }}`, `{{ person_id2 }}`**: Replace with the IDs of the people.
- **`{{ team_id }}`**: Replace with the ID of the team.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 33. Change a Phone Column

**Description:** Update a phone column with a new phone number and country code.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ phone_column_id }}\": {\"phone\": \"{{ phone_number }}\", \"countryShortName\": \"{{ country_code }}\"}}"
```

- **`{{ phone_column_id }}`**: Replace with the ID of the phone column.
- **`{{ phone_number }}`**: Replace with the phone number.
- **`{{ country_code }}`**: Replace with the country code (e.g., "US").

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 34. Change a Rating Column

**Description:** Update a rating column with a new rating value.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ rating_column_id }}\": {\"rating\": {{ rating_value }}}}"
```

- **`{{ rating_column_id }}`**: Replace with the ID of the rating column.
- **`{{ rating_value }}`**: Replace with the rating value (e.g., 1 to 5).

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 35. Change a Status Column

**Description:** Set a new label for a status column.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}",
    create_labels_if_missing: {{ create_labels_if_missing }}
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ status_column_id }}\": {\"label\": \"{{ status_label }}\"}}"
```

- **`{{ status_column_id }}`**: Replace with the ID of the status column.
- **`{{ status_label }}`**: Replace with the status label.
- **`{{ create_labels_if_missing }}`**: Replace with `true` or `false`.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 36. Change a Tags Column

**Description:** Update a tags column with specified tag IDs.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}",
    create_labels_if_missing: {{ create_labels_if_missing }}
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ tags_column_id }}\": {\"tag_ids\": [{{ tag_id1 }}, {{ tag_id2 }}]}}"
```

- **`{{ tags_column_id }}`**: Replace with the ID of the tags column.
- **`{{ tag_id1 }}`, `{{ tag_id2 }}`**: Replace with the IDs of the tags.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 37. Change a Text Column

**Description:** Set a new value for a text column.

### **Mutation Template**

```graphql
mutation {
  change_simple_column_value(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_id: "{{ text_column_id }}",
    value: "{{ text_value }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ text_column_id }}`**: Replace with the ID of the text column.
- **`{{ text_value }}`**: Replace with the new text content.

### **Expected Response Structure**

```json
{
  "data": {
    "change_simple_column_value": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 38. Change a Timeline Column

**Description:** Update a timeline column with start and end dates.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ timeline_column_id }}\": {\"from\": \"{{ start_date }}\", \"to\": \"{{ end_date }}\"}}"
```

- **`{{ timeline_column_id }}`**: Replace with the ID of the timeline column.
- **`{{ start_date }}`**, **`{{ end_date }}`**: Replace with dates in `YYYY-MM-DD` format.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 39. Change a Week Column

**Description:** Set the start and end dates for a week column.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ week_column_id }}\": {\"week\": {\"startDate\": \"{{ start_date }}\", \"endDate\": \"{{ end_date }}\"}}}"
```

- **`{{ week_column_id }}`**: Replace with the ID of the week column.
- **`{{ start_date }}`**, **`{{ end_date }}`**: Replace with dates in `YYYY-MM-DD` format.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 40. Change a World Clock Column

**Description:** Update the timezone for a world clock column.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{{ column_values_json }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_values_json }}`**: Use the following JSON string:

```json
"{\"{{ world_clock_column_id }}\": {\"timezone\": \"{{ timezone }}\"}}"
```

- **`{{ world_clock_column_id }}`**: Replace with the ID of the world clock column.
- **`{{ timezone }}`**: Replace with the timezone identifier (e.g., "Europe/London").

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  }
}
```

---

## 41. Clear a Text Column

**Description:** Clear the content of a text column by setting its value to an empty string.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{\"{{ text_column_id }}\": \"\"}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ item_id }}`**: Replace with the ID of the item.
- **`{{ board_id }}`**: Replace with the ID of the board.
- **`{{ text_column_id }}`**: Replace with the ID of the text column you want to clear.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 42. Clear a Numbers Column

**Description:** Clear the value of a numbers column by setting it to an empty string.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{\"{{ numbers_column_id }}\": \"\"}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ numbers_column_id }}`**: Replace with the ID of the numbers column you want to clear.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 43. Clear a Files Column

**Description:** Clear all files in a files column.

### **Mutation Template**

```graphql
mutation {
  change_column_value(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_id: "{{ files_column_id }}",
    value: "{\"clear_all\": true}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ files_column_id }}`**: Replace with the ID of the files column you want to clear.

### **Expected Response Structure**

```json
{
  "data": {
    "change_column_value": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 44. Clear a Connect Boards Column

**Description:** Clear all connected items in a connect boards column.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{\"{{ connect_boards_column_id }}\": {}}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ connect_boards_column_id }}`**: Replace with the ID of the connect boards column you want to clear.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 45. Clear a Dependency Column

**Description:** Clear a dependency column by removing all linked dependencies.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{\"{{ dependency_column_id }}\": {}}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ dependency_column_id }}`**: Replace with the ID of the dependency column you want to clear.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 46. Clear a Status Column

**Description:** Clear a status column by removing the assigned label.

### **Mutation Template**

```graphql
mutation {
  change_multiple_column_values(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_values: "{\"{{ status_column_id }}\": {}}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ status_column_id }}`**: Replace with the ID of the status column you want to clear.

### **Expected Response Structure**

```json
{
  "data": {
    "change_multiple_column_values": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 47. Clear a People Column

**Description:** Clear all people or teams assigned in a people column.

### **Mutation Template**

```graphql
mutation {
  change_column_value(
    item_id: {{ item_id }},
    board_id: {{ board_id }},
    column_id: "{{ people_column_id }}",
    value: "{\"clear_all\": true}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ people_column_id }}`**: Replace with the ID of the people column you want to clear.

### **Expected Response Structure**

```json
{
  "data": {
    "change_column_value": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 48. Get Specific Values in Column Values for a Location Column

**Description:** Retrieve specific details within a location column, such as country, street, and street number.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
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

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the IDs of the items you want to query.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "country": "{{ country1 }}",
            "street": "{{ street1 }}",
            "street_number": "{{ street_number1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "country": "{{ country2 }}",
            "street": "{{ street2 }}",
            "street_number": "{{ street_number2 }}"
          }
        ]
      }
    ]
  }
}
```

---

## 49. Get Specific Values in Column Values for a Status Column

**Description:** Fetch detailed information in a status column, including label and update ID.

### **Query Template**

```graphql
query {
  items(ids: {{ item_id }}) {
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

**Instructions:**

- **`{{ item_id }}`**: Replace with the ID of the item you want to query.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "value": "{{ value }}",
            "type": "{{ type }}",
            "label": "{{ label }}",
            "update_id": "{{ update_id }}"
          }
          // Additional column values...
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 50. Get Specific Values in Column Values for a Checkbox Column

**Description:** Retrieve the checked status and the last updated time of a checkbox column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on CheckboxValue {
        checked
        updated_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the IDs of the items you want to query.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "checked": {{ checked1 }},
            "updated_at": "{{ updated_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "checked": {{ checked2 }},
            "updated_at": "{{ updated_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---


## 51. Get Specific Values in Column Values for a Connect Boards Column

**Description:** Fetch details from a connect boards column, such as linked item IDs and the linked items themselves.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on BoardRelationValue {
        linked_item_ids
        linked_items {
          id
          name
        }
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the IDs of the items you want to query.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "linked_item_ids": [{{ linked_item_id1 }}, {{ linked_item_id2 }}],
            "linked_items": [
              {
                "id": "{{ linked_item_id1 }}",
                "name": "{{ linked_item_name1 }}"
              },
              {
                "id": "{{ linked_item_id2 }}",
                "name": "{{ linked_item_name2 }}"
              }
            ]
          }
        ]
      },
      {
        "column_values": [
          {
            "linked_item_ids": [{{ linked_item_id3 }}],
            "linked_items": [
              {
                "id": "{{ linked_item_id3 }}",
                "name": "{{ linked_item_name3 }}"
              }
            ]
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 52. Get Specific Values in Column Values for a Country Column

**Description:** Retrieve country details and the last update time for a country column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on CountryValue {
        country
        country_code
        updated_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the IDs of the items you want to query.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "country": "{{ country_name1 }}",
            "country_code": "{{ country_code1 }}",
            "updated_at": "{{ updated_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "country": "{{ country_name2 }}",
            "country_code": "{{ country_code2 }}",
            "updated_at": "{{ updated_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 53. Get Specific Values in Column Values for a Date Column

**Description:** Retrieve date and time details from a date column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on DateValue {
        date
        time
        changed_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "date": "{{ date1 }}",
            "time": "{{ time1 }}",
            "changed_at": "{{ changed_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "date": "{{ date2 }}",
            "time": "{{ time2 }}",
            "changed_at": "{{ changed_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 54. Get Specific Values in Column Values for a Dependency Column

**Description:** Fetch linked item IDs and the last updated time for a dependency column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on DependencyValue {
        linked_item_ids
        updated_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "linked_item_ids": [{{ linked_item_id1 }}, {{ linked_item_id2 }}],
            "updated_at": "{{ updated_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "linked_item_ids": [{{ linked_item_id3 }}],
            "updated_at": "{{ updated_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 55. Get Specific Values in Column Values for a Dropdown Column

**Description:** Retrieve selected values and column details for a dropdown column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on DropdownValue {
        values {
          id
          name
        }
        column {
          id
        }
        updated_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "values": [
              {
                "id": "{{ option_id1 }}",
                "name": "{{ option_name1 }}"
              },
              {
                "id": "{{ option_id2 }}",
                "name": "{{ option_name2 }}"
              }
            ],
            "column": {
              "id": "{{ dropdown_column_id }}"
            },
            "updated_at": "{{ updated_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "values": [],
            "column": {
              "id": "{{ dropdown_column_id }}"
            },
            "updated_at": "{{ updated_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 56. Get Specific Values in Column Values for an Email Column

**Description:** Retrieve the email address and last update time for an email column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on EmailValue {
        email
        text
        updated_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "email": "{{ email1 }}",
            "text": "{{ text1 }}",
            "updated_at": "{{ updated_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "email": "{{ email2 }}",
            "text": "{{ text2 }}",
            "updated_at": "{{ updated_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 57. Get Specific Values in Column Values for an Hour Column

**Description:** Fetch the hour and minute values from an hour column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on HourValue {
        hour
        minute
        changed_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "hour": {{ hour1 }},
            "minute": {{ minute1 }},
            "changed_at": "{{ changed_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "hour": {{ hour2 }},
            "minute": {{ minute2 }},
            "changed_at": "{{ changed_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 58. Get Specific Values in Column Values for a Link Column

**Description:** Retrieve the URL and display text from a link column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on LinkValue {
        url
        text
        changed_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "url": "{{ url1 }}",
            "text": "{{ text1 }}",
            "changed_at": "{{ changed_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "url": "{{ url2 }}",
            "text": "{{ text2 }}",
            "changed_at": "{{ changed_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 59. Get Specific Values in Column Values for a Long Text Column

**Description:** Retrieve the text content and value from a long text column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on LongTextValue {
        text
        value
        updated_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "text": "{{ text_content1 }}",
            "value": "{{ value1 }}",
            "updated_at": "{{ updated_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "text": "{{ text_content2 }}",
            "value": "{{ value2 }}",
            "updated_at": "{{ updated_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 60. Get Specific Values in Column Values for a Monday Doc Column

**Description:** Retrieve file information from a Monday Doc column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on DocValue {
        file {
          id
          name
          url
          created_at
          file_extension
        }
        updated_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "file": {
              "id": "{{ file_id1 }}",
              "name": "{{ file_name1 }}",
              "url": "{{ file_url1 }}",
              "created_at": "{{ created_at1 }}",
              "file_extension": "{{ file_extension1 }}"
            },
            "updated_at": "{{ updated_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "file": {
              "id": "{{ file_id2 }}",
              "name": "{{ file_name2 }}",
              "url": "{{ file_url2 }}",
              "created_at": "{{ created_at2 }}",
              "file_extension": "{{ file_extension2 }}"
            },
            "updated_at": "{{ updated_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 61. Get Specific Values in Column Values for a Numbers Column

**Description:** Retrieve the numeric value and ID from a numbers column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on NumbersValue {
        number
        id
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the IDs of the items you want to query.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "number": {{ number_value1 }},
            "id": "{{ numbers_column_id }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "number": {{ number_value2 }},
            "id": "{{ numbers_column_id }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 62. Get Specific Values in Column Values for a People Column

**Description:** Fetch information about persons and teams from a people column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
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

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "persons_and_teams": [
              {
                "id": "{{ person_or_team_id1 }}"
              },
              {
                "id": "{{ person_or_team_id2 }}"
              }
            ]
          }
        ]
      },
      {
        "column_values": [
          {
            "persons_and_teams": []
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 63. Get Specific Values in Column Values for a Phone Column

**Description:** Retrieve the phone number and country code from a phone column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on PhoneValue {
        country_short_name
        phone
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "country_short_name": "{{ country_code1 }}",
            "phone": "{{ phone_number1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "country_short_name": "{{ country_code2 }}",
            "phone": "{{ phone_number2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 64. Get Specific Values in Column Values for a Status Column

**Description:** Retrieve the index and value of a status column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on StatusValue {
        index
        value
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "index": {{ status_index1 }},
            "value": "{{ status_value1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "index": {{ status_index2 }},
            "value": "{{ status_value2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 65. Using `items_page` with Query Parameters

**Description:** Retrieve items from a board with specific filters on column values using query parameters.

### **Query Template**

```graphql
query {
  boards(ids: {{ board_id }}) {
    items_page(
      limit: {{ limit }},
      query_params: {
        rules: [{ column_id: "{{ column_id }}", compare_value: "{{ compare_value }}" }],
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

**Instructions:**

- **`{{ board_id }}`**: Replace with the board ID.
- **`{{ limit }}`**: Replace with the number of items to retrieve.
- **`{{ column_id }}`**: Replace with the column ID to filter on.
- **`{{ compare_value }}`**: Replace with the value to compare.

### **Expected Response Structure**

```json
{
  "data": {
    "boards": [
      {
        "items_page": {
          "cursor": "{{ next_cursor }}",
          "items": [
            {
              "id": "{{ item_id1 }}",
              "name": "{{ item_name1 }}"
            },
            // Additional items...
          ]
        }
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 66. Using `next_items_page`

**Description:** Fetch the next set of items based on a cursor for pagination.

### **Query Template**

```graphql
query {
  next_items_page(
    limit: {{ limit }},
    cursor: "{{ cursor }}"
  ) {
    cursor
    items {
      id
      name
    }
  }
}
```

**Instructions:**

- **`{{ limit }}`**: Number of items to retrieve.
- **`{{ cursor }}`**: The cursor obtained from the previous `items_page` or `next_items_page` call.

### **Expected Response Structure**

```json
{
  "data": {
    "next_items_page": {
      "cursor": "{{ next_cursor }}",
      "items": [
        {
          "id": "{{ item_id1 }}",
          "name": "{{ item_name1 }}"
        },
        // Additional items...
      ]
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 67. Using `items_page`

**Description:** Retrieve a paginated set of items from a board.

### **Query Template**

```graphql
query {
  boards(ids: {{ board_id }}) {
    items_page(limit: {{ limit }}) {
      cursor
      items {
        id
        name
      }
    }
  }
}
```

**Instructions:**

- **`{{ board_id }}`**: Replace with the board ID.
- **`{{ limit }}`**: Number of items to retrieve.

### **Expected Response Structure**

```json
{
  "data": {
    "boards": [
      {
        "items_page": {
          "cursor": "{{ next_cursor }}",
          "items": [
            {
              "id": "{{ item_id1 }}",
              "name": "{{ item_name1 }}"
            },
            // Additional items...
          ]
        }
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 68. Using `items_page_by_column_values`

**Description:** Retrieve items from a board that match specific column values.

### **Query Template**

```graphql
query {
  items_page_by_column_values(
    limit: {{ limit }},
    board_id: {{ board_id }},
    columns: [
      { column_id: "{{ column_id1 }}", column_values: ["{{ value1 }}", "{{ value2 }}"] },
      { column_id: "{{ column_id2 }}", column_values: ["{{ value3 }}"] }
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

**Instructions:**

- **`{{ limit }}`**: Number of items to retrieve.
- **`{{ board_id }}`**: Replace with the board ID.
- **`{{ column_id1 }}`, `{{ column_id2 }}`**: Column IDs to filter on.
- **`{{ value1 }}`, `{{ value2 }}`, `{{ value3 }}`**: Values to match in the columns.

### **Expected Response Structure**

```json
{
  "data": {
    "items_page_by_column_values": {
      "cursor": "{{ next_cursor }}",
      "items": [
        {
          "id": "{{ item_id1 }}",
          "name": "{{ item_name1 }}"
        },
        // Additional items...
      ]
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 69. Move an Item to a Different Board

**Description:** Move an item to a specified board and group.

### **Mutation Template**

```graphql
mutation {
  move_item_to_board(
    item_id: {{ item_id }},
    board_id: {{ target_board_id }},
    group_id: "{{ target_group_id }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ item_id }}`**: ID of the item to move.
- **`{{ target_board_id }}`**: ID of the board to move the item to.
- **`{{ target_group_id }}`**: ID of the group within the target board.

### **Expected Response Structure**

```json
{
  "data": {
    "move_item_to_board": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 70. Get Items Linked to a Specific Item

**Description:** Retrieve items that are linked to a specified item through a connect boards column.

### **Query Template**

```graphql
query {
  items(ids: {{ item_id }}) {
    linked_items(
      linked_board_id: {{ linked_board_id }},
      link_to_item_column_id: "{{ connect_boards_column_id }}"
    ) {
      id
      name
    }
  }
}
```

**Instructions:**

- **`{{ item_id }}`**: ID of the item whose linked items you want to retrieve.
- **`{{ linked_board_id }}`**: ID of the linked board.
- **`{{ connect_boards_column_id }}`**: ID of the connect boards column.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "linked_items": [
          {
            "id": "{{ linked_item_id1 }}",
            "name": "{{ linked_item_name1 }}"
          },
          // Additional linked items...
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 71. Clear Column Values

**Description:** Clear the value of a specific column by setting it to `null`.

### **Mutation Template**

```graphql
mutation {
  change_simple_column_value(
    board_id: {{ board_id }},
    item_id: {{ item_id }},
    column_id: "{{ column_id }}",
    value: null
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ column_id }}`**: Replace with the ID of the column you want to clear.

### **Expected Response Structure**

```json
{
  "data": {
    "change_simple_column_value": {
      "id": "{{ item_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 72. Get Specific Values in Column Values for a Rating Column

**Description:** Retrieve the rating value and last updated time for a rating column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on RatingValue {
        rating
        updated_at
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "rating": {{ rating_value1 }},
            "updated_at": "{{ updated_at1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "rating": {{ rating_value2 }},
            "updated_at": "{{ updated_at2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 73. Get Specific Values in Column Values for a Tags Column

**Description:** Retrieve tag IDs and associated text from a tags column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on TagsValue {
        tag_ids
        text
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "tag_ids": [{{ tag_id1 }}, {{ tag_id2 }}],
            "text": "{{ tags_text1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "tag_ids": [{{ tag_id3 }}],
            "text": "{{ tags_text2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 74. Get Specific Values in Column Values for a Text Column

**Description:** Retrieve the text content and value from a text column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on TextValue {
        text
        value
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "text": "{{ text_content1 }}",
            "value": "{{ text_value1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "text": "{{ text_content2 }}",
            "value": "{{ text_value2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 75. Get Specific Values in Column Values for a Timeline Column

**Description:** Retrieve the start and end dates of a timeline column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on TimelineValue {
        from
        to
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "from": "{{ start_date1 }}",
            "to": "{{ end_date1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "from": "{{ start_date2 }}",
            "to": "{{ end_date2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 76. Get Specific Values in Column Values for a Week Column

**Description:** Retrieve the start and end dates of a week column.

### **Query Template**

```graphql
query {
  items(ids: [{{ item_id1 }}, {{ item_id2 }}]) {
    column_values {
      ... on WeekValue {
        start_date
        end_date
      }
    }
  }
}
```

**Instructions:**

- **`{{ item_id1 }}`, `{{ item_id2 }}`**: Replace with the item IDs.

### **Expected Response Structure**

```json
{
  "data": {
    "items": [
      {
        "column_values": [
          {
            "start_date": "{{ start_date1 }}",
            "end_date": "{{ end_date1 }}"
          }
        ]
      },
      {
        "column_values": [
          {
            "start_date": "{{ start_date2 }}",
            "end_date": "{{ end_date2 }}"
          }
        ]
      }
    ]
  },
  "account_id": {{ account_id }}
}
```

---

## 77. Create a Tag

**Description:** Create a new tag or retrieve an existing tag with the specified name.

### **Mutation Template**

```graphql
mutation {
  create_or_get_tag(tag_name: "{{ tag_name }}") {
    id
  }
}
```

**Instructions:**

- **`{{ tag_name }}`**: Replace with the name of the tag.

### **Expected Response Structure**

```json
{
  "data": {
    "create_or_get_tag": {
      "id": "{{ tag_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 78. Create an Update

**Description:** Create an update attached to a specified item.

### **Mutation Template**

```graphql
mutation {
  create_update(
    item_id: {{ item_id }},
    body: "{{ update_body }}"
  ) {
    id
  }
}
```

**Instructions:**

- **`{{ item_id }}`**: ID of the item to attach the update to.
- **`{{ update_body }}`**: Content of the update.

### **Expected Response Structure**

```json
{
  "data": {
    "create_update": {
      "id": "{{ update_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## 79. Create a Webhook

**Description:** Set up a webhook to monitor events on a specified board.

### **Mutation Template**

```graphql
mutation {
  create_webhook(
    board_id: {{ board_id }},
    url: "{{ webhook_url }}",
    event: {{ event_type }},
    config: "{{ config_json }}"
  ) {
    id
    board_id
  }
}
```

**Instructions:**

- **`{{ board_id }}`**: ID of the board to monitor.
- **`{{ webhook_url }}`**: Endpoint URL for the webhook.
- **`{{ event_type }}`**: Event to monitor (e.g., `change_column_value`).
- **`{{ config_json }}`**: Configuration JSON string for the webhook.

**Example Configuration for Status Column Changes:**

```json
"{\"columnId\":\"{{ status_column_id }}\", \"columnValue\":{\"$any$\":true}}"
```

### **Expected Response Structure**

```json
{
  "data": {
    "create_webhook": {
      "id": "{{ webhook_id }}",
      "board_id": "{{ board_id }}"
    }
  },
  "account_id": {{ account_id }}
}
```

---

## General Notes

- **IDs and Values**: Ensure all placeholders like `{{ item_id }}`, `{{ board_id }}`, `{{ column_id }}`, etc., are replaced with actual values from your Monday.com account.
- **JSON Formatting**: When providing JSON values in mutations, ensure that the JSON string is properly escaped and formatted.
- **Pagination**: When dealing with paginated queries like `items_page`, make sure to handle the `cursor` for fetching subsequent pages.
- **Clearing Column Values**: To clear a column value, you can set it to `null`, an empty string `""`, or an empty object `{}`, depending on the column type.
- **Error Handling**: Always check for errors in the response and handle them appropriately in your application.
- **Official Documentation**: Consult the [Monday.com API documentation](https://api.developer.monday.com/docs) for the most up-to-date information on API capabilities and limitations.

---

