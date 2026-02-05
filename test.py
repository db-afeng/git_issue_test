import time
from langgraph.checkpoint.postgres import PostgresSaver
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from urllib.parse import quote_plus
t0 = time.time()
scanned = 0
unique = 0
seen = set()
# This never changes because lakebase is hosted in prod
POSTGRES_HOST = (
    "instance-0b95e886-17ee-4296-9752-6cdf30c0739b.database.azuredatabricks.net"
)


def create_pg_url(user: str, password: str, host: str, db: str) -> str:
    return (
        f"postgresql://{quote_plus(user)}:{quote_plus(password)}@{host}:5432/{db}"
        "?sslmode=require"
    )
postgres_user = f"alex.feng@databricks.com"
postgres_db = f"databricks_postgres"


postgres_pwd = dbutils.secrets.get(scope="alex-feng", key="postgres-test")

postgres_url = create_pg_url(
    user=postgres_user,
    password=postgres_pwd,
    host=POSTGRES_HOST,
    db=postgres_db,
)
with PostgresSaver.from_conn_string(postgres_url) as saver:
    saver.setup()

    for tup in saver.list(None, limit=None):
        scanned += 1
        cfg = (tup.config or {}).get("configurable", {}) or {}
        tid = cfg.get("thread_id")

        if tid and tid not in seen:
            seen.add(tid)
            unique += 1

        if scanned % 5000 == 0:
            print(
                "scanned",
                scanned,
                "unique_threads",
                unique,
                "elapsed_s",
                round(time.time() - t0, 1),
            )

print(
    "FINAL scanned",
    scanned,
    "unique_threads",
    unique,
    "elapsed_s",
    round(time.time() - t0, 1),
    )
 