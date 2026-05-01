#!/usr/bin/env python3
"""
Script de Validação: Guia Completo de Testes

PROPÓSITO:
    Valida que você implementou corretamente o guia de testes.
    Verifica estrutura, arquivos, imports e testes.

USO:
    python validar_implementacao.py

SAÍDA:
    ✅ Verde: OK
    ❌ Vermelho: Precisa corrigir
    ⚠️  Amarelo: Opcional mas recomendado
"""

import sys
from pathlib import Path
import subprocess


class Colors:
    """Cores ANSI para terminal"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_header(texto):
    """Imprime cabeçalho de seção"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{texto}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")


def check(condicao, mensagem_ok, mensagem_erro):
    """
    Verifica condição e imprime resultado

    Args:
        condicao: True se OK, False se erro
        mensagem_ok: Mensagem se passou
        mensagem_erro: Mensagem se falhou

    Returns:
        True se passou, False se falhou
    """
    if condicao:
        print(f"{Colors.GREEN}✅ {mensagem_ok}{Colors.END}")
        return True
    else:
        print(f"{Colors.RED}❌ {mensagem_erro}{Colors.END}")
        return False


def check_warning(condicao, mensagem_ok, mensagem_aviso):
    """Verifica condição opcional (warning)"""
    if condicao:
        print(f"{Colors.GREEN}✅ {mensagem_ok}{Colors.END}")
    else:
        print(f"{Colors.YELLOW}⚠️  {mensagem_aviso}{Colors.END}")


def check_directory_structure():
    """Valida estrutura de diretórios"""
    print_header("1. Estrutura de Diretórios")

    checks = []

    # Diretórios principais
    diretorios = [
        ("src/", "Diretório src/ existe"),
        ("src/core/", "Diretório src/core/ existe"),
        ("src/utils/", "Diretório src/utils/ existe"),
        ("tests/", "Diretório tests/ existe"),
        ("tests/unit/", "Diretório tests/unit/ existe"),
        ("tests/unit/core/", "Diretório tests/unit/core/ existe"),
        ("tests/unit/utils/", "Diretório tests/unit/utils/ existe"),
        ("tests/integration/", "Diretório tests/integration/ existe"),
    ]

    for dir_path, msg in diretorios:
        checks.append(check(
            Path(dir_path).exists(),
            msg,
            f"Diretório {dir_path} NÃO existe. Execute: mkdir -p {dir_path}"
        ))

    return all(checks)


def check_init_files():
    """Valida arquivos __init__.py"""
    print_header("2. Arquivos __init__.py")

    checks = []

    init_files = [
        "src/__init__.py",
        "src/core/__init__.py",
        "src/utils/__init__.py",
        "tests/__init__.py",
        "tests/unit/__init__.py",
        "tests/unit/core/__init__.py",
        "tests/unit/utils/__init__.py",
        "tests/integration/__init__.py",
    ]

    for init_file in init_files:
        checks.append(check(
            Path(init_file).exists(),
            f"{init_file} existe",
            f"{init_file} NÃO existe. Execute: touch {init_file}"
        ))

    return all(checks)


def check_source_modules():
    """Valida módulos de código fonte"""
    print_header("3. Módulos de Código Fonte")

    checks = []

    # Verificar arquivos existem
    modulos = [
        ("src/core/env.py", "Módulo env.py", ["carregar_env", "exigir_variaveis", "modelo_padrao"]),
        ("src/core/clients.py", "Módulo clients.py", ["criar_openai_client", "criar_langfuse_client", "finalizar_langfuse"]),
        ("src/utils/error_handling.py", "Módulo error_handling.py", ["executar_seguro"]),
    ]

    for arquivo, nome, funcoes in modulos:
        path = Path(arquivo)
        checks.append(check(
            path.exists(),
            f"{nome} existe",
            f"{nome} NÃO existe. Veja Capítulo 6 do guia."
        ))

        if path.exists():
            # Verificar se funções existem no arquivo
            conteudo = path.read_text()
            for funcao in funcoes:
                checks.append(check(
                    f"def {funcao}" in conteudo,
                    f"  └─ Função {funcao}() existe",
                    f"  └─ Função {funcao}() NÃO existe"
                ))

    return all(checks)


def check_test_files():
    """Valida arquivos de teste"""
    print_header("4. Arquivos de Teste")

    checks = []

    # conftest.py
    conftest = Path("tests/conftest.py")
    checks.append(check(
        conftest.exists(),
        "tests/conftest.py existe",
        "tests/conftest.py NÃO existe. Veja Capítulo 7 do guia."
    ))

    if conftest.exists():
        conteudo = conftest.read_text()
        fixtures_esperadas = [
            "temp_env_file",
            "clean_env",
            "mock_env",
            "mock_openai_response",
            "mock_openai_client",
            "mock_langfuse_client",
            "mock_observe_decorator",
            "mock_propagate_attributes",
            "full_mock_setup",
        ]

        for fixture in fixtures_esperadas:
            checks.append(check(
                f"def {fixture}" in conteudo,
                f"  └─ Fixture {fixture} existe",
                f"  └─ Fixture {fixture} NÃO existe"
            ))

    # Arquivos de teste
    test_files = [
        ("tests/unit/core/test_env.py", "Testes de env.py"),
        ("tests/unit/core/test_clients.py", "Testes de clients.py"),
        ("tests/unit/utils/test_error_handling.py", "Testes de error_handling.py"),
    ]

    for arquivo, nome in test_files:
        path = Path(arquivo)
        checks.append(check(
            path.exists(),
            f"{nome} existe",
            f"{nome} NÃO existe. Veja Capítulo 8 do guia."
        ))

    return all(checks)


def check_config_files():
    """Valida arquivos de configuração"""
    print_header("5. Arquivos de Configuração")

    checks = []

    # pyproject.toml
    pyproject = Path("pyproject.toml")
    checks.append(check(
        pyproject.exists(),
        "pyproject.toml existe",
        "pyproject.toml NÃO existe. Veja Capítulo 5 do guia."
    ))

    if pyproject.exists():
        conteudo = pyproject.read_text()
        checks.append(check(
            "[tool.pytest.ini_options]" in conteudo,
            "  └─ Configuração pytest existe",
            "  └─ Configuração pytest NÃO existe"
        ))
        checks.append(check(
            "[tool.coverage" in conteudo,
            "  └─ Configuração coverage existe",
            "  └─ Configuração coverage NÃO existe"
        ))

    # .gitignore
    gitignore = Path(".gitignore")
    check_warning(
        gitignore.exists(),
        ".gitignore existe",
        ".gitignore NÃO existe (opcional mas recomendado)"
    )

    # .env
    env_file = Path(".env")
    check_warning(
        env_file.exists(),
        ".env existe",
        ".env NÃO existe (necessário para rodar scripts reais, não para testes)"
    )

    return all(checks)


def check_dependencies():
    """Valida dependências instaladas"""
    print_header("6. Dependências Python")

    checks = []

    dependencias = [
        ("pytest", "pytest"),
        ("pytest-cov", "pytest_cov"),
        ("pytest-mock", "pytest_mock"),
    ]

    for nome, modulo in dependencias:
        try:
            __import__(modulo)
            checks.append(check(
                True,
                f"{nome} instalado",
                ""
            ))
        except ImportError:
            checks.append(check(
                False,
                "",
                f"{nome} NÃO instalado. Execute: pip install {nome}"
            ))

    return all(checks)


def run_imports():
    """Tenta importar módulos para verificar sintaxe"""
    print_header("7. Validação de Imports")

    checks = []

    imports = [
        ("from src.core.env import carregar_env", "Importar carregar_env"),
        ("from src.core.clients import criar_openai_client", "Importar criar_openai_client"),
        ("from src.utils.error_handling import executar_seguro", "Importar executar_seguro"),
    ]

    for import_str, descricao in imports:
        try:
            exec(import_str)
            checks.append(check(True, descricao, ""))
        except Exception as e:
            checks.append(check(
                False,
                "",
                f"{descricao} FALHOU: {e}"
            ))

    return all(checks)


def run_pytest():
    """Roda pytest e verifica resultado"""
    print_header("8. Executar Testes")

    try:
        # Rodar pytest
        result = subprocess.run(
            ["pytest", "--collect-only", "-q"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            # Contar testes coletados
            output = result.stdout
            if "no tests ran" in output.lower():
                check(
                    False,
                    "",
                    "Nenhum teste encontrado. Você criou os testes?"
                )
                return False
            else:
                # Extrair número de testes
                linhas = output.split('\n')
                for linha in linhas:
                    if 'selected' in linha or 'collected' in linha:
                        check(True, f"Testes coletados: {linha.strip()}", "")
                        return True

                check(True, "Testes foram coletados com sucesso", "")
                return True
        else:
            check(
                False,
                "",
                f"Pytest falhou ao coletar testes:\n{result.stderr}"
            )
            return False

    except FileNotFoundError:
        check(
            False,
            "",
            "pytest não encontrado. Execute: pip install pytest"
        )
        return False
    except subprocess.TimeoutExpired:
        check(
            False,
            "",
            "Pytest demorou muito. Há algo errado?"
        )
        return False


def print_summary(resultados):
    """Imprime resumo final"""
    print_header("Resumo da Validação")

    total = len(resultados)
    passou = sum(resultados)
    falhou = total - passou

    percentual = (passou / total * 100) if total > 0 else 0

    print(f"Total de verificações: {total}")
    print(f"{Colors.GREEN}✅ Passou: {passou}{Colors.END}")
    if falhou > 0:
        print(f"{Colors.RED}❌ Falhou: {falhou}{Colors.END}")
    print(f"\nPercentual: {percentual:.1f}%")

    if percentual >= 95:
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 PARABÉNS! Implementação completa!{Colors.END}")
        print(f"{Colors.GREEN}Você pode rodar: pytest --cov=src{Colors.END}")
        return 0
    elif percentual >= 70:
        print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠️  Quase lá! Faltam alguns itens.{Colors.END}")
        print(f"{Colors.YELLOW}Revise os itens marcados com ❌ acima.{Colors.END}")
        return 1
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ Ainda há muito a fazer.{Colors.END}")
        print(f"{Colors.RED}Siga o guia passo a passo (guia-completo-testes-langfuse.md){Colors.END}")
        return 1


def main():
    """Função principal"""
    print(f"\n{Colors.BOLD}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}Validação de Implementação - Guia de Testes{Colors.END}")
    print(f"{Colors.BOLD}{'='*60}{Colors.END}")

    resultados = []

    # Executar verificações
    resultados.append(check_directory_structure())
    resultados.append(check_init_files())
    resultados.append(check_source_modules())
    resultados.append(check_test_files())
    resultados.append(check_config_files())
    resultados.append(check_dependencies())
    resultados.append(run_imports())
    resultados.append(run_pytest())

    # Resumo
    exit_code = print_summary(resultados)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
