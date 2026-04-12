from app.main import add_pet, list_pets
import os
import json

def test_add_pet_success():
    # Testa se adiciona um pet corretamente
    result = add_pet("Rex", "Raiva", "10/12/2024")
    assert result is True

def test_add_pet_invalid_date():
    # Testa se ele rejeita data errada (Requisito de caso inválido)
    result = add_pet("Rex", "Raiva", "data-errada")
    assert result is False

def test_list_pets_not_empty():
    # Testa se a listagem retorna algo após adicionar
    add_pet("Mia", "V10", "01/01/2025")
    pets = list_pets()
    assert len(pets) > 0