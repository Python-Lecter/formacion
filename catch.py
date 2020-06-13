import subprocess
import time
import os
from operator import itemgetter

# -- set update/round time (seconds)
period = 5
# -- set sorting order. up = most used first, use either "up" or "down"
order = "up"

# Directory where the log will be safe
home = os.environ["HOME"]
logdir = home+"/.usagelogs"

# Metodo para ejecutar comandos y retornar la stdout||staderr
def get(command):
    try:
        return subprocess.check_output(command).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        pass

# Inicializar variables de Tiempo Lista de Aplicaciones y Lista de ventanas
t, applist, winlist = 0, [], []

#Recoleccion de datos infinitamente
while True:
    # Tiempo de refresco
    time.sleep(period)
    # ObteniendoPrint cross@ubuntucrossD:~$ xdotool getactivewindow getwindowpid //17305
    frpid = get(["xdotool", "getactivewindow", "getwindowpid"])
    # ObteniendoPrint cross@ubuntucrossD:~$ xdotool getactivewindow getwindowname //cross@ubuntucrossD: ~
    frname = get(["xdotool", "getactivewindow", "getwindowname"])
    # ObteniendoPrint en terminal cross@ubuntucrossD:~$ ps -p 17359 o comm= //bash si no regresa nada es Unknown
    app = get(["ps", "-p", frpid, "o", "comm="]) if frpid != None else "Unknown"
    # fix a few names
    if "bash" in app:
        app = "gnome-terminal-bash"
    elif app == "soffice.bin":
        app = "libreoffice"
    # Agregar app a la lista solo si es nueva entrada
    if not app in applist:
        applist.append(app)