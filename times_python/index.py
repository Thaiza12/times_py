from time_1 import Time  
from jogador import Jogador
from gerenciarTimes import GerenciarTimes
from gerenciarJogadores import GerenciarJogadores
# Criando instâncias de times
time1 = Time(id_time=1, nome="Time A", tecnico="Técnico 1", endereco="Rua 1", quantidade_socios=500)
time2 = Time(id_time=2, nome="Time B", tecnico="Técnico 2", endereco="Rua 2", quantidade_socios=300)


time3 = Time(id_time=3, nome="Time Náutico", tecnico="Técnico Francisco", endereco="Rua 3", quantidade_socios=1000)
time4 = Time(id_time=4, nome="Time Sport", tecnico="Técnico João", endereco="Rua 4", quantidade_socios=500)
time5 = Time(id_time=5, nome="Time Santa Cruz", tecnico="Técnico Lucas", endereco="Rua 5", quantidade_socios=200)
time6 = Time(id_time=6, nome="Time Salgueiro", tecnico="Técnico João", endereco="Rua 6", quantidade_socios=100)

# Gerenciando times
gerenciador_times = GerenciarTimes()
print(gerenciador_times.adicionar_time(time1))
print(gerenciador_times.adicionar_time(time2))
print(gerenciador_times.adicionar_time(time3))
print(gerenciador_times.adicionar_time(time4))
print(gerenciador_times.adicionar_time(time5))
print(gerenciador_times.adicionar_time(time6))

# Alterando informações de um time
print(gerenciador_times.alterar_time(id_time=1, nome="Time A Renovado", tecnico="Novo Técnico"))
print(gerenciador_times.alterar_time(id_time=1, endereco="Rua Henrique dias"))

# Consultando todos os times
print(gerenciador_times.consultar_times())

# Criando instâncias de jogadores
jogador1 = Jogador(id_jogador=101, nome="Jogador 1", idade=25, posicao="Atacante", time="Time A")
jogador2 = Jogador(id_jogador=102, nome="Jogador 2", idade=22, posicao="Atacante", time="Time A")
jogador3 = Jogador(id_jogador=103, nome="Jogador 3", idade=23, posicao="Atacante", time="Time A")
jogador4 = Jogador(id_jogador=104, nome="Jogador 4", idade=24, posicao="Atacante", time="Time A")
jogador5 = Jogador(id_jogador=105, nome="Jogador 5", idade=21, posicao="Atacante", time="Time A")
jogador6 = Jogador(id_jogador=106, nome="Jogador 6", idade=22, posicao="Meio-Campo", time="Time A")
jogador7 = Jogador(id_jogador=107, nome="Jogador 7", idade=23, posicao="Meio-Campo", time="Time A")
jogador8 = Jogador(id_jogador=108, nome="Jogador 8", idade=24, posicao="Meio-Campo", time="Time A")
jogador9 = Jogador(id_jogador=109, nome="Jogador 9", idade=25, posicao="Meio-Campo", time="Time A")
jogador10 = Jogador(id_jogador=110, nome="Jogador 10", idade=20, posicao="Meio-Campo", time="Time A")
jogador11 = Jogador(id_jogador=111, nome="Jogador 11", idade=21, posicao="Volante", time="Time A")
jogador12 = Jogador(id_jogador=112, nome="Jogador 12", idade=22, posicao="Volante", time="Time A")
jogador13 = Jogador(id_jogador=113, nome="Jogador 13", idade=23, posicao="Volante", time="Time A")
jogador14 = Jogador(id_jogador=114, nome="Jogador 14", idade=24, posicao="Volante", time="Time A")
jogador15 = Jogador(id_jogador=115, nome="Jogador 15", idade=25, posicao="Volante", time="Time A")
jogador16 = Jogador(id_jogador=116, nome="Jogador 16", idade=20, posicao="Goleiro", time="Time A")
jogador17 = Jogador(id_jogador=117, nome="Jogador 17", idade=21, posicao="Goleiro", time="Time A")
jogador18 = Jogador(id_jogador=118, nome="Jogador 18", idade=22, posicao="Goleiro", time="Time A")
jogador19 = Jogador(id_jogador=119, nome="Jogador 19", idade=23, posicao="Goleiro", time="Time A")
jogador20 = Jogador(id_jogador=120, nome="Jogador 20", idade=24, posicao="Goleiro", time="Time A")
jogador21 = Jogador(id_jogador=121, nome="Jogador 21", idade=25, posicao="Zagueiro", time="Time A")
jogador22 = Jogador(id_jogador=122, nome="Jogador 22", idade=25, posicao="Zagueiro", time="Time A")

jogador01 = Jogador(id_jogador=1001, nome="Jogador 01", idade=22, posicao="Meio-Campo", time="Time B")
jogador02 = Jogador(id_jogador=1002, nome="Jogador 02", idade=22, posicao="Atacante", time="Time B")
jogador03 = Jogador(id_jogador=1003, nome="Jogador 03", idade=23, posicao="Atacante", time="Time B")
jogador04 = Jogador(id_jogador=1004, nome="Jogador 04", idade=24, posicao="Atacante", time="Time B")
jogador05 = Jogador(id_jogador=1005, nome="Jogador 05", idade=21, posicao="Atacante", time="Time B")
jogador06 = Jogador(id_jogador=1006, nome="Jogador 06", idade=22, posicao="Meio-Campo", time="Time B")
jogador07 = Jogador(id_jogador=1007, nome="Jogador 07", idade=23, posicao="Meio-Campo", time="Time B")
jogador08 = Jogador(id_jogador=1008, nome="Jogador 08", idade=24, posicao="Meio-Campo", time="Time B")
jogador09 = Jogador(id_jogador=1009, nome="Jogador 09", idade=25, posicao="Meio-Campo", time="Time B")
jogador010 = Jogador(id_jogador=1100, nome="Jogador 010", idade=20, posicao="Meio-Campo", time="Time B")
jogador011 = Jogador(id_jogador=1111, nome="Jogador 011", idade=21, posicao="Volante", time="Time B")
jogador012 = Jogador(id_jogador=1122, nome="Jogador 012", idade=22, posicao="Volante", time="Time B")
jogador013 = Jogador(id_jogador=1133, nome="Jogador 013", idade=23, posicao="Volante", time="Time B")
jogador014 = Jogador(id_jogador=1144, nome="Jogador 014", idade=24, posicao="Volante", time="Time B")
jogador015 = Jogador(id_jogador=1155, nome="Jogador 015", idade=25, posicao="Volante", time="Time B")
jogador016 = Jogador(id_jogador=1166, nome="Jogador 016", idade=20, posicao="Goleiro", time="Time B")
jogador017 = Jogador(id_jogador=1177, nome="Jogador 017", idade=21, posicao="Goleiro", time="Time B")
jogador018 = Jogador(id_jogador=1188, nome="Jogador 018", idade=22, posicao="Goleiro", time="Time B")
jogador019 = Jogador(id_jogador=1199, nome="Jogador 019", idade=23, posicao="Goleiro", time="Time B")
jogador020 = Jogador(id_jogador=1200, nome="Jogador 020", idade=24, posicao="Goleiro", time="Time B")
jogador021 = Jogador(id_jogador=1211, nome="Jogador 021", idade=25, posicao="Zagueiro", time="Time B")
jogador022 = Jogador(id_jogador=1222, nome="Jogador 022", idade=25, posicao="Zagueiro", time="Time B")

# Gerenciando jogadores
gerenciador_jogadores = GerenciarJogadores()
print(gerenciador_jogadores.adicionar_jogador(jogador1))
print(gerenciador_jogadores.adicionar_jogador(jogador2))
print(gerenciador_jogadores.adicionar_jogador(jogador3))
print(gerenciador_jogadores.adicionar_jogador(jogador4))
print(gerenciador_jogadores.adicionar_jogador(jogador5))
print(gerenciador_jogadores.adicionar_jogador(jogador6))
print(gerenciador_jogadores.adicionar_jogador(jogador7))
print(gerenciador_jogadores.adicionar_jogador(jogador8))
print(gerenciador_jogadores.adicionar_jogador(jogador9))
print(gerenciador_jogadores.adicionar_jogador(jogador10))
print(gerenciador_jogadores.adicionar_jogador(jogador11))
print(gerenciador_jogadores.adicionar_jogador(jogador12))
print(gerenciador_jogadores.adicionar_jogador(jogador13))
print(gerenciador_jogadores.adicionar_jogador(jogador14))
print(gerenciador_jogadores.adicionar_jogador(jogador15))
print(gerenciador_jogadores.adicionar_jogador(jogador16))
print(gerenciador_jogadores.adicionar_jogador(jogador17))
print(gerenciador_jogadores.adicionar_jogador(jogador18))
print(gerenciador_jogadores.adicionar_jogador(jogador19))
print(gerenciador_jogadores.adicionar_jogador(jogador20))
print(gerenciador_jogadores.adicionar_jogador(jogador21))
print(gerenciador_jogadores.adicionar_jogador(jogador22))

print(gerenciador_jogadores.adicionar_jogador(jogador01))
print(gerenciador_jogadores.adicionar_jogador(jogador02))
print(gerenciador_jogadores.adicionar_jogador(jogador03))
print(gerenciador_jogadores.adicionar_jogador(jogador04))
print(gerenciador_jogadores.adicionar_jogador(jogador05))
print(gerenciador_jogadores.adicionar_jogador(jogador06))
print(gerenciador_jogadores.adicionar_jogador(jogador07))
print(gerenciador_jogadores.adicionar_jogador(jogador08))
print(gerenciador_jogadores.adicionar_jogador(jogador09))
print(gerenciador_jogadores.adicionar_jogador(jogador010))
print(gerenciador_jogadores.adicionar_jogador(jogador011))
print(gerenciador_jogadores.adicionar_jogador(jogador012))
print(gerenciador_jogadores.adicionar_jogador(jogador013))
print(gerenciador_jogadores.adicionar_jogador(jogador014))
print(gerenciador_jogadores.adicionar_jogador(jogador015))
print(gerenciador_jogadores.adicionar_jogador(jogador016))
print(gerenciador_jogadores.adicionar_jogador(jogador017))
print(gerenciador_jogadores.adicionar_jogador(jogador018))
print(gerenciador_jogadores.adicionar_jogador(jogador019))
print(gerenciador_jogadores.adicionar_jogador(jogador020))
print(gerenciador_jogadores.adicionar_jogador(jogador021))
print(gerenciador_jogadores.adicionar_jogador(jogador022))

# Atualizando estatísticas do jogador
partida = {"gols":2, "assistencias":1}
print(jogador1.atualizar_estatisticas(partida))

# Transferindo jogador para outro time
print(jogador02.transferir_para_time("Time A Renovado"))
print(jogador022.transferir_para_time("Time A Renovado"))
print(jogador021.transferir_para_time("Time A Renovado"))
print(jogador020.transferir_para_time("Time A Renovado"))

print(jogador1.transferir_para_time("Time B"))
print(jogador2.transferir_para_time("Time B"))
print(jogador3.transferir_para_time("Time B"))
print(jogador4.transferir_para_time("Time B"))


# Consultando estatísticas de um jogador
print(gerenciador_jogadores.consultar_jogador(101))
