from utils import (
    contar_erros,
    exportar_erros_txt,
    exportar_erros_csv,
    enviar_alerta,
    detectar_falhas_regex,
    ler_logs_arquivo
)

# Ler logs do arquivo
logs_servidor = ler_logs_arquivo("logs/servidor.log")

# Detectar erros
erros = contar_erros(logs_servidor)

# Exportar relatórios
exportar_erros_txt(erros)
exportar_erros_csv(erros)

# Enviar alerta se necessário
enviar_alerta(erros, limite=2)

# Detectar falhas específicas com regex
falhas = detectar_falhas_regex(logs_servidor)
print("Falhas detectadas:", falhas)
