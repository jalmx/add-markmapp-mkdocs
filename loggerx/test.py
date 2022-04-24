import loggerx

lista = [1,25,2,5,6,5,6,5,56,6,5,65,6,64,6]

l = loggerx.LogX(__name__)

for i in lista:
    l.w(f"waarrgg {i}")
    l.e(f"errorrrrr {i}")

