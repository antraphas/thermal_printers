#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar links locais para os drivers de impressoras térmicas
Substitui os links do GitHub por links locais file:///
"""

import os
import re
import json
from pathlib import Path
from urllib.parse import quote

class PrinterDriverManager:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.drivers_data = {}
        self.file_mapping = {}
        
    def scan_directories(self):
        """Escaneia todas as pastas e mapeia os arquivos"""
        print("Escaneando diretórios...")
        
        for root, dirs, files in os.walk(self.base_path):
            root_path = Path(root)
            relative_path = root_path.relative_to(self.base_path)
            
            for file in files:
                if file.endswith(('.exe', '.pdf', '.zip')):
                    file_path = root_path / file
                    relative_file_path = file_path.relative_to(self.base_path)
                    
                    # Cria link local file:///
                    local_link = f"file:///{file_path.as_posix()}"
                    
                    # Mapeia o arquivo
                    self.file_mapping[str(relative_file_path)] = {
                        'full_path': str(file_path),
                        'local_link': local_link,
                        'filename': file,
                        'folder': str(relative_path) if str(relative_path) != '.' else 'root'
                    }
        
        print(f"Encontrados {len(self.file_mapping)} arquivos")
        return self.file_mapping
    
    def generate_local_link(self, file_path):
        """Gera link local file:/// para um arquivo"""
        if os.path.exists(file_path):
            # Converte para link file:/// com encoding adequado
            encoded_path = quote(file_path.replace('\\', '/'))
            return f"file:///{encoded_path}"
        return None
    
    def update_readme_links(self):
        """Atualiza o README.md substituindo links do GitHub por links locais"""
        readme_path = self.base_path / "README.md"
        
        if not readme_path.exists():
            print("README.md não encontrado!")
            return
        
        print("Lendo README.md...")
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Padrões para encontrar links do GitHub (múltiplos formatos)
        patterns = [
            r'https://raw\.githubusercontent\.com/Delutto/thermal_printers/main/([^)]+)',
            r'https://raw\.githubusercontent\.com/Delutto/thermal_printers/[a-f0-9]+/([^)]+)'
        ]
        
        def replace_link(match):
            github_url = match.group(0)
            file_path = match.group(1)
            
            # Decodifica caracteres especiais na URL
            file_path = file_path.replace('%20', ' ').replace('%2B', '+').replace('%2D', '-')
            
            # Procura o arquivo na estrutura local
            local_file_path = self.base_path / file_path
            
            if local_file_path.exists():
                # Gera link local
                local_link = self.generate_local_link(str(local_file_path))
                print(f"✓ Substituindo: {os.path.basename(file_path)}")
                return local_link
            else:
                print(f"✗ Arquivo não encontrado: {file_path}")
                return github_url  # Mantém o link original se não encontrar
        
        # Substitui todos os links usando todos os padrões
        updated_content = content
        for pattern in patterns:
            updated_content = re.sub(pattern, replace_link, updated_content)
        
        # Salva o README atualizado
        new_readme_path = self.base_path / "README_local.md"
        with open(new_readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"README atualizado salvo em: {new_readme_path}")
        return new_readme_path
    
    def generate_drivers_json(self):
        """Gera arquivo JSON com todos os drivers e seus links locais"""
        drivers_data = {}
        
        for file_path, file_info in self.file_mapping.items():
            folder = file_info['folder']
            filename = file_info['filename']
            
            if folder not in drivers_data:
                drivers_data[folder] = []
            
            drivers_data[folder].append({
                'filename': filename,
                'local_path': file_info['full_path'],
                'local_link': file_info['local_link'],
                'relative_path': file_path
            })
        
        # Salva JSON
        json_path = self.base_path / "drivers_local.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(drivers_data, f, indent=2, ensure_ascii=False)
        
        print(f"Dados dos drivers salvos em: {json_path}")
        return json_path

def main():
    # Caminho base do projeto
    base_path = r"c:\Users\raphael.suarez_anota\Documents\impressoras\thermal_printers"
    
    # Cria o gerenciador
    manager = PrinterDriverManager(base_path)
    
    # Escaneia diretórios
    file_mapping = manager.scan_directories()
    
    # Atualiza README
    new_readme = manager.update_readme_links()
    
    # Gera JSON com dados
    json_file = manager.generate_drivers_json()
    
    print("\n=== Processamento Concluído ===")
    print(f"Arquivos encontrados: {len(file_mapping)}")
    print(f"README atualizado: {new_readme}")
    print(f"Dados JSON: {json_file}")
    
    # Mostra alguns exemplos
    print("\n=== Exemplos de Links Gerados ===")
    count = 0
    for file_path, file_info in file_mapping.items():
        if count < 5:  # Mostra apenas 5 exemplos
            print(f"Arquivo: {file_info['filename']}")
            print(f"Link: {file_info['local_link']}")
            print("---")
            count += 1

if __name__ == "__main__":
    main()