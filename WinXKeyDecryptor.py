import winreg

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion", access=winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
value = winreg.QueryValueEx(key, "DigitalProductId")
vcp = list(value[0])
vcp[66] = 1
cp = list(vcp[52:])

alph = "BCDFGHJKMPQRTVWXY2346789"
out = ''
sp = 'N'
last = 0

for i in range(24,-1,-1):
    cur = 0
    for j in range(14,-1,-1):
        cur = cp[j] + cur * 256
        cp[j] = cur//24
        cur = cur % 24
    out = alph[cur] + out
    last = cur

pto = out[1:last+1]
result = pto + sp + out[last+1:]
print("out: {}".format(out))
print("pto: {}".format(pto))

print("result: {}".format(result))
print('-'.join(result[i:i+5] for i in range(0,25,5)))	
po = 52
pe = 66 + 1
print(value[0][po:pe].hex())
