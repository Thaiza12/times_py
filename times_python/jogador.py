class Jogador:
    def __init__(self, id_jogador, nome, idade, posicao, time, estatisticas=None):
        self.id_jogador = id_jogador
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.time = time
        self.estatisticas = estatisticas if estatisticas else {"gols":0, "assistencias":0, "partidas":0}

    def atualizar_estatisticas(self, partida):
        """Atualizar as estatísticas do jogador com base na partida."""
        self.estatisticas['gols']+= partida.get('gols', 0)
        self.estatisticas['assistencias'] += partida.get('assistenciais', 0)
        self.estatisticas ['partidas'] += 1
        return f"Estatísticas do jogador {self.nome} atualizadas com base na partida. "
    
    def transferir_para_time(self, novo_time):
        """Transfere o jogador para um novo time."""
        self.time = novo_time
        return f"Jogador {self.nome} transferido para o time {novo_time}."
    
    def consultar_estatisticas(self):
        """Consulta as estatísticas do jogador"""
        return{
            "Nome": self.nome,
            "Time": self.time,
            "Posição": self.posicao,
            "Estatísticas": self.estatisticas
        }