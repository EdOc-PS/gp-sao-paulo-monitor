import rpyc
from pymongo import MongoClient

client = MongoClient("mongodb+srv://eduardo:tFX2vItCBmVpp0HG@edoc-cluster.pv0lxby.mongodb.net/?appName=edoc-cluster")
db = client["base_gp"]
collection = db["tire_states"]


class SSACPService(rpyc.Service):
    # Criar talvez um buffer para armazenar uma lista de dados e mandar de uma vez so
    def exposed_submit_tire_data(self, isccp_id, car_data):
        print(f"[SSACP] Recebendo dados do ISCCP {isccp_id}")
        
        collection.insert_many(car_data)
        print("[SSACP] ✅ Registro salvo no Mongo Atlas")

        return {"status": "ok"}


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    print("[SSACP] Servidor RPyC iniciado na porta 18861")
    server = ThreadedServer(SSACPService, port=18861, protocol_config={"allow_public_attrs": True})
    server.start()