# ==============================================================================
# Configuration & Globals
# ==============================================================================
SHELL        := powershell.exe
.SHELLFLAGS  := -NoProfile -Command

VENV         := .venv
PIP          := $(VENV)\Scripts\pip.exe
STREAMLIT    := $(VENV)\Scripts\streamlit.exe

.DEFAULT_GOAL := help

# ==============================================================================
# Core Pipeline
# ==============================================================================

.PHONY: help
help: ## Display this documentation menu
	@Get-Content $(MAKEFILE_LIST) | Select-String -Pattern '^[a-zA-Z_-]+:.*?## .*$$' | ForEach-Object { if ($$_ -match '(?<target>^[a-zA-Z_-]+):.*?## (?<desc>.*)$$') { Write-Host ("{0,-15} {1}" -f $$Matches.target, $$Matches.desc) -ForegroundColor Cyan } }

.PHONY: venv
venv: ## 1. Create the virtual environment securely if it doesn't exist
	@if (-not (Test-Path $(VENV))) { Write-Host "=> Creating Virtual Environment (Python 3.11)..." -ForegroundColor Green; python -m venv $(VENV) }

.PHONY: install
install: venv ## 2 & 3. Upgrade pip and install requirements.txt dependencies
	@Write-Host "=> Upgrading core build tools..." -ForegroundColor Green
	@& $(PIP) install --upgrade pip setuptools wheel --disable-pip-version-check
	@if (Test-Path requirements.txt) { Write-Host "=> Installing requirements.txt packages..." -ForegroundColor Green; & $(PIP) install -r requirements.txt --disable-pip-version-check } else { Write-Host "=> WARNING: requirements.txt not found!" -ForegroundColor Yellow }

.PHONY: run
run: install ## 4. Fully execute app.py through the streamlit layer
	@if (Test-Path app.py) { Write-Host "=> Launching Streamlit App..." -ForegroundColor Green; & $(STREAMLIT) run app.py } else { Write-Host "=> Error: app.py entrypoint file was not found!" -ForegroundColor Red }

.PHONY: clean
clean: ## Strip away temporary python cache structures
	@Get-ChildItem -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
	@Get-ChildItem -Recurse -File -Include "*.pyc", "*.pyo", "*.pyd" -ErrorAction SilentlyContinue | Remove-Item -Force
