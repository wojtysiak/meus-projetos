from conexão_banco import cursor,conexao
import flet as ft
import funções
import telas
from datetime import datetime


def main(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     messages = ft.Column(tight=True)

#     def handle_change(e: ft.Event[ft.DatePicker]):
#         if int(e.control.value.strftime('%Y')) < 1998:
#             messages.controls.append(
#                   ft.Text(f"mentiu Date changed: {e.control.value.strftime('%m/%d/%Y')}")
#             )
#         else:
#             messages.controls.append(
#                   ft.Text(f" Date changed: {e.control.value.strftime('%m/%d/%Y')}")
#             )


#     def handle_dismissal(_: ft.Event[ft.DialogControl]):
#         messages.controls.append(ft.Text("DatePicker dismissed"))

    

#     def valida_pica(e: ft.Event[ft.DatePicker]):

#       messages.controls.append(ft.Text(f'{e.control.value}'))


#     picker = ft.DatePicker(
#         date_picker_mode = datetime.now(),
#         on_change=valida_pica
#     )

#     page.add(ft.FloatingActionButton(content='data',on_click=lambda _:page.show_dialog(picker)),messages)
# #         ft.SafeArea(
# #             content=ft.Column(
# #                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
# #                 controls=[
# #                     ft.Button(
# #                         icon=ft.Icons.CALENDAR_MONTH,
# #                         on_click=lambda _: page.show_dialog(picker),
# #                         content="Pick date",
# #                     ),
# #                     messages,
# #                 ],
# #             ),
# #         )
# #     )
      tela=telas.Cadastrar_Produto(page)
      page.add(tela)


if __name__ == "__main__":
    ft.run(main)