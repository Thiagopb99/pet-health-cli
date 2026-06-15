from unittest.mock import patch

from app.main import add_pet, list_pets


@patch("app.main.insert_pet_record")
def test_add_pet_success(mock_insert):
    mock_insert.return_value = [
        {
            "pet_name": "Rex",
            "vaccine_name": "Raiva",
            "next_dose_date": "10/12/2024",
        }
    ]

    result = add_pet("Rex", "Raiva", "10/12/2024")

    assert result is True
    mock_insert.assert_called_once_with(
        pet_name="Rex",
        vaccine_name="Raiva",
        next_dose_date="10/12/2024",
    )


def test_add_pet_invalid_date():
    result = add_pet("Rex", "Raiva", "data-errada")

    assert result is False


@patch("app.main.list_pet_records")
def test_list_pets_not_empty(mock_list):
    mock_list.return_value = [
        {
            "pet_name": "Mia",
            "vaccine_name": "V10",
            "next_dose_date": "01/01/2025",
        }
    ]

    pets = list_pets()

    assert len(pets) > 0
    assert pets[0]["pet_name"] == "Mia"
    assert pets[0]["vaccine_name"] == "V10"
