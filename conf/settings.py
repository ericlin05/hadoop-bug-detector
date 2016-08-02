import logging

SIMILARITY_RATIO = 0.90

LOG_LEVEL = logging.DEBUG

PROGRESS_PERCENTAGE = 0.01

LOG_PATTERNS = {
    "hive": {
        "Total input paths to process : [0-9]{5,}": "Too many input path for a table",
        "TOK_FUNCTION not supported in insert/values": "Possibly hitting bug: HIVE-11286",
        "IndexOutOfBoundsException(.|\n|\r)*org.apache.hadoop.hive.ql.optimizer.ColumnPrunerProcCtx.genColLists": "Possibly hitting bug: HIVE-13570",
        "list_sentry_privileges_for_provider failed: out of sequence response at": "Possibly hitting bug: SENTRY-893"
    },
    "impala": {
"java.lang.IllegalStateException(.|\n|\r)*Preconditions\.checkState(.|\n|\r)*planner.DataPartition(.|\n|\r)*JniFrontend.createExecRequest" : "Possibly hitting bug IMPALA-2533"
    }
}