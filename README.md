# Simple-To-Do

#### Video Demo: <URL HERE>

#### Description:
This is a command-line To-Do List Manager built in Python that allows users to manage their tasks easily. Users can add, remove, and view tasks, as well as save and load tasks from a file.

## Project Structure:
- project.py
- test_project.py
- tasks.txt
- requirements.txt


### File Descriptions:

- **`project.py`**:
  - Contains the core functionality of the To-Do List Manager.
  - Defines the following functions:
    - `add_task(task)`: Adds a new task to the list.
    - `remove_task(index)`: Removes a task by its index (1-based).
    - `view_tasks()`: Displays all tasks in the list.
    - `save_tasks_to_file()`: Saves the current list of tasks to `tasks.txt`.
    - `load_tasks_from_file()`: Loads tasks from `tasks.txt` when the program starts.
  - The `main()` function provides a command-line interface for user interaction.

- **`test_project.py`**:
  - Contains unit tests for the functions defined in `project.py`.
  - Utilizes the `pytest` framework to test the following:
    - `test_add_task()`: Verifies that tasks are added correctly.
    - `test_remove_task()`: Checks that tasks can be removed correctly by index.
    - `test_view_tasks()`: Tests that the tasks are displayed as expected.

- **`tasks.txt`** (Optional):
  - This file is created automatically when tasks are saved. It stores the current tasks in the To-Do List Manager.

- **`requirements.txt`**:
  - Lists any external libraries required for this project. (Add libraries here if you use any that are not built-in.)

### How to Run the Project:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**

    ```bash
    python project.py
    ```

4. **Run tests**
    ```bash
    pytest test_project.py
    ```

### Acknowledgements
I would like to thank the CS50 teaching team for their guidance and the invaluable knowledge shared throughout the course.
