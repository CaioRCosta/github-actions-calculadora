# Calculadora — GitHub Actions

Pequeno programa em Python (`calculadora.py`) com 8 testes de unidade (`test_calculadora.py`), executados automaticamente pelo GitHub Actions a cada commit.

O workflow (`.github/workflows/ci.yml`) roda em uma matriz de:

- **Sistemas operacionais:** Ubuntu, macOS e Windows
- **Versões do Python:** 3.11, 3.12 e 3.13

Total: 9 jobs por commit.

## Rodar localmente

```bash
pip install -r requirements.txt
python -m pytest -v
```
