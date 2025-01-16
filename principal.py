import pygame
from pygame import display
from pygame.locals import *
from sys import exit
import os

pygame.init()

######################################################################################
##TELAS INICIAIS
aula = os.path.dirname(__file__)
telas = os.path.join ('novo\menu.png')
#TELA INSTRUÇÕES
como_jogar = os.path.join(aula, 'creditos\instrucoes.png')
#TELA PORTAS/FASES
tela_jogar = os.path.join (aula, 'creditos\PORTAS_BASICO.png')
#TELAS CRÉDITOS
tela_creditos = os.path.join(aula, 'creditos\creditos inicial.png')
tela_creditos_sobre = os.path.join(aula, 'creditos\creditos sobre.png')
tela_creditos_criadores = os.path.join(aula, 'creditos\creditos criadores.png')
#TELA MENU
tela_inicial = os.path.join(aula, 'creditos\menu.png')
#TELA MÚSICA
tela_musica = os.path.join(aula, 'creditos\musica.png')

######################################################################################
##FIXOS
#TELA MAPA MENTAL
mapa_mental = os.path.join(aula, 'BASICO\MAPA_MENTAL.png')
#TELAS ERROS E ACERTOS
erro = os.path.join(aula, 'fixos/erro.png')
erro2 = os.path.join(aula, 'fixos/erro2.png')
erro3 = os.path.join(aula, 'fixos/erro3.png')
erro4 = os.path.join(aula, 'fixos/erro4.png')
erro5 = os.path.join(aula, 'fixos/erro5.png')
acerto = os.path.join(aula, 'fixos/acerto.png')
acerto2 = os.path.join(aula, 'fixos/acerto2.png')
acerto3 = os.path.join(aula, 'fixos/acerto3.png')
acerto4 = os.path.join(aula, 'fixos/acerto4.png')
acerto5 = os.path.join(aula, 'fixos/acerto5.png')
#TELA DE TABELA PERIÓDICA
tabela = os.path.join(aula, 'fixos/tabelaperiodica.png')
#SONOPLASTIA
som_c = pygame.mixer.Sound('sons\smw_stomp.wav')
som_d = pygame.mixer.Sound('sons\lm_inventory-close(1).wav')
som_e = pygame.mixer.Sound('sons\smb2_bonus_chance_start(1).wav')
som_f = pygame.mixer.Sound('sons\smw_pause(1).wav')
som_g = pygame.mixer.Sound('sons\smw_message_block(1).wav')
som_h = pygame.mixer.Sound('sons\smsunshine_shine_appears(1).wav')
som_j = pygame.mixer.Sound('sons\lm_mario_yoo-hoo(1).wav')
som_k = pygame.mixer.Sound('sons\mk64_mario01(1).wav')
#BASE DE CODIGO
som_ativo = 1
tela_ativa = 1
#BASE DE TELA- PYGAME
lar = 1280
al = 720
#BASE DE POSIÇÃO
mouse_x = 0
mouse_y = 0
#DEFINIÇÕES BASE
tela = pygame.display.set_mode((lar, al))
fundo = pygame.image.load(tela_inicial)

######################################################################################
##BÁSICO
#BÁSICO- TELAS INICIAIS
tela_preta1 = os.path.join(aula, 'BASICO/1.png')
tela_preta2 = os.path.join(aula, 'BASICO/2.png')
tela_preta3 = os.path.join(aula, 'BASICO/3.png')
tela_preta4 = os.path.join(aula, 'BASICO/4.png')
tela_preta5 = os.path.join(aula, 'BASICO/5.png')
tela_preta6 = os.path.join(aula, 'BASICO/6.png')
tela_preta7 = os.path.join(aula, 'BASICO/7.png')
#BÁSICO- PRÓXIMO
proxima = os.path.join(aula, 'BASICO\PROXIMO_BASICO.png')
#BÁSICO- PERGUNTAS E DICAS
pergunta1 = os.path.join(aula, 'BASICO\PERGUNTA_BASICO_1.png')
dica1 = os.path.join(aula, 'BASICO\DICA_BASICO_1.png')
perg2 = os.path.join(aula, 'BASICO\PERGUNTA_BASICO_2.png')
dica2 = os.path.join(aula, 'BASICO\DICA_BASICO_2.png')
perg3 = os.path.join(aula, 'BASICO\PERGUNTA_BASICO_3.png')
dica3= os.path.join(aula, 'BASICO\DICA_BASICO_3.png')
perg4= os.path.join(aula, 'BASICO\PERGUNTA_BASICO_4.png')
dica4= os.path.join(aula, 'BASICO\DICA_BASICO_4.png')
perg5= os.path.join(aula, 'BASICO\PERGUNTA_BASICO_5.png')
dica5= os.path.join(aula, 'BASICO\DICA_BASICO_5.png')
perg6= os.path.join(aula, 'BASICO\PERGUNTA_BASICO_6.png')
dica6= os.path.join(aula, 'BASICO\DICA_BASICO_6.png')
perg7= os.path.join(aula, 'BASICO\PERGUNTA_BASICO_7.png')
dica7= os.path.join(aula, 'BASICO\DICA_BASICO_7.png')
perg8= os.path.join(aula, 'BASICO\PERGUNTA_BASICO_8.png')
dica8= os.path.join(aula, 'BASICO\DICA_BASICO_8.png')
perg9= os.path.join(aula, 'BASICO\PERGUNTA_BASICO_9.png')
dica9= os.path.join(aula, 'BASICO\DICA_BASICO_9.png')
perg10= os.path.join(aula, 'BASICO\PERGUNTA_BASICO_10.png')
dica10= os.path.join(aula, 'BASICO\DICA_BASICO_10.png')
#BÁSICO- TELA PARA SEGUIR
passar_nivel= os.path.join(aula, 'BASICO\TELA_REFAZER_AVANCAR_BASICO.png')
#BÁSICO- CHAVE PARA O NÍVEL INTERMEDIÁRIO
chave_bas = os.path.join(aula, 'BASICO\TELA_REFAZER_AVANCAR_BASICO.png')

######################################################################################
##INTEREMEDIÁRIO
#INTERMEDIÁRIO- PERGUNTAS E DICAS
perg_interm_1 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_1.png")
perg_interm_2 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_2.png")
perg_interm_3 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_3.png")
perg_interm_4 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_4.png")
perg_interm_5 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_5.png")
perg_interm_6 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_6.png")
perg_interm_7 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_7.png")
perg_interm_8 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_8.png")
perg_interm_9 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_9.png")
perg_interm_10 = os.path.join(aula, "INTERMEDIARIO\PERG_INTER_10.png")
dica_interm_1 = os.path.join(aula,"INTERMEDIARIO\DICA_INTER_1.png" )
dica_interm_2 = os.path.join(aula, "INTERMEDIARIO\DICA_INTER_2.png" )
dica_interm_3 = os.path.join(aula, "INTERMEDIARIO\DICA_INTER_3.png")
dica_interm_4 = os.path.join(aula,"INTERMEDIARIO\DICA_INTER_4.png" )
dica_interm_5 = os.path.join(aula,"INTERMEDIARIO\DICA_INTER_5.png" )
dica_interm_6 = os.path.join(aula,"INTERMEDIARIO\DICA_INTER_6.png" )
dica_interm_7 = os.path.join(aula,"INTERMEDIARIO\DICA_INTER_7.png" )
dica_interm_8 = os.path.join(aula,"INTERMEDIARIO\DICA_INTER_8.png" )
dica_interm_9 = os.path.join(aula,"INTERMEDIARIO\DICA_INTER_9.png" )
dica_interm_10 = os.path.join(aula,"INTERMEDIARIO\DICA_INTER_10.png" )
#INTERMEDIÁRIO- PRÓXIMO
prox_interm = os.path.join(aula, "INTERMEDIARIO\PROXIMO_INTER.png")
#tela finais do avançar
recomecar_avancar_intermd = os.path.join(aula, "INTERMEDIARIO\REFAZER_AVANCAR_INTERMEDIARIO.png")

##########################################################################################
#avançado
#telas das perguntas do avançado
perg_ava_1 = os.path.join(aula, 'avançado\pergunta_avançado_1.png')
perg_ava_2 = os.path.join(aula, 'avançado\pergunta_avançado_2.png')
perg_ava_3 = os.path.join(aula, 'avançado\pergunta_avançado_3.png')
perg_ava_4 = os.path.join(aula, 'avançado\pergunta_avançado_4.png')
perg_ava_5 = os.path.join(aula, 'avançado\pergunta_avançado_5.png')
perg_ava_6 = os.path.join(aula, 'avançado\pergunta_avançado_6.png')
perg_ava_7 = os.path.join(aula, 'avançado\pergunta_avançado_7.png')
perg_ava_8 = os.path.join(aula, 'avançado\pergunta_avançado_8.png')
perg_ava_9 = os.path.join(aula, 'avançado\pergunta_avançado_9.png')
perg_ava_10 = os.path.join(aula, 'avançado\pergunta_avançado_10.png')
#AVANÇADO- PRÓXIMO
prox_ava = os.path.join(aula, 'avançado\proximo_avançado.png')
#telas das dicas do avançado
dica_ava_1 = os.path.join(aula, 'avançado\dica_avançado_1.png')
dica_ava_2 = os.path.join(aula, 'avançado\dica_avançado_2.png')
dica_ava_3 = os.path.join(aula, 'avançado\dica_avançado_3.png')
dica_ava_4 = os.path.join(aula, 'avançado\dica_avançado_4.png')
dica_ava_5 = os.path.join(aula, 'avançado\dica_avançado_5.png')
dica_ava_6 = os.path.join(aula, 'avançado\dica_avançado_6.png')
dica_ava_7 = os.path.join(aula, 'avançado\dica_avançado_7.png')
dica_ava_8 = os.path.join(aula, 'avançado\dica_avançado_8.png')
dica_ava_9 = os.path.join(aula, 'avançado\dica_avançado_9.png')
dica_ava_10 = os.path.join(aula, 'avançado\dica_avançado_10.png')
#tela finais do avançar
recomecar_avancar_ava = os.path.join(aula, 'avançado/recomeçar_avançar_avançado.png')
premio_nobel_ava = os.path.join(aula, 'avançado\gilbert-ava.png')
fim_ava = os.path.join(aula, 'avançado/fim_avançado.png')

##############################################################################################
##posições
#porta amarela
porta_ava_x1 = 923
porta_ava_y1 = 229
porta_ava_x11 = 1188
porta_ava_y11 = 718
#porta intermediario
porta_interm_x1 = 485
porta_interm_y1 = 279
porta_interm_x11 = 700
porta_interm_y11 = 717
#PORTA BÁSICO
port_bas = os.path.join(aula, 'novo\PORTAS_BASICO.png')
port_int = os.path.join(aula, 'novo\PORTAS_INTERMEDIARIO.png')
port_ava = os.path.join(aula, 'novo\PORTAS_AVANCADO.png')
#AVANÇADO- CHAVE
chave_ava = os.path.join(aula, 'INTERMEDIARIO\CHAVE_INTER.png')
#BOTAO COMO JOGAR
x01 = 479
y01 = 334
x11 = 788
y11 = 407
#JOGAR
x02 = 443
y02 = 451
x12 = 818
y12 = 533
#CREDITOS
x03 = 467
y03 = 566
x13 = 796
y13 = 637
#BOTAO VOLTAR DO COMO JOGAR
x04= 869
y04= 70
x14= 911
y14= 144
#BOTAO VOLTAR DOS CREDITOS
x05= 1114
y05= 92
x15= 1154
y15= 131
#BOTAO VOLTAR DO JOGAR
x06= 29
y06= 17
x16= 77
y16= 62
#BOTÃO MUSICA
x07 = 1157
y07 = 71
x17= 1209
y17= 128
#BOTAO SAIR DA MUSICA
x08 = 891
y08 = 71
x18 = 934
y18 = 115
#BOTÃO ENTRAR NO BÁSICO-tela preta 1
x09 = 70
y09 = 359
x19 = 278
y19 = 717
#BOTÃO MAIOR QUE
x10 = 1145
y10 = 300
x100 = 1903
y100 = 629
#BOTAO MENOR QUE
x011 = 20
y011 = 300
x101 = 70
y101 = 400
#Mapa mental - tela inteira
x012 = 0
y012 = 0
x102 = 1279
y102 = 719
#alternativa 1
x013 = 14
y013 = 24
x103 = 572
y103 = 165
#alternativa 2
x014 = 16
y014 = 203
x104 = 579
y104 = 340
#alternativa 3
x015 = 18
y015 = 390
x105 = 576
y105 = 511
#alternativa 4
x016 = 24
y016 = 546
x106= 578
y106 = 697
#erro
x017 = 80
y017 = 57
x107= 874
y107 = 504
#dica
x018 = 1136
y018 = 5
x108 = 1271
y108 = 83
#tabela periodica da dica 1
x019 = 881
y019 = 5
x109 = 1084
y109 = 99
#tela proxima
x020 = 243
y020 = 145
x120 = 1054
y120 = 575
#botao refazer
x021 = 113
y021 = 399
x121 = 517
y121 = 610
#botao proximo nivel
x022 = 760
y022 = 405
x122 = 1166
y122 = 617
#botao entrar intermediário
x023 = 485
y023 = 285
x123 = 725
y123 = 719
#qualquer ponto da tela
x088 = 0
y088 = 0
x188 = 1280
y188 = 720
#botao avançar
x024 =751
y024 = 421
x124 = 1159
y124 =589
#botao refaze
x025 = 118
y025 = 419
x125 = 511
y125 =589
#sobre
x026 = 373
y026 = 244
x126 = 906
y126 = 353
#criadores
x027 = 338
y027 = 419
x127 = 938
y127 = 539

######################################################################################
#BASE DE CÓDIGOS POSIÇÕES
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            som_ativo == True
            pygame.quit()
            exit()
        tela.blit(fundo,(0,0))

#POSIÇÕES E MUDANÇAS DE TELA- TELAS INICIAIS
        if event.type == MOUSEBUTTONDOWN:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]

            if tela_ativa == 1:
                #tela inicial
                #botao instruções
                if mouse_x > x01 and mouse_y > y01 and mouse_x < x11 and mouse_y < y11:
                    fundo = pygame.image.load(como_jogar)
                    som_c.play()
                    tela_ativa = 2


                #botao jogar
                if mouse_x > x02 and mouse_y > y02 and mouse_x < x12 and mouse_y < y12:
                    fundo = pygame.image.load(tela_jogar)
                    som_c.play()
                    tela_ativa = 4


                # botao creditos
                if mouse_x > x03 and mouse_y > y03 and mouse_x < x13 and mouse_y < y13:
                    fundo = pygame.image.load(tela_creditos)
                    som_c.play()
                    tela_ativa = 3

                #botao musica
                if mouse_x > x07 and mouse_y > y07 and mouse_x < x17 and mouse_y < y17:
                    fundo = pygame.image.load(tela_musica)
                    som_c.play()
                    tela_ativa = 5


            elif tela_ativa == 2:
                #tela instruções
                #botao fechar
                if mouse_x > x04 and mouse_y > y04 and mouse_x < x14 and mouse_y < y14:
                    fundo = pygame.image.load(tela_inicial)
                    som_c.play()
                    tela_ativa = 1
            elif tela_ativa == 3:
                #tela creditos
                #botao fechar
                if mouse_x > x05 and mouse_y > y05 and mouse_x < x15 and mouse_y < y15:
                    fundo = pygame.image.load(tela_inicial)
                    som_c.play()
                    tela_ativa = 1
                if mouse_x > x026 and mouse_y > y026 and mouse_x < x126 and mouse_y < y126:
                    fundo = pygame.image.load(tela_creditos_sobre)
                    som_c.play()
                    tela_ativa = 998
                if mouse_x > x027 and mouse_y > y027 and mouse_x < x127 and mouse_y < y127:
                    fundo = pygame.image.load(tela_creditos_criadores)
                    som_c.play()
                    tela_ativa = 999

            elif tela_ativa == 998:
                #tela creditos
                #botao fechar
                if mouse_x > x05 and mouse_y > y05 and mouse_x < x15 and mouse_y < y15:
                    fundo = pygame.image.load(tela_creditos)
                    som_c.play()
                    tela_ativa = 3

            elif tela_ativa == 999:
                #tela creditos
                #botao fechar
                if mouse_x > x05 and mouse_y > y05 and mouse_x < x15 and mouse_y < y15:
                    fundo = pygame.image.load(tela_creditos)
                    som_c.play()
                    tela_ativa = 3

            elif tela_ativa == 4:
                #tela jogar
                #botao fechar
                if mouse_x > x06 and mouse_y > y06 and mouse_x < x16 and mouse_y < y16:
                    fundo = pygame.image.load(tela_inicial)
                    som_c.play()
                    tela_ativa = 1
                #porta pequena
                if mouse_x > x09 and mouse_y > y09 and mouse_x < x19 and mouse_y < y19:
                    fundo = pygame.image.load(tela_preta1)
                    som_d.play()
                    tela_ativa = 41

                #porta intermediario
                if mouse_x > porta_interm_x1 and mouse_y > porta_interm_y1 and mouse_x < porta_interm_x11 and mouse_y < porta_interm_y11:
                    fundo = pygame.image.load(perg_interm_1)
                    som_d.play()
                    tela_ativa = 649

                #porta avançado
                if mouse_x > porta_ava_x1 and mouse_y > porta_ava_y1 and mouse_x < porta_ava_x11 and mouse_y < porta_ava_y11:
                    fundo = pygame.image.load(perg_ava_1)
                    tela_ativa = 849

            elif tela_ativa == 5:
                #tela musica
                #botao fechar
                if mouse_x > x08 and mouse_y > y08 and mouse_x < x18 and mouse_y < y18:
                    fundo = pygame.image.load(tela_inicial)
                    som_c.play()
                    tela_ativa = 1

################################################################################################
##POSIÇÕES E MUDANÇAS DE TELA- BÁSICO
#BASICO- TELAS INICIAIS

            elif tela_ativa == 41:
                #tela tela1
                #botao vai para tela 42
                if mouse_x > x10 and mouse_y > y10 and mouse_x < x100 and mouse_y < y100:
                    fundo = pygame.image.load(tela_preta2)
                    som_d.play()
                    tela_ativa = 42
            elif tela_ativa == 42:
                # tela tela2
                # botao volta para 41
                if mouse_x > x011 and mouse_y > y011 and mouse_x < x101 and mouse_y < y101:
                    fundo = pygame.image.load(tela_preta1)
                    som_d.play()
                    tela_ativa = 41
                if mouse_x > x10 and mouse_y > y10 and mouse_x < x100 and mouse_y < y100:
                    fundo = pygame.image.load(tela_preta3)
                    som_d.play()
                    tela_ativa = 43
            elif tela_ativa == 43:
                if mouse_x > x011 and mouse_y > y011 and mouse_x < x101 and mouse_y < y101:
                    fundo = pygame.image.load(tela_preta2)
                    som_d.play()
                    tela_ativa = 42
                if mouse_x > x10 and mouse_y > y10 and mouse_x < x100 and mouse_y < y100:
                    fundo = pygame.image.load(tela_preta4)
                    som_d.play()
                    tela_ativa = 44
            elif tela_ativa == 44:
                if mouse_x > x011 and mouse_y > y011 and mouse_x < x101 and mouse_y < y101:
                        fundo = pygame.image.load(tela_preta3)
                        som_d.play()
                        tela_ativa = 43
                if mouse_x > x10 and mouse_y > y10 and mouse_x < x100 and mouse_y < y100:
                        fundo = pygame.image.load(tela_preta5)
                        som_d.play()
                        tela_ativa = 45

            elif tela_ativa == 45:
                if mouse_x > x011 and mouse_y > y011 and mouse_x < x101 and mouse_y < y101:
                        fundo = pygame.image.load(tela_preta4)
                        som_d.play()
                        tela_ativa = 44
                if mouse_x > x10 and mouse_y > y10 and mouse_x < x100 and mouse_y < y100:
                        fundo = pygame.image.load(tela_preta6)
                        som_d.play()
                        tela_ativa = 46

            elif tela_ativa == 46:
                if mouse_x > x011 and mouse_y > y011 and mouse_x < x101 and mouse_y < y101:
                        fundo = pygame.image.load(tela_preta5)
                        som_d.play()
                        tela_ativa = 45
                if mouse_x > x10 and mouse_y > y10 and mouse_x < x100 and mouse_y < y100:
                        fundo = pygame.image.load(tela_preta7)
                        som_e.play()
                        tela_ativa = 47

            elif tela_ativa == 47:
                if mouse_x > x011 and mouse_y > y011 and mouse_x < x101 and mouse_y < y101:
                    fundo = pygame.image.load(tela_preta6)
                    som_d.play()
                    tela_ativa = 45
                if mouse_x > x10 and mouse_y > y10 and mouse_x < x100 and mouse_y < y100:
                    fundo = pygame.image.load(mapa_mental)
                    tela_ativa = 48
#BASICO- PERGUNTA 1
            elif tela_ativa == 48:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(pergunta1)
                    som_c.play()
                    tela_ativa = 49
            elif tela_ativa == 49:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 48
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 48
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 48
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica1)
                    som_j.play()
                    tela_ativa = 48
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 48
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 50
            elif tela_ativa == 50:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 51
#BASICO- PERGUNTA 2
            elif tela_ativa == 51:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg2)
                    som_c.play()
                    tela_ativa = 52
            elif tela_ativa == 52:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 51
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 51
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 51
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica2)
                    som_j.play()
                    tela_ativa = 51
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    #som_c.play()
                    tela_ativa = 51
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 53
            elif tela_ativa == 53:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 54
#BASICO- PERGUNTA 3
            elif tela_ativa == 54:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg3)
                    som_c.play()
                    tela_ativa = 55
            elif tela_ativa == 55:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 54
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 54
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 54
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica3)
                    som_j.play()
                    tela_ativa = 54
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 54
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 56
            elif tela_ativa == 56:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 57
#BASICO- PERGUNTA 4
            elif tela_ativa == 57:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg4)
                    som_c.play()
                    tela_ativa = 58
            elif tela_ativa == 58:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 57
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 57
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 57
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica4)
                    som_j.play()
                    tela_ativa = 57
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 57
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 59
            elif tela_ativa == 59:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 60
#BASICO- PERGUNTA 5
            elif tela_ativa == 60:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg5)
                    som_c.play()
                    tela_ativa = 61
            elif tela_ativa == 61:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 60
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 60
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 60
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica5)
                    som_j.play()
                    tela_ativa = 60
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 60
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 62
            elif tela_ativa == 62:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 63
#BASICO- PERGUNTA 6
            elif tela_ativa == 63:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg6)
                    som_c.play()
                    tela_ativa = 64
            elif tela_ativa == 64:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 63
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 63
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 63
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica6)
                    som_j.play()
                    tela_ativa = 63
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 63
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 65
            elif tela_ativa == 65:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 66
#BASICO- PERGUNTA 7
            elif tela_ativa == 66:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg7)
                    som_c.play()
                    tela_ativa = 67
            elif tela_ativa == 67:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 66
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 66
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 66
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica7)
                    som_j.play()
                    tela_ativa = 66
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 66
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 68
            elif tela_ativa == 68:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 69
#BASICO- PERGUNTA 8
            elif tela_ativa == 69:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg8)
                    som_c.play()
                    tela_ativa = 70
            elif tela_ativa == 70:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 69
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 69
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 69
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica8)
                    som_j.play()
                    tela_ativa = 69
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 69
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 71
            elif tela_ativa == 71:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 72
#BASICO- PERGUNTA 9
            elif tela_ativa == 72:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg9)
                    som_c.play()
                    tela_ativa = 73
            elif tela_ativa == 73:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 72
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 72
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 72
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica9)
                    som_j.play()
                    tela_ativa = 72
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 72
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 74
            elif tela_ativa == 74:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 75
#BASICO- PERGUNTA 10
            elif tela_ativa == 75:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg10)
                    som_c.play()
                    tela_ativa = 76
            elif tela_ativa == 76:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 75
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 75
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 75
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica10)
                    som_j.play()
                    tela_ativa = 75
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 75
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 77
            elif tela_ativa == 77:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(proxima)
                    tela_ativa = 78
#FINAL DO BASICO

            elif tela_ativa == 78:
                if mouse_x > x088 and mouse_y > y088 and mouse_x < x188 and mouse_y < y188:
                    fundo = pygame.image.load(chave_bas)
                    tela_ativa = 79

            elif tela_ativa == 79:
                fundo = pygame.image.load(passar_nivel)
                tela_ativa = 80

            elif tela_ativa == 80:
                if mouse_x > x025 and mouse_y > y025 and mouse_x < x125 and mouse_y < y125:
                    fundo = pygame.image.load(tela_jogar)
                    tela_ativa = 4

                if mouse_x > x024 and mouse_y > y024 and mouse_x < x124 and mouse_y < y124:
                    fundo = pygame.image.load(tela_jogar)
                    tela_ativa = 4

####################################################################################################
##POSIÇÕES E MUDANÇAS DE TELA- INTERMEDIÁRIO
#pergunta avançado 1
            elif tela_ativa == 649:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_1)
                    som_c.play()
                    tela_ativa = 650
            elif tela_ativa == 650:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro)
                    som_f.play()
                    tela_ativa = 649
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 649
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 649
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_1)
                    som_j.play()
                    tela_ativa = 649
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 649
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(acerto)
                    som_g.play()
                    tela_ativa = 651
            elif tela_ativa == 651:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 652
#pergunta avançado 2
            elif tela_ativa == 652:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_2)
                    som_c.play()
                    tela_ativa = 653
            elif tela_ativa == 653:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 652
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 652
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 652
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_2)
                    som_j.play()
                    tela_ativa = 652
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 652
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(acerto2)
                    som_g.play()
                    tela_ativa = 654
            elif tela_ativa == 654:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 655
#pergunta avançado 3
            elif tela_ativa == 655:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_3)
                    som_c.play()
                    tela_ativa = 656
            elif tela_ativa == 656:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro)
                    som_f.play()
                    tela_ativa = 655
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 655
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 655
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_3)
                    som_j.play()
                    tela_ativa = 655
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 655
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(acerto3)
                    som_g.play()
                    tela_ativa = 657
            elif tela_ativa == 657:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 658
#pergunta avançado 4
            elif tela_ativa == 658:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_4)
                    som_c.play()
                    tela_ativa = 659
            elif tela_ativa == 659:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 658
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 658
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 658
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_4)
                    som_j.play()
                    tela_ativa = 658
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 658
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 660
            elif tela_ativa == 660:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 661
#pergunta avançado 5
            elif tela_ativa == 661:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_5)
                    som_c.play()
                    tela_ativa = 662
            elif tela_ativa == 662:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 661
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 661
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 661
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_5)
                    som_j.play()
                    tela_ativa = 661
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 661
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(acerto2)
                    som_g.play()
                    tela_ativa = 663
            elif tela_ativa == 663:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 664
#pergunta avançado 6
            elif tela_ativa == 664:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_6)
                    som_c.play()
                    tela_ativa = 665
            elif tela_ativa == 665:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro)
                    som_f.play()
                    tela_ativa = 664
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 664
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 664
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_6)
                    som_j.play()
                    tela_ativa = 664
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 664
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(acerto3)
                    som_g.play()
                    tela_ativa = 666
            elif tela_ativa == 666:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 667
#pergunta avançado 7
            elif tela_ativa == 667:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_7)
                    som_c.play()
                    tela_ativa = 668
            elif tela_ativa == 668:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 667
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 667
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 667
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_7)
                    som_j.play()
                    tela_ativa = 667
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 667
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 669
            elif tela_ativa == 669:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 670
#pergunta avançado 8
            elif tela_ativa == 670:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_8)
                    som_c.play()
                    tela_ativa = 671
            elif tela_ativa == 671:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 670
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 670
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 670
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_8)
                    som_j.play()
                    tela_ativa = 670
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 670
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(acerto2)
                    som_g.play()
                    tela_ativa = 672
            elif tela_ativa == 672:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 673
#pergunta avançado 9
            elif tela_ativa == 673:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_9)
                    som_c.play()
                    tela_ativa = 674
            elif tela_ativa == 674:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro)
                    som_f.play()
                    tela_ativa = 673
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 673
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 673
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_9)
                    som_j.play()
                    tela_ativa = 673
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 673
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(acerto3)
                    som_g.play()
                    tela_ativa = 675
            elif tela_ativa == 675:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_interm)
                    tela_ativa = 676
#pergunta avançado 10
            elif tela_ativa == 676:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_interm_10)
                    som_c.play()
                    tela_ativa = 677
            elif tela_ativa == 677:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 676
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 676
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 676
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_interm_10)
                    som_j.play()
                    tela_ativa = 676
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 676
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 678
#tela recomeçar ou avançar avançado

            elif tela_ativa == 678:
                if mouse_x > x088 and mouse_y > y088 and mouse_x < x188 and mouse_y < y188:
                    fundo = pygame.image.load(chave_ava)
                    tela_ativa = 679

            elif tela_ativa == 679:
                fundo = pygame.image.load(recomecar_avancar_intermd)
                tela_ativa = 680

            elif tela_ativa == 680:
                if mouse_x > x025 and mouse_y > y025 and mouse_x < x125 and mouse_y < y125:
                    fundo = pygame.image.load(port_int)
                    tela_ativa = 4

                if mouse_x > x024 and mouse_y > y024 and mouse_x < x124 and mouse_y < y124:
                    fundo = pygame.image.load(tela_jogar)
                    tela_ativa = 4

####################################################################################################
##POSIÇÕES E MUDANÇAS DE TELA- AVANÇADO
#pergunta avançado 1
            elif tela_ativa == 849:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_1)
                    som_c.play()
                    tela_ativa = 850
            elif tela_ativa == 850:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro)
                    som_f.play()
                    tela_ativa = 849
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 849
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 849
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_1)
                    som_j.play()
                    tela_ativa = 849
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 849
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(acerto)
                    som_g.play()
                    tela_ativa = 851
            elif tela_ativa == 851:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 852
#pergunta avançado 2
            elif tela_ativa == 852:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_2)
                    som_c.play()
                    tela_ativa = 853
            elif tela_ativa == 853:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 852
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 852
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 852
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_2)
                    som_j.play()
                    tela_ativa = 852
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 852
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto2)
                    som_g.play()
                    tela_ativa = 854
            elif tela_ativa == 854:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 855
#pergunta avançado 3
            elif tela_ativa == 855:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_3)
                    som_c.play()
                    tela_ativa = 856
            elif tela_ativa == 856:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro)
                    som_f.play()
                    tela_ativa = 855
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 855
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 855
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_3)
                    som_j.play()
                    tela_ativa = 855
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 855
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto3)
                    som_g.play()
                    tela_ativa = 857
            elif tela_ativa == 857:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 858
#pergunta avançado 4
            elif tela_ativa == 858:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_4)
                    som_c.play()
                    tela_ativa = 859
            elif tela_ativa == 859:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 858
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 858
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 858
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_4)
                    som_j.play()
                    tela_ativa = 858
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 858
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 860
            elif tela_ativa == 860:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 861
#pergunta avançado 5
            elif tela_ativa == 861:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_5)
                    som_c.play()
                    tela_ativa = 862
            elif tela_ativa == 862:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 861
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 861
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 861
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_5)
                    som_j.play()
                    tela_ativa = 861
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 861
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(acerto2)
                    som_g.play()
                    tela_ativa = 863
            elif tela_ativa == 863:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 864
#pergunta avançado 6
            elif tela_ativa == 864:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_6)
                    som_c.play()
                    tela_ativa = 865
            elif tela_ativa == 865:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro)
                    som_f.play()
                    tela_ativa = 864
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 864
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 864
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_6)
                    som_j.play()
                    tela_ativa = 864
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 864
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(acerto3)
                    som_g.play()
                    tela_ativa = 866
            elif tela_ativa == 866:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 867
#pergunta avançado 7
            elif tela_ativa == 867:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_7)
                    som_c.play()
                    tela_ativa = 868
            elif tela_ativa == 868:
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 867
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 867
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 867
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_7)
                    som_j.play()
                    tela_ativa = 867
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 867
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 869
            elif tela_ativa == 869:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 870
#pergunta avançado 8
            elif tela_ativa == 870:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_8)
                    som_c.play()
                    tela_ativa = 871
            elif tela_ativa == 871:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 870
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 870
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 870
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_8)
                    som_j.play()
                    tela_ativa = 870
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 870
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(acerto2)
                    som_g.play()
                    tela_ativa = 872
            elif tela_ativa == 872:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 873
#pergunta avançado 9
            elif tela_ativa == 873:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_9)
                    som_c.play()
                    tela_ativa = 874
            elif tela_ativa == 874:
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro)
                    som_f.play()
                    tela_ativa = 873
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(erro2)
                    som_f.play()
                    tela_ativa = 873
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 873
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_9)
                    som_j.play()
                    tela_ativa = 873
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 873
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(acerto3)
                    som_g.play()
                    tela_ativa = 875
            elif tela_ativa == 875:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(prox_ava)
                    tela_ativa = 876
#pergunta avançado 10
            elif tela_ativa == 876:
                if mouse_x > x020 and mouse_y > y020 and mouse_x < x120 and mouse_y < y120:
                    fundo = pygame.image.load(perg_ava_10)
                    som_c.play()
                    tela_ativa = 877
            elif tela_ativa == 877:
                if mouse_x > x013 and mouse_y > y013 and mouse_x < x103 and mouse_y < y103:
                    fundo = pygame.image.load(erro4)
                    som_f.play()
                    tela_ativa = 876
                if mouse_x > x014 and mouse_y > y014 and mouse_x < x104 and mouse_y < y104:
                    fundo = pygame.image.load(erro3)
                    som_f.play()
                    tela_ativa = 876
                if mouse_x > x016 and mouse_y > y016 and mouse_x < x106 and mouse_y < y106:
                    fundo = pygame.image.load(erro5)
                    som_f.play()
                    tela_ativa = 876
                if mouse_x > x018 and mouse_y > y018 and mouse_x < x108 and mouse_y < y108:
                    fundo = pygame.image.load(dica_ava_10)
                    som_j.play()
                    tela_ativa = 876
                if mouse_x > x019 and mouse_y > y019 and mouse_x < x109 and mouse_y < y109:
                    fundo = pygame.image.load(tabela)
                    som_c.play()
                    tela_ativa = 876
                if mouse_x > x015 and mouse_y > y015 and mouse_x < x105 and mouse_y < y105:
                    fundo = pygame.image.load(acerto4)
                    som_g.play()
                    tela_ativa = 878
#tela recomeçar ou avançar avançado
            elif tela_ativa == 878:
                fundo = pygame.image.load(recomecar_avancar_ava)
                tela_ativa = 879

            elif tela_ativa == 879:
                if mouse_x > x025 and mouse_y > y025 and mouse_x < x125 and mouse_y < y125:
                    fundo = pygame.image.load(port_ava)
                    tela_ativa = 4

                if mouse_x > x024 and mouse_y > y024 and mouse_x < x124 and mouse_y < y124:
                    fundo = pygame.image.load(premio_nobel_ava)
                    tela_ativa = 880
# tela fim do jogo avançado
            elif tela_ativa == 880:
                if mouse_x > x088 and mouse_y > y088 and mouse_x < x188 and mouse_y < y188:
                    fundo = pygame.image.load(fim_ava)
                    tela_ativa =881

            elif tela_ativa == 881:
                if mouse_x > x088 and mouse_y > y088 and mouse_x < x188 and mouse_y < y188:
                    fundo = pygame.image.load(tela_inicial)
                    tela_ativa = 1




    pygame.display.flip()