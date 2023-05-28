def make24(ts: str):
    ts = ts.split()
    if ts[1] == 'a.m.':
        return "0"+ts[0] if len(ts[0]) == 4 else ts[0]
    else:
        hours, minutes = ts[0].split(':')
        if int(hours) < 12:
            hours = int(hours)+12
        else:
            return "00:00"
        return str(hours)+":"+minutes


t = '11:15 p.m.'
print(make24(t))