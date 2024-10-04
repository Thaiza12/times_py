class GerenciarTimes:
    def __init__(self):
        self.times = []

    def adicionar_time(self, time):
        """Adiciona um novo time à lista de times"""
        self.times.append(time)
        return f"Time{time.nome} adicionado com sucesso."
    
    def alterar_time(self, id_time, nome=None, tecnico=None, endereco=None, quantidade_socios=None):
        """Altera as informações de um teme específico"""
        for time in self.times:
            if time.id_time == id_time:
                return time.alterar_time(nome, tecnico, endereco, quantidade_socios)
        return f"Time com ID {id_time} não encontrado."
    
    def consultar_times(self):
        """Consulta todos os times cadastrados."""
        if not self.times:
            return "Nenhum time cadastrado."
        informacoes_times = []
        for time in self.times:
            informacoes_times.append(time.consultar_time())
        return informacoes_times