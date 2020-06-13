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

def summarize():
    # Abrir archivo log con manejo de exepciones
    # wt=write text(default)
    with open(log, "wt") as report:
        totaltime = sum(it[2] for it in winlist)
        report.write("")
        alldata = []
        for app in applist:
            appdata, windata = [], []
            apptime = sum([it[2] for it in winlist if it[0] == app])
            appperc = round(100*apptime/totaltime)
            for d in [app, apptime, appperc]:
                appdata.append(d)
            wins = [r for r in winlist if r[0] == app]
            for w in wins:
                wperc = str(round(100*w[2]/totaltime))
                windata.append([w[1], w[2], wperc])
            windata = sorted(windata, key=itemgetter(1))
            windata = windata[::-1] if order == "up" else windata
            appdata.append(windata)
            alldata.append(appdata)
        alldata = sorted(alldata, key = itemgetter(1))
        alldata = alldata[::-1] if order == "up" else alldata
        for item in alldata:
            app, apptime, appperc = item[0], item[1], item[2]
            report.write(
                ("-"*60) \
                 +"\n" \
                 +app \
                 +"\n" \
                 +time_format(apptime) \
                 +" ("+str(appperc)+"%)\n" \
                 +("-"*60) \
                 +"\n"
            )
            for w in item[3]:
                wname, time, perc = w[0]

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
    # Inicializando checklist con winlist value
    checklist = [item[1] for item in winlist]
    # Si no hay registros en checklist
    # inicializo winlist
    if not fname in checklist:
        winlist.append([app, frname, 1*period])
    # Si ya existe un registro en la checklist solo se
    # se actualiza la winlist
    else:
        winlist[checklist.index(frname)][
            2] = winlist[checklist.index(frname)][2]+1*period
    if t == 60/period:
        summarize()
        t = 0
    else:
        t += 1