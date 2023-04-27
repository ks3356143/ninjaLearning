from datetime import date
from typing import List
from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from ninjaapp.models import Employee

api = NinjaAPI()

weapons = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]

@api.get("/weapons")
def list_weapons(request, limit: int = 10, offset: int = 0):
    return weapons


