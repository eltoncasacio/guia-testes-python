# Guia Completo: Testes Profissionais em Python 🧪

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pytest](https://img.shields.io/badge/tested%20with-pytest-red.svg)](https://docs.pytest.org/)
[![TDD](https://img.shields.io/badge/methodology-TDD-green.svg)](https://en.wikipedia.org/wiki/Test-driven_development)
[![Coverage](https://img.shields.io/badge/coverage-95%25+-brightgreen.svg)](https://github.com/eltoncasacio/guia-testes-python)
[![GitHub stars](https://img.shields.io/github/stars/eltoncasacio/guia-testes-python?style=social)](https://github.com/eltoncasacio/guia-testes-python/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/eltoncasacio/guia-testes-python?style=social)](https://github.com/eltoncasacio/guia-testes-python/network/members)

Aprenda do zero a criar testes profissionais com pytest, mocking e fixtures.

## 🎯 Para quem é este guia?

- ✅ Desenvolvedores Python iniciantes/intermediários
- ✅ Quem quer aprender testes do jeito certo
- ✅ Equipes que querem padronizar testes
- ✅ Quem busca 95%+ de cobertura de código

## 📚 O que você vai aprender?

- **Fundamentos sólidos:** Tipos de testes, pirâmide, AAA pattern
- **Mocking completo:** Mock, Stub, Spy, Fake
- **Fixtures pytest:** Escopos, parametrização, conftest.py
- **Cobertura de código:** Medir, interpretar, atingir 95%+
- **Código production-ready:** Padrões profissionais

## 📖 Conteúdo

| Arquivo | Páginas | Tempo | Descrição |
|---------|---------|-------|-----------|
| [00-COMECE-AQUI.md](guia/00-COMECE-AQUI.md) | 3 | 5min | Início rápido |
| [01-guia-completo.md](guia/01-guia-completo.md) | ~80 | 14-19h | Curso completo |
| [02-indice.md](guia/02-indice.md) | 5 | 10min | Navegação |
| [03-cheatsheet.md](guia/03-cheatsheet.md) | 10 | - | Referência rápida |
| [04-resumo.md](guia/04-resumo.md) | 8 | 15min | Visão geral |
| [05-instrucoes.md](guia/05-instrucoes.md) | 8 | 10min | Como usar |

## 🚀 Quick Start

```bash
# 1. Clonar repositório
git clone https://github.com/seu-usuario/guia-testes-python.git
cd guia-testes-python

# 2. Ler instruções
cat guia/00-COMECE-AQUI.md

# 3. Começar pelo guia principal
cat guia/01-guia-completo.md
```

## 📊 Estrutura do Curso

### Parte 1: Fundamentos (3-4 horas)
- Cap 1: Introdução
- Cap 2: Fundamentos de Testes
- Cap 3: Mocking - Conceito Central
- Cap 4: Fixtures Pytest

### Parte 2: Setup (30 min)
- Cap 5: Setup do Projeto

### Parte 3: Prática (8-12 horas)
- Cap 6: Refatoração
- Cap 7: Criar Fixtures
- Cap 8: Escrever Testes

### Parte 4: Qualidade (1-2 horas)
- Cap 9: Medir Cobertura
- Cap 10: Validação

## 💡 Metodologia: TDD (Test-Driven Development)

**Este guia ensina TDD de verdade!**

Você NÃO vai encontrar código pronto. Em vez disso, você vai:

1. **Ler o teste** (fornecido no guia)
2. **Implementar o código** para passar no teste
3. **Validar** que funciona
4. **Refatorar** se necessário

**Exemplo de fluxo:**
```bash
# 1. Criar estrutura de diretórios
mkdir -p seu-projeto/src/core
mkdir -p seu-projeto/tests/unit/core

# 2. Copiar teste do guia
# (Capítulo 8 fornece test_env.py completo)

# 3. Rodar teste (vai falhar - normal!)
pytest tests/unit/core/test_env.py

# 4. Implementar código em src/core/env.py
# (Seguindo orientações do Capítulo 6)

# 5. Rodar teste novamente (deve passar!)
pytest tests/unit/core/test_env.py -v
```

**Por que esta abordagem é melhor:**
- ✅ Aprende TDD praticando (não só lendo)
- ✅ Entende cada linha de código (você escreveu!)
- ✅ Memoriza melhor (aprendizado ativo)
- ✅ Desenvolve muscle memory
- ✅ Não copia/cola sem entender

## 🛠️ Validação

Use o script de validação para verificar sua implementação:

```bash
python ferramentas/validar_implementacao.py
```

## 🎓 Resultado Final

Ao completar o guia implementando tudo você mesmo, você terá:

- ✅ Compreensão profunda de testes (teoria + prática)
- ✅ Código testável que VOCÊ escreveu
- ✅ Cobertura 95%+ (validada com pytest-cov)
- ✅ Experiência real com TDD
- ✅ 3 módulos funcionais + 12+ testes
- ✅ Portfolio para mostrar em entrevistas
- ✅ Habilidades production-ready

## 📚 Recursos Adicionais

- [Pytest Docs](https://docs.pytest.org/)
- [Real Python - Testing](https://realpython.com/python-testing/)
- [Python Testing with pytest](https://pragprog.com/titles/bopytest/)

## 📝 Licença

MIT - Use livremente em seus projetos!

## 🤝 Contribuições

Contribuições são bem-vindas! Melhorias, correções e novos exemplos.

## ⭐ Apoie o Projeto

Se este guia te ajudou, deixe uma ⭐ no repositório!
