"""Validação reproduzível do comportamento vulnerável e da correção."""
import unittest

import app
import app_fixed


class TesteAutenticacao(unittest.TestCase):
    def setUp(self):
        self.banco = app.criar_banco()

    def tearDown(self):
        self.banco.close()

    def test_login_valido(self):
        for modulo in (app, app_fixed):
            self.assertTrue(modulo.autenticar(self.banco, "admin_lab", "SenhaFicticia123"))

    def test_senha_errada(self):
        for modulo in (app, app_fixed):
            self.assertFalse(modulo.autenticar(self.banco, "admin_lab", "invalida"))

    def test_injecao_de_laboratorio(self):
        # Entrada fictícia conhecida, usada apenas no SQLite em memória.
        entrada = "' OR 1=1 --"
        self.assertTrue(app.autenticar(self.banco, entrada, "invalida"))
        self.assertFalse(app_fixed.autenticar(self.banco, entrada, "invalida"))


if __name__ == "__main__":
    unittest.main()
