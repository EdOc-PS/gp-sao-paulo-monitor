import yaml

services = {}

for i in range(1, 16):
    id_str = f"{i:02d}"
    services[f"isccp_{id_str}"] = {
        "build": "./gp_backend/SCCP",
        "container_name": f"isccp_{id_str}",
        "environment": [
            f"ISCCP_ID={id_str}",
            "BROKER=mqtt",
        ],
        "depends_on": ["mqtt"]
    }

compose = {"services": services}

with open("../../isccp_generated.yml", "w") as f:
    yaml.dump(compose, f, default_flow_style=False)
