"""Exemplo propositalmente vulnerável para laboratório local, sem rede.

NÃO utilizar em aplicações reais. Dados e credenciais são fictícios.
"""
import sqlite3


def criar_banco():
    banco = sqlite3.connect(":memory:")
    banco.execute("CREATE TABLE usuarios (usuario TEXT, senha TEXT)")
    banco.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
        ("admin_lab", "SenhaFicticia123"),
    )
    return banco


def autenticar(banco, usuario, senha):
    # VULNERÁVEL (CWE-89): mistura valores fornecidos pelo usuário com SQL.
    consulta = (
        f"SELECT usuario FROM usuarios "
        f"WHERE usuario = '{usuario}' AND senha = '{senha}'"
    )
    return banco.execute(consulta).fetchone() is not None


if __name__ == "__main__":
    with criar_banco() as banco:
        usuario = input("Usuário de laboratório: ")
        senha = input("Senha de laboratório: ")
        print("Acesso permitido" if autenticar(banco, usuario, senha) else "Acesso negado")
