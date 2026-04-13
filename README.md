# Odoo 18 - Todo List Management Module

A custom Odoo 18 module for managing Todo Lists with status tracking, priority levels, and attendee management.

---

## 📋 Features

- ✅ Create and manage Todo Lists with title, tags, dates and priority
- ✅ Status tracking: **Draft → In Progress → Complete**
- ✅ Priority levels: **Low / Medium / High**
- ✅ Todo items with inline editing and completion checkbox
- ✅ Attendee management linked to system users
- ✅ 3 sub-menus: All / Incomplete / Complete
- ✅ Default tags: Work, Event, Life Achievement

---

## 🚀 Installation

### Prerequisites
- Odoo 18.0
- Python 3.12
- PostgreSQL

### Steps

1. Clone this repository into your custom addons folder:
```bash
git clone git@github.com:Angelalala07/odoo-todo-list.git
```

2. Add the folder to your Odoo addons path:
```bash
python odoo-bin -r odoo -w odoo --addons-path=addons,/path/to/custom-addons --db-filter=odoo -d odoo -u todo_list
```

3. Go to **Apps** in Odoo, search for **Todo List** and click **Activate**

---

## 📖 How to Use

### Creating a Todo List
1. Click **Todo List** in the top navigation bar
2. Click the **New** button
3. Fill in the **Title** (required)
4. Select **Tags** (Work, Event, Life Achievement or create your own)
5. Select **Priority** (Low / Medium / High)
6. Set **Start Date** and **End Date** (required)
7. Click **Save**

### Managing Status
| Button | Action |
|--------|--------|
| **Progress** | Changes status from Draft → In Progress |
| **Done** | Changes status from In Progress → Complete (only appears when all items are checked) |

> ⚠️ Status bar is also clickable to change status directly

### Adding Todo Items
1. Open a Todo List record
2. Click the **List** tab
3. Click **Add a line** to add items inline
4. Fill in **Item Name** and **Description**
5. The **Is Complete** checkbox only appears when status is **In Progress**
6. When status is **Complete**, all items become **non-editable**

### Adding Attendees
1. Open a Todo List record
2. Click the **Attendee** tab
3. Click **Add a line** and select a user
4. When status is **Complete**, attendees become **non-editable**

### Managing Tags
1. Click **Todo List → Tags** in the navigation menu
2. Click **New** to create a tag
3. Enter a **Tag Name** and select a **Color**
4. Click **Save**

### Filtering Records
Use the **search bar** to filter by:
- 🔍 **Title** — search by name
- 🏷️ **Tags** — filter by tag
- 📊 **Status** — Draft / In Progress / Complete
- 🚩 **Priority** — Low / Medium / High

---

## 📁 Module Structure

    todo_list/
    ├── __init__.py
    ├── __manifest__.py
    ├── models/
    │   ├── __init__.py
    │   ├── todo_list.py
    │   └── todo_item.py
    ├── views/
    │   └── todo_list_views.xml
    ├── data/
    │   └── todo_tags.xml
    ├── security/
    │   └── ir.model.access.csv
    └── static/
        └── src/css/
            └── todo_list.css