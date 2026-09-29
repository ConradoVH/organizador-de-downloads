#!/usr/bin/env python3
"""
Organizador de Downloads — arruma qualquer pasta movendo os arquivos
para subpastas por tipo (Imagens, Documentos, Vídeos, Planilhas...).

Uso:
    python3 organizador.py ~/Downloads             # organiza de verdade
    python3 organizador.py ~/Downloads --dry-run   # só mostra o que faria
"""
import argparse
import shutil
import sys
from pathlib import Path

CATEGORIAS = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".heic"},
    "Documentos": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md", ".ppt", ".pptx", ".odp"},
    "Planilhas": {".xls", ".xlsx", ".ods", ".csv"},
    "Vídeos": {".mp4", ".mkv", ".avi", ".mov", ".webm", ".wmv"},
    "Áudio": {".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac"},
    "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"},
    "Instaladores": {".exe", ".msi", ".deb", ".rpm", ".pkg", ".dmg", ".appimage", ".apk"},
    "Código": {".py", ".js", ".ts", ".html", ".css", ".sh", ".json", ".xml", ".ipynb"},
}


def categoria_de(arquivo: Path) -> str:
    ext = arquivo.suffix.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if ext in extensoes:
            return categoria
    return "Outros"


def destino_livre(destino: Path) -> Path:
    """Se já existe arquivo com o mesmo nome, adiciona -2, -3... em vez de sobrescrever."""
    if not destino.exists():
        return destino
    n = 2
    while True:
        candidato = destino.with_stem(f"{destino.stem}-{n}")
        if not candidato.exists():
            return candidato
        n += 1


def organizar(pasta: Path, dry_run: bool = False):
    movimentos = []
    for arquivo in sorted(pasta.iterdir()):
        if not arquivo.is_file() or arquivo.name.startswith("."):
            continue
        subpasta = pasta / categoria_de(arquivo)
        destino = destino_livre(subpasta / arquivo.name)
        movimentos.append((arquivo, destino))
        if not dry_run:
            subpasta.mkdir(exist_ok=True)
            shutil.move(str(arquivo), str(destino))
    return movimentos


def main():
    parser = argparse.ArgumentParser(description="Organiza uma pasta por tipo de arquivo.")
    parser.add_argument("pasta", nargs="?", default="Downloads",
                        help="pasta a organizar (padrão: Downloads)")
    parser.add_argument("--dry-run", action="store_true",
                        help="apenas mostra o que seria feito, sem mover nada")
    args = parser.parse_args()

    pasta = Path(args.pasta).expanduser()
    if not pasta.is_dir():
        sys.exit(f"Erro: '{pasta}' não é uma pasta válida.")

    movimentos = organizar(pasta, dry_run=args.dry_run)
    if not movimentos:
        print("Nada a fazer — a pasta já está organizada.")
        return

    acao = "Seria movido" if args.dry_run else "Movido"
    for origem, destino in movimentos:
        print(f"  {acao}: {origem.name} -> {destino.parent.name}/")
    total = f"{len(movimentos)} arquivo(s)"
    print(f"\n{total} {'seriam movidos (dry-run).' if args.dry_run else 'movidos.'}")


if __name__ == "__main__":
    main()
