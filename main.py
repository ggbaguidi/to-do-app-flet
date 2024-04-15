"""main module"""
import flet as ft
from task import Task

class TodoApp(ft.Column):
    """UI components"""
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.new_task = None
        self.tasks = None

    def build(self):
        """build method"""
        super().build()

        self.new_task = ft.TextField(
            hint_text="Whats needs to be done?", expand=True)
        self.tasks = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, _):
        """add clicked method"""
        if self.new_task.value:
            task = Task(self.new_task.value, self.delete_clicked)
            self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def delete_clicked(self, task):
        """delete ckicked method"""
        self.tasks.controls.remove(task)
        self.update()


if __name__ == "__main__":
    def main(page: ft.Page):
        """entry function"""
        page.title = "ToDo App"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.update()

        todo1 = TodoApp()
        todo2 = TodoApp()

        page.add(todo1, todo2)

    ft.app(target=main)
