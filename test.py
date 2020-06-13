winlist = []
fname = "Anibal"
sname = "Lecter"

checklist = [item[1] for item in winlist]
if not fname in checklist:#Se agrega a winlist xq no esta
    winlist.append([fname, sname, 5])
else:#Ya existe fname solo actualizo el uptime
    winlist[checklist.index(fname)][2]  = winlist[checklist.index(fname)][2]+1*5
