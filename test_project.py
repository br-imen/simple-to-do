import pytest
from project import add_task, remove_task, view_tasks, todo_list


def setup_function():
    """Setup test environment by clearing the todo_list."""
    todo_list.clear()


def test_add_task():
    add_task("Buy groceries")
    assert todo_list == ["Buy groceries"]


def test_remove_task():
    add_task("Read book")
    add_task("Write code")
    remove_task(1)
    assert todo_list == ["Write code"]


def test_view_tasks(capsys):
    add_task("Go jogging")
    view_tasks()
    captured = capsys.readouterr()
    assert "1. Go jogging" in captured.out
