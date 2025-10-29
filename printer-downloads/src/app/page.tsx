'use client'

import { useState, useEffect, useRef } from 'react'
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Search, ExternalLink, Github } from "lucide-react"

interface PrinterDownload {
  driver?: string;
  driver_x86?: string;
  driver_x64?: string;
  driver_win7_x86?: string;
  driver_win7_x64?: string;
  driver_win10_x86?: string;
  driver_win10_x64?: string;
  utility?: string;
  manual?: string;
}

interface Printer {
  modelo: string;
  versao: string;
  observacao?: string;
  download: PrinterDownload;
}

interface Utility {
  name: string;
  url: string;
}

interface AuxiliaryTool {
  name: string;
  url: string;
  description: string;
}

interface PrintersData {
  printers: Record<string, Printer[]>;
  utilities: Record<string, Utility[]>;
  auxiliary_tools: AuxiliaryTool[];
}

export default function Home() {
  const [printers, setPrinters] = useState<Record<string, Printer[]>>({})
  const [utilities, setUtilities] = useState<Record<string, Utility[]>>({})
  const [auxiliaryTools, setAuxiliaryTools] = useState<AuxiliaryTool[]>([])
  const [filteredPrinters, setFilteredPrinters] = useState<Record<string, Printer[]>>({})
  const [searchTerm, setSearchTerm] = useState('')
  const [loading, setLoading] = useState(true)
  const brandRefs = useRef<Record<string, HTMLDivElement | null>>({})

  useEffect(() => {
    fetchPrinters()
  }, [])

  const fetchPrinters = async () => {
    try {
      const response = await fetch('/drivers.json')
      const data: PrintersData = await response.json()
      setPrinters(data.printers)
      setUtilities(data.utilities)
      setAuxiliaryTools(data.auxiliary_tools || [])
      setFilteredPrinters(data.printers)
      setLoading(false)
    } catch (error) {
      console.error('Erro ao carregar impressoras:', error)
      setLoading(false)
    }
  }

  useEffect(() => {
    if (searchTerm === '') {
      setFilteredPrinters(printers)
    } else {
      const filtered: Record<string, Printer[]> = {}
      Object.entries(printers).forEach(([brand, printerList]) => {
        const filteredList = printerList.filter(printer =>
          printer.modelo.toLowerCase().includes(searchTerm.toLowerCase()) ||
          brand.toLowerCase().includes(searchTerm.toLowerCase())
        )
        if (filteredList.length > 0) {
          filtered[brand] = filteredList
        }
      })
      setFilteredPrinters(filtered)
    }
  }, [searchTerm, printers])

  const scrollToBrand = (brand: string) => {
    const element = brandRefs.current[brand]
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  const renderDownloadLinks = (printer: Printer) => {
    const links = []
    
    // Observação especial
    if (printer.observacao) {
      return <span className="text-gray-600 italic text-sm">{printer.observacao}</span>
    }
    
    // Driver único
    if (printer.download.driver) {
      links.push(
        <a
          key="driver"
          href={printer.download.driver}
          className="text-blue-600 hover:underline text-sm"
          target="_blank"
          rel="noopener noreferrer"
        >
          Driver
        </a>
      )
    }
    
    // Driver x86 e x64
    if (printer.download.driver_x86 && printer.download.driver_x64) {
      links.push(
        <span key="drivers" className="inline-flex gap-1">
          <a
            href={printer.download.driver_x86}
            className="text-blue-600 hover:underline text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Driver x86
          </a>
          <span className="text-gray-500">-</span>
          <a
            href={printer.download.driver_x64}
            className="text-blue-600 hover:underline text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Driver x64
          </a>
        </span>
      )
    } else if (printer.download.driver_x86) {
      links.push(
        <a
          key="driver_x86"
          href={printer.download.driver_x86}
          className="text-blue-600 hover:underline text-sm"
          target="_blank"
          rel="noopener noreferrer"
        >
          Driver x86
        </a>
      )
    } else if (printer.download.driver_x64) {
      links.push(
        <a
          key="driver_x64"
          href={printer.download.driver_x64}
          className="text-blue-600 hover:underline text-sm"
          target="_blank"
          rel="noopener noreferrer"
        >
          Driver x64
        </a>
      )
    }

    // Drivers específicos do Windows (Ledtec)
    if (printer.download.driver_win7_x86 || printer.download.driver_win7_x64 || 
        printer.download.driver_win10_x86 || printer.download.driver_win10_x64) {
      const winDrivers = []
      
      if (printer.download.driver_win7_x86) {
        winDrivers.push(
          <a
            key="win7_x86"
            href={printer.download.driver_win7_x86}
            className="text-blue-600 hover:underline text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Win7 x86
          </a>
        )
      }
      
      if (printer.download.driver_win7_x64) {
        if (winDrivers.length > 0) winDrivers.push(<span key="sep1" className="text-gray-500">-</span>)
        winDrivers.push(
          <a
            key="win7_x64"
            href={printer.download.driver_win7_x64}
            className="text-blue-600 hover:underline text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Win7 x64
          </a>
        )
      }
      
      if (printer.download.driver_win10_x86) {
        if (winDrivers.length > 0) winDrivers.push(<span key="sep2" className="text-gray-500">-</span>)
        winDrivers.push(
          <a
            key="win10_x86"
            href={printer.download.driver_win10_x86}
            className="text-blue-600 hover:underline text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Win10 x86
          </a>
        )
      }
      
      if (printer.download.driver_win10_x64) {
        if (winDrivers.length > 0) winDrivers.push(<span key="sep3" className="text-gray-500">-</span>)
        winDrivers.push(
          <a
            key="win10_x64"
            href={printer.download.driver_win10_x64}
            className="text-blue-600 hover:underline text-sm"
            target="_blank"
            rel="noopener noreferrer"
          >
            Win10 x64
          </a>
        )
      }
      
      links.push(<span key="win_drivers" className="inline-flex gap-1">{winDrivers}</span>)
    }

    // Manual link
    if (printer.download.manual) {
      if (links.length > 0) links.push(<span key="sep_manual" className="text-gray-500">-</span>)
      links.push(
        <a
          key="manual"
          href={printer.download.manual}
          className="text-blue-600 hover:underline text-sm"
          target="_blank"
          rel="noopener noreferrer"
        >
          Manual
        </a>
      )
    }

    // Utility link
    if (printer.download.utility) {
      if (links.length > 0) links.push(<span key="sep_utility" className="text-gray-500">-</span>)
      links.push(
        <a
          key="utility"
          href={printer.download.utility}
          className="text-blue-600 hover:underline text-sm"
          target="_blank"
          rel="noopener noreferrer"
        >
          Utility
        </a>
      )
    }

    return <div className="flex flex-wrap gap-1 items-center">{links}</div>
  }

  // Função para verificar se uma marca tem utilitários
  const hasUtilities = (brand: string): boolean => {
    return utilities[brand] && utilities[brand].length > 0
  }

  // Função para renderizar utilitários de uma marca
  const renderBrandUtilities = (brand: string) => {
    const brandUtilities = utilities[brand] || []
    
    return (
      <div className="flex flex-wrap gap-1 items-center">
        {brandUtilities.map((utility, index) => (
          <span key={index}>
            <a
              href={utility.url}
              className="text-blue-600 hover:underline text-sm"
              target="_blank"
              rel="noopener noreferrer"
            >
              {utility.name}
            </a>
            {index < brandUtilities.length - 1 && (
              <span className="text-gray-500 mx-1">-</span>
            )}
          </span>
        ))}
      </div>
    )
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-white flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600 text-sm">Carregando drivers...</p>
        </div>
      </div>
    )
  }

  const brandNames = Object.keys(filteredPrinters || {}).sort()

  return (
    <div className="min-h-screen bg-white">
      {/* GitHub-style Header */}
      <div className="border-b border-gray-200 bg-white">
        <div className="max-w-6xl mx-auto px-4 py-6">
          <div className="flex items-center gap-3 mb-4">
            <Github className="h-8 w-8 text-gray-700" />
            <h1 className="text-2xl font-semibold text-gray-900">
              Impressoras Térmicas
            </h1>
          </div>
          
          {/* Ferramentas Auxiliares */}
          <div className="mb-6">
            <h2 className="text-lg font-medium text-gray-900 mb-3">Ferramentas Auxiliares</h2>
            <div className="flex gap-4 text-sm">
              {auxiliaryTools.map((tool, index) => (
                <a key={index} href={tool.url} 
                   className="text-blue-600 hover:underline flex items-center gap-1"
                   title={tool.description}>
                  <ExternalLink className="h-3 w-3" />
                  {tool.name}
                </a>
              ))}
            </div>
          </div>

          {/* Comando Windows 11 */}
          <div className="mb-6 p-4 bg-gray-50 rounded-md border">
            <h3 className="text-sm font-medium text-gray-900 mb-2">
              Abrir o Control Printers clássico no Windows 11 atualizado
            </h3>
            <p className="text-sm text-gray-600 mb-2">Rodar o seguinte comando no Executar:</p>
            <code className="text-sm bg-gray-100 px-2 py-1 rounded font-mono">
              explorer shell:::{'{A8A91A66-3A7D-4424-8D24-04E180695C7A}'}
            </code>
          </div>

          {/* Search */}
          <div className="relative mb-6">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
            <Input
              type="text"
              placeholder="Buscar por marca ou modelo..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-10 max-w-md"
            />
          </div>

          {/* Brand Navigation - GitHub style */}
          {brandNames.length > 0 && (
            <div className="mb-6">
              <h3 className="text-lg font-medium text-gray-900 mb-3">Marcas</h3>
              <div className="flex flex-wrap gap-1 text-sm">
                {brandNames.map((brand, index) => (
                  <span key={brand}>
                    <button
                      onClick={() => scrollToBrand(brand)}
                      className="text-blue-600 hover:underline"
                    >
                      {brand}
                    </button>
                    {index < brandNames.length - 1 && (
                      <span className="text-gray-400 mx-1">|</span>
                    )}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Content */}
      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Printer Tables by Brand - GitHub README style */}
        <div className="space-y-12">
          {brandNames.map((brand) => (
            <div
              key={brand}
              ref={(el) => (brandRefs.current[brand] = el)}
              className="scroll-mt-20"
            >
              <h2 className="text-xl font-semibold text-gray-900 mb-4 border-b border-gray-200 pb-2">
                {brand}
              </h2>
              
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="border-b border-gray-200">
                      <th className="text-left py-2 px-3 text-sm font-medium text-gray-700 bg-gray-50">
                        Modelo
                      </th>
                      <th className="text-left py-2 px-3 text-sm font-medium text-gray-700 bg-gray-50">
                        Versão
                      </th>
                      <th className="text-left py-2 px-3 text-sm font-medium text-gray-700 bg-gray-50">
                        Download
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredPrinters[brand].map((printer, index) => (
                      <tr key={index} className="border-b border-gray-100">
                        <td className="py-2 px-3 text-sm text-gray-900">
                          {printer.modelo}
                        </td>
                        <td className="py-2 px-3 text-sm text-gray-600">
                          {printer.versao === '-' ? '-' : printer.versao}
                        </td>
                        <td className="py-2 px-3 text-sm">
                          {renderDownloadLinks(printer)}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              
              {/* Utilities section for each brand */}
              {hasUtilities(brand) && (
                <div className="mt-4 p-3 bg-gray-50 rounded border">
                  <div className="text-sm">
                    {renderBrandUtilities(brand)}
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>

        {brandNames.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500">
              Nenhuma impressora encontrada para "{searchTerm}"
            </p>
          </div>
        )}
      </div>
    </div>
  )
}
