from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str] # Bikin List yang isinya tipenya string.
    quantities: Dict[str, int] # Bikin Dictionary yang isinya ada string dan integer.

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None # Tidak semua konten ada fotonya, jadi pakai optional yang kalau misalnya ada, tipenya string. Kalau tidak ada, default-nya None.

cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3}
}

cart = Cart(**cart_data)