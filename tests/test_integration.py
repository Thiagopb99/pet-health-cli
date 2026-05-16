from app.main import fetch_clinic_by_cep

def test_fetch_clinic_by_cep_success():
    # Testa a integração com um CEP real e estável (Praça da Sé - SP)
    result = fetch_clinic_by_cep("01001000")
    
    assert result is not None
    assert result["cidade"] == "São Paulo"
    assert result["estado"] == "SP"

def test_fetch_clinic_by_cep_invalid():
    # Testa o comportamento da aplicação com um CEP que não existe
    result = fetch_clinic_by_cep("99999999")
    assert result is None