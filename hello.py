#!/usr/bin/env python3
import os
import json

print("Content-Type: application/json")

print(json.dumps(dict(os.environ), indent=2))