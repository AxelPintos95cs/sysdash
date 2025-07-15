user_email = input("Ingresá tu correo para recibir alertas: ")
email_pass = input("Ingresá la contraseña del remitente (ej: alertas@example.com): ")

template_path = "./alertmanager/config.yml"
output_path = "./alertmanager/config.yml"

with open(template_path, "r") as f:
    config = f.read()

config = config.replace("{{USER_EMAIL}}", user_email)
config = config.replace("{{EMAIL_PASSWORD}}", email_pass)

with open(output_path, "w") as f:
    f.write(config)

print("✅ Configuración de alertas actualizada con tu email.")
