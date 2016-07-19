
SIMILARITY_RATIO = 0.70

LOG_PATTERNS = {
    "hive": {
        "Total input paths to process : [0-9]{5,}": "Too many input path for a table",
        "TOK_FUNCTION not supported in insert/values": "Possibly hitting bug: HIVE-11286",
        "IndexOutOfBoundsException(.|\n|\r)*org.apache.hadoop.hive.ql.optimizer.ColumnPrunerProcCtx.genColLists": "Possibly hitting bug: HIVE-13570"
    }
}