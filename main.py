import customtkinter
from pystray import Icon as icon, MenuItem as menu_item
from PIL import Image 
import keyboard


match customtkinter.get_appearance_mode():
    case "Light":
        tray_icon_image = Image.open('icons/dark_keyboard.png')

    case "Dark":
        tray_icon_image = Image.open('icons/light_keyboard.png')


def notify(tray_icon: icon, message: str) -> None:
    if tray_icon.HAS_NOTIFICATION:
        tray_icon.notify(message)


def quit_window(tray_icon: icon, tray_item: menu_item) -> None:
    tray_icon.stop()


def disable_clear_mode(tray_icon: icon, tray_item: menu_item) -> None:
    notify(tray_icon, 'Clear mode is disabled')

    tray_menu = (
        menu_item('Enable clear mode', enable_clear_mode),
        menu_item('Quit', quit_window)
    )

    tray_icon.menu = tray_menu

    for i in range(150):
        keyboard.unblock_key(i)


def enable_clear_mode(tray_icon: icon, tray_item: menu_item) -> None:
    notify(tray_icon, 'Clear mode is enabled')

    tray_menu = (
        menu_item('Disable clear mode', disable_clear_mode), 
        menu_item('Quit', quit_window)
    )

    tray_icon.menu = tray_menu

    for i in range(150):
        keyboard.block_key(i)


def show_tray_menu() -> None:
    tray_menu = (menu_item('Enable clear mode', enable_clear_mode), menu_item('Quit', quit_window))
    tray_icon = icon('Tray image', tray_icon_image, 'Keyboard cleaner', tray_menu)
    tray_icon.run()


if __name__ == "__main__":
    show_tray_menu()

