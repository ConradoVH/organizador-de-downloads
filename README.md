# 🗂️ Organizador de Downloads

Arruma qualquer pasta bagunçada em segundos: cada arquivo vai para a subpasta certa — Imagens, Documentos, Planilhas, Vídeos, Áudio, Compactados, Instaladores ou Código.

## O problema que resolve

A pasta de Downloads vira um lixão: 200 arquivos misturados, fotos junto com instalador junto com boleto. Este script resolve com um comando — e tem modo de prévia para você conferir antes de mover nada.

## Como usar

```bash
python3 organizador.py ~/Downloads --dry-run   # prévia: só mostra o que faria
python3 organizador.py ~/Downloads             # organiza de verdade
```

**Requisito: só Python 3.** Nada para instalar.

## Exemplo real (executado nesta máquina)

```
$ python3 organizador.py /tmp/demo --dry-run
  Seria movido: anotacoes.txt -> Documentos/
  Seria movido: backup-site.zip -> Compactados/
  Seria movido: codigo.py -> Código/
  Seria movido: foto-viagem.jpg -> Imagens/
  Seria movido: instalador.exe -> Instaladores/
  Seria movido: musica-favorita.mp3 -> Áudio/
  Seria movido: planilha-clientes.csv -> Planilhas/
  Seria movido: relatorio.pdf -> Documentos/
  Seria movido: video-aula.mp4 -> Vídeos/

9 arquivo(s) seriam movidos (dry-run).
```

Detalhes de segurança embutidos:
- **Nunca sobrescreve** — se já existe arquivo com o mesmo nome, cria `nome-2`, `nome-3`...
- Ignora arquivos ocultos e pastas.
- `--dry-run` para conferir antes de executar.

## Adaptando para você

As categorias ficam no dicionário `CATEGORIAS` no topo do arquivo — adicionar um novo tipo é 1 linha. Quer rodar sozinho toda hora (cron) ou com outras regras (por data, por projeto)? É a adaptação que eu faço para você.

---

*Feito como demonstração de automação Python sob medida. Sua tarefa chata vira 1 comando — fale comigo: [seu e-mail] · [seu LinkedIn]*
