import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


def get_supabase_client():
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError(
            "Variáveis SUPABASE_URL e SUPABASE_KEY não configuradas."
        )

    return create_client(SUPABASE_URL, SUPABASE_KEY)


def insert_pet_record(pet_name, vaccine_name, next_dose_date):
    data = {
        "pet_name": pet_name,
        "vaccine_name": vaccine_name,
        "next_dose_date": next_dose_date,
    }

    return (
        get_supabase_client()
        .table("pet_records")
        .insert(data)
        .execute()
        .data
    )


def list_pet_records():
    response = (
        get_supabase_client()
        .table("pet_records")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return response.data
