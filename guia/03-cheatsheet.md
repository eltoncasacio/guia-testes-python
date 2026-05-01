# 📝 Cheatsheet: Testes em Python

Referência rápida para consulta durante desenvolvimento.

---

## 🚀 Comandos Essenciais

### Rodar Testes

```bash
# Todos os testes
pytest

# Verbose (mostra cada teste)
pytest -v

# Apenas unitários
pytest tests/unit/

# Apenas integração
pytest tests/integration/

# Arquivo específico
pytest tests/unit/core/test_env.py

# Teste específico
pytest tests/unit/core/test_env.py::test_carregar_env_arquivo_valido

# Parar no primeiro erro
pytest -x

# Modo quiet (menos output)
pytest -q

# Mostrar print statements
pytest -s

# Rodar em paralelo
pytest -n auto

# Rodar apenas testes que falharam
pytest --lf

# Rodar testes que falharam primeiro
pytest --ff
```

### Cobertura

```bash
# Cobertura no terminal
pytest --cov=src

# Com linhas faltando
pytest --cov=src --cov-report=term-missing

# Gerar HTML
pytest --cov=src --cov-report=html
open htmlcov/index.html

# Falhar se < 95%
pytest --cov=src --cov-fail-under=95

# Omitir arquivo da cobertura
pytest --cov=src --cov-report=term-missing --cov-omit="*/tests/*"
```

### Linting

```bash
# Verificar código
ruff check src/ tests/

# Corrigir automaticamente
ruff check --fix src/ tests/

# Formatar código
ruff format src/ tests/
```

---

## 📐 Estrutura de Teste (AAA Pattern)

```python
def test_exemplo():
    # ===== ARRANGE (Preparar) =====
    # Setup: preparar dados, mocks, estado inicial
    dados = {"key": "value"}
    esperado = "resultado esperado"

    # ===== ACT (Agir) =====
    # Executar a função/método que está sendo testado
    resultado = funcao_a_testar(dados)

    # ===== ASSERT (Verificar) =====
    # Verificar que resultado é o esperado
    assert resultado == esperado
```

---

## ✅ Assertions Comuns

```python
# Igualdade
assert x == y
assert x != y

# Identidade
assert x is y
assert x is not y

# Verdadeiro/Falso
assert x
assert not x
assert x is True
assert x is False

# Comparação
assert x > y
assert x >= y
assert x < y
assert x <= y

# Pertencimento
assert x in lista
assert x not in lista
assert key in dicionario

# Tipo
assert isinstance(x, str)
assert type(x) is int

# None
assert x is None
assert x is not None

# Strings
assert "substring" in texto
assert texto.startswith("prefix")
assert texto.endswith("suffix")

# Listas/Tuplas
assert len(lista) == 3
assert lista[0] == primeiro_elemento

# Aproximadamente igual (floats)
assert abs(x - y) < 0.001
```

---

## 🎭 Pytest Assertions Especiais

```python
import pytest

# Exceções
with pytest.raises(ValueError):
    funcao_que_lanca_erro()

# Exceção com mensagem específica
with pytest.raises(ValueError, match="mensagem esperada"):
    funcao_que_lanca_erro()

# Capturar exceção para inspecionar
with pytest.raises(ValueError) as exc_info:
    funcao_que_lanca_erro()
assert "detalhe" in str(exc_info.value)

# Warnings
with pytest.warns(UserWarning):
    funcao_que_gera_warning()

# Deprecation
with pytest.deprecated_call():
    funcao_depreciada()
```

---

## 🔧 Fixtures

### Fixture Básica

```python
@pytest.fixture
def dados():
    """Fixture que retorna dados"""
    return {"key": "value"}

# Usar
def test_algo(dados):
    assert dados["key"] == "value"
```

### Fixture com Setup e Cleanup

```python
@pytest.fixture
def recurso():
    """Fixture com setup e teardown"""
    # Setup
    recurso = criar_recurso()

    yield recurso  # Fornece para o teste

    # Cleanup (sempre roda, mesmo se teste falhar)
    recurso.close()
```

### Fixture Parametrizada

```python
@pytest.fixture(params=["a", "b", "c"])
def letra(request):
    """Roda teste 3x, uma para cada letra"""
    return request.param

def test_com_letras(letra):
    # Roda 3x: letra="a", letra="b", letra="c"
    assert len(letra) == 1
```

### Escopos de Fixture

```python
@pytest.fixture(scope="function")  # Padrão, 1x por teste
def func_scope():
    return "função"

@pytest.fixture(scope="class")  # 1x por classe
def class_scope():
    return "classe"

@pytest.fixture(scope="module")  # 1x por arquivo
def module_scope():
    return "módulo"

@pytest.fixture(scope="session")  # 1x por sessão inteira
def session_scope():
    return "sessão"
```

---

## 🎭 Mocking com pytest-mock

### Mock Básico

```python
def test_com_mock(mocker):
    # Criar mock
    mock_obj = mocker.Mock()

    # Configurar retorno
    mock_obj.metodo.return_value = 42

    # Usar
    resultado = mock_obj.metodo()
    assert resultado == 42

    # Verificar chamada
    mock_obj.metodo.assert_called_once()
```

### Patch de Função

```python
def test_patch_funcao(mocker):
    # Substituir função por mock
    mock_funcao = mocker.patch('modulo.funcao')
    mock_funcao.return_value = "mockado"

    # Usar
    from modulo import funcao
    resultado = funcao()

    assert resultado == "mockado"
    mock_funcao.assert_called_once()
```

### Patch de Método de Classe

```python
def test_patch_metodo(mocker):
    # Substituir método
    mocker.patch('modulo.Classe.metodo', return_value="mock")

    # Usar
    obj = Classe()
    resultado = obj.metodo()

    assert resultado == "mock"
```

### Mock com Side Effect

```python
def test_side_effect(mocker):
    # Lançar exceção
    mock = mocker.Mock(side_effect=ValueError("erro"))

    with pytest.raises(ValueError):
        mock()

    # Retornar valores diferentes
    mock = mocker.Mock(side_effect=[1, 2, 3])
    assert mock() == 1
    assert mock() == 2
    assert mock() == 3
```

### Verificar Chamadas

```python
def test_verificar_chamadas(mocker):
    mock = mocker.Mock()

    mock.metodo(1, 2, key="value")

    # Foi chamado?
    mock.metodo.assert_called()
    mock.metodo.assert_called_once()

    # Com argumentos específicos?
    mock.metodo.assert_called_with(1, 2, key="value")
    mock.metodo.assert_called_once_with(1, 2, key="value")

    # Quantas vezes?
    assert mock.metodo.call_count == 1

    # Nunca chamado?
    mock.outro_metodo.assert_not_called()
```

---

## 🌍 Mocking de Ambiente

```python
def test_env_var(monkeypatch):
    # Definir variável
    monkeypatch.setenv('API_KEY', 'test-key')
    assert os.getenv('API_KEY') == 'test-key'

    # Remover variável
    monkeypatch.delenv('API_KEY', raising=False)
    assert os.getenv('API_KEY') is None

    # Modificar sys.path
    monkeypatch.syspath_prepend('/caminho')
```

---

## 🎯 Markers

```python
# Marcar teste
@pytest.mark.slow
def test_demorado():
    pass

@pytest.mark.integration
def test_integracao():
    pass

# Pular teste
@pytest.mark.skip(reason="Não implementado ainda")
def test_futuro():
    pass

# Pular condicionalmente
@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requer Python 3.10+")
def test_python310():
    pass

# Marcar como esperado falhar
@pytest.mark.xfail(reason="Bug conhecido #123")
def test_com_bug():
    pass

# Rodar apenas testes marcados
# pytest -m slow
# pytest -m "not slow"
# pytest -m "integration and not slow"
```

---

## 📊 Parametrização

```python
# Parametrizar teste
@pytest.mark.parametrize("entrada,esperado", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_dobro(entrada, esperado):
    assert entrada * 2 == esperado

# Múltiplos parâmetros
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_produto(x, y):
    # Roda 6x: todas combinações de x e y
    assert x * y == x * y
```

---

## 📁 Fixtures Úteis Built-in

```python
def test_tmp_path(tmp_path):
    """Diretório temporário (Path)"""
    arquivo = tmp_path / "teste.txt"
    arquivo.write_text("conteúdo")
    assert arquivo.read_text() == "conteúdo"

def test_tmp_path_factory(tmp_path_factory):
    """Factory de diretórios temporários"""
    dir1 = tmp_path_factory.mktemp("dir1")
    dir2 = tmp_path_factory.mktemp("dir2")

def test_capsys(capsys):
    """Capturar stdout/stderr"""
    print("teste")
    captured = capsys.readouterr()
    assert "teste" in captured.out

def test_monkeypatch(monkeypatch):
    """Modificar objetos temporariamente"""
    monkeypatch.setattr('sys.platform', 'linux')
    monkeypatch.setenv('HOME', '/fake/home')

def test_request(request):
    """Informações sobre teste/fixture"""
    print(request.node.name)  # Nome do teste
    print(request.config)     # Config do pytest
```

---

## 🔍 Debugging

```python
# Adicionar breakpoint
def test_debug():
    x = calcular()
    breakpoint()  # Pausa aqui (Python 3.7+)
    assert x == 42

# Rodar com debugger
# pytest --pdb  # Para no primeiro erro
# pytest --pdbcls=IPython.terminal.debugger:Pdb  # Usa IPdb

# Comandos do pdb
# n (next)       - Próxima linha
# s (step)       - Entrar na função
# c (continue)   - Continuar até próximo breakpoint
# l (list)       - Mostrar código
# p variavel     - Imprimir variável
# q (quit)       - Sair
```

---

## 📦 Organização de Testes

```
tests/
├── conftest.py          # Fixtures compartilhadas
├── unit/                # Testes unitários
│   ├── conftest.py      # Fixtures para unitários
│   ├── core/
│   │   └── test_*.py
│   └── utils/
│       └── test_*.py
└── integration/         # Testes de integração
    ├── conftest.py      # Fixtures para integração
    └── test_*.py
```

---

## ⚙️ Configuração pytest.ini / pyproject.toml

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "-v",
    "--strict-markers",
    "--cov=src",
    "--cov-report=term-missing",
]
markers = [
    "slow: marca testes lentos",
    "integration: testes de integração",
]
```

---

## 🎨 Boas Práticas

### ✅ FAÇA

```python
# Nome descritivo
def test_calcular_desconto_com_percentual_valido():
    pass

# Uma coisa por teste
def test_criar_usuario():
    # Testa APENAS criação
    pass

# Arrange-Act-Assert claro
def test_exemplo():
    # Arrange
    dados = preparar()
    # Act
    resultado = processar(dados)
    # Assert
    assert resultado == esperado

# Teste isolado (sem dependências)
def test_independente():
    # Não depende de outros testes
    # Sempre funciona sozinho
    pass
```

### ❌ NÃO FAÇA

```python
# Nome vago
def test_usuario():  # ❌ Testa o que?
    pass

# Múltiplas coisas
def test_usuario_completo():  # ❌ Testa tudo
    criar()
    editar()
    deletar()

# Sem assertions
def test_sem_verificacao():  # ❌ Não verifica nada
    processar_dados()
    # Faltou assert!

# Testes dependentes
def test_primeiro():  # ❌ Dependência
    global dados
    dados = criar()

def test_segundo():  # ❌ Depende do anterior
    assert dados.id == 1
```

---

## 📚 Recursos Rápidos

- [Pytest Docs](https://docs.pytest.org/)
- [Pytest Cheatsheet](https://gist.github.com/kwmiebach/3fd49612ef7a52b5ce3a)
- [Python Testing](https://realpython.com/python-testing/)

---

**Guia Completo:** `guia-completo-testes-langfuse.md`
**Validação:** `python validar_implementacao.py`
