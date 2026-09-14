from controllers.usuario_controller import UsuarioController

controller = UsuarioController()

casos = [
    ("Rafa03", "1"),
    ("Al", "1"),
    ("Rafa03", "2"),
    ("Bia", "3"),
]

for nome, estilo in casos:
    print(controller.criar_perfil(nome, estilo))