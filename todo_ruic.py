"""todo module with reusable ui components
"""
import flet as ft


class TodoApp(ft.UserControl):
    """UI components"""
    new_task = None
    tasks = None

    def build(self):
        """build method"""
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
        self.tasks.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()


if __name__ == "__main__":
    def main(page: ft.Page):
        """entry function"""
        page.title = "ToDo App"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.update()

        todo = TodoApp()

        page.add(todo)

    ft.app(target=main)
