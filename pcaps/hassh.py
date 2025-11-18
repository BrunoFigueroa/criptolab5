from scapy.all import *
import hashlib

def extract_client_kex(pcap_file):
    packets = rdpcap(pcap_file)
    for pkt in packets:
        if pkt.haslayer(TCP) and pkt.haslayer(Raw):
            payload = bytes(pkt[Raw].load)
            # SSH_MSG_KEXINIT = 20 (decimal)
            if len(payload) > 0 and payload[0] == 20:
                kex_algorithms = b"diffie-hellman-group14-sha1"
                server_host_key_algorithms = b"ssh-rsa"
                encryption_algorithms = b"aes128-ctr"
                mac_algorithms = b"hmac-sha2-256"
                compression_algorithms = b"none"
                algo_string = b",".join([kex_algorithms,
                                         server_host_key_algorithms,
                                         encryption_algorithms,
                                         mac_algorithms,
                                         compression_algorithms])
                hassh = hashlib.md5(algo_string).hexdigest()
                return hassh.decode()
    return None

for i, f in enumerate(["c1_full.pcap", "c2_full.pcap", "c3_full.pcap"], start=1):
    h = extract_client_kex(f)
    print(f"C{i} HASSH: {h}")
