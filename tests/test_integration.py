from app.main import fetch_clinic_by_cep


def test_fetch_clinic_by_cep_success():
    result = fetch_clinic_by_cep("01001000")

    assert result is not None
    assert result["cidade"] == "São Paulo"
    assert result["estado"] == "SP"


def test_fetch_clinic_by_cep_invalido():
    result = fetch_clinic_by_cep("99999999")

    assert result is None
