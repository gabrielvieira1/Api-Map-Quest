hostnames=["R1","R2","R3","S1","S2"]
print(type(hostnames))
print(len(hostnames))

switches=[]
devices=["R1","R2","R3","S1","S2"]
for item in devices:
        if "S" in item:
            switches.append(item)

print(switches)


file=open("devices.txt", "r")
for item in file:
    print(item)
file.close()

file=open("devices.txt", "r")
for item in file:
    item=item.strip()
    print(item)
file.close()

devices=[]
print("Teste novo")
file=open("devices.txt","r")
for item in file:
   item=item.strip()
   devices.append(item)
file.close()
print(devices)

