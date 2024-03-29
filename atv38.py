hINICIO = int(input("hora de inicio: "))
mINICIO = int(input("minuto de inicio: "))
sINICIO = int(input("segundo de inicio: "))
segundosPASSADOS = int(input("Segundos passados: "))

totalSegundos = (hINICIO*3600) + (mINICIO*60) + sINICIO + segundosPASSADOS
hfim = totalSegundos // 3600
mfim = (totalSegundos % 3600) // 60
sfim = totalSegundos % 60

print(f"{hfim}:{mfim}:{sfim}")