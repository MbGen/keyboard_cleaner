import customtkinter
from pystray import Icon as icon, MenuItem as menu_item
from PIL import Image 
import keyboard

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

match customtkinter.get_appearance_mode():
    case "Light":
        tray_icon_image = Image.open('icons/dark_keyboard.png')

    case "Dark":
        tray_icon_image = Image.open('icons/light_keyboard.png')


app = customtkinter.CTk()
app.title("Keyboard cleaner")
app.geometry("400x200")

clear_mode = False

def quit_window(tray_icon: icon, tray_item: menu_item) -> None:
    tray_icon.stop()
    app.destroy()

def disable_clear_mode(tray_icon: icon, tray_item: menu_item) -> None:
    if tray_icon.HAS_NOTIFICATION:
        tray_icon.notify('Clear mode is diabled')

    tray_menu = (
        menu_item('Enable clear mode', enable_clear_mode),
        menu_item('Quit', quit_window)
    )
    tray_icon.menu = tray_menu
    for i in range(150):
        keyboard.unblock_key(i)

def enable_clear_mode(tray_icon: icon, tray_item: menu_item) -> None:
    if tray_icon.HAS_NOTIFICATION:
        tray_icon.notify('Clear mode is enabled')

    tray_menu = (
        menu_item('Disable clear mode', disable_clear_mode), 
        menu_item('Quit', quit_window)
    )
    tray_icon.menu = tray_menu
    for i in range(150):
        keyboard.block_key(i)

def hide_window() -> None:
    tray_menu = (menu_item('Enable clear mode', enable_clear_mode), menu_item('Quit', quit_window))
    tray_icon = icon('Tray image', tray_icon_image, 'Keyboard cleaner', tray_menu)
    tray_icon.run()


if __name__ == "__main__":
    app.wm_state(newstate='withdraw')
    app.protocol('WM_DELETE_WINDOW', hide_window())
    app.mainloop()
