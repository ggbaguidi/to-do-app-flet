"""hello module
"""
import flet as ft

if __name__ == "__main__":
    def main(page: ft.Page):
        """main function"""
        page.add(ft.Text(value="Hello, World !"))

    ft.app(target=main)
