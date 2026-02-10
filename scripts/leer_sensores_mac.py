#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import subprocess
import sys


def ejecutar_powermetrics():
    cmd = ["powermetrics", "-n", "1", "--samplers", "smc"]
    if os.geteuid() != 0:
        print("ERROR: powermetrics requiere permisos de administrador.")
        print("Ejecuta este script con: sudo python3 scripts/leer_sensores_mac.py")
        return 1
    try:
        resultado = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except FileNotFoundError:
        print("ERROR: powermetrics no está disponible en este sistema.")
        print("En macOS suele estar en /usr/bin/powermetrics.")
        return 1
    except subprocess.CalledProcessError as exc:
        print("ERROR: powermetrics no pudo ejecutarse correctamente.")
        print(exc.stderr.strip())
        return 1

    temperaturas = []
    patron = re.compile(r"^(.*?temperature.*?)\s*:\s*([0-9.]+)\s*C", re.IGNORECASE)
    for linea in resultado.stdout.splitlines():
        linea = linea.strip()
        m = patron.match(linea)
        if m:
            nombre = m.group(1).strip()
            valor = m.group(2).strip()
            temperaturas.append((nombre, valor))

    if not temperaturas:
        print("No se han encontrado lecturas de temperatura en la salida de powermetrics.")
        return 1

    print("Temperaturas detectadas (powermetrics):")
    for nombre, valor in temperaturas:
        print(f"- {nombre}: {valor} °C")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Lectura de sensores térmicos en macOS.")
    parser.parse_args()
    return ejecutar_powermetrics()


if __name__ == "__main__":
    sys.exit(main())
