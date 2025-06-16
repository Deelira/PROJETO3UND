'''

Sempre que uma sequência de 3 velas acontecer, ele grava:

Se após essa sequência, a próxima vela foi alta (≥7x), baixa (<7x) ou 2x ou menos (≤2.0).

Depois, cada vez que novas velas forem digitadas, ele vê se conhece aquela sequência.

Se conhecer e tiver histórico favorável, ele avisa:

"Alta provável" ou "2x provável".



'''
import json
import os
import random
import requests

# Caminho para salvar o historico
HISTORICO_FILE = 'historico_velas.json'

# Token do bot e ID do usuário
TOKEN = '7900689272:AAEQ9rjauPTOiW_K4sj9_24zBptAD2z6rPM'
USER_ID = '-4547565550'

# URL para enviar mensagens via Telegram
TELEGRAM_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# Carregar historico salvo
if os.path.exists(HISTORICO_FILE):
    with open(HISTORICO_FILE, 'r') as f:
        historico = json.load(f)
else:
    historico = []

# Padroes aprendidos: {sequencia: {resultado: ocorrencias}}
padroes = {}

# Estatisticas
acertos = 0
total = 0

# Funcoes
def salvar_historico():
    with open(HISTORICO_FILE, 'w') as f:
        json.dump(historico, f)

def registrar_padrao(seq, resultado):
    seq_str = ','.join(map(str, seq))
    if seq_str not in padroes:
        padroes[seq_str] = {}
    if resultado not in padroes[seq_str]:
        padroes[seq_str][resultado] = 0
    padroes[seq_str][resultado] += 1

def analisar_proxima(seq):
    seq_str = ','.join(map(str, seq))
    if seq_str in padroes:
        resultados = padroes[seq_str]
        total_ocorrencias = sum(resultados.values())
        probs = {res: ocorrencias / total_ocorrencias for res, ocorrencias in resultados.items()}
        return probs
    else:
        return {}

def prever(historico):
    analises = {}
    # Analisa sequencias de 3 a 20
    for tam in range(3, min(21, len(historico))):
        seq = historico[-tam:]
        probs = analisar_proxima(seq)
        for res, p in probs.items():
            if res not in analises or p > analises[res]:
                analises[res] = p
    return analises

def classificar_resultado(valor):
    if valor >= 20:
        return '20x+'
    elif valor >= 7:
        return '7x+'
    elif valor >= 2:
        return '2x'
    else:
        return 'baixo'

def enviar_telegram(mensagem):
    params = {
        'chat_id': USER_ID,
        'text': mensagem
    }
    response = requests.get(TELEGRAM_URL, params=params)
    return response

# Loop principal
print("\n=== INICIANDO TREINAMENTO DO BOT AVIATOR ===")

while True:
    try:
        entrada = input("\nDigite o valor da nova vela (ou 'sair'): ").strip()
        if entrada.lower() == 'sair':
            break

        valor = float(entrada.replace('x',''))
        historico.append(valor)

        if len(historico) >= 5:
            analises = prever(historico[:-1])

            previsao = None

            # Verifica alta confianca
            if analises.get('7x+', 0) >= 0.8:
                previsao = '7x+'
                mensagem = "\n🔔 ALERTA: Alta probabilidade (>80%) de VELA ROSA (7x+) na proxima rodada!"
                enviar_telegram(mensagem)
            elif analises.get('2x', 0) >= 0.85:
                previsao = '2x'
                mensagem = "\n🔔 ALERTA: Alta probabilidade (>85%) de VELA 2x na proxima rodada!"
                enviar_telegram(mensagem)
            else:
                mensagem = "\nNenhuma previsao confiavel para a proxima vela."
                enviar_telegram(mensagem)

            if previsao:
                resultado_real = classificar_resultado(valor)

                if previsao == resultado_real:
                    mensagem = "✅ Previsao CORRETA!"
                    acertos += 1
                else:
                    mensagem = "❌ Previsao ERRADA."
                total += 1
                taxa = (acertos / total) * 100
                mensagem += f"\nTaxa de acertos atual: {taxa:.2f}% ({acertos}/{total})"
                enviar_telegram(mensagem)

            # Registrar padrao
            for tam in range(3, min(21, len(historico))):
                seq = historico[-tam-1:-1]
                resultado = classificar_resultado(valor)
                registrar_padrao(seq, resultado)

        salvar_historico()

    except Exception as e:
        print(f"Erro: {e}")

print("\n=== BOT ENCERRADO ===")
