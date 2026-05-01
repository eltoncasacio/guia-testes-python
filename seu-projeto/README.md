# Diretório do Seu Projeto

Este diretório é onde você vai implementar seu código seguindo o guia de testes.

## 📁 Estrutura que você vai criar:

```
seu-projeto/
├── .env                        # Variáveis de ambiente (criar baseado no guia)
├── pyproject.toml              # Configuração do projeto (template no guia)
├── requirements-dev.txt        # Dependências de desenvolvimento (template no guia)
│
├── src/                        # Seu código de produção
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── env.py              # Você implementa este módulo
│   │   └── clients.py          # Você implementa este módulo
│   └── utils/
│       ├── __init__.py
│       └── error_handling.py   # Você implementa este módulo
│
└── tests/                      # Seus testes
    ├── conftest.py             # Fixtures compartilhadas (template no guia)
    ├── unit/
    │   ├── __init__.py
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── test_env.py          # Exemplos completos no guia
    │   │   └── test_clients.py      # Exemplos completos no guia
    │   └── utils/
    │       ├── __init__.py
    │       └── test_error_handling.py  # Exemplos completos no guia
    └── integration/
        ├── __init__.py
        └── test_basic_flow.py       # Exemplo completo no guia
```

## 🚀 Como começar:

1. **Leia o guia principal**: `guia/01-guia-completo.md`
2. **Siga os capítulos em ordem**: O guia te orienta passo a passo
3. **Implemente você mesmo**: Não copie código pronto - aprenda fazendo!
4. **Use TDD**: Escreva os testes primeiro (fornecidos no guia), depois implemente o código

## 💡 Templates disponíveis no guia:

O guia fornece templates e exemplos completos para:
- ✅ Arquivos de configuração (pyproject.toml, .env, requirements-dev.txt)
- ✅ Testes completos (todos os arquivos test_*.py)
- ✅ Fixtures (conftest.py)
- ✅ Orientações para implementação do código

## ⚠️ Importante:

**Este diretório está vazio propositalmente!**

Você vai criar toda a estrutura seguindo o guia. Isso garante que você:
- Entenda cada decisão arquitetural
- Pratique TDD de verdade
- Aprenda fazendo (não copiando)
- Desenvolva muscle memory

Bons estudos! 🎓
