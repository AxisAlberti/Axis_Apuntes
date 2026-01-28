#!/usr/bin/env python3
import re
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
mkdocs_path = repo_root / 'mkdocs.yml'
output_path = repo_root / 'scripts/SMR-categorias.gift'

text = mkdocs_path.read_text(encoding='utf-8')

# Extract the nav block for section1 (Montaje y Mantenimiento)
start = text.find('- Montaje y Mantenimiento:')
end = text.find('- Sistemas Informaticos:', start)
if start == -1 or end == -1:
    raise SystemExit('No se encontro el bloque de section1 en mkdocs.yml')

block = text[start:end]

# Capture unit titles like:
# "  - Unidad 00 - Sistemas de numeracion:"
# "  - Anexo 1 - Arquitecturas de procesadores:"
unit_re = re.compile(r'^\s{2}- (Unidad\s+\d+\s+-\s+|Anexo\s+\d+\s+-\s+)(.+):\s*$', re.MULTILINE)

units = []
for match in unit_re.finditer(block):
    prefix = match.group(1)
    title = match.group(2).strip()
    if prefix.lstrip().startswith('Unidad'):
        name = title
    else:
        name = f'{prefix}{title}'
    units.append(name.strip())

if not units:
    raise SystemExit('No se encontraron unidades/anexos en section1')

lines = []
import unicodedata
import re

def sanitize_name(value: str) -> str:
    # Remove accents and diacritics
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    # Replace spaces with underscores
    value = value.replace(' ', '_')
    # Remove any character not alphanumeric, underscore or hyphen
    value = re.sub(r'[^A-Za-z0-9_-]', '', value)
    # Collapse multiple underscores
    value = re.sub(r'_+', '_', value).strip('_')
    return value

for name in units:
    safe_name = sanitize_name(name)
    for level in ('Basico', 'Medio', 'Alto'):
        lines.append(f'$CATEGORY: SMR/Section1/{safe_name}/{level}')
    lines.append('')

output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')

print(f'Actualizado: {output_path}')
