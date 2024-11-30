import pyautogui as pgui
# for window
# import webbrowser as wb
import subprocess 

# wb.open("//usr//bin//gnome-text-editor")
subprocess.Popen("gnome-text-editor")

pgui.sleep(1)

for x in range (20):
    pgui.typewrite("Hello vijay How Are you !!")
    pgui.sleep(0.3)
    pgui.press('enter')
    pgui.sleep(0.3)