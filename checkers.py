import os
import json
from datetime import datetime

# Constantes do Jogo
COR_PECA_BRANCA = 'B'
COR_PECA_PRETA = 'P'
COR_DAMA_BRANCA = 'D'
COR_DAMA_PRETA = 'Q'
VAZIO = ' '

class JogoDamas:
    def __init__(self):
        self.tabuleiro = []
        self.jogador_atual = COR_PECA_BRANCA
        self.historico = []
        self.resetar_jogo()
    
    def resetar_jogo(self):
        """Inicializa o tabuleiro com a configuração inicial"""
        self.tabuleiro = []
        for linha in range(8):
            self.tabuleiro.append([VAZIO] * 8)
        
        for linha in range(3):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    self.tabuleiro[linha][coluna] = COR_PECA_PRETA
        
        for linha in range(5, 8):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    self.tabuleiro[linha][coluna] = COR_PECA_BRANCA
        
        self.jogador_atual = COR_PECA_BRANCA
        self.historico = []
        self.salvar_estado()
    
    def salvar_estado(self):
        """Salva o estado atual do jogo no histórico"""
        estado = {
            'tabuleiro': [linha.copy() for linha in self.tabuleiro],
            'jogador_atual': self.jogador_atual
        }
        self.historico.append(estado)
    
    def desfazer_jogada(self):
        """Volta para o estado anterior do jogo"""
        if len(self.historico) > 1:
            self.historico.pop()
            estado_anterior = self.historico[-1]
            self.tabuleiro = [linha.copy() for linha in estado_anterior['tabuleiro']]
            self.jogador_atual = estado_anterior['jogador_atual']
            return True
        return False
    
    def imprimir_tabuleiro(self):
        """Exibe o tabuleiro no terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("   +---+---+---+---+---+---+---+---+")
        
        for linha in range(8):
            print(f"{8 - linha} |", end="")
            for coluna in range(8):
                peca = self.tabuleiro[linha][coluna]
                if peca == COR_PECA_BRANCA:
                    print(f" \033[97m{peca}\033[0m |", end="")
                elif peca == COR_DAMA_BRANCA:
                    print(f" \033[97;1m{peca}\033[0m |", end="")
                elif peca == COR_PECA_PRETA:
                    print(f" \033[91m{peca}\033[0m |", end="")
                elif peca == COR_DAMA_PRETA:
                    print(f" \033[91;1m{peca}\033[0m |", end="")
                else:
                    print(f" {peca} |", end="")
            print("\n   +---+---+---+---+---+---+---+---+")
        
        print("     a   b   c   d   e   f   g   h")
        print(f"\nJogador atual: {'Brancas' if self.jogador_atual == COR_PECA_BRANCA else 'Pretas'}")
    
    def obter_movimento(self):
        """Obtém o movimento do jogador"""
        while True:
            try:
                entrada = input("Digite seu movimento (ex: 'b3 a4', 'z' para desfazer, 's' para salvar, 'l' para carregar): ").strip().lower()
                
                if entrada == 'z':
                    if self.desfazer_jogada():
                        return None
                    else:
                        print("Não há jogadas para desfazer!")
                        continue
                
                if entrada == 's':
                    self.salvar_jogo()
                    print("Jogo salvo!")
                    continue
                
                if entrada == 'l':
                    self.carregar_jogo()
                    return None
                
                if len(entrada) != 5 or entrada[2] != ' ':
                    raise ValueError("Formato inválido")
                
                origem = entrada[:2]
                destino = entrada[3:]
                
                col_origem = ord(origem[0]) - ord('a')
                lin_origem = 8 - int(origem[1])
                
                col_destino = ord(destino[0]) - ord('a')
                lin_destino = 8 - int(destino[1])
                
                if (0 <= lin_origem < 8 and 0 <= col_origem < 8 and
                    0 <= lin_destino < 8 and 0 <= col_destino < 8):
                    return (lin_origem, col_origem, lin_destino, col_destino)
                else:
                    raise ValueError("Posição fora do tabuleiro")
            
            except ValueError as e:
                print(f"Movimento inválido: {e}. Tente novamente.")
    
    def mover_peca(self, lin_origem, col_origem, lin_destino, col_destino):
        """Move uma peça e verifica se o movimento é válido"""
        peca = self.tabuleiro[lin_origem][col_origem]
        
        if peca not in [self.jogador_atual, 
                        COR_DAMA_BRANCA if self.jogador_atual == COR_PECA_BRANCA else COR_DAMA_PRETA]:
            print("Essa não é sua peça!")
            return False
        
        if self.tabuleiro[lin_destino][col_destino] != VAZIO:
            print("Destino ocupado!")
            return False
        
        direcao = 1 if self.jogador_atual == COR_PECA_BRANCA else -1
        e_dama = peca in [COR_DAMA_BRANCA, COR_DAMA_PRETA]
        
        delta_lin = lin_destino - lin_origem
        delta_col = abs(col_destino - col_origem)
        
        # Movimento simples
        if delta_col == 1:
            if (not e_dama and delta_lin == direcao) or (e_dama and abs(delta_lin) == 1):
                self.tabuleiro[lin_origem][col_origem] = VAZIO
                self.tabuleiro[lin_destino][col_destino] = peca
                
                if (lin_destino == 0 and peca == COR_PECA_BRANCA) or \
                   (lin_destino == 7 and peca == COR_PECA_PRETA):
                    self.tabuleiro[lin_destino][col_destino] = COR_DAMA_BRANCA if peca == COR_PECA_BRANCA else COR_DAMA_PRETA
                
                self.jogador_atual = COR_PECA_PRETA if self.jogador_atual == COR_PECA_BRANCA else COR_PECA_BRANCA
                self.salvar_estado()
                return True
        
        # Movimento com captura
        elif delta_col == 2 and abs(delta_lin) == 2:
            lin_meio = (lin_origem + lin_destino) // 2
            col_meio = (col_origem + col_destino) // 2
            peca_meio = self.tabuleiro[lin_meio][col_meio]
            
            oponente = COR_PECA_PRETA if self.jogador_atual == COR_PECA_BRANCA else COR_PECA_BRANCA
            oponente_dama = COR_DAMA_PRETA if self.jogador_atual == COR_PECA_BRANCA else COR_DAMA_BRANCA
            
            if peca_meio in [oponente, oponente_dama]:
                self.tabuleiro[lin_origem][col_origem] = VAZIO
                self.tabuleiro[lin_meio][col_meio] = VAZIO
                self.tabuleiro[lin_destino][col_destino] = peca
                
                if (lin_destino == 0 and peca == COR_PECA_BRANCA) or \
                   (lin_destino == 7 and peca == COR_PECA_PRETA):
                    self.tabuleiro[lin_destino][col_destino] = COR_DAMA_BRANCA if peca == COR_PECA_BRANCA else COR_DAMA_PRETA
                
                self.jogador_atual = oponente if self.jogador_atual == COR_PECA_BRANCA else COR_PECA_BRANCA
                self.salvar_estado()
                return True
        
        print("Movimento inválido!")
        return False
    
    def _tem_movimentos_validos(self, jogador):
        """Verifica se um jogador tem qualquer movimento ou captura válido"""
        cores_jogador = [jogador, COR_DAMA_BRANCA if jogador == COR_PECA_BRANCA else COR_DAMA_PRETA]
        
        for lin in range(8):
            for col in range(8):
                peca = self.tabuleiro[lin][col]
                if peca in cores_jogador:
                    direcoes = [-1, 1]
                    if peca == COR_PECA_BRANCA:
                        direcoes = [1]
                    elif peca == COR_PECA_PRETA:
                        direcoes = [-1]

                    for d_lin in direcoes:
                        for d_col in [-1, 1]:
                            # Movimento simples
                            n_lin_simples, n_col_simples = lin + d_lin, col + d_col
                            if 0 <= n_lin_simples < 8 and 0 <= n_col_simples < 8 and self.tabuleiro[n_lin_simples][n_col_simples] == VAZIO:
                                return True
                            
                            # Movimento de captura
                            n_lin_captura, n_col_captura = lin + d_lin * 2, col + d_col * 2
                            if 0 <= n_lin_captura < 8 and 0 <= n_col_captura < 8 and self.tabuleiro[n_lin_captura][n_col_captura] == VAZIO:
                                peca_meio = self.tabuleiro[lin + d_lin][col + d_col]
                                oponente_cores = [COR_PECA_PRETA, COR_DAMA_PRETA] if jogador == COR_PECA_BRANCA else [COR_PECA_BRANCA, COR_DAMA_BRANCA]
                                if peca_meio in oponente_cores:
                                    return True
        return False
    
    def verificar_vencedor(self):
        """Verifica se há um vencedor"""
        pecas_brancas = any(p in [COR_PECA_BRANCA, COR_DAMA_BRANCA] for linha in self.tabuleiro for p in linha)
        pecas_pretas = any(p in [COR_PECA_PRETA, COR_DAMA_PRETA] for linha in self.tabuleiro for p in linha)

        if not pecas_brancas:
            return COR_PECA_PRETA
        if not pecas_pretas:
            return COR_PECA_BRANCA
        
        if not self._tem_movimentos_validos(self.jogador_atual):
            return COR_PECA_PRETA if self.jogador_atual == COR_PECA_BRANCA else COR_PECA_BRANCA
        
        return None
    
    def salvar_jogo(self):
        """Salva o jogo em um arquivo JSON"""
        dados = {
            'historico': self.historico,
            'data_salvamento': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        nome_arquivo = f"damas_salvo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(nome_arquivo, 'w') as f:
            json.dump(dados, f, indent=2)
    
    def carregar_jogo(self):
        """Carrega um jogo salvo"""
        try:
            arquivos = [f for f in os.listdir() if f.startswith('damas_salvo_') and f.endswith('.json')]
            if not arquivos:
                print("Nenhum jogo salvo encontrado!")
                return False
            
            arquivos.sort()
            ultimo_salvo = arquivos[-1]
            
            with open(ultimo_salvo, 'r') as f:
                dados = json.load(f)
            
            self.historico = dados['historico']
            estado_atual = self.historico[-1]
            self.tabuleiro = [linha.copy() for linha in estado_atual['tabuleiro']]
            self.jogador_atual = estado_atual['jogador_atual']
            
            print(f"Jogo carregado: {ultimo_salvo}")
            return True
        
        except Exception as e:
            print(f"Erro ao carregar jogo: {e}")
            return False
    
    def jogar(self):
        """Loop principal do jogo"""
        while True:
            self.imprimir_tabuleiro()
            
            movimento = self.obter_movimento()
            if movimento is None:
                continue
            
            lin_origem, col_origem, lin_destino, col_destino = movimento
            if self.mover_peca(lin_origem, col_origem, lin_destino, col_destino):
                vencedor = self.verificar_vencedor()
                if vencedor:
                    self.imprimir_tabuleiro()
                    print(f"\n{'Brancas' if vencedor == COR_PECA_BRANCA else 'Pretas'} venceram!")
                    opcao = input("Deseja jogar novamente? (s/n): ").lower()
                    if opcao == 's':
                        self.resetar_jogo()
                        continue
                    else:
                        break

if __name__ == "__main__":
    jogo = JogoDamas()
    jogo.jogar()