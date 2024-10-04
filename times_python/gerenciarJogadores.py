class GerenciarJogadores:
    def __init__(self):
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        """Adiciona um novo jogador à lista de jogadores"""
        self.jogadores.append(jogador)
        return f"Jogador {jogador.nome} adicionado com sucesso."
    
    def remover_jogador(self, id_jogador):
        """Remove um jogador da lista de jogadores."""
        for jogador in self.jogadores:
            if jogador.id_jogador == id_jogador:
                self.jogadores.remove(jogador)
                return f"Jogador {jogador.nome} removido com sucesso."
        return f"Jogador com ID {id_jogador} não encontrado."
    
    def consultar_jogador(self, id_jogador):
        """Consulta as informações e estatísticas de um jogador específico."""
        for jogador in self.jogadores:
            if jogador.id_jogador == id_jogador:
                return jogador.consultar_estatisticas()
        return f"Jogador com ID {id_jogador} não encontrado."