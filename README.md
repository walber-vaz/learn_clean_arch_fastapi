# Projeto FastAPI com Clean Architecture

Uma aplicação web moderna construída com FastAPI, SQLModel e princípios de Clean Architecture.

## Visão Geral da Arquitetura

Este projeto segue os princípios da Clean Architecture para manter a separação de responsabilidades e garantir testabilidade e manutenibilidade.

```
┌─────────────────────────────────────────────────────────┐
│                     Camada de Apresentação              │
│                                                         │
│  ┌─────────────────┐          ┌───────────────────┐     │
│  │   Controllers   │          │      Schemas      │     │
│  └─────────────────┘          └───────────────────┘     │
└───────────────────────────────────────────────────┬─────┘
                                                    │
                                                    ▼
┌─────────────────────────────────────────────────────────┐
│                     Camada de Use Cases                 │
│                                                         │
│  ┌─────────────────┐    ┌──────────────────────┐        │
│  │   Casos de Uso  │    │  Interface de Casos  │        │
│  └─────────────────┘    │        de Uso        │        │
│                         └──────────────────────┘        │
└───────────────────────────────────────────────────┬─────┘
                                                    │
                                                    ▼
┌─────────────────────────────────────────────────────────┐
│                     Camada de Domínio                   │
│                                                         │
│  ┌─────────────────┐    ┌───────────────┐               │
│  │    Entidades    │    │ Interfaces de │               │
│  └─────────────────┘    │  Repositório  │               │
│                         └───────────────┘               │
│                                                         │
└──────────────────────────────┬──────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────┐
│                  Camada de Infraestrutura               │
│                                                         │
│  ┌─────────────────┐    ┌───────────────────────┐       │
│  │  Configuração   │    │   Implementações de   │       │
│  │   do Banco      │    │      Repositório      │       │
│  └─────────────────┘    └───────────────────────┘       │
│                                                         │
│  ┌─────────────────────────────────────────────┐        │
│  │               Dependências                  │        │
│  └─────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────┘
```

### Test coverage

Os estão em desenvolvimento, mas já é possível ver a cobertura de testes.

```
All checks passed!
================ test session starts =================
platform linux -- Python 3.13.2, pytest-8.3.4, pluggy-1.5.0
cachedir: .pytest_cache
configfile: pyproject.toml
testpaths: tests
plugins: order-1.3.0, anyio-4.8.0, cov-6.0.0, asyncio-0.25.3
asyncio: mode=Mode.AUTO, asyncio_default_fixture_loop_scope=session
collected 38 items

tests/unit/infrastructure/repositories/test_sqlmodel_user_repository.py::test_create_user PASSED
tests/unit/presentation/controllers/test_create_user_user_controller.py::test_create_user_endpoint PASSED
tests/unit/presentation/controllers/test_get_user_user_controller.py::test_get_user_success PASSED
tests/unit/presentation/controllers/test_list_users_user_controller.py::test_list_users_endpoint PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_create_request_valid_data PASSED
tests/unit/use_cases/user/test_create_user.py::test_create_user_use_case_success PASSED
tests/unit/use_cases/user/test_get_user.py::test_get_user_use_case_success PASSED
tests/unit/use_cases/user/test_list_users.py::test_list_users_use_case_success PASSED
tests/unit/infrastructure/repositories/test_sqlmodel_user_repository.py::test_find_by_email PASSED
tests/unit/presentation/controllers/test_create_user_user_controller.py::test_create_user_endpoint_value_error PASSED
tests/unit/presentation/controllers/test_get_user_user_controller.py::test_get_user_not_found PASSED
tests/unit/presentation/controllers/test_list_users_user_controller.py::test_list_users_empty PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_create_request_invalid_name_characters PASSED
tests/unit/use_cases/user/test_create_user.py::test_create_user_use_case_email_already_exists PASSED
tests/unit/use_cases/user/test_get_user.py::test_get_user_use_case_user_not_found PASSED
tests/unit/use_cases/user/test_list_users.py::test_list_users_use_case_empty_result PASSED
tests/unit/infrastructure/repositories/test_sqlmodel_user_repository.py::test_list_users PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_create_request_short_name PASSED
tests/unit/use_cases/user/test_list_users.py::test_list_users_use_case_exact_page_size PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_create_request_short_password PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_create_request_password_no_uppercase PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_create_request_password_no_digit PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_create_request_password_no_special_character PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_empty PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_name_only PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_email_only PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_password_only PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_all_fields PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_invalid_name_characters PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_short_name PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_name_capitalization PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_invalid_email PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_short_password PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_password_no_uppercase PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_password_no_digit PASSED
tests/unit/presentation/schemas/user/test_request.py::test_user_update_request_password_no_special_character PASSED
tests/unit/domain/entities/test_user.py::test_user_entities_creation PASSED
tests/unit/infrastructure/security/test_password.py::test_password_hash PASSED

---------- coverage: platform linux, python 3.13.2-final-0 -----------
Name                                                              Stmts   Miss  Cover
-------------------------------------------------------------------------------------
src/app/__init__.py                                                   0      0   100%
src/app/constants.py                                                 12      0   100%
src/app/domain/__init__.py                                            0      0   100%
src/app/domain/entities/__init__.py                                   3      0   100%
src/app/domain/entities/user.py                                      14      0   100%
src/app/domain/repositories/__init__.py                               0      0   100%
src/app/domain/repositories/user_repository.py                       13      0   100%
src/app/infrastructure/__init__.py                                    0      0   100%
src/app/infrastructure/config/__init__.py                             0      0   100%
src/app/infrastructure/config/database.py                            12      3    75%
src/app/infrastructure/config/settings.py                             8      0   100%
src/app/infrastructure/dependencies/__init__.py                       0      0   100%
src/app/infrastructure/dependencies/user_dependencies.py             11      0   100%
src/app/infrastructure/repositories/__init__.py                       0      0   100%
src/app/infrastructure/repositories/sqlmodel_user_repository.py      26      0   100%
src/app/infrastructure/security/__init__.py                           0      0   100%
src/app/infrastructure/security/password.py                           6      0   100%
src/app/main.py                                                       5      0   100%
src/app/presentation/__init__.py                                      0      0   100%
src/app/presentation/controllers/__init__.py                          0      0   100%
src/app/presentation/controllers/user_controller.py                  30      0   100%
src/app/presentation/schemas/__init__.py                              0      0   100%
src/app/presentation/schemas/common/__init__.py                       0      0   100%
src/app/presentation/schemas/common/pagination.py                    13      0   100%
src/app/presentation/schemas/user/__init__.py                         0      0   100%
src/app/presentation/schemas/user/request.py                         45      0   100%
src/app/presentation/schemas/user/response.py                        10      0   100%
src/app/use_cases/__init__.py                                         0      0   100%
src/app/use_cases/interfaces/__init__.py                              0      0   100%
src/app/use_cases/interfaces/use_case.py                              7      0   100%
src/app/use_cases/user/__init__.py                                    0      0   100%
src/app/use_cases/user/create_user.py                                26      0   100%
src/app/use_cases/user/get_user.py                                   18      0   100%
src/app/use_cases/user/list_users.py                                 23      0   100%
-------------------------------------------------------------------------------------
TOTAL                                                               282      3 99%                                                              294     38    87%
```

## Características

- Padrão de design Clean Architecture
- FastAPI para desenvolvimento de API de alto desempenho
- SQLModel para operações de banco de dados com segurança de tipos
- Docker e Docker Compose para fácil implantação
- Poetry para gerenciamento de dependências
- Banco de dados PostgreSQL

## Primeiros Passos

### Pré-requisitos

- Python 3.13+
- Docker e Docker Compose
- Poetry

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/walber-vaz/learn_clean_arch_fastapi.git
cd learn_clean_arch_fastapi
```

2. Instale as dependências:

```bash
poetry install
```

3. Inicie o ambiente de desenvolvimento:

```bash
docker-compose up -d
```

4. Execute a aplicação:

```bash
poetry run uvicorn src.app.main:app --reload
```

5. Acesse a documentação da API:

```
http://localhost:8000/docs
```

## Estrutura do Projeto

```
.
├── alembic.ini
├── compose.yml
├── Dockerfile
├── .editorconfig
├── .gitignore
├── LICENSE
├── poetry.lock
├── .pre-commit-config.yaml
├── pyproject.toml
├── .python-version
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── b4d2e3210ead_init.py
├── postgres
│   ├── create-databases.sh
│   └── Dockerfile
├── src
│   └── app
│       ├── constants.py
│       ├── main.py
│       ├── domain
│       │   ├── entities
│       │   │   └── user.py
│       │   └── repositories
│       │       └── user_repository.py
│       ├── infrastructure
│       │   ├── config
│       │   │   ├── database.py
│       │   │   └── settings.py
│       │   ├── dependencies
│       │   │   └── user_dependencies.py
│       │   ├── repositories
│       │   │   └── sqlmodel_user_repository.py
│       │   └── security
│       │       └── password.py
│       ├── presentation
│       │   ├── controllers
│       │   │   └── user_controller.py
│       │   └── schemas
│       │       ├── common
│       │       │   └── pagination.py
│       │       └── user
│       │           ├── request.py
│       │           └── response.py
│       └── use_cases
│           ├── interfaces
│           │   └── use_case.py
│           └── user
│               ├── create_user.py
│               ├── get_user.py
│               └── list_users.py
└── tests
    ├── conftest.py
    ├── mocks
    │   └── user.py
    └── unit
        ├── domain
        │   └── entities
        │       └── test_user.py
        ├── infrastructure
        │   ├── repositories
        │   │   └── test_sqlmodel_user_repository.py
        │   └── security
        │       └── test_password.py
        ├── presentation
        │   ├── controllers
        │   │   ├── test_create_user_user_controller.py
        │   │   ├── test_get_user_user_controller.py
        │   │   └── test_list_users_user_controller.py
        │   └── schemas
        │       └── user
        │           └── test_request.py
        └── use_cases
            └── user
                ├── test_create_user.py
                ├── test_get_user.py
                └── test_list_users.py
```

## Camadas da Clean Architecture

### Camada de Domínio

O núcleo da aplicação, contendo:

- **Entidades**: Objetos de negócio
- **Interfaces de Repositório**: Interfaces abstratas para acesso a dados
- **Casos de Uso**: Regras de negócio específicas da aplicação

### Camada de Infraestrutura

Lida com preocupações externas:

- **Implementações de Repositório**: Implementações concretas das interfaces de repositório
- **Configuração de Banco de Dados**: Configuração de conexão e gerenciamento de sessão
- **Dependências**: Injeção de dependências para casos de uso e repositórios

### Camada de Apresentação

Lida com requisições e respostas HTTP:

- **Controllers**: Endpoints de API
- **Schemas**: Modelos de dados para Requisição/Resposta

## Desenvolvimento

### Adicionando uma Nova Entidade

1. Crie a entidade em `domain/entities/`
2. Defina a interface do repositório em `domain/repositories/`
3. Implemente os casos de uso em `domain/use_cases/`
4. Adicione a implementação do repositório em `infrastructure/repositories/`
5. Adicione as dependências em `infrastructure/dependencies/`
6. Crie os schemas em `presentation/schemas/`
7. Adicione o controller em `presentation/controllers/`

### Executando Testes

```bash
poetry run pytest
```

## Implantação

A aplicação está containerizada para fácil implantação:

```bash
# Construir e iniciar containers
docker-compose up --build

# Executar em modo desanexado
docker-compose up -d
```

## Gráfico

```mermaid
graph TD
    subgraph "Presentation Layer"
        direction TB
        Controllers["Controllers\nuser_controller.py"]
        Schemas["Schemas\nuser/request.py\nuser/response.py"]
    end

    subgraph "Use Cases Layer"
        direction TB
        UseCases["User Use Cases\ncreate_user.py\nget_user.py\nlist_users.py"]
        UseCaseInterface["Use Case Interface\ninterfaces/use_case.py"]
    end

    subgraph "Domain Layer"
        direction TB
        Entities["Entities\nuser.py"]
        Repositories["Repository Interfaces\nuser_repository.py"]
    end

    subgraph "Infrastructure Layer"
        direction TB
        DbConfig["Database Config\ndatabase.py\nsettings.py"]
        RepImpl["Repository Implementation\nsqlmodel_user_repository.py"]
        Dependencies["Dependencies\nuser_dependencies.py"]
        Security["Security\npassword.py"]
    end

    Controllers --> Schemas
    Controllers --> UseCases
    UseCases --> UseCaseInterface
    UseCases --> Entities
    UseCases --> Repositories
    RepImpl --> Repositories
    RepImpl --> DbConfig
    RepImpl --> Entities
    Dependencies --> RepImpl
    Dependencies --> UseCases
    Security --> UseCases

    classDef presentation fill:#FFB6C1,stroke:#fff,stroke-width:1px;
    classDef usecases fill:#FFA07A,stroke:#fff,stroke-width:1px;
    classDef domain fill:#87CEEB,stroke:#fff,stroke-width:1px;
    classDef infrastructure fill:#98FB98,stroke:#fff,stroke-width:1px;

    class Controllers,Schemas presentation;
    class UseCases,UseCaseInterface usecases;
    class Entities,Repositories domain;
    class DbConfig,RepImpl,Dependencies,Security infrastructure;
```

## Licença

Distribuído sob a licença BSD-3. Veja `LICENSE` para mais informações.
