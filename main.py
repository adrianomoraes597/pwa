import flet as ft

# Nome dos ícones dentro do direório `/assets/icons`
# icon-192.png, icon-512.png - Ícones para o Windows.
# icon-maskable-192.png, icon-maskable-512.png - Ícones para o Android.
# apple-touch-icon-192.png - Ícones para o iOS.
# loading-animation.png - Ícone para a splash screen (tela inicial de carregamento)

# Arquivos dentro de `assets`
# favicon.png - Ícone usado nos navegadores
# manifest.json - Arquivo com as configurações do PWA


# Exemplo de código para teste
def main(page: ft.Page):
    page.title = "Contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')