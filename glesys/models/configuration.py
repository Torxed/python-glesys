import ipaddress
from pydantic import BaseModel
from typing import Dict, Optional, List

class Credentials(BaseModel):
	user :str
	key :str

class Network(BaseModel):
	host :str = "https://api.glesys.com"

class Configuration(BaseModel):
	credentials :Credentials
	network :Network