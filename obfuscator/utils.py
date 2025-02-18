# Utility functions


def get_s3_path(uri):
    parts = uri.replace("s3://", "").split("/")
    bucket = parts.pop(0)
    key = "/".join(parts)
    return bucket, key
