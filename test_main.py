import unittest
import main
import os

class TestToDoList(unittest.TestCase):
    def setUp(self):
        # Ensure the todo_list.json file does not exist before each test
        if os.path.exists(main.TODO_FILE):
            os.remove(main.TODO_FILE)

    def tearDown(self):
        # Clean up by removing the todo_list.json file after each test
        if os.path.exists(main.TODO_FILE):
            os.remove(main.TODO_FILE)

    def test_add_task(self):
        main.add_task("Test task")
        tasks = main.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['task'], "Test task")
        self.assertFalse(tasks[0]['completed'])

    def test_view_tasks(self):
        main.add_task("Test task")
        main.view_tasks()
        # Manual check: View the output

    def test_delete_task(self):
        main.add_task("Test task")
        main.delete_task(1)
        tasks = main.load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_mark_task_completed(self):
        main.add_task("Test task")
        main.mark_task_completed(1)
        tasks = main.load_tasks()
        self.assertTrue(tasks[0]['completed'])

if __name__ == "__main__":
    unittest.main()
