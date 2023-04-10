titulo= "Historias divertidas"
saludo ="Bienvenidos"
print()
for row in range(3):
    for col in range(len(titulo) + 4) :
        if (row == 0 or row == 2):
            print("+", end="")
   
    if row == 1:
          print("  " + titulo + " ")

    print()

print(f"""
        **{saludo}**
             :) 🎉

             a jugar 🏓
""")

print()
adj = input("Adjetivo: ")
verbo1 = input("primer verbo: ")
verbo2 = input("segundo verbo: ")
empresa = input("empresa: ")
sustantivo_plural = input("sustantivo plural: ")

historia = f"Programar es tan {adj} !!  Siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} con {empresa} y alcanza tus {sustantivo_plural}"
print()
print(historia)
