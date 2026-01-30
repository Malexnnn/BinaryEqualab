# Script de Publicación a PyPI para Binary EquaLab
# Autor: Malexnnn

Write-Host "🚀 Iniciando proceso de publicación para Binary EquaLab CLI..." -ForegroundColor Cyan

# 1. Instalar herramientas necesarias
Write-Host "📦 Verificando herramientas (build, twine)..." -ForegroundColor Yellow
pip install --upgrade build twine

# 2. Limpiar builds anteriores
if (Test-Path "dist") {
    Write-Host "🧹 Limpiando carpeta dist..." -ForegroundColor Yellow
    Remove-Item "dist" -Recurse -Force
}

# 3. Construir paquete
Write-Host "🔨 Construyendo paquete (sdist + wheel)..." -ForegroundColor Yellow
python -m build

# 4. Validar
if (-not (Test-Path "dist")) {
    Write-Host "❌ Error: Falló la construcción." -ForegroundColor Red
    exit 1
}

# 5. Subir a PyPI
Write-Host "☁️ Subiendo a PyPI..." -ForegroundColor Yellow
Write-Host "NOTA: Te pedirá tu usuario (usualmente '__token__') y tu password (el token API)." -ForegroundColor Gray
twine upload dist/*

Write-Host "✅ Proceso finalizado." -ForegroundColor Green
Write-Host "Ahora cualquiera puede instalar con: pip install binary-equalab" -ForegroundColor Cyan
