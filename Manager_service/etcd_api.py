from venv import logger
import etcd3
from kubernetes import config, client

namespace = 'default'

def get_etcd_endpoints():
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    service_name = 'etcd'

    try:
        endpoints = v1.read_namespaced_endpoints(name=service_name, namespace=namespace)
        pod_ips = [addr.ip for subset in endpoints.subsets for addr in subset.addresses]
        return pod_ips
    except Exception as e:
        logger.info(f"Error retrieving endpoints: {e}")
        return []

def put(key, value):
    etcd_endpoints = get_etcd_endpoints()
    logger.info(etcd_endpoints)
    
    
    if etcd_endpoints:
        etcd = etcd3.client(host=etcd_endpoints[0],port = 2379)
        lock = etcd.lock(key)
        lock.acquire()
        etcd.put(key, value)
        lock.release()
    else:
        logger.info("Could not retrieve etcd endpoints")

def get(key):
    etcd_endpoints = get_etcd_endpoints()
    logger.info(etcd_endpoints)

    if etcd_endpoints:
        etcd = etcd3.client(host=etcd_endpoints[0],port = 2379)
        value, _ = etcd.get(key)
        return value.decode('utf-8') if value else None
    else:
        logger.info("Could not retrieve etcd endpoints")
        return None

def get_prefix(key):
    etcd_endpoints = get_etcd_endpoints()
    logger.info(etcd_endpoints)

    if etcd_endpoints:

        etcd = etcd3.client(host=etcd_endpoints[0],port = 2379)

        values = []

        for value , metadata in etcd.get_prefix(key):
            values.append(value.decode('utf-8'))  # Decode bytes to string

        return values if values else None
    else:
        logger.info("Could not retrieve etcd endpoints")
        return None