import pyautogui
import time
import keyboard
import threading

program_running = False
lock = threading.Lock()
start_requested = False  # Agregamos una variable para rastrear si se ha solicitado iniciar


def start_program():
    global program_running, start_requested
    if not program_running and start_requested:
        start_requested = False  # Reiniciamos el inicio solicitado
        program_running = True
        print("Programa iniciado")
        time.sleep(1)
        for i in range(500):
            with lock:
                if not program_running:
                    break
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.3)
            pyautogui.hotkey('alt', 'tab')
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.3)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.hotkey('alt', 'tab')
            pyautogui.press('down')
def stop_program():
    global program_running, start_requested
    if program_running:
        with lock:
            program_running = False
        print("Programa detenido")
def request_start():
    global start_requested
    start_requested = True
keyboard.add_hotkey('ctrl+shift+|', request_start)  # Cambiamos la llamada a start_program por request_start
keyboard.add_hotkey('esc', stop_program)
if __name__ == "__main__":
    t = threading.Thread(target=start_program)
    t.start()

