"""task module"""
import flet as ft


class Task(ft.Column):
    """task class"""
    def __init__(self, task_name, task_status_change, task_delete, *args, **kwargs):
        """create a task instance method"""
        super().__init__(args, kwargs)
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
        self.display_task = None
        self.display_view = None
        self.edit_view = None
        self.edit_name = None

    def build(self):
        """build widget method"""
        super().build()
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.EDIT_OUTLINED,
                            tooltip="Edit-To DO",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINED,
                            tooltip="Delete-To DO",
                            on_click=self.delete_clicked,
                        )
                    ]
                )
            ]
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update-To Do",
                    on_click=self.save_clicked,
                ),
            ]
        )

        return ft.Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, _):
        """edit method when the button is clicked"""
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def delete_clicked(self, _):
        """delete method when the button is clicked"""
        self.task_delete(self)

    def save_clicked(self, _):
        """update method when the button is clicked"""
        self.display_task.label = self.edit_name.value
        self.edit_name.value = ""
        self.edit_view.visible = False
        self.display_view.visible = True
        self.update()

    def status_changed(self, _):
        "change the status"
        self.completed = self.display_task.value
        self.task_status_change(self)
