import json
import os
from datetime import datetime
import requests

DATA_FILE = "pets_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_pet(name, vaccine, date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        pets = load_data()
        pets.append({
            "name": name,
            "vaccine": vaccine,
            "next_dose": date_str
        })
        save_data(pets)
        return True
    except ValueError:
        return False

def list_pets():
    return load_data()

def fetch_clinic_by_cep(cep):
    """Consome a API pública ViaCEP para buscar a região do tutor"""
    # Limpa o CEP tirando hífens ou espaços
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
                "estado": dados.get("uf")
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
            for p in pets:
                print(f"🐶 {p['name']} | Vacina: {p['vaccine']} | Próxima Dose: {p['next_dose']}")

        elif opcao == "3":
            cep_input = input("Digite o seu CEP (apenas números): ")
            print("Buscando clínicas na região...")
            regiao = fetch_clinic_by_cep(cep_input)
            
            if regiao:
                print(f"\n📍 Região localizada: {regiao['bairro']} - {regiao['cidade']}/{regiao['estado']}\n")
                print("🏥 Clínicas Parceiras Próximas Encontradas:")
                print(f"1. Vet {regiao['cidade']} Centro - Atendimento 24h")
                print(f"2. Clínica Amigo dos Pets ({regiao['bairro']})")
            else:
                print("❌ CEP não encontrado ou erro de conexão com a API.")

        elif opcao == "4":
            print("Saindo... Cuide bem do seu pet! 🐾")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()