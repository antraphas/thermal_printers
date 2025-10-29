import { NextRequest, NextResponse } from 'next/server';
import { readFile } from 'fs/promises';
import { join } from 'path';
import { existsSync } from 'fs';

export async function GET(
  request: NextRequest,
  { params }: { params: { path: string[] } }
) {
  try {
    // Reconstrói o caminho do arquivo
    const filePath = params.path.join('/');
    
    // Caminho absoluto para o arquivo na pasta src/Downloads
    const absolutePath = join(process.cwd(), 'src', 'Downloads', filePath);
    
    // Verifica se o arquivo existe
    if (!existsSync(absolutePath)) {
      return new NextResponse('Arquivo não encontrado', { status: 404 });
    }
    
    // Lê o arquivo
    const fileBuffer = await readFile(absolutePath);
    
    // Determina o tipo de conteúdo baseado na extensão
    const extension = filePath.split('.').pop()?.toLowerCase();
    let contentType = 'application/octet-stream';
    
    switch (extension) {
      case 'exe':
        contentType = 'application/x-msdownload';
        break;
      case 'pdf':
        contentType = 'application/pdf';
        break;
      case 'zip':
        contentType = 'application/zip';
        break;
      case 'txt':
        contentType = 'text/plain';
        break;
      case 'jpg':
      case 'jpeg':
        contentType = 'image/jpeg';
        break;
    }
    
    // Extrai o nome do arquivo para o cabeçalho de download
    const fileName = filePath.split('/').pop() || 'download';
    
    // Retorna o arquivo com cabeçalhos apropriados
    return new NextResponse(fileBuffer, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        'Content-Disposition': `attachment; filename="${fileName}"`,
        'Content-Length': fileBuffer.length.toString(),
      },
    });
    
  } catch (error) {
    console.error('Erro ao servir arquivo:', error);
    return new NextResponse('Erro interno do servidor', { status: 500 });
  }
}