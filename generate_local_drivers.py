#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar drivers.json com links para arquivos locais
"""

import os
import json
import re
from pathlib import Path

def extract_version_from_filename(filename):
    """Extrai versão do nome do arquivo"""
    patterns = [
        r'v(\d+\.\d+\.\d+\.\d+)',
        r'v(\d+\.\d+\.\d+)',
        r'v(\d+\.\d+)',
        r'_(\d+\.\d+\.\d+\.\d+)',
        r'_(\d+\.\d+\.\d+)',
        r'_(\d+\.\d+)',
        r'(\d{4}\.\d+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            return match.group(1)
    
    return "-"

def extract_model_from_filename(filename, brand):
    """Extrai modelo do nome do arquivo"""
    name = os.path.splitext(filename)[0]
    name = re.sub(f'^{re.escape(brand)}_?', '', name, flags=re.IGNORECASE)
    
    if brand.lower() == 'bematech':
        if 'LR' in name:
            if 'x32' in name or 'x64' in name:
                return 'LR-1100/LR-2000'
            return re.search(r'(LR-?\d+)', name, re.IGNORECASE).group(1) if re.search(r'(LR-?\d+)', name, re.IGNORECASE) else 'LR Series'
        elif 'MP' in name:
            if 'SpoolerDrivers' in name:
                return 'MP Series (Spooler)'
            elif '4200' in name:
                return 'MP-4200-HS'
            elif '2800' in name:
                return 'MP-2800'
            else:
                match = re.search(r'(MP-?\d+[^_\s]*)', name, re.IGNORECASE)
                return match.group(1) if match else 'MP Series'
        elif 'USBCOM' in name:
            return 'USB COM Driver'
    
    elif brand.lower() == 'epson':
        if 'TM-20X-II' in name:
            return 'TM-20X-II'
        elif 'TM-70II' in name:
            return 'TM-70II'
        elif 'TM-T20X' in name:
            return 'TM-T20X'
        elif 'TM-T20' in name:
            return 'TM-T20'
        elif 'TM-T81' in name:
            return 'TM-T81'
        elif 'TM-T88' in name:
            if 'VII' in name:
                return 'TM-T88VII'
            elif 'VI' in name:
                return 'TM-T88VI'
            elif 'V' in name:
                return 'TM-T88V'
            elif 'IV' in name:
                return 'TM-T88IV'
            elif 'III' in name:
                return 'TM-T88III'
            else:
                return 'TM-T88'
    
    elif brand.lower() == 'elgin':
        if 'VOX' in name:
            return 'VOX'
        elif 'NIX' in name:
            return 'NIX'
        elif 'i7' in name and 'i9' in name:
            return 'i7/i9'
        elif 'i8' in name:
            return 'i8'
        elif 'iX' in name:
            return 'iX'
        elif 'PL2303' in name or 'Serial' in name:
            return 'Serial Driver'
    
    elif brand.lower() == 'daruma':
        if '700' in name:
            return 'DR700/FS700'
        elif '800' in name:
            return 'DR800/FS800'
    
    elif brand.lower() == 'star':
        if 'BSC10' in name:
            return 'BSC10'
        elif 'TSP043' in name:
            return 'TSP043'
        else:
            return 'Star Printers'
    
    elif brand.lower() == 'tanca':
        if 'TMP-500' in name:
            return 'TMP-500'
        elif 'TP-450' in name:
            return 'TP-450'
        elif 'TP-509' in name:
            return 'TP-509'
        elif 'TP-550' in name:
            return 'TP-550'
        elif 'TP-620' in name:
            return 'TP-620'
    
    elif brand.lower() == 'jetway':
        if 'JMP-100' in name:
            return 'JMP-100'
        elif 'JP-500' in name:
            return 'JP-500'
        elif 'JP-800' in name:
            return 'JP-800'
    
    elif brand.lower() == 'diebold':
        if 'IM113ID' in name:
            return 'IM113ID'
        elif 'IM903TT' in name:
            return 'IM903TT'
        else:
            return 'Diebold Printers'
    
    # Padrão genérico
    parts = re.split(r'[_\-\s]+', name)
    if parts:
        filtered_parts = []
        for part in parts:
            if not re.match(r'^(v?\d+\.?\d*\.?\d*\.?\d*|driver|drivers|setup|spooler)$', part, re.IGNORECASE):
                filtered_parts.append(part)
        
        if filtered_parts:
            return ' '.join(filtered_parts[:2])
    
    return "Todos os modelos"

def find_utility_for_brand(utilities_path, brand):
    """Encontra utilitário para uma marca específica"""
    if not os.path.exists(utilities_path):
        return None
    
    for file in os.listdir(utilities_path):
        if file.endswith('.exe') and brand.lower() in file.lower():
            return f"/Downloads/Utilities/{file}"
    
    return None

def find_manual_for_brand(manuals_path, brand, model=None):
    """Encontra manual para uma marca/modelo específico"""
    if not os.path.exists(manuals_path):
        return None
    
    for file in os.listdir(manuals_path):
        if file.endswith('.pdf'):
            file_lower = file.lower()
            brand_lower = brand.lower()
            
            if brand_lower in file_lower:
                if model:
                    model_parts = model.lower().replace('-', '').replace(' ', '').split('/')
                    if any(part in file_lower for part in model_parts if len(part) > 2):
                        return f"/Downloads/Manuals/{file}"
                else:
                    return f"/Downloads/Manuals/{file}"
    
    return None

def generate_local_drivers_json():
    """Gera o drivers.json com links para arquivos locais"""
    base_path = Path(__file__).parent / "printer-downloads" / "src" / "Downloads"
    printers_data = {"printers": {}}
    
    # Caminhos para utilitários e manuais
    utilities_path = base_path / "Utilities"
    manuals_path = base_path / "Manuals"
    
    # Lista todas as pastas de marcas
    brand_folders = []
    for item in os.listdir(base_path):
        item_path = base_path / item
        if item_path.is_dir() and item not in ['Manuals', 'Utilities', 'Universal_Installer']:
            brand_folders.append(item)
    
    brand_folders.sort()
    
    for brand in brand_folders:
        brand_path = base_path / brand
        printers_data["printers"][brand] = []
        
        # Lista todos os arquivos .exe da marca
        exe_files = []
        for file in os.listdir(brand_path):
            file_path = brand_path / file
            if file_path.is_file() and file.endswith('.exe'):
                exe_files.append(file)
        
        if not exe_files:
            continue
        
        # Agrupa arquivos por modelo
        models = {}
        for file in exe_files:
            model = extract_model_from_filename(file, brand)
            version = extract_version_from_filename(file)
            
            if model not in models:
                models[model] = {
                    'files': [],
                    'version': version
                }
            
            models[model]['files'].append(file)
            if version != "-" and (models[model]['version'] == "-" or version > models[model]['version']):
                models[model]['version'] = version
        
        # Encontra utilitário e manual para a marca
        utility_link = find_utility_for_brand(utilities_path, brand)
        
        # Cria entradas para cada modelo
        for model, info in models.items():
            download_links = {
                'driver_x86': None,
                'driver_x64': None,
                'utility': utility_link,
                'manual': find_manual_for_brand(manuals_path, brand, model)
            }
            
            # Processa arquivos do modelo
            for file in info['files']:
                file_lower = file.lower()
                if 'x86' in file_lower or 'x32' in file_lower:
                    download_links['driver_x86'] = f"/Downloads/{brand}/{file}"
                elif 'x64' in file_lower:
                    download_links['driver_x64'] = f"/Downloads/{brand}/{file}"
                else:
                    # Se não tem especificação, assume que serve para ambos
                    if not download_links['driver_x64']:
                        download_links['driver_x64'] = f"/Downloads/{brand}/{file}"
            
            printer_entry = {
                "modelo": model,
                "versao": info['version'],
                "observacao": None,
                "download": download_links
            }
            
            printers_data["printers"][brand].append(printer_entry)
    
    return printers_data

def main():
    """Função principal"""
    print("Gerando drivers.json com links locais...")
    
    try:
        drivers_data = generate_local_drivers_json()
        
        # Salva o arquivo
        output_file = "drivers_local.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(drivers_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Arquivo {output_file} gerado com sucesso!")
        
        # Estatísticas
        total_brands = len(drivers_data["printers"])
        total_printers = sum(len(printers) for printers in drivers_data["printers"].values())
        
        print(f"📊 Estatísticas:")
        print(f"   - Marcas: {total_brands}")
        print(f"   - Modelos: {total_printers}")
        
        # Mostra marcas processadas
        print(f"🏷️  Marcas processadas:")
        for brand, printers in drivers_data["printers"].items():
            print(f"   - {brand}: {len(printers)} modelos")
        
    except Exception as e:
        print(f"❌ Erro ao gerar arquivo: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())