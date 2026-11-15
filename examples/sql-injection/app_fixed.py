"""Versão corrigida do exemplo local de SQL Injection (CWE-89)."""
from app import criar_banco


def autenticar(banco, usuario, senha):
    # O driver recebe o SQL separado dos valores; dados não viram comandos.
    consulta = "SELECT usuario FROM usuarios WHERE usuario = ? AND senha = ?"
    return banco.execute(consulta, (usuario, senha)).fetchone() is not None


if __name__ == "__main__":
    with criar_banco() as banco:
        usuario = input("Usuário de laboratório: ")
        senha = input("Senha de laboratório: ")
        print("Acesso permitido" if autenticar(banco, usuario, senha) else "Acesso negado")
