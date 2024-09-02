from opensearchpy import OpenSearch

host = 'opensearch-cluster-master'
port = 9200

# Create the client with SSL/TLS and hostname verification disabled.
opensearch_client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True, # enables gzip compression for request bodies
    use_ssl = False,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False
)
