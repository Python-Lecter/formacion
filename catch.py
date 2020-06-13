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

# Inicializar variables de Tiempo Lista de Aplicaciones y Lista de ventanas
t, applist, winlist = 0, [], []

#Recoleccion de datos infinitamente
while True:
    # Tiempo de refresco
    time.sleep(period)
    # Obteniendo el pid con la funcion get
    frpid = get(["xdotool", "getactivewindow", "getwindowpid"])
    frname = get(["xdotool", "getactivewindow", "getwindowname"])