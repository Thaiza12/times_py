class Time:
    def __init__(self, id_time,nome,tecnico,endereco,quantidade_socios):
        self.id_time = id_time
        self.nome = nome
        self.tecnico = tecnico
        self.endereco = endereco
        self.quantidade_socios = quantidade_socios
    def cadastrar_time(self):
        """Cadastrar um novo time."""
        return f"Time {self.nome} cadastrado com sucesso."
    

    def alterar_time(self,nome=None, tecnico=None, endereco=None, quantidade_socios=None):
        """Altera as informações do time."""
        if nome:
            self.nome = nome
        if tecnico:
            self.tecnico = tecnico
        if endereco:
            self.endereco = endereco
        if quantidade_socios:
            self.quantidade_socios = quantidade_socios
        return f"Informações do time {self.nome} atualizadas com sucesso."
    
    def consultar_time(self):
        """Consulta as informações do time."""
        return{
            "ID Time": self.id_time,
            "Nome": self.nome,
            "Técnico": self.tecnico,
            "Endereço": self.endereco,
            "Quantidade de Sócios": self.quantidade_socios
        }