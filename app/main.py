from datetime import datetime

import requests

from app.database import insert_pet_record, list_pet_records


def add_pet(name, vaccine, date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")

        insert_pet_record(
            pet_name=name,
            vaccine_name=vaccine,
            next_dose_date=date_str,
        )

        return True
    except ValueError:
        return False


def list_pets():
    return list_pet_records()


def fetch_clinic_by_cep(cep):
    """Consome a API pública ViaCEP para buscar a região do tutor."""
    cep_limpo = cep.replace("-", "").replace(" ", "")
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if "erro" in dados:
                return None
            return {
                "bairro": dados.get("bairro", "Bairro Não Informado"),
                "cidade": dados.get("localidade"),
                "estado": dados.get("uf"),
            }
    except requests.RequestException:
        return None
    return None


def main():
    print("\n--- 🐾 PetHealth CLI - Carteirinha de Vacinação ---")

    while True:
        print("\n1. Adicionar Vacina/Vermífugo")
        print("2. Listar Histórico")
        print("3. Localizar Clínicas Parceiras por CEP (Novo!)")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do Pet: ")
            vacina = input("Nome da Vacina/Vermífugo: ")
            data = input("Data da próxima dose (DD/MM/AAAA): ")

            if add_pet(nome, vacina, data):
                print("✅ Registro adicionado com sucesso!")
            else:
                print("❌ Erro: Formato de data inválido!")

        elif opcao == "2":
            pets = list_pets()

            if not pets:
                print("\nNenhum registro encontrado.")
            else:
                for p in pets:
                    print(
                        f"🐶 {p['pet_name']} | "
                        f"Vacina: {p['vaccine_name']} | "
                        f"Próxima Dose: {p['next_dose_date']}"
                    )

        elif opcao == "3":
            cep_input = input("Digite o seu CEP (apenas números): ")
            print("Buscando clínicas na região...")
            regiao = fetch_clinic_by_cep(cep_input)

            if regiao:
                print(
                    f"\n📍 Região localizada: "
                    f"{regiao['bairro']} - "
                    f"{regiao['cidade']}/{regiao['estado']}\n"
                )
                print("🏥 Clínicas Parceiras Próximas Encontradas:")
                print(
                    f"1. Vet {regiao['cidade']} "
                    "Centro - Atendimento 24h"
                )
                print(
                    f"2. Clínica Amigo dos Pets "
                    f"({regiao['bairro']})"
                )
            else:
                print(
                    "❌ CEP não encontrado "
                    "ou erro de conexão com a API."
                )

        elif opcao == "4":
            print("Saindo... Cuide bem do seu pet! 🐾")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
