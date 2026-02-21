"""
Crea tres variables:

age = 20
has_id = True
registered = False

Crea una expresión que sea True solo si:

Es mayor o igual a 18

Tiene ID

Está registrado
"""

age = 20
has_id = True
registered = False

if age >= 18 and has_id and registered:
    allowed = True
else:
    allowed = False

print("Allowed:", allowed, "\n")


#opcion two; allowed = age >= 18 and has_id and registered

"""
Usa not para verificar que un usuario NO esté en una lista de bloqueados.
"""

user = "Mandalorian"
users_disallowed = ["Grogu", "Asoka", "Luke", "Mandalorian", "Yoda"]
print(user not in users_disallowed)