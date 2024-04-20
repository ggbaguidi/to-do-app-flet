"""main module"""
import flet as ft
from task import Task

class TodoApp(ft.Column):
    """UI components"""
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.new_task = None
        self.filter = None
        self.view = None
        self.tasks = None

    def build(self):
        """build method"""
        super().build()

        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="all"), ft.Tab(text="active"), ft.Tab(text="completed")],
        )

        self.view = ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                    ],
                ),
            ],
        )

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                    ],
                ),
            ],
        )

    def add_clicked(self, _):
        """add clicked method"""
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.delete_clicked)
            self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def delete_clicked(self, task):
        """delete ckicked method"""
        self.tasks.controls.remove(task)
        self.update()

    def update(self):
        """update"""
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and not task.completed)
                or (status == "completed" and task.completed)
            )
        super().update()

    def tabs_changed(self, _):
        """tabs changed"""
        self.update()

    def task_status_change(self, _):
        """change the task status"""
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
