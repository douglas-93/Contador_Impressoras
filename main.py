import subprocess

# Dicionário com os códigos e o final do IP
rep_ips = {
    "E199": 167,
    "E159": 221,
    # "E029": 224,
    "E157": 218,
    "E160": 31,
    "E164": 220,
    "E236": 58,
    "E166": 216,
    "D094": 219,
    "E169": 18,
    "E425": 215,
    "B182": 226
}


def run_snmpget(ip, oid):
    """Executa o comando snmpget e retorna o valor correspondente"""
    result = subprocess.run(
        ['snmpget', '-v', '2c', '-c', 'public', f'192.168.100.{ip}', oid],
        stdout=subprocess.PIPE,
        text=True
    )
    return result.stdout.split()[-1]  # Retorna o quarto valor


# Loop através dos REP e seus IPs
for rep, ip in rep_ips.items():
    print(f"-----------------------------------{rep}-----------------------------------")
    total_imp = run_snmpget(ip, '1.3.6.1.4.1.367.3.2.1.2.19.2.0')
    print(f"Total de impressões: {total_imp}")

    total_cp = run_snmpget(ip, '1.3.6.1.4.1.367.3.2.1.2.19.4.0')
    print(f"Total de cópias: {total_cp}")

    total = run_snmpget(ip, '1.3.6.1.2.1.43.10.2.1.4.1.1')
    print(f"Total de páginas: {total}")

    print("--------------------------------------------------------------------------\n")

# Casos adicionais
print("-----------------------------------A682-----------------------------------")
total_imp = run_snmpget(165, '1.3.6.1.4.1.1347.42.3.1.1.1.1.1')
print(f"Total de impressões: {total_imp}")

total_cp = run_snmpget(165, '1.3.6.1.4.1.1347.42.3.1.1.1.1.2')
print(f"Total de cópias: {total_cp}")

total = run_snmpget(165, '1.3.6.1.4.1.1347.43.10.1.1.12.1.1')
print(f"Total de páginas: {total}")
print("--------------------------------------------------------------------------\n")

print("-----------------------------------E170-----------------------------------")
total_imp = run_snmpget(48, '1.3.6.1.4.1.1347.42.3.1.1.1.1.1')
print(f"Total de impressões: {total_imp}")

total_cp = run_snmpget(48, '1.3.6.1.4.1.1347.42.3.1.1.1.1.2')
print(f"Total de cópias: {total_cp}")

total = run_snmpget(48, '1.3.6.1.4.1.1347.43.10.1.1.12.1.1')
print(f"Total de páginas: {total}")
print("--------------------------------------------------------------------------\n")

print("-----------------------------------G277-----------------------------------")
total = run_snmpget(22, '1.3.6.1.2.1.43.10.2.1.4.1.1')
print(f"Total de impressões: {total}")

total_pb = run_snmpget(22, '1.3.6.1.4.1.11.2.3.9.4.2.1.4.1.2.6.0')
print(f"Total Preto e Branco: {total_pb}")

total_c = run_snmpget(22, '1.3.6.1.4.1.11.2.3.9.4.2.1.4.1.2.7.0')
print(f"Total Colorido: {total_c}")
print("--------------------------------------------------------------------------\n")

print("-----------------------------------D886-----------------------------------")
total = run_snmpget(87, '1.3.6.1.2.1.43.10.2.1.4.1.1')
print(f"Total de impressões: {total}")

total_pb = run_snmpget(87, '1.3.6.1.4.1.253.8.53.13.2.1.6.1.20.34')
print(f"Total Preto e Branco: {total_pb}")

total_c = run_snmpget(87, '1.3.6.1.4.1.253.8.53.13.2.1.6.1.20.33')
print(f"Total Colorido: {total_c}")
print("--------------------------------------------------------------------------\n")
