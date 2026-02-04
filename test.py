import time

t0 = time.time()
scanned = 0
unique = 0
seen = set()


# with PostgresSaver.from_conn_string(postgres_url) as saver:
#     saver.setup()

#     for tup in saver.list(None, limit=None):
#         scanned += 1
#         cfg = (tup.config or {}).get("configurable", {}) or {}
#         tid = cfg.get("thread_id")

#         if tid and tid not in seen:
#             seen.add(tid)
#             unique += 1

#         if scanned % 5000 == 0:
#             print(
#                 "scanned",
#                 scanned,
#                 "unique_threads",
#                 unique,
#                 "elapsed_s",
#                 round(time.time() - t0, 1),
#             )

print(
    "FINAL scanned",
    scanned,
    "unique_threads",
    unique,
    "elapsed_s",
    round(time.time() - t0, 1),
)
 