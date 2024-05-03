from faker import Faker
import random
import string

fake = Faker()


def generate_username(name):
    # Generar un username aleatorio basado en el nombre
    username = ''.join(char for char in name.lower().replace(" ", "") if char.isalnum())
    if username.isalpha():  # Si el username es solo letras, agregamos números
        username += str(random.randint(1, 100))
    return username


def generate_email(username):
    # Generar un correo electrónico aleatorio basado en el username
    email = username + "@example.com"
    return email


def generate_password():
    # Generar una contraseña aleatoria de longitud 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password


def generate_user_data(num_users):
    users_data = []
    for _ in range(num_users):
        name = fake.name()
        username = generate_username(name)
        email = generate_email(username)
        password = generate_password()
        users_data.append({"name": name, "username": username, "email": email, "password": password})
    return users_data


if __name__ == "__main__":
    num_users = int(input("Ingrese el número de usuarios a generar: "))
    users_data = generate_user_data(num_users)
    for user in users_data:
        print("Nombre:", user["name"])
        print("Username:", user["username"])
        print("Correo electrónico:", user["email"])
        print("Contraseña:", user["password"])
        print("-----------------------------")
