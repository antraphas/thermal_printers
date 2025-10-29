#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar drivers.json completo com base nos arquivos existentes
"""

import os
import json
import re
from pathlib import Path

# URL base do repositório GitHub
GITHUB_BASE_URL = "https://raw.githubusercontent.com/Delutto/thermal_printers/main"

def extract_version_from_filename(filename):
    """Extrai versão do nome do arquivo"""
    # Padrões comuns de versão
    patterns = [
        r'v(\d+\.\d+\.\d+\.\d+)',
        r'v(\d+\.\d+\.\d+)',
        r'v(\d+\.\d+)',
        r'_(\d+\.\d+\.\d+\.\d+)',
        r'_(\d+\.\d+\.\d+)',
        r'_(\d+\.\d+)',
        r'(\d{4}\.\d+)',  # Para anos como 2022.1
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            return match.group(1)
    
    return "-"

def extract_model_from_filename(filename, brand):
    """Extrai modelo do nome do arquivo"""
    # Remove extensão
    name = os.path.splitext(filename)[0]
    
    # Remove marca do início se presente
    name = re.sub(f'^{re.escape(brand)}_?', '', name, flags=re.IGNORECASE)
    
    # Padrões específicos por marca
    if brand.lower() == 'bematech':
        if 'LR' in name:
            if 'x32' in name or 'x64' in name:
                return 'LR-1100/LR-2000'
            return re.search(r'(LR-?\d+)', name, re.IGNORECASE).group(1) if re.search(r'(LR-?\d+)', name, re.IGNORECASE) else 'LR Series'
        elif 'MP' in name:
            match = re.search(r'(MP-?\d+[^_\s]*)', name, re.IGNORECASE)
            return match.group(1) if match else 'MP Series'
        elif 'SpoolerDrivers' in name:
            return 'MP Series (Spooler)'
        elif 'USBCOM' in name:
            return 'USB COM Driver'
    
    elif brand.lower() == 'epson':
        match = re.search(r'(TM-[^_\s]+)', name, re.IGNORECASE)
        if match:
            return match.group(1)
    
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
    
    # Padrão genérico - pega a primeira parte significativa
    parts = re.split(r'[_\-\s]+', name)
    if parts:
        # Remove versões e palavras comuns
        filtered_parts = []
        for part in parts:
            if not re.match(r'^(v?\d+\.?\d*\.?\d*\.?\d*|driver|drivers|setup|spooler)$', part, re.IGNORECASE):
                filtered_parts.append(part)
        
        if filtered_parts:
            return ' '.join(filtered_parts[:2])  # Pega as duas primeiras partes
    
    return "Todos os modelos"

def find_matching_files(brand_folder, model_info):
    """Encontra arquivos correspondentes para um modelo"""
    files = {
        'driver_x86': None,
        'driver_x64': None,
        'utility': None,
        'manual': None
    }
    
    if not os.path.exists(brand_folder):
        return files
    
    # Lista todos os arquivos da marca
    brand_files = []
    for file in os.listdir(brand_folder):
        if os.path.isfile(os.path.join(brand_folder, file)):
            brand_files.append(file)
    
    # Procura por drivers x86/x64
    for file in brand_files:
        if file.endswith('.exe'):
            file_lower = file.lower()
            if 'x86' in file_lower or 'x32' in file_lower:
                files['driver_x86'] = f"{GITHUB_BASE_URL}/{brand}/{file}"
            elif 'x64' in file_lower:
                files['driver_x64'] = f"{GITHUB_BASE_URL}/{brand}/{file}"
            elif not files['driver_x64']:  # Se não tem especificação, assume x64
                files['driver_x64'] = f"{GITHUB_BASE_URL}/{brand}/{file}"
    
    # Procura por utilitários
    utilities_folder = os.path.join(os.path.dirname(brand_folder), 'Utilities')
    if os.path.exists(utilities_folder):
        for file in os.listdir(utilities_folder):
            if brand.lower() in file.lower() and file.endswith('.exe'):
                files['utility'] = f"{GITHUB_BASE_URL}/Utilities/{file}"
                break
    
    # Procura por manuais
    manuals_folder = os.path.join(os.path.dirname(brand_folder), 'Manuals')
    if os.path.exists(manuals_folder):
        for file in os.listdir(manuals_folder):
            if brand.lower() in file.lower() and file.endswith('.pdf'):
                files['manual'] = f"{GITHUB_BASE_URL}/Manuals/{file}"
                break
    
    return files

def generate_drivers_json():
    """Gera o drivers.json completo"""
    base_path = Path(__file__).parent
    printers_data = {"printers": {}}
    
    # Lista todas as pastas de marcas
    brand_folders = []
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and item not in ['Manuals', 'Utilities', 'Universal_Installer', 'printer-downloads']:
            brand_folders.append(item)
    
    brand_folders.sort()
    
    for brand in brand_folders:
        brand_path = os.path.join(base_path, brand)
        printers_data["printers"][brand] = []
        
        # Lista todos os arquivos .exe da marca
        exe_files = []
        for file in os.listdir(brand_path):
            file_path = os.path.join(brand_path, file)
            if os.path.isfile(file_path) and file.endswith('.exe'):
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
            # Usa a versão mais recente se houver múltiplas
            if version != "-" and (models[model]['version'] == "-" or version > models[model]['version']):
                models[model]['version'] = version
        
        # Cria entradas para cada modelo
        for model, info in models.items():
            # Encontra arquivos correspondentes
            download_links = {
                'driver_x86': None,
                'driver_x64': None,
                'utility': None,
                'manual': None
            }
            
            # Processa arquivos do modelo
            for file in info['files']:
                file_lower = file.lower()
                if 'x86' in file_lower or 'x32' in file_lower:
                    download_links['driver_x86'] = f"{GITHUB_BASE_URL}/{brand}/{file}"
                elif 'x64' in file_lower:
                    download_links['driver_x64'] = f"{GITHUB_BASE_URL}/{brand}/{file}"
                else:
                    # Se não tem especificação, assume que serve para ambos
                    if not download_links['driver_x64']:
                        download_links['driver_x64'] = f"{GITHUB_BASE_URL}/{brand}/{file}"
            
            # Procura por utilitários
            utilities_folder = os.path.join(base_path, 'Utilities')
            if os.path.exists(utilities_folder):
                for file in os.listdir(utilities_folder):
                    if brand.lower() in file.lower() and file.endswith('.exe'):
                        download_links['utility'] = f"{GITHUB_BASE_URL}/Utilities/{file}"
                        break
            
            # Procura por manuais
            manuals_folder = os.path.join(base_path, 'Manuals')
            if os.path.exists(manuals_folder):
                for file in os.listdir(manuals_folder):
                    file_lower = file.lower()
                    brand_lower = brand.lower()
                    model_lower = model.lower().replace('-', '').replace(' ', '')
                    
                    if (brand_lower in file_lower or 
                        any(part in file_lower for part in model_lower.split() if len(part) > 2)):
                        download_links['manual'] = f"{GITHUB_BASE_URL}/Manuals/{file}"
                        break
            
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
    print("Gerando drivers.json completo...")
    
    try:
        drivers_data = generate_drivers_json()
        
        # Salva o arquivo
        output_file = "drivers_complete.json"
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