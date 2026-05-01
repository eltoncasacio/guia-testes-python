# Guia Completo: Testes Profissionais em Python para Langfuse

**Versão:** 1.0
**Data:** Abril 2026
**Autor:** Claude Code + Elton Casaccia
**Objetivo:** Aprender a criar testes profissionais do zero
**Páginas:** ~80-100 (quando convertido para PDF)
**Tempo estimado:** 14-19 horas de implementação

---

## 📑 Índice

### Parte 1: Fundamentos Teóricos (3-4 horas)
- [Capítulo 1: Introdução](#-capítulo-1-introdução)
- [Capítulo 2: Fundamentos de Testes](#-capítulo-2-fundamentos-de-testes)
- [Capítulo 3: Mocking - Conceito Central](#-capítulo-3-mocking---conceito-central)
- [Capítulo 4: Fixtures Pytest](#-capítulo-4-fixtures-pytest)

### Parte 2: Setup e Configuração (30 min)
- [Capítulo 5: Setup do Projeto](#-capítulo-5-setup-do-projeto)

### Parte 3: Implementação Prática (8-12 horas)
- [Capítulo 6: Refatoração](#-capítulo-6-refatoração)
- [Capítulo 7: Criar Fixtures](#-capítulo-7-criar-fixtures)
- [Capítulo 8: Escrever Testes](#-capítulo-8-escrever-testes)

### Parte 4: Validação e Qualidade (1-2 horas)
- [Capítulo 9: Medir Cobertura](#-capítulo-9-medir-cobertura)
- [Capítulo 10: Validação e Próximos Passos](#-capítulo-10-validação-e-próximos-passos)

### Apêndices
- [Apêndice A: Referência Rápida](#apêndice-a-referência-rápida)

---

## 📘 Capítulo 1: Introdução

### 1.1 Sobre este guia

Este é um guia **educacional hands-on** para você aprender a criar testes profissionais em Python. Não vamos apenas implementar testes — vamos entender **por que**, **como** e **quando** testar.

**O que torna este guia diferente:**

- ✅ **Educacional primeiro**: Cada conceito é explicado em detalhes
- ✅ **Código completo**: Todos os exemplos são funcionais e comentados
- ✅ **Aprenda fazendo**: Você implementa cada parte
- ✅ **Referência permanente**: Serve como curso e documentação

**Este NÃO é um guia de:**
- ❌ Copy-paste sem entender
- ❌ Testes superficiais só para cobertura
- ❌ Teoria sem prática

### 1.2 O que você vai aprender

Ao completar este guia, você saberá:

1. **Fundamentos de testes**
   - Tipos de testes (unitário, integração, E2E)
   - Pirâmide de testes
   - AAA Pattern (Arrange, Act, Assert)
   - Quando usar cada tipo

2. **Mocking - Conceito central**
   - O que são mocks e por que usar
   - Como mockar APIs externas (OpenAI, Langfuse)
   - Diferença entre Mock, Stub, Spy, Fake
   - Testes determinísticos e rápidos

3. **Fixtures Pytest**
   - O que são fixtures e para que servem
   - Escopos (function, class, module, session)
   - Fixtures parametrizadas
   - conftest.py e compartilhamento

4. **Refatoração para testabilidade**
   - Separação de responsabilidades
   - Factory pattern
   - Dependency injection
   - Código limpo e testável

5. **Testes na prática**
   - Escrever testes unitários
   - Escrever testes de integração
   - Medir cobertura de código
   - Atingir 95%+ de cobertura

6. **Boas práticas**
   - Testes independentes
   - Testes rápidos
   - Testes legíveis
   - Evitar armadilhas comuns

### 1.3 Pré-requisitos

**Conhecimento técnico:**
- Python intermediário (funções, classes, imports)
- Noções de terminal/bash
- Git básico (opcional, mas recomendado)

**Software necessário:**
- Python 3.10+ instalado
- pip funcionando
- Editor de código (VSCode, PyCharm, etc.)
- Terminal

**Tempo disponível:**
- 14-19 horas distribuídas em vários dias
- Não precisa fazer tudo de uma vez!

### 1.4 Estrutura final do projeto

Ao terminar este guia, seu projeto terá esta estrutura:

```
langfuse/
├── .env                    # Variáveis de ambiente (não commitado)
├── .gitignore             # Arquivos ignorados pelo Git
├── pyproject.toml         # Configuração do projeto
├── README.md              # Documentação do projeto
│
├── src/                   # Código fonte (production)
│   ├── __init__.py
│   │
│   ├── core/              # Módulos principais
│   │   ├── __init__.py
│   │   ├── env.py         # Gerenciamento de variáveis de ambiente
│   │   └── clients.py     # Factories de clientes (OpenAI, Langfuse)
│   │
│   ├── utils/             # Utilitários
│   │   ├── __init__.py
│   │   └── error_handling.py  # Tratamento de erros
│   │
│   └── examples/          # Scripts de exemplo (migrados)
│       ├── __init__.py
│       ├── basico.py
│       ├── prompt_management.py
│       └── llm_as_judge.py
│
└── tests/                 # Testes
    ├── __init__.py
    ├── conftest.py        # Fixtures compartilhadas
    │
    ├── unit/              # Testes unitários
    │   ├── __init__.py
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── test_env.py
    │   │   └── test_clients.py
    │   └── utils/
    │       ├── __init__.py
    │       └── test_error_handling.py
    │
    └── integration/       # Testes de integração
        ├── __init__.py
        └── test_examples_basic.py
```

**Métricas de qualidade esperadas:**
- ✅ Cobertura de testes: **95%+**
- ✅ Tempo de execução: **< 5 segundos**
- ✅ Testes independentes: **100%**
- ✅ Zero warnings no pytest

### 1.5 Tempo estimado de implementação

| Fase | Atividade | Tempo estimado |
|------|-----------|----------------|
| **Fase 1** | Leitura Capítulos 1-4 (conceitos) | 3-4 horas |
| **Fase 2** | Setup inicial (Capítulo 5) | 30 minutos |
| **Fase 3** | Refatoração (Capítulo 6) | 2-3 horas |
| **Fase 4** | Criar fixtures (Capítulo 7) | 1-2 horas |
| **Fase 5** | Escrever testes (Capítulo 8) | 6-8 horas |
| **Fase 6** | Validação e cobertura (Cap. 9-10) | 1 hora |
| **TOTAL** | | **14-19 horas** |

**Recomendação:**
- Dia 1: Fases 1-2 (conceitos + setup)
- Dia 2: Fase 3 (refatoração)
- Dia 3-4: Fases 4-5 (fixtures + testes)
- Dia 5: Fase 6 (validação)

---

## 📘 Capítulo 2: Fundamentos de Testes

### 2.1 O que são testes e por que testar?

**Definição:**
Testes são código que verifica se o código de produção funciona corretamente.

**Analogia:**
Imagine que você construiu um carro. Antes de vender, você:
- Testa os freios (teste unitário do sistema de freios)
- Testa o motor (teste unitário do motor)
- Testa dirigir pela cidade (teste de integração)
- Testa em uma viagem longa (teste E2E - end-to-end)

**Por que testar?**

1. **Confiança**: Saber que mudanças não quebraram nada
2. **Documentação**: Testes mostram como usar o código
3. **Design melhor**: Código testável é código bem estruturado
4. **Menos bugs**: Pega erros antes de produção
5. **Refatoração segura**: Mude código sem medo
6. **Economia**: Bug em produção custa 100x mais que em desenvolvimento

**Exemplo do mundo real:**

```python
# Código sem testes
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

# Você deploya em produção...
# Cliente reclama: desconto de 150% deu preço negativo!
# Você percebe que não validou percentual...
```

```python
# Com testes, você pegaria isso antes:
def test_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_desconto(100, 150)  # ❌ Falha! Função não valida.

# Você corrige antes de deployar:
def calcular_desconto(preco, percentual):
    if not 0 <= percentual <= 100:
        raise ValueError("Percentual deve estar entre 0 e 100")
    return preco - (preco * percentual / 100)
```

### 2.2 Tipos de testes: Unitário vs Integração vs E2E

#### Teste Unitário

**Definição:** Testa uma unidade isolada (função, classe, método).

**Características:**
- ✅ Muito rápido (milissegundos)
- ✅ Testa apenas uma coisa
- ✅ Usa mocks para dependências externas
- ✅ Determinístico (sempre mesmo resultado)

**Exemplo:**
```python
# Função a testar
def somar(a, b):
    return a + b

# Teste unitário
def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0
```

#### Teste de Integração

**Definição:** Testa interação entre múltiplos componentes.

**Características:**
- ⏱️ Mais lento que unitário (segundos)
- 🔗 Testa integração entre partes
- 🌐 Pode usar dependências reais (banco, API)
- 🎯 Foca em fluxos completos

**Exemplo:**
```python
# Teste de integração
def test_salvar_e_buscar_usuario(db):
    # Usa banco real (ou em memória)
    usuario = criar_usuario("João", "joao@email.com")
    salvar_usuario(db, usuario)

    resultado = buscar_usuario_por_email(db, "joao@email.com")
    assert resultado.nome == "João"
```

#### Teste E2E (End-to-End)

**Definição:** Testa sistema completo do ponto de vista do usuário.

**Características:**
- 🐌 Lento (minutos)
- 🌍 Usa sistema real (frontend + backend + banco)
- 💰 Caro de manter
- 🎭 Simula usuário real

**Exemplo:**
```python
# Teste E2E (com Selenium, Playwright, etc.)
def test_fluxo_compra_completo(browser):
    browser.abrir("https://loja.com")
    browser.clicar_produto("Notebook")
    browser.adicionar_carrinho()
    browser.finalizar_compra()
    browser.preencher_pagamento("4111111111111111")
    browser.confirmar()

    assert browser.ver_texto("Compra realizada com sucesso!")
```

#### Comparação

| Aspecto | Unitário | Integração | E2E |
|---------|----------|------------|-----|
| **Velocidade** | ⚡ Muito rápido | ⏱️ Moderado | 🐌 Lento |
| **Escopo** | Função/método | Múltiplos módulos | Sistema completo |
| **Isolamento** | Total (mocks) | Parcial | Nenhum (sistema real) |
| **Custo manutenção** | 💚 Baixo | 💛 Médio | 💔 Alto |
| **Quantidade** | 📈 Muitos (70-80%) | 📊 Moderados (15-20%) | 📉 Poucos (5-10%) |

### 2.3 Pirâmide de testes

A "Pirâmide de Testes" é um conceito que mostra a proporção ideal de cada tipo:

```
        /\
       /  \      ← E2E (5-10%)
      /----\     Poucos, mas críticos
     /      \
    /--------\   ← Integração (15-20%)
   / Unitário \  Fluxos importantes
  /------------\
 /______________\ ← Unitário (70-80%)
                  Muitos, rápidos, granulares
```

**Por que pirâmide?**

1. **Base larga (unitários):**
   - Rápidos: suite completa roda em segundos
   - Baratos: fácil escrever e manter
   - Precisos: apontam exato onde falhou

2. **Meio (integração):**
   - Testam que partes funcionam juntas
   - Não testam todas combinações (impossível)
   - Focam em fluxos críticos

3. **Topo (E2E):**
   - Apenas para happy paths principais
   - Muito lentos e frágeis
   - Úteis como smoke tests

**Anti-pattern: Pirâmide invertida** ⚠️

```
  ______________   ← Muitos E2E (ruim!)
 \            /    Lento, frágil, caro
  \          /
   \--------/      ← Alguns integração
    \      /
     \----/        ← Poucos unitários
      \  /
       \/
```

Projetos com pirâmide invertida sofrem de:
- ❌ Testes levam 30+ minutos
- ❌ Quebram por motivos aleatórios (flakiness)
- ❌ Ninguém quer escrever testes novos
- ❌ CI/CD sempre vermelho

### 2.4 AAA Pattern (Arrange, Act, Assert)

AAA é um padrão para estruturar testes de forma clara e legível.

**Estrutura:**

1. **Arrange (Preparar):** Configure o cenário
2. **Act (Agir):** Execute a ação a testar
3. **Assert (Verificar):** Verifique o resultado

**Exemplo sem AAA (confuso):**

```python
def test_calcular_total():
    assert calcular_total([10, 20, 30]) == 60
```

**Exemplo com AAA (claro):**

```python
def test_calcular_total():
    # ===== ARRANGE =====
    itens = [10, 20, 30]
    total_esperado = 60

    # ===== ACT =====
    resultado = calcular_total(itens)

    # ===== ASSERT =====
    assert resultado == total_esperado
```

**Por que AAA ajuda:**
- ✅ Separa responsabilidades
- ✅ Fácil identificar o que está sendo testado
- ✅ Facilita debug quando teste falha
- ✅ Documentação clara

**Exemplo mais complexo:**

```python
def test_criar_usuario_com_email_valido():
    # ===== ARRANGE =====
    # Preparar dados de entrada
    nome = "Maria Silva"
    email = "maria@exemplo.com"
    senha = "senha123"

    # Preparar mocks/dependências
    mock_db = MockDatabase()

    # ===== ACT =====
    # Executar a função que queremos testar
    usuario = criar_usuario(
        nome=nome,
        email=email,
        senha=senha,
        db=mock_db
    )

    # ===== ASSERT =====
    # Verificar múltiplos aspectos
    assert usuario.nome == nome
    assert usuario.email == email
    assert usuario.senha_hash != senha  # Foi hasheada
    assert usuario.id is not None  # Foi salvo
    assert mock_db.salvar_foi_chamado()  # DB foi usado
```

### 2.5 Exemplo prático: teste de função simples

Vamos criar um teste completo do zero para consolidar os conceitos.

**Função a testar:**

```python
# src/utils/texto.py
def formatar_nome_completo(primeiro_nome: str, sobrenome: str) -> str:
    """
    Formata nome completo com primeira letra maiúscula.

    Exemplos:
        >>> formatar_nome_completo("joão", "silva")
        "João Silva"

        >>> formatar_nome_completo("MARIA", "santos")
        "Maria Santos"
    """
    primeiro = primeiro_nome.strip().capitalize()
    sobre = sobrenome.strip().capitalize()
    return f"{primeiro} {sobre}"
```

**Teste completo (AAA Pattern):**

```python
# tests/unit/utils/test_texto.py
import pytest
from src.utils.texto import formatar_nome_completo


def test_formatar_nome_completo_basico():
    """Testa formatação básica de nome"""
    # ===== ARRANGE =====
    primeiro = "joão"
    sobrenome = "silva"
    esperado = "João Silva"

    # ===== ACT =====
    resultado = formatar_nome_completo(primeiro, sobrenome)

    # ===== ASSERT =====
    assert resultado == esperado


def test_formatar_nome_completo_tudo_maiusculo():
    """Testa que converte MAIÚSCULAS para Capitalize"""
    # ===== ARRANGE =====
    primeiro = "MARIA"
    sobrenome = "SANTOS"
    esperado = "Maria Santos"

    # ===== ACT =====
    resultado = formatar_nome_completo(primeiro, sobrenome)

    # ===== ASSERT =====
    assert resultado == esperado


def test_formatar_nome_completo_com_espacos():
    """Testa que remove espaços extras"""
    # ===== ARRANGE =====
    primeiro = "  pedro  "
    sobrenome = "  costa  "
    esperado = "Pedro Costa"

    # ===== ACT =====
    resultado = formatar_nome_completo(primeiro, sobrenome)

    # ===== ASSERT =====
    assert resultado == esperado


def test_formatar_nome_completo_casos_mistos():
    """Testa múltiplos casos com parametrização"""
    # Arrange: lista de casos (input, expected)
    casos = [
        ("ana", "paula", "Ana Paula"),
        ("CARLOS", "eduardo", "Carlos Eduardo"),
        ("  lucia  ", "  FERREIRA  ", "Lucia Ferreira"),
        ("x", "y", "X Y"),  # Edge case: nomes de 1 letra
    ]

    for primeiro, sobrenome, esperado in casos:
        # Act
        resultado = formatar_nome_completo(primeiro, sobrenome)

        # Assert
        assert resultado == esperado, \
            f"Falhou para ({primeiro}, {sobrenome})"
```

**Executando os testes:**

```bash
# Rodar todos os testes do arquivo
pytest tests/unit/utils/test_texto.py -v

# Saída esperada:
# tests/unit/utils/test_texto.py::test_formatar_nome_completo_basico PASSED
# tests/unit/utils/test_texto.py::test_formatar_nome_completo_tudo_maiusculo PASSED
# tests/unit/utils/test_texto.py::test_formatar_nome_completo_com_espacos PASSED
# tests/unit/utils/test_texto.py::test_formatar_nome_completo_casos_mistos PASSED
#
# ==================== 4 passed in 0.02s ====================
```

**Lições do exemplo:**

1. **Um teste, um cenário**: Cada função testa um caso específico
2. **Nome descritivo**: `test_formatar_nome_completo_tudo_maiusculo` é claro
3. **AAA explícito**: Comentários marcam cada seção
4. **Múltiplos testes**: Não tentamos testar tudo em um teste só
5. **Rápido**: 4 testes em 0.02 segundos

**Próximo passo:**

Agora que entendemos os fundamentos, vamos aprender sobre **Mocking** — o conceito mais importante para testar código com dependências externas (APIs, bancos de dados, etc.).

---

## 📘 Capítulo 3: Mocking - Conceito Central

### 3.1 O problema: testar código com dependências externas

Imagine que você tem este código:

```python
# src/services/chatbot.py
import openai

def gerar_resposta(pergunta: str) -> str:
    """Gera resposta usando GPT-4"""
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": pergunta}]
    )

    return response.choices[0].message.content
```

**Como testar isso?**

❌ **Opção 1: Chamar API real**
```python
def test_gerar_resposta():
    resultado = gerar_resposta("Qual a capital do Brasil?")
    assert "Brasília" in resultado
```

**Problemas:**
- 💰 **Custo**: Cada teste custa dinheiro (tokens)
- 🐌 **Lento**: Cada teste leva 1-5 segundos
- 🌐 **Requer internet**: Não funciona offline
- 🎲 **Não determinístico**: GPT pode responder diferente
- 🔑 **Requer credenciais**: Precisa API key configurada
- 🚫 **Pode falhar**: Se API estiver fora, teste quebra

Se você tem 100 testes assim:
- ⏱️ Tempo total: **5-10 minutos**
- 💸 Custo: **$5-10 por rodada**
- 😫 Ninguém vai rodar os testes frequentemente

✅ **Opção 2: Usar MOCK**
```python
def test_gerar_resposta(mock_openai):
    # mock_openai retorna resposta fake instantaneamente
    resultado = gerar_resposta("Qual a capital do Brasil?")
    assert resultado == "Resposta mockada do GPT"
```

**Vantagens:**
- ⚡ **Rápido**: Milissegundos
- 💚 **Grátis**: Zero custo
- 🔌 **Offline**: Funciona sem internet
- 🎯 **Determinístico**: Sempre mesma resposta
- 🔓 **Sem credenciais**: Não precisa API key
- 💪 **Confiável**: Nunca falha por problema externo

### 3.2 O que é um Mock? O que é um Stub?

**Test Doubles** são objetos falsos usados em testes. Existem vários tipos:

#### Mock

**Definição:** Objeto falso que **verifica se foi usado corretamente**.

**Exemplo:**
```python
def test_salvar_usuario_chama_db(mock_db):
    salvar_usuario("João", mock_db)

    # Mock verifica que foi chamado com argumentos corretos
    mock_db.insert.assert_called_once_with("João")
```

#### Stub

**Definição:** Objeto falso que **retorna valores predefinidos**.

**Exemplo:**
```python
def test_buscar_preco_produto(stub_api):
    # Stub configurado para retornar 99.90
    stub_api.get_preco.return_value = 99.90

    preco = buscar_preco("produto-123", stub_api)
    assert preco == 99.90
```

#### Spy

**Definição:** Objeto **real que é observado** (grava chamadas).

**Exemplo:**
```python
def test_enviar_email(spy_mailer):
    enviar_notificacao("user@exemplo.com", spy_mailer)

    # Spy grava que send_email foi chamado
    assert spy_mailer.send_email.call_count == 1
    assert spy_mailer.send_email.called_with("user@exemplo.com")
```

#### Fake

**Definição:** Implementação **funcional simplificada**.

**Exemplo:**
```python
class FakeDatabase:
    """Banco em memória para testes"""
    def __init__(self):
        self.data = {}

    def insert(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

def test_crud_operations():
    db = FakeDatabase()  # Banco fake em memória
    db.insert("user:1", {"nome": "João"})
    assert db.get("user:1")["nome"] == "João"
```

#### Resumo comparativo

| Tipo | O que faz | Quando usar |
|------|-----------|-------------|
| **Mock** | Verifica comportamento | Quando você quer garantir que algo foi chamado |
| **Stub** | Retorna dados fake | Quando você precisa de resposta controlada |
| **Spy** | Observa objeto real | Quando quer usar real + verificar chamadas |
| **Fake** | Implementação simplificada | Quando mock é muito complexo (ex: banco em memória) |

**Na prática:** Python usa principalmente **Mock** (que faz papel de Mock + Stub).

### 3.3 Por que mockar OpenAI e Langfuse?

No nosso projeto Langfuse, temos duas APIs externas principais:

#### 1. OpenAI API

**O que faz:**
- Gera texto com GPT
- Processa embeddings
- Transcreve áudio
- etc.

**Por que mockar:**
- 💰 **Custo alto**: GPT-4 custa $0.03 por 1K tokens
- 🐌 **Lento**: 1-5 segundos por chamada
- 🎲 **Não determinístico**: Mesma pergunta, resposta diferente
- 🌐 **Depende de internet**

**Como mockar:**
```python
# Em vez de chamar OpenAI real
mock_openai.chat.completions.create.return_value = MockResponse(
    choices=[MockChoice(message=MockMessage(content="Resposta fake"))]
)
```

#### 2. Langfuse API

**O que faz:**
- Rastreia traces de LLM
- Armazena prompts
- Calcula métricas
- Gera dashboards

**Por que mockar:**
- 🌐 **Requer instância rodando**: Precisa Langfuse server ativo
- 🐌 **Latência de rede**: Cada trace leva tempo
- 💾 **Polui dados**: Testes criam dados fake no dashboard
- 🔧 **Complexo configurar**: Precisa setup de infra

**Como mockar:**
```python
mock_langfuse.get_current_trace_id.return_value = "trace-fake-12345"
mock_langfuse.flush.return_value = None  # Não envia nada
```

### 3.4 Benefícios: velocidade, custo, determinismo

#### Velocidade

**Sem mocks:**
```
Teste 1: OpenAI call........... 2.3s ⏱️
Teste 2: OpenAI call........... 1.8s ⏱️
Teste 3: OpenAI call........... 3.1s ⏱️
Teste 4: OpenAI call........... 2.5s ⏱️
Teste 5: OpenAI call........... 2.0s ⏱️
────────────────────────────────────
Total: 11.7s 😫
```

**Com mocks:**
```
Teste 1: Mock.............. 0.001s ⚡
Teste 2: Mock.............. 0.001s ⚡
Teste 3: Mock.............. 0.001s ⚡
Teste 4: Mock.............. 0.001s ⚡
Teste 5: Mock.............. 0.001s ⚡
────────────────────────────────────
Total: 0.005s 🚀
```

**Diferença: 2.340x mais rápido!**

#### Custo

**Sem mocks (100 testes/dia por desenvolvedor):**
```
Cenário: 3 desenvolvedores, 20 dias úteis/mês

100 testes × $0.001/teste × 3 devs × 20 dias = $60/mês
```

**Com mocks:**
```
$0/mês 💚
```

#### Determinismo

**Sem mocks (GPT real):**
```python
# Teste 1 (segunda-feira 9h)
resultado = gerar_resposta("Resuma: IA revoluciona educação")
assert "inteligência artificial" in resultado.lower()  # ✅ PASSOU

# Teste 2 (terça-feira 10h) - MESMO código, MESMO teste
resultado = gerar_resposta("Resuma: IA revoluciona educação")
assert "inteligência artificial" in resultado.lower()  # ❌ FALHOU!
# GPT respondeu: "Tecnologia transforma ensino com machine learning"
```

**Com mocks:**
```python
# Sempre retorna a mesma resposta
mock_response.choices[0].message.content = "IA transforma educação"

resultado = gerar_resposta("qualquer coisa")
assert resultado == "IA transforma educação"  # ✅ SEMPRE PASSA
```

### 3.5 Quando mockar vs quando usar dados reais

#### ✅ Use MOCKS para:

1. **Testes unitários**
   - Testar lógica isolada
   - Foco em um componente

2. **APIs externas pagas**
   - OpenAI, Anthropic, etc.
   - Qualquer serviço que cobra por uso

3. **Serviços lentos**
   - Chamadas de rede
   - Processamento pesado

4. **Serviços instáveis**
   - APIs que caem frequentemente
   - Serviços em manutenção

5. **Situações difíceis de reproduzir**
   - Erros de rede
   - Rate limits
   - Timeouts

#### ❌ Use DADOS REAIS para:

1. **Testes de integração (alguns)**
   - Testar que integração funciona de verdade
   - Mas rode menos frequentemente (nightly builds)

2. **Testes E2E críticos**
   - Fluxos de pagamento
   - Autenticação
   - Funcionalidades core

3. **Smoke tests em staging**
   - Antes de deploy em produção
   - Validação final

#### Estratégia híbrida (recomendada)

```
Testes unitários (95%)     → 100% mocks
Testes integração (4%)     → 50% mocks, 50% reais
Testes E2E (1%)            → 0% mocks (tudo real)
```

**Exemplo prático:**
```python
# Unitário: mocka OpenAI
def test_formatar_prompt_para_gpt(mock_openai):
    prompt = formatar_prompt("teste")
    assert "### Instruções" in prompt

# Integração: usa OpenAI real 1x/dia
@pytest.mark.integration
@pytest.mark.slow
def test_pipeline_completo_openai_real():
    """Roda apenas em CI/CD, não localmente"""
    resultado = pipeline_completo("pergunta real")
    assert len(resultado) > 0
```

### 3.6 Exemplo prático: mock de OpenAI passo a passo

Vamos criar um mock completo de OpenAI do zero.

#### Passo 1: Entender a estrutura da resposta real

```python
# Resposta real do OpenAI
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Olá"}]
)

# Estrutura da resposta:
print(response.choices[0].message.content)  # "Olá! Como posso ajudar?"
print(response.model)                        # "gpt-4"
print(response.usage.total_tokens)           # 15
```

#### Passo 2: Criar mock que simula essa estrutura

```python
from unittest.mock import Mock

def criar_mock_openai_response(texto: str = "Resposta mockada"):
    """Factory para criar resposta mockada"""

    # Cria mock da mensagem
    mock_message = Mock()
    mock_message.content = texto

    # Cria mock do choice
    mock_choice = Mock()
    mock_choice.message = mock_message

    # Cria mock do usage
    mock_usage = Mock()
    mock_usage.prompt_tokens = 10
    mock_usage.completion_tokens = 20
    mock_usage.total_tokens = 30

    # Cria mock da resposta completa
    mock_response = Mock()
    mock_response.choices = [mock_choice]
    mock_response.model = "gpt-4o-mini"
    mock_response.usage = mock_usage

    return mock_response
```

#### Passo 3: Criar fixture pytest

```python
# tests/conftest.py
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_openai_client(mocker):
    """Mock do cliente OpenAI"""

    # Cria resposta fake
    mock_response = criar_mock_openai_response("Texto mockado")

    # Cria cliente fake
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = mock_response

    # Substitui importação real pelo mock
    mocker.patch('openai.OpenAI', return_value=mock_client)

    return mock_client
```

#### Passo 4: Usar no teste

```python
def test_gerar_resposta_openai(mock_openai_client):
    # ===== ARRANGE =====
    pergunta = "Qual a capital do Brasil?"

    # ===== ACT =====
    from src.services.chatbot import gerar_resposta
    resultado = gerar_resposta(pergunta)

    # ===== ASSERT =====
    # Verifica retorno
    assert resultado == "Texto mockado"

    # Verifica que OpenAI foi chamado corretamente
    mock_openai_client.chat.completions.create.assert_called_once()

    # Verifica argumentos da chamada
    call_args = mock_openai_client.chat.completions.create.call_args
    assert call_args.kwargs['model'] == "gpt-4"
    assert call_args.kwargs['messages'][0]['content'] == pergunta
```

### 3.7 Bibliotecas: unittest.mock vs pytest-mock

Python tem duas opções principais para mocking:

#### unittest.mock (built-in)

**Vantagens:**
- ✅ Já vem com Python (stdlib)
- ✅ Não precisa instalar nada
- ✅ Bem documentado

**Desvantagens:**
- ❌ Sintaxe verbosa
- ❌ Precisa fazer cleanup manual
- ❌ Difícil usar com pytest fixtures

**Exemplo:**
```python
from unittest.mock import Mock, patch

def test_com_unittest_mock():
    with patch('openai.OpenAI') as mock_openai:
        mock_openai.return_value.chat.completions.create.return_value = Mock(
            choices=[Mock(message=Mock(content="teste"))]
        )

        resultado = gerar_resposta("oi")
        assert resultado == "teste"
```

#### pytest-mock (recomendado)

**Vantagens:**
- ✅ Integração perfeita com pytest
- ✅ Sintaxe mais limpa
- ✅ Cleanup automático
- ✅ Funciona com fixtures

**Desvantagens:**
- ❌ Precisa instalar: `pip install pytest-mock`

**Exemplo:**
```python
def test_com_pytest_mock(mocker):
    mock_openai = mocker.patch('openai.OpenAI')
    mock_openai.return_value.chat.completions.create.return_value = Mock(
        choices=[Mock(message=Mock(content="teste"))]
    )

    resultado = gerar_resposta("oi")
    assert resultado == "teste"
```

#### Comparação lado a lado

```python
# ===== unittest.mock =====
from unittest.mock import patch, Mock

@patch('src.services.api.requests.get')
def test_fetch_data_unittest(mock_get):
    mock_get.return_value = Mock(status_code=200, json=lambda: {"data": "ok"})
    resultado = fetch_data()
    assert resultado == {"data": "ok"}


# ===== pytest-mock =====
def test_fetch_data_pytest(mocker):
    mock_get = mocker.patch('src.services.api.requests.get')
    mock_get.return_value = Mock(status_code=200, json=lambda: {"data": "ok"})
    resultado = fetch_data()
    assert resultado == {"data": "ok"}
```

**Recomendação:** Use **pytest-mock** neste projeto para consistência e simplicidade.

---

**Recapitulando Capítulo 3:**

✅ Aprendemos por que mockar (velocidade, custo, determinismo)
✅ Entendemos diferentes tipos de test doubles
✅ Vimos quando mockar vs usar dados reais
✅ Criamos mock completo de OpenAI passo a passo
✅ Comparamos unittest.mock vs pytest-mock

**Próximo capítulo:** Fixtures Pytest — como organizar setup reutilizável.

---

## 📘 Capítulo 4: Fixtures Pytest

### 4.1 O que são fixtures?

**Definição:**
Fixtures são funções que fornecem dados ou configuração reutilizável para testes.

**Analogia:**
Imagine uma cozinha profissional:
- ❌ **Sem fixtures**: Cada cozinheiro prepara seus próprios ingredientes
- ✅ **Com fixtures**: Mise en place (ingredientes já preparados e organizados)

**Problema sem fixtures:**

```python
def test_criar_usuario_1():
    # Setup duplicado
    db = conectar_banco_teste()
    limpar_tabela_usuarios(db)

    usuario = criar_usuario("João", db)
    assert usuario.nome == "João"

    # Cleanup
    limpar_tabela_usuarios(db)
    desconectar_banco(db)


def test_criar_usuario_2():
    # Setup duplicado DE NOVO
    db = conectar_banco_teste()
    limpar_tabela_usuarios(db)

    usuario = criar_usuario("Maria", db)
    assert usuario.email == "maria@test.com"

    # Cleanup DE NOVO
    limpar_tabela_usuarios(db)
    desconectar_banco(db)


# 10 testes = 10x o mesmo setup! 😫
```

**Solução com fixture:**

```python
@pytest.fixture
def db_limpo():
    """Fixture: banco de dados limpo"""
    # Setup
    db = conectar_banco_teste()
    limpar_tabela_usuarios(db)

    yield db  # Fornece para o teste

    # Cleanup (roda automaticamente após teste)
    limpar_tabela_usuarios(db)
    desconectar_banco(db)


def test_criar_usuario_1(db_limpo):
    usuario = criar_usuario("João", db_limpo)
    assert usuario.nome == "João"


def test_criar_usuario_2(db_limpo):
    usuario = criar_usuario("Maria", db_limpo)
    assert usuario.email == "maria@test.com"


# Setup e cleanup automáticos! 🎉
```

### 4.2 Para que servem? (evitar repetição)

Fixtures servem para:

#### 1. **Eliminar duplicação de código**

```python
# ❌ Sem fixture: código duplicado
def test_a():
    config = {"api_key": "test", "timeout": 30}
    resultado = processar(config)
    assert resultado

def test_b():
    config = {"api_key": "test", "timeout": 30}  # Duplicado!
    resultado = processar(config)
    assert resultado


# ✅ Com fixture: DRY (Don't Repeat Yourself)
@pytest.fixture
def config():
    return {"api_key": "test", "timeout": 30}

def test_a(config):
    resultado = processar(config)
    assert resultado

def test_b(config):
    resultado = processar(config)
    assert resultado
```

#### 2. **Garantir setup e cleanup**

```python
@pytest.fixture
def arquivo_temporario():
    # Setup: cria arquivo
    arquivo = Path("/tmp/teste.txt")
    arquivo.write_text("dados de teste")

    yield arquivo

    # Cleanup: deleta arquivo (SEMPRE roda, mesmo se teste falhar)
    arquivo.unlink()


def test_ler_arquivo(arquivo_temporario):
    conteudo = arquivo_temporario.read_text()
    assert conteudo == "dados de teste"
    # Arquivo é deletado automaticamente após o teste
```

#### 3. **Organizar dependências complexas**

```python
@pytest.fixture
def usuario_autenticado(db_limpo, servidor_api):
    """Fixture que depende de outras fixtures"""
    usuario = criar_usuario("teste@email.com", db_limpo)
    token = autenticar(usuario, servidor_api)
    return {"usuario": usuario, "token": token}


def test_acessar_recurso_protegido(usuario_autenticado):
    # usuario_autenticado já traz tudo pronto
    response = fazer_request("/api/dados", usuario_autenticado["token"])
    assert response.status_code == 200
```

#### 4. **Melhorar legibilidade dos testes**

```python
# ❌ Teste confuso: muito setup obscurece o que está sendo testado
def test_calcular_frete():
    produto = Produto(peso=5, dimensoes=(10, 20, 30))
    endereco = Endereco(cep="12345-678", cidade="São Paulo", estado="SP")
    transportadora = Transportadora(nome="Rápida", taxa_base=10.0)

    frete = calcular_frete(produto, endereco, transportadora)
    assert frete == 25.0


# ✅ Teste claro: fixtures escondem complexidade
def test_calcular_frete(produto_padrao, endereco_sp, transportadora_rapida):
    frete = calcular_frete(produto_padrao, endereco_sp, transportadora_rapida)
    assert frete == 25.0
```

### 4.3 Quando usar fixtures

#### ✅ Use fixtures quando:

1. **Múltiplos testes precisam do mesmo setup**
   ```python
   @pytest.fixture
   def client_api():
       return APIClient(base_url="https://test.com", api_key="test")
   ```

2. **Setup é complexo ou demorado**
   ```python
   @pytest.fixture(scope="module")  # Cria apenas 1x por módulo
   def modelo_ml_treinado():
       # Treinar modelo leva tempo, fazer só 1x
       return treinar_modelo(epochs=100)
   ```

3. **Precisa garantir cleanup**
   ```python
   @pytest.fixture
   def servidor_mock():
       servidor = IniciarServidorMock(porta=8080)
       yield servidor
       servidor.parar()  # Cleanup garantido
   ```

4. **Quer isolar testes (ambientes independentes)**
   ```python
   @pytest.fixture
   def diretorio_temporario(tmp_path):
       # Cada teste tem seu próprio diretório
       return tmp_path / "meu_teste"
   ```

#### ❌ NÃO use fixtures quando:

1. **Setup é trivial (1 linha)**
   ```python
   # ❌ Desnecessário
   @pytest.fixture
   def numero():
       return 42

   def test_algo(numero):
       assert numero == 42


   # ✅ Melhor assim
   def test_algo():
       numero = 42
       assert numero == 42
   ```

2. **Usado em apenas 1 teste**
   ```python
   # ❌ Fixture usada só 1x
   @pytest.fixture
   def config_especifica():
       return {"modo": "especial"}

   def test_unico_caso(config_especifica):
       processar(config_especifica)


   # ✅ Melhor inline
   def test_unico_caso():
       config_especifica = {"modo": "especial"}
       processar(config_especifica)
   ```

3. **Valores podem ser constantes**
   ```python
   # ❌ Fixture para constante
   @pytest.fixture
   def api_url():
       return "https://api.exemplo.com"


   # ✅ Melhor como constante
   API_URL = "https://api.exemplo.com"
   ```

### 4.4 Escopos: function, class, module, session

Fixtures têm **escopo** que define quando são criadas e destruídas.

#### `function` (padrão)

**Quando:** Criada antes de **cada teste**, destruída depois.

**Use para:** Dados que devem ser isolados entre testes.

```python
@pytest.fixture(scope="function")  # scope="function" é o padrão
def contador():
    return {"valor": 0}


def test_incrementar(contador):
    contador["valor"] += 1
    assert contador["valor"] == 1


def test_incrementar_novamente(contador):
    contador["valor"] += 1
    assert contador["valor"] == 1  # ✅ Novo contador, começa em 0
```

#### `class`

**Quando:** Criada **1x por classe** de testes.

**Use para:** Dados compartilhados dentro de uma classe.

```python
@pytest.fixture(scope="class")
def db_connection():
    conn = conectar_banco()
    yield conn
    conn.close()


class TestUsuarios:
    def test_criar(self, db_connection):
        # Usa mesma conexão
        criar_usuario("João", db_connection)

    def test_listar(self, db_connection):
        # Usa mesma conexão
        usuarios = listar_usuarios(db_connection)
```

#### `module`

**Quando:** Criada **1x por arquivo** de teste.

**Use para:** Recursos caros de criar (servidor mock, modelo ML).

```python
@pytest.fixture(scope="module")
def servidor_api():
    servidor = IniciarServidorAPI(porta=5000)
    yield servidor
    servidor.parar()


def test_endpoint_1(servidor_api):
    # Usa mesmo servidor
    response = requests.get(f"{servidor_api.url}/endpoint1")


def test_endpoint_2(servidor_api):
    # Usa mesmo servidor
    response = requests.get(f"{servidor_api.url}/endpoint2")
```

#### `session`

**Quando:** Criada **1x por sessão inteira** de testes.

**Use para:** Recursos muito caros (banco de dados, cache Redis).

```python
@pytest.fixture(scope="session")
def banco_dados_teste():
    db = criar_banco_teste()
    yield db
    db.drop_all_tables()
    db.close()


def test_a(banco_dados_teste):
    # Usa mesmo banco
    pass


def test_b(banco_dados_teste):
    # Usa mesmo banco
    pass
```

#### Comparação visual

```
session    |====================| (1x para todos os testes)
           ▼
module     |======| |======|      (1x por arquivo)
           ▼       ▼
class      |==| |==|              (1x por classe)
           ▼   ▼
function   ||| ||| ||| |||        (1x por teste)
           test1 test2 test3 ...
```

#### Escolhendo o escopo correto

| Critério | Escopo recomendado |
|----------|-------------------|
| Cada teste deve ter dados limpos | `function` |
| Setup é caro (>1s) | `module` ou `session` |
| Dados podem ser compartilhados | `class` ou `module` |
| Recurso global (banco, cache) | `session` |
| Testes modificam o estado | `function` (isolar) |

### 4.5 Fixtures parametrizadas

Fixtures podem gerar **múltiplos valores** automaticamente.

#### Exemplo básico

```python
@pytest.fixture(params=["gpt-4", "gpt-4o-mini", "gpt-3.5-turbo"])
def modelo_openai(request):
    """Fixture que roda teste com 3 modelos diferentes"""
    return request.param


def test_gerar_texto(modelo_openai):
    # Este teste roda 3x, 1x para cada modelo
    resultado = chamar_gpt(modelo=modelo_openai, prompt="Oi")
    assert len(resultado) > 0
```

**Saída pytest:**
```
test_exemplo.py::test_gerar_texto[gpt-4] PASSED
test_exemplo.py::test_gerar_texto[gpt-4o-mini] PASSED
test_exemplo.py::test_gerar_texto[gpt-3.5-turbo] PASSED
```

#### Exemplo com dados complexos

```python
@pytest.fixture(params=[
    {"idioma": "pt", "resposta_esperada": "Olá"},
    {"idioma": "en", "resposta_esperada": "Hello"},
    {"idioma": "es", "resposta_esperada": "Hola"},
])
def config_idioma(request):
    return request.param


def test_traducao(config_idioma):
    # Roda 3x, 1x por idioma
    resultado = traduzir("oi", config_idioma["idioma"])
    assert resultado == config_idioma["resposta_esperada"]
```

#### Exemplo prático: testar múltiplos bancos

```python
@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def banco_dados(request):
    tipo = request.param

    if tipo == "sqlite":
        db = SQLiteDB(":memory:")
    elif tipo == "postgres":
        db = PostgresDB("postgresql://test:test@localhost/test")
    elif tipo == "mysql":
        db = MySQLDB("mysql://test:test@localhost/test")

    db.criar_tabelas()
    yield db
    db.drop_tabelas()


def test_crud_usuario(banco_dados):
    # Teste roda com SQLite, Postgres E MySQL!
    usuario = Usuario(nome="João")
    banco_dados.salvar(usuario)

    resultado = banco_dados.buscar(Usuario, id=usuario.id)
    assert resultado.nome == "João"
```

### 4.6 Exemplo prático: fixture de ambiente temporário

Vamos criar uma fixture que cria um diretório temporário com arquivos de teste.

```python
import pytest
from pathlib import Path
import tempfile
import shutil


@pytest.fixture
def ambiente_temporario():
    """
    Cria ambiente temporário com arquivos para teste

    Estrutura criada:
        /tmp/test_XXXX/
        ├── config.json
        ├── dados/
        │   ├── arquivo1.txt
        │   └── arquivo2.txt
        └── saida/
    """
    # Setup: cria diretório temporário
    dir_temp = Path(tempfile.mkdtemp(prefix="test_"))

    # Cria estrutura de pastas
    dir_dados = dir_temp / "dados"
    dir_saida = dir_temp / "saida"
    dir_dados.mkdir()
    dir_saida.mkdir()

    # Cria arquivo de config
    (dir_temp / "config.json").write_text('{"modo": "teste"}')

    # Cria arquivos de dados
    (dir_dados / "arquivo1.txt").write_text("Conteúdo 1")
    (dir_dados / "arquivo2.txt").write_text("Conteúdo 2")

    # Yield: fornece para o teste
    yield dir_temp

    # Cleanup: deleta tudo após teste
    shutil.rmtree(dir_temp)


def test_processar_arquivos(ambiente_temporario):
    # ===== ARRANGE =====
    # ambiente_temporario já criou tudo
    dir_dados = ambiente_temporario / "dados"

    # ===== ACT =====
    arquivos = list(dir_dados.glob("*.txt"))

    # ===== ASSERT =====
    assert len(arquivos) == 2
    assert arquivos[0].read_text() in ["Conteúdo 1", "Conteúdo 2"]


def test_escrever_resultado(ambiente_temporario):
    # ===== ARRANGE =====
    dir_saida = ambiente_temporario / "saida"
    arquivo_resultado = dir_saida / "resultado.txt"

    # ===== ACT =====
    arquivo_resultado.write_text("Processado com sucesso")

    # ===== ASSERT =====
    assert arquivo_resultado.exists()
    assert arquivo_resultado.read_text() == "Processado com sucesso"

    # Cleanup automático: ambiente_temporario deleta tudo
```

### 4.7 conftest.py e compartilhamento de fixtures

#### O que é conftest.py?

**Definição:**
Arquivo especial do pytest que define fixtures **compartilhadas** entre múltiplos arquivos de teste.

**Características:**
- ✅ Não precisa ser importado (pytest descobre automaticamente)
- ✅ Fixtures disponíveis para todos os testes no diretório e subdiretórios
- ✅ Pode ter múltiplos conftest.py em diferentes níveis

#### Estrutura de diretórios

```
tests/
├── conftest.py          # Fixtures globais (todos os testes)
│
├── unit/
│   ├── conftest.py      # Fixtures para testes unitários
│   ├── test_a.py
│   └── test_b.py
│
└── integration/
    ├── conftest.py      # Fixtures para testes de integração
    ├── test_x.py
    └── test_y.py
```

#### Exemplo de conftest.py global

```python
# tests/conftest.py
import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_env(monkeypatch):
    """Fixture: variáveis de ambiente mockadas"""
    monkeypatch.setenv('API_KEY', 'test-key')
    monkeypatch.setenv('DEBUG', 'true')
    yield


@pytest.fixture
def mock_openai_response():
    """Fixture: resposta mockada do OpenAI"""
    mock_response = Mock()
    mock_response.choices = [Mock()]
    mock_response.choices[0].message.content = "Resposta mockada"
    return mock_response


@pytest.fixture
def mock_logger():
    """Fixture: logger mockado"""
    return Mock()
```

#### Usando fixtures do conftest.py

```python
# tests/unit/test_servico.py
# NÃO precisa importar nada!

def test_processar_com_env(mock_env):
    # mock_env está disponível automaticamente
    import os
    assert os.getenv('API_KEY') == 'test-key'


def test_chamar_openai(mock_openai_response):
    # mock_openai_response também está disponível
    assert mock_openai_response.choices[0].message.content == "Resposta mockada"
```

#### Fixtures hierárquicas

```python
# tests/conftest.py (nível raiz)
@pytest.fixture
def config_base():
    return {"timeout": 30}


# tests/integration/conftest.py (sobrescreve/estende)
@pytest.fixture
def config_base():
    # Estende a config base
    return {"timeout": 60, "retry": 3}  # Timeout maior para integração
```

#### Boas práticas

1. **Organize por escopo:**
   ```
   conftest.py global    → Fixtures usadas em TODOS os testes
   conftest.py unit/     → Fixtures específicas de unitários
   conftest.py integration/ → Fixtures específicas de integração
   ```

2. **Documente fixtures:**
   ```python
   @pytest.fixture
   def usuario_admin():
       """
       Fixture: Usuário com permissões de admin

       Returns:
           dict: {"id": 1, "role": "admin", "token": "abc123"}
       """
       return {"id": 1, "role": "admin", "token": "abc123"}
   ```

3. **Evite muitas fixtures em um arquivo:**
   - Máximo 10-15 fixtures por conftest.py
   - Se passar disso, considere quebrar em módulos

---

**Recapitulando Capítulo 4:**

✅ Aprendemos o que são fixtures e por que usar
✅ Entendemos quando usar (e quando NÃO usar)
✅ Exploramos escopos (function, class, module, session)
✅ Vimos fixtures parametrizadas
✅ Criamos exemplo prático de ambiente temporário
✅ Aprendemos sobre conftest.py e compartilhamento

**Próximo capítulo:** Setup do Projeto — estrutura de diretórios, dependências e configuração.

---

## 📘 Capítulo 5: Setup do Projeto

### 5.1 Estrutura de diretórios a criar

Vamos criar a estrutura completa do projeto passo a passo.

#### Passo 1: Criar diretórios principais

```bash
cd /Users/eltoncasaccia/fullcycle/fctech/langfuse

# Criar estrutura de diretórios
mkdir -p src/core
mkdir -p src/utils
mkdir -p src/examples
mkdir -p tests/unit/core
mkdir -p tests/unit/utils
mkdir -p tests/integration
```

#### Passo 2: Criar arquivos __init__.py

```bash
# Marcar diretórios como pacotes Python
touch src/__init__.py
touch src/core/__init__.py
touch src/utils/__init__.py
touch src/examples/__init__.py
touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/unit/core/__init__.py
touch tests/unit/utils/__init__.py
touch tests/integration/__init__.py
```

#### Passo 3: Verificar estrutura criada

```bash
tree -I '__pycache__|*.pyc|.pytest_cache' --dirsfirst
```

**Saída esperada:**
```
.
├── src/
│   ├── core/
│   │   └── __init__.py
│   ├── examples/
│   │   └── __init__.py
│   ├── utils/
│   │   └── __init__.py
│   └── __init__.py
├── tests/
│   ├── integration/
│   │   └── __init__.py
│   ├── unit/
│   │   ├── core/
│   │   │   └── __init__.py
│   │   ├── utils/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   └── __init__.py
├── .env
└── pyproject.toml (criaremos a seguir)
```

### 5.2 Dependências a instalar

#### Passo 1: Instalar pytest e plugins

```bash
# Core do pytest
pip install pytest

# Plugins essenciais
pip install pytest-cov      # Cobertura de código
pip install pytest-mock     # Mocking integrado
pip install pytest-xdist    # Rodar testes em paralelo (opcional)

# Bibliotecas auxiliares para testes
pip install faker           # Dados fake (nomes, emails, etc.)
pip install freezegun       # Mockar tempo/datas
```

#### Passo 2: Verificar instalação

```bash
pytest --version
# Saída esperada: pytest 8.x.x
```

#### Passo 3: Criar requirements-dev.txt

```bash
cat > requirements-dev.txt << 'EOF'
# Testes
pytest>=8.0.0
pytest-cov>=4.1.0
pytest-mock>=3.12.0
pytest-xdist>=3.5.0

# Ferramentas de teste
faker>=22.0.0
freezegun>=1.4.0

# Linting e type checking
ruff>=0.1.0
pyright>=1.1.0

# Desenvolvimento
ipython>=8.0.0
EOF
```

```bash
# Instalar todas de uma vez
pip install -r requirements-dev.txt
```

### 5.3 Configurar pyproject.toml

Vamos criar configuração completa do projeto.

```bash
cat > pyproject.toml << 'EOF'
[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[project]
name = "langfuse-testing-guide"
version = "0.1.0"
description = "Guia prático de testes profissionais em Python"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "langfuse>=2.0.0",
    "openai>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.1.0",
    "pytest-mock>=3.12.0",
    "pytest-xdist>=3.5.0",
    "faker>=22.0.0",
    "freezegun>=1.4.0",
    "ruff>=0.1.0",
    "pyright>=1.1.0",
]

# ============================================================
# PYTEST: Configuração de testes
# ============================================================
[tool.pytest.ini_options]
# Diretórios onde procurar testes
testpaths = ["tests"]

# Padrão de nomes de arquivos de teste
python_files = ["test_*.py", "*_test.py"]

# Padrão de nomes de classes de teste
python_classes = ["Test*"]

# Padrão de nomes de funções de teste
python_functions = ["test_*"]

# Opções padrão ao rodar pytest
addopts = [
    "-v",                          # Verbose (mostra cada teste)
    "--strict-markers",            # Erro se usar marker não registrado
    "--tb=short",                  # Traceback curto em falhas
    "--cov=src",                   # Medir cobertura do diretório src/
    "--cov-report=term-missing",   # Mostrar linhas não cobertas
    "--cov-report=html",           # Gerar relatório HTML
    "--cov-fail-under=95",         # Falhar se cobertura < 95%
]

# Markers customizados (para categorizar testes)
markers = [
    "slow: marca testes lentos (integração, E2E)",
    "integration: testes de integração",
    "unit: testes unitários",
    "smoke: testes de fumaça (críticos)",
]

# Filtrar warnings
filterwarnings = [
    "error",                       # Transformar warnings em erros
    "ignore::DeprecationWarning",  # Ignorar deprecation warnings
]

# ============================================================
# COVERAGE: Configuração de cobertura
# ============================================================
[tool.coverage.run]
# Diretórios a medir cobertura
source = ["src"]

# Rodar testes em paralelo (se usar pytest-xdist)
parallel = true

# Arquivos a omitir da cobertura
omit = [
    "*/tests/*",
    "*/__pycache__/*",
    "*/site-packages/*",
    "*/__init__.py",
]

[tool.coverage.report]
# Precisão de porcentagem
precision = 2

# Mostrar linhas faltando
show_missing = true

# Pular arquivos vazios
skip_empty = true

# Pular arquivos cobertos 100%
skip_covered = false

# Falhar se cobertura < 95%
fail_under = 95.0

# Ordenar por cobertura (menos cobertos primeiro)
sort = "Cover"

[tool.coverage.html]
# Diretório para relatório HTML
directory = "htmlcov"

# ============================================================
# RUFF: Linting e formatação
# ============================================================
[tool.ruff]
# Comprimento máximo de linha
line-length = 100

# Versão Python alvo
target-version = "py310"

# Diretórios a ignorar
exclude = [
    ".git",
    "__pycache__",
    ".pytest_cache",
    "htmlcov",
    "*.egg-info",
]

[tool.ruff.lint]
# Regras ativadas
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort (imports)
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
]

# Regras ignoradas
ignore = [
    "E501",  # Linha muito longa (já configurado line-length)
]

[tool.ruff.lint.per-file-ignores]
# Testes podem ter imports não usados
"tests/**/*.py" = ["F401", "F811"]

# ============================================================
# PYRIGHT: Type checking
# ============================================================
[tool.pyright]
# Diretórios a verificar
include = ["src", "tests"]

# Diretórios a ignorar
exclude = [
    "**/__pycache__",
    ".pytest_cache",
    "htmlcov",
]

# Modo de type checking
typeCheckingMode = "basic"  # "off" | "basic" | "strict"

# Reportar imports faltando
reportMissingImports = true

# Reportar uso de tipos desconhecidos
reportUnknownParameterType = false
reportUnknownArgumentType = false
reportUnknownVariableType = false

# Python version
pythonVersion = "3.10"
EOF
```

### 5.4 Criar .gitignore

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Ambientes virtuais
venv/
ENV/
env/
.venv

# Pytest
.pytest_cache/
.coverage
htmlcov/
.tox/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Dados sensíveis
.env
.env.local
*.pem
*.key

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Temporários
tmp/
temp/
EOF
```

### 5.5 Validar setup

Após criar tudo, valide que está funcionando:

```bash
# 1. Verificar estrutura
ls -la src/ tests/

# 2. Testar pytest (deve dizer "no tests ran" - normal)
pytest --collect-only

# 3. Testar cobertura (deve dar erro de <95%, normal - ainda não tem código)
pytest --cov=src || echo "Normal: ainda não há código para testar"

# 4. Verificar linting
ruff check src/ tests/ || echo "Normal: ainda não há código"

# 5. Verificar type checking
pyright src/ || echo "Normal: ainda não há código"
```

**Saída esperada:**
```
collected 0 items
========== no tests ran in 0.01s ==========
```

### 5.6 Criar README.md básico

```bash
cat > README.md << 'EOF'
# Langfuse Testing Guide

Projeto de exemplo: testes profissionais em Python.

## Setup

```bash
# Instalar dependências
pip install -r requirements-dev.txt

# Configurar .env
cp .env.example .env
# Editar .env com suas chaves
```

## Rodar testes

```bash
# Todos os testes
pytest

# Apenas unitários
pytest tests/unit/

# Apenas integração
pytest tests/integration/

# Com cobertura
pytest --cov=src --cov-report=html
# Ver relatório: open htmlcov/index.html

# Testes específicos
pytest tests/unit/core/test_env.py -v

# Rodar em paralelo (mais rápido)
pytest -n auto
```

## Estrutura

```
src/              # Código de produção
├── core/         # Módulos principais
├── utils/        # Utilitários
└── examples/     # Scripts de exemplo

tests/            # Testes
├── conftest.py   # Fixtures compartilhadas
├── unit/         # Testes unitários
└── integration/  # Testes de integração
```

## Métricas

- **Cobertura alvo:** 95%+
- **Tempo de execução:** < 5s
- **Testes independentes:** 100%
EOF
```

---

**Checklist Capítulo 5:**

✅ Estrutura de diretórios criada
✅ `__init__.py` em todos os pacotes
✅ Dependências instaladas
✅ `pyproject.toml` configurado
✅ `.gitignore` criado
✅ `README.md` criado
✅ Setup validado

**Próximo capítulo:** Refatoração — vamos extrair código reutilizável para `src/core/` e `src/utils/`.

---

## 📘 Capítulo 6: Refatoração

### 6.1 Extrair `src/core/env.py`

Vamos criar o módulo responsável por gerenciar variáveis de ambiente.

**Arquivo:** `src/core/env.py`

```python
"""
Módulo: Gerenciamento de Variáveis de Ambiente

PROPÓSITO:
    Carregar e validar variáveis de ambiente do arquivo .env
    sem depender de bibliotecas externas (python-dotenv).

POR QUE SEPARAMOS ISSO:
    - Reutilização: múltiplos scripts precisam carregar .env
    - Testabilidade: fácil testar parsing isoladamente
    - Responsabilidade única: só trata de variáveis de ambiente

📚 Conceito: Separação de responsabilidades (SRP - Single Responsibility Principle)
"""

from __future__ import annotations
import os
from pathlib import Path

# Detecta raiz do projeto (2 níveis acima deste arquivo)
# src/core/env.py → src/core/ → src/ → raiz/
ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"


def carregar_env() -> None:
    """
    Carrega variáveis de um arquivo .env para os.environ

    COMO FUNCIONA:
        1. Verifica se .env existe
        2. Lê linha por linha
        3. Ignora comentários (#) e linhas vazias
        4. Faz parsing de KEY=valor
        5. Remove aspas (" e ')
        6. Define em os.environ (se ainda não definida)

    POR QUE FAZER PARSING MANUAL:
        - Evita dependência de python-dotenv
        - Mais leve para projetos pequenos
        - Controle total sobre comportamento

    EXEMPLO DE .env:
        LANGFUSE_PUBLIC_KEY="pk-123"
        OPENAI_API_KEY='sk-456'  # comentário
        # linha de comentário ignorada

    EDGE CASES TRATADOS:
        - Arquivo não existe → não faz nada (usa vars do sistema)
        - Linhas vazias → ignora
        - Comentários → ignora
        - Valores com '=' no meio → divide apenas no primeiro '='
        - Valores com aspas → remove
        - Var já existe no sistema → mantém a do sistema (não sobrescreve)

    📚 Conceito: Parsing de arquivos texto, manipulação de strings
    """
    # Se .env não existe, retorna sem erro (permite usar env vars do sistema)
    if not ENV_FILE.exists():
        return

    # Lê todo o conteúdo do arquivo de uma vez
    for raw_line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        # Remove espaços no início e fim
        line = raw_line.strip()

        # Ignora linhas vazias, comentários e linhas sem '='
        if not line or line.startswith("#") or "=" not in line:
            continue

        # Separa em KEY e valor (apenas no primeiro '=')
        # Exemplo: "API_KEY=valor=com=igual" → key="API_KEY", value="valor=com=igual"
        key, value = line.split("=", 1)

        # Remove espaços e aspas do valor
        # .strip() remove espaços
        # .strip('"') remove aspas duplas
        # .strip("'") remove aspas simples
        value = value.strip().strip('"').strip("'")

        # Define no ambiente APENAS se ainda não existe
        # setdefault: só define se a chave não existir
        # Isso permite que env vars do sistema tenham prioridade
        os.environ.setdefault(key.strip(), value)


def exigir_variaveis(nomes: list[str]) -> None:
    """
    Valida que variáveis obrigatórias existem no ambiente

    PARÂMETROS:
        nomes: Lista de nomes de variáveis obrigatórias

    LANÇA:
        RuntimeError: Se alguma variável estiver ausente

    POR QUE VALIDAR:
        - Fail fast: erro imediato, não no meio da execução
        - Mensagem clara: lista exata do que falta
        - Evita erros confusos (ex: None em API key)

    EXEMPLO DE USO:
        exigir_variaveis([
            "LANGFUSE_PUBLIC_KEY",
            "LANGFUSE_SECRET_KEY",
            "OPENAI_API_KEY"
        ])

    COMPORTAMENTO:
        - Se todas existem → retorna sem fazer nada
        - Se alguma falta → lança RuntimeError com lista das faltantes

    📚 Conceito: Validação de entrada, fail-fast pattern
    """
    # List comprehension: cria lista apenas com vars ausentes
    # os.getenv(nome) retorna None se não existe
    faltando = [nome for nome in nomes if not os.getenv(nome)]

    # Se lista está vazia, todas as vars existem → retorna
    if not faltando:
        return

    # Junta nomes com vírgula para mensagem legível
    variaveis = ", ".join(faltando)

    # Lança erro com mensagem útil
    raise RuntimeError(
        f"Variáveis obrigatórias ausentes: {variaveis}. "
        "Configure no arquivo .env da raiz do projeto."
    )


def modelo_padrao() -> str:
    """
    Retorna modelo OpenAI padrão com fallback

    RETORNA:
        Valor de OPENAI_MODEL ou "gpt-4o-mini" se não definido

    POR QUE USAR FALLBACK:
        - Conveniência: funciona sem configurar OPENAI_MODEL
        - Custo: gpt-4o-mini é mais barato para exemplos
        - Flexibilidade: pode trocar via .env

    EXEMPLO:
        # .env vazio ou sem OPENAI_MODEL
        modelo_padrao()  # → "gpt-4o-mini"

        # .env com OPENAI_MODEL="gpt-4"
        modelo_padrao()  # → "gpt-4"

    📚 Conceito: Default values, configuração flexível
    """
    return os.getenv("OPENAI_MODEL", "gpt-4o-mini")
```

**Instruções de implementação:**

1. Criar arquivo:
```bash
cat > src/core/env.py << 'EOF'
[Copiar código acima]
EOF
```

2. Verificar que criou corretamente:
```bash
python -c "from src.core.env import carregar_env; print('✅ Importação OK')"
```

### 6.2 Criar `src/core/clients.py`

Vamos criar factories para clientes OpenAI e Langfuse.

**Arquivo:** `src/core/clients.py`

```python
"""
Módulo: Factories de Clientes (OpenAI e Langfuse)

PROPÓSITO:
    Centralizar criação de clientes configurados.

PATTERN: Factory Method
    Em vez de fazer `OpenAI()` diretamente em cada script,
    usamos uma função factory. Benefícios:
    - Configuração centralizada
    - Fácil trocar implementação
    - Fácil mockar em testes
    - Dependency Injection facilitada

EXEMPLO SEM FACTORY (problema):
    # Em 10 arquivos diferentes:
    from openai import OpenAI
    client = OpenAI()  # Duplicado 10x!

    # Se quisermos adicionar retry ou logging:
    # → Precisamos mudar 10 arquivos 😫

EXEMPLO COM FACTORY (solução):
    # Em 10 arquivos:
    from src.core.clients import criar_openai_client
    client = criar_openai_client()

    # Para adicionar retry:
    # → Mudamos apenas clients.py 🎉

📚 Conceito: Factory Pattern, Dependency Injection
"""

from langfuse.openai import OpenAI
from langfuse import Langfuse, get_client


def criar_openai_client() -> OpenAI:
    """
    Factory: Cria cliente OpenAI wrappado com Langfuse

    O QUE É:
        OpenAI client da biblioteca langfuse.openai (não openai direta).
        Este client intercepta chamadas e envia traces para Langfuse.

    COMO FUNCIONA:
        langfuse.openai.OpenAI herda de openai.OpenAI
        + adiciona instrumentação automática (observability)

    RETORNA:
        Cliente OpenAI pronto para usar

    CONFIGURAÇÃO:
        Lê automaticamente do ambiente:
        - OPENAI_API_KEY (obrigatória)
        - OPENAI_ORG_ID (opcional)
        - OPENAI_BASE_URL (opcional, para proxies)

    EXEMPLO DE USO:
        client = criar_openai_client()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Oi"}]
        )
        # ^ Isso já cria trace no Langfuse automaticamente

    POR QUE FACTORY:
        - Se quisermos trocar para outro provider (Anthropic, etc.),
          mudamos só aqui
        - Em testes, mockamos esta função
        - Podemos adicionar retry logic, logging, etc. aqui

    POSSÍVEIS EXTENSÕES FUTURAS:
        - Adicionar tenacity para retry
        - Adicionar logging de erros
        - Rotacionar entre múltiplas API keys
        - Usar cache local (tipo langchain cache)

    📚 Conceito: Factory Pattern, Wrapper Pattern
    """
    # Simplesmente cria e retorna
    # O client já lê OPENAI_API_KEY do ambiente automaticamente
    return OpenAI()


def criar_langfuse_client() -> Langfuse:
    """
    Factory: Cria cliente Langfuse

    O QUE FAZ:
        Retorna singleton global do Langfuse.

    ALTERNATIVA:
        Pode usar `Langfuse()` diretamente para criar nova instância.
        Aqui usamos `get_client()` que retorna singleton compartilhado.

    POR QUE SINGLETON:
        - Evita criar múltiplas conexões
        - Melhor para batching de traces
        - Gerenciamento de estado centralizado

    CONFIGURAÇÃO:
        Lê automaticamente do ambiente:
        - LANGFUSE_PUBLIC_KEY (obrigatória)
        - LANGFUSE_SECRET_KEY (obrigatória)
        - LANGFUSE_BASE_URL (opcional, padrão: https://cloud.langfuse.com)

    RETORNA:
        Cliente Langfuse configurado

    EXEMPLO DE USO:
        langfuse = criar_langfuse_client()
        trace_id = langfuse.get_current_trace_id()
        prompt = langfuse.get_prompt("nome-prompt")

    📚 Conceito: Singleton Pattern, Factory Pattern
    """
    return get_client()  # Retorna singleton global


def finalizar_langfuse() -> None:
    """
    Flush de traces pendentes para API Langfuse

    POR QUE NECESSÁRIO:
        Langfuse envia traces de forma assíncrona (background threads).
        Ao final do script, precisamos garantir que tudo foi enviado
        antes de sair, senão traces podem ser perdidos.

    O QUE FAZ:
        - Aguarda envio de traces pendentes
        - Bloqueia até completar (síncrono)
        - Fecha conexões

    QUANDO CHAMAR:
        Sempre no final do script, antes de sair.
        Idealmente em bloco finally para garantir execução.

    EXEMPLO:
        try:
            # ... código do script
            gerar_resposta_gpt(...)
        finally:
            finalizar_langfuse()  # Garante flush mesmo se houver erro

    O QUE ACONTECE SE NÃO CHAMAR:
        - Traces podem não aparecer no dashboard
        - Dados podem ser perdidos
        - Warnings no console sobre threads não finalizados

    📚 Conceito: Cleanup, flush de buffers, context management
    """
    get_client().flush()
```

**Instruções de implementação:**

```bash
cat > src/core/clients.py << 'EOF'
[Copiar código acima]
EOF
```

### 6.3 Criar `src/utils/error_handling.py`

Vamos criar utilitário para tratamento de erros.

**Arquivo:** `src/utils/error_handling.py`

```python
"""
Módulo: Tratamento de Erros

PROPÓSITO:
    Centralizar lógica de captura e exibição de erros de forma amigável.

POR QUE CENTRALIZAR:
    - DRY: Evita duplicar try/except em todo arquivo
    - Consistência: Mensagens de erro padronizadas
    - Manutenção: Mudar formato de erro em um lugar só

📚 Conceito: Exception handling, DRY, user-friendly errors
"""

import sys
from typing import Callable, TypeVar

# TypeVar para preservar tipo de retorno da função
T = TypeVar('T')


def executar_seguro(func: Callable[[], T]) -> T:
    """
    Wrapper: Executa função com tratamento de erro amigável

    POR QUE USAR:
        - Transforma erros técnicos em mensagens úteis para o usuário
        - Centraliza tratamento (DRY - Don't Repeat Yourself)
        - Evita duplicação de try/except em múltiplos lugares

    PARÂMETROS:
        func: Função sem argumentos (lambda ou callable) que será executada

    RETORNA:
        Resultado da função se sucesso

    LANÇA:
        SystemExit(1): Se houver erro (sai do programa com código de erro)

    COMO FUNCIONA:
        1. Tenta executar função fornecida
        2. Se sucesso, retorna resultado
        3. Se der erro:
           - Mostra mensagem amigável com dicas de troubleshooting
           - Mostra detalhe técnico do erro
           - Propaga exceção original (mantém stack trace)
           - Sai com código 1 (convenção Unix: 0=sucesso, 1=erro)

    EXEMPLO DE USO:
        # Sem wrapper (código duplicado em vários lugares):
        try:
            resultado = chamar_openai()
        except Exception as e:
            print("Erro ao chamar API...")
            print(f"Detalhe: {e}")
            sys.exit(1)

        # Com wrapper (limpo e reutilizável):
        resultado = executar_seguro(lambda: chamar_openai())

    EXEMPLO PRÁTICO:
        def processar_dados():
            executar_seguro(lambda: carregar_env())
            executar_seguro(lambda: validar_credenciais())
            resultado = executar_seguro(lambda: chamar_api_externa())
            return resultado

    TÉCNICAS USADAS:
        - try/except: captura qualquer exceção
        - SystemExit(1): código 1 indica erro (convenção Unix)
        - raise ... from exc: mantém stack trace original (PEP 3134)
        - Callable[[], T]: type hint para função sem args retornando T

    MENSAGENS DE ERRO:
        As mensagens sugerem verificações comuns:
        - API keys inválidas ou expiradas
        - Créditos esgotados
        - URLs incorretas
        - Problemas de conectividade

    📚 Conceito: Exception handling, wrapper pattern, DRY, fail-fast
    """
    try:
        # Executa a função passada como parâmetro
        return func()

    except Exception as exc:
        # Capturou erro: mostra mensagem amigável
        print("❌ Erro ao executar operação.")
        print("🔍 Verificações sugeridas:")
        print("   - OPENAI_API_KEY está correta e ativa?")
        print("   - Você tem créditos disponíveis no OpenAI?")
        print("   - LANGFUSE_BASE_URL está acessível?")
        print("   - LANGFUSE_PUBLIC_KEY e SECRET_KEY estão corretas?")
        print("   - Sua internet está funcionando?")
        print(f"\n💡 Detalhe técnico do erro:")
        print(f"   {type(exc).__name__}: {exc}")

        # Propaga exceção original mantendo stack trace
        # "raise ... from exc" cria cadeia de exceções (PEP 3134)
        # Isso permite debugar o erro original se necessário
        raise SystemExit(1) from exc


def exibir_erro_formatado(erro: Exception, contexto: str = "") -> None:
    """
    Exibe erro de forma formatada e legível

    USO:
        Para quando você NÃO quer sair do programa,
        apenas logar o erro de forma bonita.

    PARÂMETROS:
        erro: Exceção capturada
        contexto: Descrição do que estava sendo feito

    EXEMPLO:
        try:
            processar_arquivo(path)
        except Exception as e:
            exibir_erro_formatado(e, f"Processando {path}")
            # Continua executando...

    📚 Conceito: Logging, error formatting
    """
    print(f"\n❌ Erro: {type(erro).__name__}")
    if contexto:
        print(f"📍 Contexto: {contexto}")
    print(f"💬 Mensagem: {erro}")
    print()
```

**Instruções de implementação:**

```bash
cat > src/utils/error_handling.py << 'EOF'
[Copiar código acima]
EOF
```

**Validação:**

```bash
# Testar imports
python -c "
from src.core.env import carregar_env, exigir_variaveis, modelo_padrao
from src.core.clients import criar_openai_client, criar_langfuse_client
from src.utils.error_handling import executar_seguro
print('✅ Todos os módulos importados com sucesso!')
"
```

---

**Recapitulando até aqui:**

✅ Criamos `src/core/env.py` (gerenciamento de variáveis de ambiente)
✅ Criamos `src/core/clients.py` (factories de clientes)
✅ Criamos `src/utils/error_handling.py` (tratamento de erros)

**Próxima seção:** Vamos criar as fixtures do pytest no `tests/conftest.py`.

---

## 📘 Capítulo 7: Criar Fixtures

Este é o capítulo mais importante do guia prático. Aqui você vai criar o arquivo `tests/conftest.py` com TODAS as fixtures que serão usadas nos testes.

### 7.1 Introdução ao conftest.py

**O que é:** Arquivo especial do pytest que define fixtures compartilhadas.

**Por que é importante:**
- ✅ Fixtures disponíveis para TODOS os testes automaticamente
- ✅ Não precisa importar (pytest descobre sozinho)
- ✅ Centraliza configuração de mocks
- ✅ Evita duplicação de código

**Arquivo:** `tests/conftest.py`

### 7.2 Código completo do conftest.py

Copie o código abaixo INTEIRAMENTE para `tests/conftest.py`:

```python
"""
GUIA: Fixtures Pytest - Setup Reutilizável

O QUE É ESTE ARQUIVO:
    conftest.py é especial do pytest. Define fixtures
    compartilhadas entre TODOS os testes do projeto.

POR QUE USAR FIXTURES:
    - Evitar repetição de código de setup
    - Manter testes limpos e focados
    - Centralizar configuração de mocks

COMO USAR:
    def test_exemplo(mock_openai_client):  # ← pytest injeta automaticamente
        # mock_openai_client já está pronto para usar
        resultado = fazer_chamada()
        assert resultado == "..."

ESTRUTURA DESTE ARQUIVO:
    SEÇÃO 1: Fixtures de Ambiente
        - temp_env_file: arquivo .env temporário
        - clean_env: limpa variáveis de ambiente
        - mock_env: define variáveis mockadas

    SEÇÃO 2: Fixtures de Mocking - OpenAI
        - mock_openai_response: resposta fake do GPT
        - mock_openai_client: cliente OpenAI mockado

    SEÇÃO 3: Fixtures de Mocking - Langfuse
        - mock_langfuse_client: cliente Langfuse mockado
        - mock_observe_decorator: mock do @observe
        - mock_propagate_attributes: mock do context manager

    SEÇÃO 4: Fixture Composta
        - full_mock_setup: combina todos os mocks

📚 Leia mais sobre fixtures no Capítulo 4
"""

import pytest
from unittest.mock import Mock, MagicMock
from pathlib import Path
import tempfile
import os


# ============================================================
# SEÇÃO 1: FIXTURES DE AMBIENTE
# ============================================================

@pytest.fixture
def temp_env_file():
    """
    FIXTURE: Arquivo .env Temporário

    O QUE FAZ:
        Cria arquivo .env temporário com variáveis fake.
        Após o teste, deleta automaticamente.

    POR QUE PRECISAMOS:
        - Isolar testes: cada teste tem seu próprio .env
        - Não poluir .env real do projeto
        - Testar diferentes configurações sem conflito

    COMO USAR:
        def test_carregar_env(temp_env_file):
            # temp_env_file é Path para .env temporário
            from src.core.env import carregar_env
            carregar_env()
            assert os.getenv('LANGFUSE_PUBLIC_KEY') == 'pk-test'

    TÉCNICA:
        - tempfile.NamedTemporaryFile: cria arquivo temporário
        - yield: pausa, roda teste, depois continua (cleanup)
        - .unlink(): deleta arquivo

    CONTEÚDO DO ARQUIVO:
        Variáveis fake mas com formato correto:
        - LANGFUSE_PUBLIC_KEY="pk-test"
        - LANGFUSE_SECRET_KEY="sk-test"
        - LANGFUSE_BASE_URL="https://test.langfuse.com"
        - OPENAI_API_KEY="sk-test-openai"
        - OPENAI_MODEL="gpt-4o-mini"

    📚 Conceitos: fixtures, isolamento de testes, cleanup automático
    """
    # Cria arquivo temporário com extensão .env
    with tempfile.NamedTemporaryFile(
        mode='w',        # modo escrita
        suffix='.env',   # extensão .env
        delete=False     # não deletar automaticamente (faremos manual)
    ) as f:
        # Escreve variáveis fake (formato real do .env)
        f.write('LANGFUSE_PUBLIC_KEY="pk-test"\n')
        f.write('LANGFUSE_SECRET_KEY="sk-test"\n')
        f.write('LANGFUSE_BASE_URL="https://test.langfuse.com"\n')
        f.write('OPENAI_API_KEY="sk-test-openai"\n')
        f.write('OPENAI_MODEL="gpt-4o-mini"\n')
        temp_path = Path(f.name)

    # YIELD: pausa aqui, roda o teste, depois volta para cleanup
    yield temp_path

    # CLEANUP: deleta arquivo após teste (roda sempre, mesmo se teste falhar)
    temp_path.unlink()


@pytest.fixture
def clean_env(monkeypatch):
    """
    FIXTURE: Limpa Variáveis de Ambiente

    O QUE FAZ:
        Remove variáveis de ambiente relacionadas ao projeto
        antes do teste para evitar interferência.

    POR QUE:
        Testes devem ser independentes.
        Se rodarmos testes com .env real carregado,
        os testes podem ser afetados por variáveis do ambiente.

    COMO USAR:
        def test_exigir_variaveis_ausentes(clean_env):
            # Ambiente limpo, variáveis não existem
            from src.core.env import exigir_variaveis
            with pytest.raises(RuntimeError):
                exigir_variaveis(['OPENAI_API_KEY'])

    TÉCNICA:
        - monkeypatch.delenv: remove variável do ambiente
        - raising=False: não dá erro se variável não existir

    VARIÁVEIS REMOVIDAS:
        - LANGFUSE_PUBLIC_KEY
        - LANGFUSE_SECRET_KEY
        - LANGFUSE_BASE_URL
        - OPENAI_API_KEY
        - OPENAI_MODEL

    📚 Conceito: Isolamento de testes, test independence
    """
    vars_to_clean = [
        'LANGFUSE_PUBLIC_KEY',
        'LANGFUSE_SECRET_KEY',
        'LANGFUSE_BASE_URL',
        'OPENAI_API_KEY',
        'OPENAI_MODEL'
    ]
    for var in vars_to_clean:
        monkeypatch.delenv(var, raising=False)
    yield


@pytest.fixture
def mock_env(monkeypatch):
    """
    FIXTURE: Define Variáveis de Ambiente Mockadas

    O QUE FAZ:
        Define variáveis fake no ambiente para testes.

    DIFERENÇA DE clean_env:
        - clean_env: REMOVE variáveis (ambiente vazio)
        - mock_env: DEFINE variáveis fake (ambiente populado)

    COMO USAR:
        def test_criar_client(mock_env):
            # Variáveis mockadas já estão definidas
            from src.core.clients import criar_openai_client
            client = criar_openai_client()
            assert client is not None

    VALORES MOCKADOS:
        - LANGFUSE_PUBLIC_KEY='pk-mock'
        - LANGFUSE_SECRET_KEY='sk-mock'
        - LANGFUSE_BASE_URL='https://mock.langfuse.com'
        - OPENAI_API_KEY='sk-mock-openai'
        - OPENAI_MODEL='gpt-4o-mini'

    📚 Conceito: Test fixtures, mocking de ambiente
    """
    monkeypatch.setenv('LANGFUSE_PUBLIC_KEY', 'pk-mock')
    monkeypatch.setenv('LANGFUSE_SECRET_KEY', 'sk-mock')
    monkeypatch.setenv('LANGFUSE_BASE_URL', 'https://mock.langfuse.com')
    monkeypatch.setenv('OPENAI_API_KEY', 'sk-mock-openai')
    monkeypatch.setenv('OPENAI_MODEL', 'gpt-4o-mini')
    yield


# ============================================================
# SEÇÃO 2: FIXTURES DE MOCKING - OPENAI
# ============================================================

@pytest.fixture
def mock_openai_response():
    """
    FIXTURE: Mock de Resposta do OpenAI

    O QUE FAZ:
        Cria objeto fake que simula resposta do GPT.

    ESTRUTURA DA RESPOSTA REAL:
        response = client.chat.completions.create(...)

        response.choices[0].message.content  # → "Texto da resposta"
        response.model                        # → "gpt-4"
        response.usage.prompt_tokens          # → 10
        response.usage.completion_tokens      # → 20
        response.usage.total_tokens           # → 30

    MOCK RETORNADO:
        Objeto Mock com mesma estrutura, mas valores fake.

    COMO USAR:
        def test_processar_resposta(mock_openai_response):
            # mock_openai_response já tem estrutura correta
            texto = mock_openai_response.choices[0].message.content
            assert texto == "Resposta mockada do GPT"

    CUSTOMIZAÇÃO:
        Se precisar de resposta diferente, pode modificar:

        def test_com_resposta_customizada(mock_openai_response):
            mock_openai_response.choices[0].message.content = "Customizada"
            assert processar(mock_openai_response) == "Customizada"

    📚 Conceito: Mock objects, data fixtures, test doubles
    """
    # Cria mock da resposta completa
    mock_response = Mock()

    # Estrutura de choices (lista de escolhas)
    mock_response.choices = [Mock()]
    mock_response.choices[0].message = Mock()
    mock_response.choices[0].message.content = "Resposta mockada do GPT"

    # Metadados da resposta
    mock_response.model = "gpt-4o-mini"

    # Informações de uso (tokens)
    mock_response.usage = Mock()
    mock_response.usage.prompt_tokens = 10
    mock_response.usage.completion_tokens = 20
    mock_response.usage.total_tokens = 30

    return mock_response


@pytest.fixture
def mock_openai_client(mocker, mock_openai_response):
    """
    FIXTURE: Mock do Cliente OpenAI

    O QUE FAZ:
        Substitui OpenAI real por versão fake que:
        - Não faz chamadas de rede
        - Retorna sempre mock_openai_response
        - Permite verificar se foi chamado

    POR QUE MOCKAR:
        - ⚡ Testes rápidos (sem latência de rede)
        - 💚 Testes grátis (não gasta créditos OpenAI)
        - 🎯 Testes determinísticos (mesma resposta sempre)
        - 🔌 Testes offline (funciona sem internet)

    COMO FUNCIONA:
        1. Cria MagicMock (objeto que aceita qualquer método)
        2. Configura .return_value para retornar resposta fake
        3. Substitui (patch) importação real por este mock

    COMO USAR:
        def test_gerar_resposta(mock_openai_client):
            # Chamadas para OpenAI usam o mock automaticamente
            from src.examples.basico import gerar_texto
            resposta = gerar_texto("teste")

            # Podemos verificar que foi chamado
            mock_openai_client.chat.completions.create.assert_called_once()

            # Podemos verificar argumentos
            args = mock_openai_client.chat.completions.create.call_args
            assert args.kwargs['model'] == 'gpt-4o-mini'

    TÉCNICA:
        - MagicMock: objeto fake que aceita qualquer chamada de método
        - mocker.patch: substitui import real por mock
        - .return_value: define o que o mock retorna quando chamado

    PATCH:
        Substitui 'langfuse.openai.OpenAI' (não 'openai.OpenAI')
        porque usamos o wrapper do Langfuse.

    📚 Conceito: Mocking, patches, MagicMock, test doubles
    📖 Releia: Capítulo 3 - Mocking
    """
    # Cria cliente mockado
    mock_client = MagicMock()

    # Configura o que retorna quando chamamos .create()
    mock_client.chat.completions.create.return_value = mock_openai_response

    # Substitui importação real pelo mock
    # Agora todo código que faz 'from langfuse.openai import OpenAI'
    # vai receber este mock ao chamar OpenAI()
    mocker.patch('langfuse.openai.OpenAI', return_value=mock_client)

    return mock_client


# ============================================================
# SEÇÃO 3: FIXTURES DE MOCKING - LANGFUSE
# ============================================================

@pytest.fixture
def mock_langfuse_client(mocker):
    """
    FIXTURE: Mock do Cliente Langfuse

    O QUE FAZ:
        Substitui Langfuse real por versão fake.

    MÉTODOS MOCKADOS:
        - get_current_trace_id() → retorna "trace-12345"
        - flush() → não faz nada (retorna None)
        - create_prompt() → retorna mock de prompt
        - get_prompt() → retorna mock de prompt

    COMO USAR:
        def test_obter_trace_id(mock_langfuse_client):
            from langfuse import get_client
            langfuse = get_client()
            trace_id = langfuse.get_current_trace_id()
            assert trace_id == "trace-12345"

    MOCK DE PROMPT:
        O mock de prompt tem:
        - .name = "test-prompt"
        - .version = 1
        - .compile() = "Prompt compilado: teste"

    USO COM PROMPTS:
        def test_usar_prompt(mock_langfuse_client):
            langfuse = get_client()
            prompt = langfuse.get_prompt("teste")
            assert prompt.name == "test-prompt"
            assert prompt.compile() == "Prompt compilado: teste"

    PATCHES:
        - langfuse.get_client → retorna mock_client
        - langfuse.Langfuse → retorna mock_client

    📚 Conceito: Mocking de APIs, test doubles, singleton mocking
    """
    # Cria cliente mockado
    mock_client = MagicMock()

    # Configura métodos comuns
    mock_client.get_current_trace_id.return_value = "trace-12345"
    mock_client.flush.return_value = None

    # Mock de prompt
    mock_prompt = Mock()
    mock_prompt.name = "test-prompt"
    mock_prompt.version = 1
    mock_prompt.compile.return_value = "Prompt compilado: teste"

    mock_client.create_prompt.return_value = mock_prompt
    mock_client.get_prompt.return_value = mock_prompt

    # Patch do get_client (singleton) e Langfuse (construtor)
    mocker.patch('langfuse.get_client', return_value=mock_client)
    mocker.patch('langfuse.Langfuse', return_value=mock_client)

    return mock_client


@pytest.fixture
def mock_observe_decorator(mocker):
    """
    FIXTURE: Mock do Decorator @observe

    O QUE FAZ:
        Substitui @observe por decorator "vazio" que não faz nada.

    POR QUE:
        @observe do Langfuse envia dados para API e rastreia execução.
        Em testes, queremos apenas testar nossa lógica,
        não o comportamento do Langfuse.

    COMO FUNCIONA:
        Cria decorator fake que retorna a função original sem modificar.

    COMO USAR:
        def test_funcao_com_observe(mock_observe_decorator):
            from langfuse.decorators import observe

            @observe()
            def minha_funcao():
                return "resultado"

            # @observe foi mockado, não faz nada
            assert minha_funcao() == "resultado"

    TÉCNICA:
        - Decorator pattern: função que retorna função
        - Function as first-class citizen
        - Nested functions

    IMPLEMENTAÇÃO:
        def fake_observe(*args, **kwargs):
            def decorator(func):
                return func  # Retorna função original sem modificar
            return decorator

    PATCHES:
        - langfuse.observe
        - langfuse.decorators.observe

    📚 Conceito: Decorators, mocking de decorators, identity function
    """
    def fake_observe(*args, **kwargs):
        """Decorator fake que não faz nada"""
        def decorator(func):
            # Retorna função original sem modificar
            return func
        return decorator

    # Patch do decorator @observe
    mocker.patch('langfuse.observe', side_effect=fake_observe)
    mocker.patch('langfuse.decorators.observe', side_effect=fake_observe)
    yield


@pytest.fixture
def mock_propagate_attributes(mocker):
    """
    FIXTURE: Mock do Context Manager propagate_attributes

    O QUE FAZ:
        Substitui propagate_attributes por context manager vazio.

    O QUE É propagate_attributes:
        Context manager do Langfuse que propaga atributos
        (como user_id) para traces filhos.

        Uso real:
            with propagate_attributes(user_id="123"):
                # traces aqui terão user_id="123"
                gerar_resposta()

    COMO FUNCIONA O MOCK:
        Context manager que não faz nada (yield vazio).

    COMO USAR:
        def test_com_propagacao(mock_propagate_attributes):
            from langfuse import propagate_attributes

            with propagate_attributes(user_id="123"):
                # propagate_attributes foi mockado
                resultado = processar()
                assert resultado == "ok"

    TÉCNICA:
        - Context manager (@contextmanager)
        - yield: entrada/saída do contexto

    IMPLEMENTAÇÃO:
        @contextmanager
        def fake_propagate(**kwargs):
            yield  # Entra e sai do contexto sem fazer nada

    PATCH:
        - langfuse.propagate_attributes

    📚 Conceito: Context managers, with statement, mocking context managers
    """
    from contextlib import contextmanager

    @contextmanager
    def fake_propagate(**kwargs):
        """Context manager fake que não faz nada"""
        yield  # Entra e sai do contexto sem fazer nada

    # Patch do context manager
    mocker.patch('langfuse.propagate_attributes', side_effect=fake_propagate)
    yield


# ============================================================
# SEÇÃO 4: FIXTURE COMPOSTA
# ============================================================

@pytest.fixture
def full_mock_setup(
    mock_env,
    mock_openai_client,
    mock_langfuse_client,
    mock_observe_decorator,
    mock_propagate_attributes
):
    """
    FIXTURE COMPOSTA: Configuração Completa de Mocks

    O QUE FAZ:
        Combina TODAS as fixtures de mocking em uma só.

    POR QUE:
        Em testes de integração, geralmente precisamos de todos os mocks.
        Em vez de listar 5 fixtures, usamos apenas esta.

    COMO USAR:
        def test_fluxo_completo(full_mock_setup):
            # Tudo está mockado:
            # - Variáveis de ambiente (mock_env)
            # - Cliente OpenAI (mock_openai_client)
            # - Cliente Langfuse (mock_langfuse_client)
            # - Decorator @observe (mock_observe_decorator)
            # - Context manager propagate_attributes

            from src.examples.basico import processar_pipeline
            resultado = processar_pipeline()
            assert resultado == "esperado"

    RETORNA:
        Dict com referências aos mocks principais:
        {
            'openai': mock_openai_client,
            'langfuse': mock_langfuse_client
        }

    EXEMPLO DE USO COM VERIFICAÇÃO:
        def test_verifica_chamadas(full_mock_setup):
            # Executar código
            processar()

            # Verificar que OpenAI foi chamado
            full_mock_setup['openai'].chat.completions.create.assert_called()

            # Verificar que Langfuse flush foi chamado
            full_mock_setup['langfuse'].flush.assert_called()

    📚 Conceito: Fixture composition, reusabilidade, integration testing
    """
    return {
        'openai': mock_openai_client,
        'langfuse': mock_langfuse_client
    }
```

### 7.3 Instruções de implementação

**Passo 1: Criar o arquivo**

```bash
cat > tests/conftest.py << 'EOF'
[Copiar TODO o código da seção 7.2 acima]
EOF
```

**Passo 2: Verificar sintaxe**

```bash
python -m py_compile tests/conftest.py
echo "✅ Sintaxe OK!"
```

**Passo 3: Testar que fixtures foram descobertas**

```bash
pytest --fixtures tests/ | grep "mock_openai_client"
# Deve mostrar a fixture mock_openai_client
```

**Passo 4: Testar uma fixture simples**

Crie teste rápido para validar:

```bash
cat > tests/test_fixtures.py << 'EOF'
"""Teste rápido para validar fixtures"""

def test_mock_env(mock_env):
    """Testa que mock_env define variáveis"""
    import os
    assert os.getenv('OPENAI_API_KEY') == 'sk-mock-openai'

def test_mock_openai_response(mock_openai_response):
    """Testa que mock de resposta tem estrutura correta"""
    assert mock_openai_response.choices[0].message.content == "Resposta mockada do GPT"
    assert mock_openai_response.model == "gpt-4o-mini"
    assert mock_openai_response.usage.total_tokens == 30

def test_full_mock_setup(full_mock_setup):
    """Testa que fixture composta retorna dict correto"""
    assert 'openai' in full_mock_setup
    assert 'langfuse' in full_mock_setup
EOF

# Rodar testes de validação
pytest tests/test_fixtures.py -v
```

**Saída esperada:**
```
tests/test_fixtures.py::test_mock_env PASSED
tests/test_fixtures.py::test_mock_openai_response PASSED
tests/test_fixtures.py::test_full_mock_setup PASSED

========== 3 passed in 0.05s ==========
```

### 7.4 Entendendo o que criamos

**Resumo das fixtures:**

| Fixture | O que faz | Quando usar |
|---------|-----------|-------------|
| `temp_env_file` | Cria .env temporário | Testar parsing de .env |
| `clean_env` | Remove variáveis do ambiente | Testar validação de vars ausentes |
| `mock_env` | Define variáveis fake | Testar código que usa env vars |
| `mock_openai_response` | Resposta fake do GPT | Testar processamento de resposta |
| `mock_openai_client` | Cliente OpenAI mockado | Testar chamadas OpenAI sem custo |
| `mock_langfuse_client` | Cliente Langfuse mockado | Testar uso de Langfuse sem API |
| `mock_observe_decorator` | Mock do @observe | Testar funções decoradas |
| `mock_propagate_attributes` | Mock do context manager | Testar propagação de atributos |
| `full_mock_setup` | Combina todos os mocks | Testes de integração |

---

**Recapitulando Capítulo 7:**

✅ Criamos `tests/conftest.py` completo com 9 fixtures
✅ Fixtures de ambiente (temp_env_file, clean_env, mock_env)
✅ Fixtures de mocking OpenAI (mock_openai_response, mock_openai_client)
✅ Fixtures de mocking Langfuse (mock_langfuse_client, mock_observe_decorator, mock_propagate_attributes)
✅ Fixture composta (full_mock_setup)
✅ Validamos que fixtures funcionam

**Próximo capítulo:** Escrever Testes — vamos criar testes unitários e de integração usando as fixtures.

---

## 📘 Capítulo 8: Escrever Testes

Agora vamos colocar tudo em prática! Você vai criar testes unitários e de integração usando as fixtures do Capítulo 7.

### 8.1 Testes Unitários - `test_env.py`

Vamos testar o módulo `src/core/env.py` de forma isolada.

**Arquivo:** `tests/unit/core/test_env.py`

```python
"""
Testes Unitários: Módulo core.env

OBJETIVO:
    Testar parsing de .env e validação de variáveis
    de forma isolada (sem arquivo real).

TÉCNICAS:
    - Fixtures temporárias (temp_env_file)
    - Monkeypatch (limpar/setar env)
    - Parametrização (@pytest.mark.parametrize)
    - Testes de exceção (pytest.raises)

CASOS DE TESTE:
    ✅ Arquivo .env válido
    ✅ Arquivo inexistente
    ✅ Parsing de aspas
    ✅ Ignorar comentários
    ✅ Variáveis obrigatórias presentes
    ✅ Variáveis obrigatórias ausentes
    ✅ Modelo padrão

📚 Conceitos: Testes unitários, AAA pattern, test isolation
"""

import pytest
import os
from pathlib import Path
from src.core.env import carregar_env, exigir_variaveis, modelo_padrao


def test_carregar_env_arquivo_valido(temp_env_file, clean_env, monkeypatch):
    """
    Testa carregamento de .env válido

    O QUE ESTAMOS TESTANDO:
        Que carregar_env() lê o arquivo e popula os.environ

    POR QUE TESTAR:
        É a função core do projeto. Se quebrar, tudo quebra.

    TÉCNICA:
        - temp_env_file: .env temporário com vars fake
        - clean_env: garante ambiente limpo
        - monkeypatch: ajusta ENV_FILE para apontar pro temporário

    AAA PATTERN APLICADO:
    """
    # ===== ARRANGE =====
    # Fazemos carregar_env() apontar para nosso .env temporário
    from src.core import env
    monkeypatch.setattr(env, 'ENV_FILE', temp_env_file)

    # Garantimos que ambiente está limpo (fixture clean_env)
    assert os.getenv('LANGFUSE_PUBLIC_KEY') is None

    # ===== ACT =====
    # Executamos a função que queremos testar
    carregar_env()

    # ===== ASSERT =====
    # Verificamos que variáveis foram carregadas
    assert os.getenv('LANGFUSE_PUBLIC_KEY') == 'pk-test'
    assert os.getenv('LANGFUSE_SECRET_KEY') == 'sk-test'
    assert os.getenv('OPENAI_API_KEY') == 'sk-test-openai'
    assert os.getenv('OPENAI_MODEL') == 'gpt-4o-mini'


def test_carregar_env_arquivo_inexistente(clean_env, monkeypatch):
    """
    Testa que carregar_env() não falha se .env não existe

    O QUE ESTAMOS TESTANDO:
        Comportamento quando .env não existe.
        Deve retornar sem erro (graceful degradation).

    POR QUE:
        Permite usar variáveis de ambiente do sistema
        (ex: em produção via Docker/K8s)
    """
    # ===== ARRANGE =====
    from src.core import env
    # Fazemos ENV_FILE apontar para arquivo que não existe
    monkeypatch.setattr(env, 'ENV_FILE', Path('/arquivo/que/nao/existe.env'))

    # ===== ACT =====
    # Não deve lançar exceção
    carregar_env()

    # ===== ASSERT =====
    # Ambiente continua vazio (sem erro)
    assert os.getenv('LANGFUSE_PUBLIC_KEY') is None


def test_exigir_variaveis_presentes(mock_env):
    """
    Testa validação quando todas as vars existem

    O QUE ESTAMOS TESTANDO:
        Que exigir_variaveis() não falha quando vars existem

    TÉCNICA:
        mock_env já define todas as vars necessárias
    """
    # ===== ACT & ASSERT =====
    # Não deve lançar exceção
    exigir_variaveis([
        'LANGFUSE_PUBLIC_KEY',
        'OPENAI_API_KEY'
    ])


def test_exigir_variaveis_ausentes(clean_env):
    """
    Testa validação quando vars obrigatórias faltam

    O QUE ESTAMOS TESTANDO:
        Que exigir_variaveis() lança RuntimeError se var falta

    TÉCNICA:
        - clean_env: garante que vars não existem
        - pytest.raises: captura exceção esperada
    """
    # ===== ARRANGE =====
    # clean_env já garantiu que vars não existem

    # ===== ACT & ASSERT =====
    # Deve lançar RuntimeError
    with pytest.raises(RuntimeError) as exc_info:
        exigir_variaveis(['OPENAI_API_KEY', 'LANGFUSE_PUBLIC_KEY'])

    # Verificamos a mensagem de erro
    erro = str(exc_info.value)
    assert 'OPENAI_API_KEY' in erro
    assert 'LANGFUSE_PUBLIC_KEY' in erro


def test_modelo_padrao_sem_env(clean_env):
    """
    Testa fallback quando OPENAI_MODEL não está definido

    O QUE ESTAMOS TESTANDO:
        Que modelo_padrao() retorna "gpt-4o-mini" por padrão
    """
    # ===== ACT =====
    modelo = modelo_padrao()

    # ===== ASSERT =====
    assert modelo == "gpt-4o-mini"


def test_modelo_padrao_com_env(monkeypatch):
    """
    Testa que modelo_padrao() respeita OPENAI_MODEL

    O QUE ESTAMOS TESTANDO:
        Que se OPENAI_MODEL está definido, usa esse valor
    """
    # ===== ARRANGE =====
    monkeypatch.setenv('OPENAI_MODEL', 'gpt-4')

    # ===== ACT =====
    modelo = modelo_padrao()

    # ===== ASSERT =====
    assert modelo == 'gpt-4'
```

**Instruções:**
```bash
cat > tests/unit/core/test_env.py << 'EOF'
[Copiar código acima]
EOF

# Rodar testes
pytest tests/unit/core/test_env.py -v
```

### 8.2 Testes Unitários - `test_clients.py`

**Arquivo:** `tests/unit/core/test_clients.py`

```python
"""Testes Unitários: Módulo core.clients"""

import pytest
from unittest.mock import Mock


def test_criar_openai_client(mock_env, mock_openai_client):
    """Testa factory de cliente OpenAI"""
    from src.core.clients import criar_openai_client

    # Act
    client = criar_openai_client()

    # Assert
    assert client is not None
    # Verifica que é o mock
    assert client == mock_openai_client


def test_criar_langfuse_client(mock_env, mock_langfuse_client):
    """Testa factory de cliente Langfuse"""
    from src.core.clients import criar_langfuse_client

    # Act
    client = criar_langfuse_client()

    # Assert
    assert client is not None
    assert client == mock_langfuse_client


def test_finalizar_langfuse(mock_langfuse_client):
    """Testa que finalizar_langfuse chama flush"""
    from src.core.clients import finalizar_langfuse

    # Act
    finalizar_langfuse()

    # Assert
    mock_langfuse_client.flush.assert_called_once()
```

**Instruções:**
```bash
cat > tests/unit/core/test_clients.py << 'EOF'
[Copiar código acima]
EOF

pytest tests/unit/core/test_clients.py -v
```

### 8.3 Testes Unitários - `test_error_handling.py`

**Arquivo:** `tests/unit/utils/test_error_handling.py`

```python
"""Testes Unitários: Módulo utils.error_handling"""

import pytest


def test_executar_seguro_sucesso():
    """Testa executar_seguro quando função sucede"""
    from src.utils.error_handling import executar_seguro

    # Arrange
    def funcao_sucesso():
        return 42

    # Act
    resultado = executar_seguro(funcao_sucesso)

    # Assert
    assert resultado == 42


def test_executar_seguro_falha():
    """Testa executar_seguro quando função falha"""
    from src.utils.error_handling import executar_seguro

    # Arrange
    def funcao_falha():
        raise ValueError("Erro proposital")

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        executar_seguro(funcao_falha)

    # Verifica código de saída
    assert exc_info.value.code == 1
```

**Instruções:**
```bash
cat > tests/unit/utils/test_error_handling.py << 'EOF'
[Copiar código acima]
EOF

pytest tests/unit/utils/test_error_handling.py -v
```

### 8.4 Teste de Integração Simples

**Arquivo:** `tests/integration/test_basic_flow.py`

```python
"""
Testes de Integração: Fluxo Básico

DIFERENÇA DE TESTE UNITÁRIO:
    - Unitário: testa função isolada
    - Integração: testa múltiplos módulos juntos

AINDA USA MOCKS:
    Sim! Mas testa integração entre NOSSOS módulos,
    ainda mockando APIs externas.
"""

import pytest


def test_fluxo_completo_carregar_env_e_criar_clients(full_mock_setup, temp_env_file, monkeypatch):
    """Testa fluxo: carregar .env → criar clients"""

    # Arrange
    from src.core import env
    monkeypatch.setattr(env, 'ENV_FILE', temp_env_file)

    # Act
    from src.core.env import carregar_env, exigir_variaveis
    from src.core.clients import criar_openai_client, criar_langfuse_client

    carregar_env()
    exigir_variaveis(['OPENAI_API_KEY', 'LANGFUSE_PUBLIC_KEY'])

    client_openai = criar_openai_client()
    client_langfuse = criar_langfuse_client()

    # Assert
    assert client_openai is not None
    assert client_langfuse is not None
```

**Instruções:**
```bash
cat > tests/integration/test_basic_flow.py << 'EOF'
[Copiar código acima]
EOF

pytest tests/integration/test_basic_flow.py -v
```

### 8.5 Rodar todos os testes

```bash
# Todos os testes
pytest -v

# Apenas unitários
pytest tests/unit/ -v

# Apenas integração
pytest tests/integration/ -v

# Com cobertura
pytest --cov=src --cov-report=term-missing

# Gerar relatório HTML
pytest --cov=src --cov-report=html
open htmlcov/index.html  # Mac
# ou
xdg-open htmlcov/index.html  # Linux
```

---

**Recapitulando Capítulo 8:**

✅ Criamos testes unitários para `src/core/env.py`
✅ Criamos testes unitários para `src/core/clients.py`
✅ Criamos testes unitários para `src/utils/error_handling.py`
✅ Criamos teste de integração básico
✅ Aprendemos a rodar testes de diferentes formas

**Próximo capítulo:** Medir Cobertura — vamos analisar cobertura de código e atingir 95%+.

---

## 📘 Capítulo 9: Medir Cobertura

### 9.1 O que é cobertura de testes?

**Definição:**
Cobertura de testes (code coverage) é a métrica que indica qual porcentagem do código é executada pelos testes.

**Tipos de cobertura:**

1. **Line Coverage (cobertura de linhas)**
   - % de linhas de código executadas
   - Mais comum e útil

2. **Branch Coverage (cobertura de branches)**
   - % de condições (if/else) testadas
   - Mais rigorosa

3. **Function Coverage**
   - % de funções chamadas

**Exemplo:**

```python
def calcular_desconto(preco, percentual):
    if percentual > 0:           # Linha 1
        return preco * percentual / 100  # Linha 2
    return 0                      # Linha 3

# Teste que cobre apenas linha 1 e 2:
def test_desconto_positivo():
    assert calcular_desconto(100, 10) == 10

# Cobertura: 66% (2 de 3 linhas)
# Linha 3 nunca foi executada!
```

### 9.2 Como medir com pytest-cov

**Comando básico:**
```bash
pytest --cov=src
```

**Com relatório detalhado:**
```bash
pytest --cov=src --cov-report=term-missing
```

**Saída exemplo:**
```
---------- coverage: platform darwin, python 3.10.8 -----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
src/__init__.py                   0      0   100%
src/core/__init__.py              0      0   100%
src/core/env.py                  25      2    92%   45-46
src/core/clients.py              10      0   100%
src/utils/__init__.py             0      0   100%
src/utils/error_handling.py      15      3    80%   23-25
-----------------------------------------------------------
TOTAL                            50      5    90%
```

**Interpretação:**
- **Stmts:** Total de statements (linhas executáveis)
- **Miss:** Statements não executados pelos testes
- **Cover:** Porcentagem de cobertura
- **Missing:** Números das linhas não cobertas

### 9.3 Interpretar relatório HTML

**Gerar relatório HTML:**
```bash
pytest --cov=src --cov-report=html
```

**Abrir no navegador:**
```bash
# Mac
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html

# Windows
start htmlcov/index.html
```

**O que você verá:**

1. **Índice (index.html)**
   - Lista todos os arquivos
   - % de cobertura de cada um
   - Clique para ver detalhes

2. **Arquivo individual (ex: src_core_env_py.html)**
   - Código fonte completo
   - Linhas cobertas: verde
   - Linhas não cobertas: vermelho
   - Linhas excluídas: cinza

**Exemplo visual:**
```
✅ Verde (coberta):
    def carregar_env():
        if not ENV_FILE.exists():
            return

❌ Vermelho (NÃO coberta):
        for linha in ENV_FILE.read_text().splitlines():
            # Esta parte nunca foi testada!
```

### 9.4 Meta de 95%: por quê?

**Por que 95% e não 100%?**

**100% é impraticável:**
- ❌ Código defensivo raro (ex: `except Exception:` que nunca acontece)
- ❌ Edge cases impossíveis de reproduzir
- ❌ Custo/benefício ruim (muito esforço para pouco ganho)

**95% é o sweet spot:**
- ✅ Cobre quase todo código crítico
- ✅ Deixa folga para casos edge
- ✅ Balanceamento custo/benefício

**Exceções comuns (não precisa cobrir):**

```python
# 1. Blocos de proteção impossíveis
try:
    processar()
except Exception:  # pragma: no cover
    # Este except nunca vai acontecer na prática
    log_erro_critico()

# 2. Código de desenvolvimento
if __name__ == "__main__":  # pragma: no cover
    main()

# 3. Imports condicionais
try:
    import módulo_opcional
except ImportError:  # pragma: no cover
    módulo_opcional = None
```

**Como usar `# pragma: no cover`:**

```python
def funcao_complexa():
    try:
        return processar_normal()
    except ErroEspecifico:
        return fallback()
    except Exception:  # pragma: no cover
        # Este branch é para segurança extrema, nunca testamos
        log_erro_critico()
        raise
```

### 9.5 Armadilhas: cobertura alta ≠ bons testes

**CUIDADO:** 100% de cobertura não significa que está tudo testado!

**Exemplo de teste ruim com 100% de cobertura:**

```python
# Código
def calcular_total(itens, desconto=0):
    subtotal = sum(itens)
    if desconto > 0:
        subtotal -= desconto
    if subtotal < 0:
        subtotal = 0
    return subtotal


# Teste RUIM (mas com 100% de cobertura!)
def test_calcular_total():
    calcular_total([10, 20], 5)  # Só executa, não verifica nada!
    # ❌ Nenhum assert!
    # ❌ Não testa casos edge
    # ❌ Não verifica resultado
```

**Teste BOM (mesmo com 100% de cobertura):**

```python
def test_calcular_total_sem_desconto():
    assert calcular_total([10, 20, 30]) == 60

def test_calcular_total_com_desconto():
    assert calcular_total([100, 50], desconto=30) == 120

def test_calcular_total_desconto_maior_que_total():
    # Edge case: desconto maior que subtotal
    assert calcular_total([10], desconto=20) == 0

def test_calcular_total_lista_vazia():
    assert calcular_total([]) == 0
```

**Lições:**
- ✅ Cobertura alta é necessária mas não suficiente
- ✅ Testes devem ter assertions (verificações)
- ✅ Testes devem cobrir casos edge
- ✅ Testes devem ser legíveis e documentar comportamento

### 9.6 Exemplo prático de análise

**Cenário:** Você roda `pytest --cov=src --cov-report=html` e vê:

```
src/core/env.py    85%   Missing: 45-50
```

**Passo 1:** Abrir htmlcov/src_core_env_py.html

**Passo 2:** Ver linhas vermelhas (não cobertas):

```python
45  def validar_formato_api_key(key: str) -> bool:
46      """Valida formato da API key"""
47      if not key or len(key) < 10:
48          return False
49      return key.startswith("sk-")
50      # Linhas 45-50 estão vermelhas!
```

**Passo 3:** Perceber que nenhum teste chama `validar_formato_api_key`

**Passo 4:** Criar teste:

```python
def test_validar_formato_api_key_valida():
    from src.core.env import validar_formato_api_key
    assert validar_formato_api_key("sk-123456789012") == True

def test_validar_formato_api_key_invalida():
    assert validar_formato_api_key("") == False
    assert validar_formato_api_key("abc") == False
    assert validar_formato_api_key("pk-123456789") == False  # Não começa com sk-
```

**Passo 5:** Rodar novamente:

```bash
pytest --cov=src --cov-report=html
```

**Resultado:**
```
src/core/env.py    100%   🎉
```

---

## 📘 Capítulo 10: Validação e Próximos Passos

### 10.1 Checklist completo

Antes de considerar seu projeto pronto, valide tudo:

#### ✅ Estrutura

```bash
# Verificar que diretórios existem
ls -la src/core src/utils tests/unit tests/integration

# Verificar __init__.py
find src/ tests/ -name "__init__.py"
```

#### ✅ Dependências

```bash
# Verificar instalação
pytest --version
coverage --version
ruff --version
```

#### ✅ Código refatorado

```bash
# Verificar que módulos importam
python -c "from src.core.env import carregar_env; print('✅ env.py OK')"
python -c "from src.core.clients import criar_openai_client; print('✅ clients.py OK')"
python -c "from src.utils.error_handling import executar_seguro; print('✅ error_handling.py OK')"
```

#### ✅ Testes escritos

```bash
# Contar testes
pytest --collect-only | grep "test session starts"

# Deve mostrar algo como:
# collected 15 items
```

#### ✅ Cobertura 95%+

```bash
# Verificar cobertura
pytest --cov=src --cov-report=term-missing --cov-fail-under=95
```

#### ✅ Linting sem erros

```bash
# Verificar código
ruff check src/ tests/

# Se houver erros, corrigir:
ruff check --fix src/ tests/
```

#### ✅ Type checking (opcional)

```bash
pyright src/
```

### 10.2 Comandos úteis

**Referência rápida:**

```bash
# === RODAR TESTES ===

# Todos, verbose
pytest -v

# Apenas unitários
pytest tests/unit/ -v

# Apenas integração
pytest tests/integration/ -v

# Parar no primeiro erro
pytest -x

# Rodar em paralelo (mais rápido)
pytest -n auto

# Rodar apenas testes que falharam na última vez
pytest --lf

# === COBERTURA ===

# Com relatório no terminal
pytest --cov=src --cov-report=term-missing

# Gerar HTML
pytest --cov=src --cov-report=html

# Falhar se < 95%
pytest --cov=src --cov-fail-under=95

# === LINTING ===

# Verificar código
ruff check src/ tests/

# Corrigir automaticamente
ruff check --fix src/ tests/

# Formatar código
ruff format src/ tests/

# === TYPE CHECKING ===

# Verificar tipos
pyright src/

# === LIMPAR ===

# Remover cache
rm -rf .pytest_cache __pycache__ htmlcov .coverage
find . -type d -name __pycache__ -exec rm -rf {} +
```

### 10.3 Próximos passos (opcional)

Após dominar o conteúdo deste guia, considere:

#### 1. CI/CD com GitHub Actions

Criar `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -r requirements-dev.txt
      - run: pytest --cov=src --cov-fail-under=95
      - run: ruff check src/ tests/
```

#### 2. Pre-commit hooks

Instalar pre-commit para rodar testes antes de cada commit:

```bash
pip install pre-commit

# Criar .pre-commit-config.yaml
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
      - id: ruff
        name: ruff
        entry: ruff check
        language: system
        types: [python]
EOF

# Ativar
pre-commit install
```

#### 3. Testes E2E (com APIs reais)

Criar testes que chamam APIs reais (rodar manualmente, não em CI):

```python
@pytest.mark.e2e
@pytest.mark.skip(reason="Testes E2E rodam apenas manualmente")
def test_openai_real():
    """Teste com API real do OpenAI"""
    from src.core.env import carregar_env
    from src.core.clients import criar_openai_client

    carregar_env()
    client = criar_openai_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Oi"}]
    )

    assert len(response.choices[0].message.content) > 0
```

#### 4. Documentação com Sphinx

Gerar documentação automática do código:

```bash
pip install sphinx sphinx-rtd-theme
sphinx-quickstart docs/
sphinx-apidoc -o docs/ src/
cd docs/ && make html
```

### 10.4 Recursos adicionais

**Documentação oficial:**
- [Pytest Docs](https://docs.pytest.org/)
- [Coverage.py](https://coverage.readthedocs.io/)
- [Python Testing (Real Python)](https://realpython.com/python-testing/)

**Livros:**
- "Test-Driven Development with Python" - Harry Percival
- "Python Testing with pytest" - Brian Okken

**Cursos:**
- [Test-Driven Development with Django](https://testdriven.io/courses/tdd-django/)
- [Testing in Python (Real Python)](https://realpython.com/learning-paths/testing-python/)

---

## 🎉 Conclusão

**Parabéns!** Você completou o guia de testes profissionais em Python.

**O que você aprendeu:**

✅ Fundamentos de testes (unitário, integração, E2E)
✅ Mocking (conceito central para testar código com APIs externas)
✅ Fixtures Pytest (setup reutilizável)
✅ Refatoração para testabilidade
✅ Escrever testes de qualidade
✅ Medir e interpretar cobertura de código
✅ Atingir 95%+ de cobertura

**Próximos passos:**

1. **Pratique:** Implemente tudo neste guia no seu projeto
2. **Experimente:** Crie novos testes para outros módulos
3. **Compartilhe:** Ensine estes conceitos para sua equipe
4. **Aprimore:** Explore CI/CD, pre-commit hooks, E2E tests

**Lembre-se:**

> "Código sem testes é código legado" - Michael Feathers

Testes não são opcional — são parte essencial de software profissional.

**Continue aprendendo!** 🚀

---

## Apêndice A: Referência Rápida

### Comandos essenciais

```bash
# Setup inicial
pip install -r requirements-dev.txt

# Rodar testes
pytest
pytest -v
pytest tests/unit/
pytest --cov=src --cov-report=html

# Linting
ruff check src/ tests/
ruff check --fix src/ tests/

# Type checking
pyright src/
```

### Estrutura de teste AAA

```python
def test_exemplo():
    # ARRANGE: preparar
    dados = criar_dados_teste()

    # ACT: executar
    resultado = funcao_a_testar(dados)

    # ASSERT: verificar
    assert resultado == esperado
```

### Fixtures úteis

```python
# Fixture básica
@pytest.fixture
def dados():
    return {"key": "value"}

# Fixture com cleanup
@pytest.fixture
def recurso():
    r = criar_recurso()
    yield r
    r.cleanup()

# Fixture parametrizada
@pytest.fixture(params=["a", "b", "c"])
def letra(request):
    return request.param
```

### Assertions comuns

```python
# Igualdade
assert resultado == esperado

# Verdadeiro/Falso
assert condicao
assert not condicao

# Pertence
assert item in lista
assert key in dicionario

# Exceção
with pytest.raises(ValueError):
    funcao_que_falha()

# Aproximadamente igual (floats)
assert abs(resultado - esperado) < 0.001
```

---

**Fim do Guia Completo: Testes Profissionais em Python para Langfuse**

**Versão:** 1.0
**Data:** Abril 2026
**Páginas:** ~80
**Tempo estimado de implementação:** 14-19 horas

