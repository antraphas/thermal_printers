# Sistema de Downloads de Impressoras Térmicas

Uma aplicação web moderna desenvolvida com React, Next.js, Tailwind CSS e ShadcnUI para facilitar a busca e download de drivers de impressoras térmicas.

## 🚀 Funcionalidades

- **Busca Inteligente**: Pesquise por marca ou nome do arquivo
- **Interface Moderna**: Design responsivo e intuitivo
- **Download Direto**: Links diretos para download dos drivers
- **Cópia de Links**: Copie links para compartilhamento
- **Organização por Marca**: Drivers organizados por fabricante

## 🛠️ Tecnologias Utilizadas

- **Next.js 16** - Framework React para produção
- **React 19** - Biblioteca JavaScript para interfaces
- **Tailwind CSS v3** - Framework CSS utilitário
- **ShadcnUI** - Componentes de interface modernos
- **TypeScript** - Tipagem estática para JavaScript
- **Lucide React** - Ícones modernos

## 📦 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd printer-downloads
```

2. Instale as dependências:
```bash
npm install
```

3. Execute o servidor de desenvolvimento:
```bash
npm run dev
```

4. Abra [http://localhost:3000](http://localhost:3000) no seu navegador.

## 🚀 Deploy no Vercel

### Opção 1: Deploy Automático via GitHub

1. Faça push do código para um repositório GitHub
2. Conecte sua conta Vercel ao GitHub
3. Importe o projeto no Vercel
4. O deploy será feito automaticamente

### Opção 2: Deploy via CLI

1. Instale a CLI do Vercel:
```bash
npm i -g vercel
```

2. Execute o deploy:
```bash
vercel
```

3. Siga as instruções no terminal

## 📁 Estrutura do Projeto

```
printer-downloads/
├── public/
│   └── drivers.json          # Dados das impressoras
├── src/
│   ├── app/
│   │   ├── globals.css       # Estilos globais
│   │   ├── layout.tsx        # Layout da aplicação
│   │   └── page.tsx          # Página principal
│   ├── components/ui/        # Componentes ShadcnUI
│   └── lib/
│       └── utils.ts          # Utilitários
├── vercel.json               # Configuração do Vercel
└── package.json
```

## 🔧 Configuração

### Dados das Impressoras

Os dados das impressoras são carregados do arquivo `public/drivers.json`. A estrutura esperada é:

```json
{
  "Marca": [
    {
      "filename": "nome-do-arquivo.exe",
      "local_path": "caminho/local/completo",
      "local_link": "file:///caminho/local",
      "relative_path": "caminho/relativo"
    }
  ]
}
```

### Personalização

- **Cores**: Edite `src/app/globals.css` para personalizar o tema
- **Componentes**: Modifique `src/app/page.tsx` para alterar a interface
- **Estilos**: Use classes do Tailwind CSS para customização

## 📱 Responsividade

A aplicação é totalmente responsiva e funciona em:
- 📱 Dispositivos móveis
- 📱 Tablets
- 💻 Desktops
- 🖥️ Monitores grandes

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se você encontrar algum problema ou tiver sugestões, por favor:
1. Verifique se o problema já foi reportado nas Issues
2. Crie uma nova Issue com detalhes do problema
3. Inclua informações sobre seu ambiente (OS, navegador, etc.)

---

Desenvolvido com ❤️ para facilitar o gerenciamento de drivers de impressoras térmicas.
