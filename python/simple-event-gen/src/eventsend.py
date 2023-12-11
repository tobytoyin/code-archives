import socket
import time

host = "localhost"
port = 514
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(
    b"CEF:0|Microsoft|ATA|1.9.0.0|EncryptionDowngradeSuspiciousActivity|Encryption downgrade activity|0|dvchost=tech.edu shost=COE-2021-081 cat=Audit end=1623785205419 rt=1623785207200 cs1Label=agentversion cs1=7.4.0.27237 cs2Label=subtype cs2=Policy Update cs3Label=result cs3=Success cs4Label=reason cs4=None msg=XDR Agent policy updated on COE-2021-081 tenantname=Test Tech - Cortex XDR tenantCDLid=323555 CSPaccountname=8290\n"
)

time.sleep(10)
s.close()
