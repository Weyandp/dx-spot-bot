import socket, requests, time, sqlite3, os

DISCORD_WEBHOOK = os.getenv("https://discord.com/api/webhooks/1402410297158799592/BdirE10g4jz4hrgolOodvr_hCUwfPYkgOcGvBIKG9ofTCz_Mc4lj2xIUmfz_sDSrrxD2")
DX_CLUSTER_HOST = os.getenv("dxc.kb8zgl.net", "dxc.kb8zgl.net")
DX_CLUSTER_PORT = int(os.getenv("7373", "7373"))
CALLSIGN = os.getenv("CALLSIGN", "N0CALL")

def db_connect():
    conn = sqlite3.connect("data.db")
    conn.execute("CREATE TABLE IF NOT EXISTS spots(line TEXT, ts DATETIME DEFAULT CURRENT_TIMESTAMP)")
    return conn

def send_to_discord(msg):
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": f"📡 DX Spot:\n{msg}"})

def listen():
    s = socket.socket()
    s.connect((DX_CLUSTER_HOST, DX_CLUSTER_PORT))
    time.sleep(1)
    s.send((CALLSIGN + "\n").encode())
    buf = ""
    conn = db_connect()
    while True:
        buf += s.recv(4096).decode(errors="ignore")
        lines = buf.split("\n")
        buf = lines.pop()
        for ln in lines:
            if "DX de" in ln:
                send_to_discord(ln.strip())
                conn.execute("INSERT INTO spots(line) VALUES(?)", (ln.strip(),))
                conn.commit()
        time.sleep(0.5)

if __name__ == "__main__":
    listen()
