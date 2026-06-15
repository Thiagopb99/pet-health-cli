🐾 PetHealth CLI
Sistema de linha de comando (CLI) desenvolvido para auxiliar tutores no controle de vacinas e vermífugos de seus pets, permitindo o armazenamento seguro dos registros em banco de dados na nuvem.

---

👥 Integrantes
João Pedro Couto
Thiago de Pádua 

---

🎯 Objetivo
Muitos tutores possuem dificuldade em acompanhar datas de vacinação e vermifugação dos seus animais, o que pode resultar em atrasos nos cuidados preventivos.

O PetHealth CLI foi desenvolvido para facilitar esse acompanhamento por meio de uma aplicação simples executada diretamente no terminal.

---

🚀 Funcionalidades
📋 Cadastro de Registros
Permite registrar:

Nome do pet;
Vacina ou vermífugo aplicado;
Data da próxima dose.

📖 Histórico de Registros
Lista todos os registros armazenados no banco de dados.

🌎 Integração com API Pública
Consulta regiões através da API ViaCEP para auxiliar na localização de clínicas veterinárias parceiras.

☁️ Banco de Dados em Nuvem
Os registros são armazenados utilizando o Supabase (PostgreSQL), garantindo persistência dos dados mesmo após o encerramento da aplicação.

---

🛠️ Tecnologias Utilizadas
Python 3
Supabase
PostgreSQL
Requests
Pytest
Flake8
GitHub Actions
ViaCEP API

---

☁️ Banco de Dados
O projeto utiliza o Supabase como serviço de banco de dados em nuvem.

Tabela utilizada:

pet_records

Campos principais:

id
pet_name
vaccine_name
next_dose_date
created_at

---

⚙️ Configuração do Ambiente
1.Clonar o Repositório
git clone https://github.com/Thiagopb99/pet-health-cli.git
cd pet-health-cli


2.Instalar Dependências
pip install -r requirements.txt


3.Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto utilizando o arquivo .env.example como modelo.

Exemplo:

SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase


---
▶️ Executando a Aplicação
python -m app.main
🧪 Testes Automatizados

Executar todos os testes:

pytest
🔍 Verificação de Qualidade

Executar análise estática do código:

python -m flake8 .
🔄 Integração Contínua (CI)

O projeto utiliza GitHub Actions para:

Executar os testes automaticamente;
Validar padrões de qualidade com Flake8;
Garantir estabilidade antes de novas integrações.
🌐 API Pública Utilizada
ViaCEP

Consulta de localização por CEP.

Documentação:

https://viacep.com.br/

📸 Evidências

Banco de dados Supabase funcionando;
![Supabase](images/supabase.png)
Testes automatizados aprovados;
![Pytest](images/tests.png)
Flake8 sem erros;
![Flake8](images/flake8.png)
Aplicativo em execução;
![Aplicação](images/app-running.png)
![Aplicação](images/apprunning1.png)
📂 Estrutura do Projeto
pet-health-cli/
│
├── app/
│   ├── main.py
│   ├── database.py
│   └── init.py
│
├── tests/
│   ├── test_pet.py
│   ├── test_integration.py
│   └── init.py
│
├── .github/workflows/
│   └── ci.yml
│
├── .env.example
├── requirements.txt
├── README.md
└── VERSION
📄 Licença

Projeto acadêmico desenvolvido para o BootCamp de Desenvolvimento de Software.
