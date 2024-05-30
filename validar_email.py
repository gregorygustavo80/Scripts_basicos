import re

email = input("Qual o seu e-mail? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
