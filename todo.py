"""to do module
"""
import flet as ft

if __name__ == "__main__":

    def main(page: ft.Page):
        """main function
        """
        def add_clicked(_):
            """add new task when click
            """
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            page.update()

        new_task = ft.TextField(hint_text="Whats needs to be done?")
        page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))


    ft.app(target=main)
