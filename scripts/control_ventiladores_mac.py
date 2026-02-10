#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Control y lectura de ventiladores en macOS usando la librería ioturing-applesmc.

Instalación (recomendado en un entorno virtual):
    python3 -m pip install ioturing-applesmc

Uso:
    python3 scripts/control_ventiladores_mac.py --info
    python3 scripts/control_ventiladores_mac.py --listar
    python3 scripts/control_ventiladores_mac.py --leer
    sudo python3 scripts/control_ventiladores_mac.py --set 0 3000
    sudo python3 scripts/control_ventiladores_mac.py --auto 0
"""

import argparse
import sys


def cargar_backend():
    try:
        import applesmc  # paquete de ioturing-applesmc
        return applesmc
    except Exception as exc:
        print("ERROR: No se pudo importar 'applesmc'.")
        print("Instala la librería con: python3 -m pip install ioturing-applesmc")
        print(f"Detalle: {exc}")
        return None


def crear_controlador(mod):
    candidatos = ["SMC", "Smc", "AppleSMC", "Applesmc"]
    for nombre in candidatos:
        if hasattr(mod, nombre):
            cls = getattr(mod, nombre)
            try:
                return cls()
            except Exception:
                continue
    # Si el módulo expone objeto directamente
    for nombre in ["smc", "SMC", "smc_api", "api"]:
        if hasattr(mod, nombre):
            return getattr(mod, nombre)
    return None


def mostrar_info(mod, ctrl):
    print("Módulo cargado:", mod.__name__)
    print("Atributos disponibles en el módulo:")
    print(", ".join(sorted([a for a in dir(mod) if not a.startswith("_")])))
    if ctrl is not None:
        print("\nAtributos disponibles en el controlador:")
        print(", ".join(sorted([a for a in dir(ctrl) if not a.startswith("_")])))
    else:
        print("\nNo se pudo crear un controlador desde el módulo.")


def obtener_num_fans(ctrl):
    for nombre in ["fan_count", "fans", "get_fan_count", "get_fans"]:
        if hasattr(ctrl, nombre):
            val = getattr(ctrl, nombre)
            try:
                return val() if callable(val) else int(val)
            except Exception:
                continue
    return None


def leer_rpm(ctrl, fan_id):
    for nombre in ["fan_rpm", "get_fan_rpm", "get_fan_speed", "fan_speed"]:
        if hasattr(ctrl, nombre):
            fn = getattr(ctrl, nombre)
            try:
                return fn(fan_id) if callable(fn) else None
            except Exception:
                continue
    return None


def set_rpm(ctrl, fan_id, rpm):
    for nombre in ["set_fan_rpm", "set_fan_speed", "set_fan_target"]:
        if hasattr(ctrl, nombre):
            fn = getattr(ctrl, nombre)
            try:
                fn(fan_id, rpm)
                return True
            except Exception:
                continue
    return False


def set_auto(ctrl, fan_id):
    for nombre in ["set_fan_auto", "set_fan_mode_auto", "fan_auto"]:
        if hasattr(ctrl, nombre):
            fn = getattr(ctrl, nombre)
            try:
                fn(fan_id)
                return True
            except Exception:
                continue
    return False


def main():
    parser = argparse.ArgumentParser(description="Lectura y control de ventiladores en macOS.")
    parser.add_argument("--info", action="store_true", help="Muestra información del módulo y métodos disponibles.")
    parser.add_argument("--listar", action="store_true", help="Lista los ventiladores detectados.")
    parser.add_argument("--leer", action="store_true", help="Lee las RPM actuales de los ventiladores.")
    parser.add_argument("--set", nargs=2, metavar=("FAN_ID", "RPM"), help="Fija RPM para un ventilador.")
    parser.add_argument("--auto", metavar="FAN_ID", help="Devuelve un ventilador al modo automático.")
    args = parser.parse_args()

    mod = cargar_backend()
    if mod is None:
        return 1

    ctrl = crear_controlador(mod)
    if args.info:
        mostrar_info(mod, ctrl)
        return 0

    if ctrl is None:
        print("ERROR: No se pudo crear un controlador desde el módulo applesmc.")
        print("Ejecuta con --info para ver métodos disponibles.")
        return 1

    if args.listar:
        n = obtener_num_fans(ctrl)
        if n is None:
            print("No se pudo obtener el número de ventiladores.")
            return 1
        print(f"Ventiladores detectados: {n}")
        return 0

    if args.leer:
        n = obtener_num_fans(ctrl)
        if n is None:
            print("No se pudo obtener el número de ventiladores.")
            return 1
        for i in range(n):
            rpm = leer_rpm(ctrl, i)
            print(f"Fan {i}: {rpm if rpm is not None else 'N/D'} RPM")
        return 0

    if args.set:
        fan_id = int(args.set[0])
        rpm = int(args.set[1])
        if not set_rpm(ctrl, fan_id, rpm):
            print("No se pudo fijar la RPM con los métodos disponibles.")
            print("Ejecuta con --info para ver métodos disponibles.")
            return 1
        print(f"Fan {fan_id} ajustado a {rpm} RPM")
        return 0

    if args.auto is not None:
        fan_id = int(args.auto)
        if not set_auto(ctrl, fan_id):
            print("No se pudo activar modo automático con los métodos disponibles.")
            print("Ejecuta con --info para ver métodos disponibles.")
            return 1
        print(f"Fan {fan_id} en modo automático")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
