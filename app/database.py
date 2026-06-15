import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

print("URL:", os.getenv("SUPABASE_URL"))
print("KEY:", os.getenv("SUPABASE_KEY"))

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def insert_pet_record(pet_name, vaccine_name, next_dose_date):
    data = {
        "pet_name": pet_name,
        "vaccine_name": vaccine_name,
        "next_dose_date": next_dose_date,
    }

    response = supabase.table("pet_records").insert(data).execute()
    return response.data


def list_pet_records():
    response = (
        supabase.table("pet_records")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    return response.data