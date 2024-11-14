
#BBBBBBBBBBBBBBBBB                             tttt               tttt
#B::::::::::::::::B                         ttt:::t            ttt:::t
#B::::::BBBBBB:::::B                        t:::::t            t:::::t
#BB:::::B     B:::::B                       t:::::t            t:::::t
#  B::::B     B:::::B   ooooooooooo   ttttttt:::::tttttttttttttt:::::ttttttt        eeeeeeeeeeee       ggggggggg   ggggg aaaaaaaaaaaaa
#  B::::B     B:::::B oo:::::::::::oo t:::::::::::::::::tt:::::::::::::::::t      ee::::::::::::ee    g:::::::::ggg::::g a::::::::::::a
#  B::::BBBBBB:::::B o:::::::::::::::ot:::::::::::::::::tt:::::::::::::::::t     e::::::eeeee:::::ee g:::::::::::::::::g aaaaaaaaa:::::a
#  B:::::::::::::BB  o:::::ooooo:::::otttttt:::::::tttttttttttt:::::::tttttt    e::::::e     e:::::eg::::::ggggg::::::gg          a::::a
#  B::::BBBBBB:::::B o::::o     o::::o      t:::::t            t:::::t          e:::::::eeeee::::::eg:::::g     g:::::g    aaaaaaa:::::a
#  B::::B     B:::::Bo::::o     o::::o      t:::::t            t:::::t          e:::::::::::::::::e g:::::g     g:::::g  aa::::::::::::a
#  B::::B     B:::::Bo::::o     o::::o      t:::::t            t:::::t          e::::::eeeeeeeeeee  g:::::g     g:::::g a::::aaaa::::::a
#  B::::B     B:::::Bo::::o     o::::o      t:::::t    tttttt  t:::::t    tttttte:::::::e           g::::::g    g:::::ga::::a    a:::::a
#BB:::::BBBBBB::::::Bo:::::ooooo:::::o      t::::::tttt:::::t  t::::::tttt:::::te::::::::e          g:::::::ggggg:::::ga::::a    a:::::a
#B:::::::::::::::::B o:::::::::::::::o      tt::::::::::::::t  tt::::::::::::::t e::::::::eeeeeeee   g::::::::::::::::ga:::::aaaa::::::a
#B::::::::::::::::B   oo:::::::::::oo         tt:::::::::::tt    tt:::::::::::tt  ee:::::::::::::e    gg::::::::::::::g a::::::::::aa:::a
#BBBBBBBBBBBBBBBBB      ooooooooooo             ttttttttttt        ttttttttttt      eeeeeeeeeeeeee      gggggggg::::::g  aaaaaaaaaa  aaaa
#                                                                                                               g:::::g
#                                                                                                   gggggg      g:::::g
#                                                                                                   g:::::gg   gg:::::g
#                                                                                                    g::::::ggg:::::::g
#                                                                                                     gg:::::::::::::g
#                                                                                                       ggg::::::ggg
#                                                                                                          gggggg
#
#                                                             Vendita Vino
#                                                              Made By Leo
#
#_________                 __                 __  .__
#\_   ___ \  ____  _______/  |______    _____/  |_|__|
#/    \  \/ /  _ \/  ___/\   __\__  \  /    \   __\  |
#\     \___(  <_> )___ \  |  |  / __ \|   |  \  | |  |
# \______  /\____/____  > |__| (____  /___|  /__| |__|
#        \/           \/            \/     \/
# Inizio dichiarazione costanti
capacitàBottiglia=2
#Fine dichiarazione costanti

#____   ____            .__      ___.   .__.__  .__
#\   \ /   /____ _______|__|____ \_ |__ |__|  | |__|
# \   Y   /\__  \\_  __ \  \__  \ | __ \|  |  | |  |
#  \     /  / __ \|  | \/  |/ __ \| \_\ \  |  |_|  |
#   \___/  (____  /__|  |__(____  /___  /__|____/__|
#               \/              \/    \/
# Inizio dichiarazione variabili
nome=""
numLitri=0.0
costoLitro=0.0
totaleVino=0.0
numeroBottiglie=0.0
costoBottiglia=0.0
totaleBottiglie=0.0
totaleFinale=0.0
# Fine dichiarazione variabili

#________          __  .__
#\______ \ _____ _/  |_|__|
# |    |  \\__  \\   __\  |
# |    `   \/ __ \|  | |  |
#/_______  (____  /__| |__|
#        \/     \/
# Inizio inserimento dati
nome=input("Inserire un nome: ")
costoLitro=float(input("Inserire il costo al litro: "))
numLitri=float(input("Numero litri: "))
costoBottiglia=float(input("Inserire il costo della bottiglia: "))
# Fine inserimento dati

#_________        .__               .__  .__
#\_   ___ \_____  |  |   ____  ____ |  | |__|
#/    \  \/\__  \ |  | _/ ___\/  _ \|  | |  |
#\     \____/ __ \|  |_\  \__(  <_> )  |_|  |
# \______  (____  /____/\___  >____/|____/__|
#        \/     \/          \/
# Inizio esecuzione calcoli
totaleVino= costoLitro * numLitri
numeroBottiglie=(numLitri//capacitàBottiglia) # // fa si che si ignori la parte decimale
totaleBottiglie=numeroBottiglie * costoBottiglia
totaleFinale=totaleVino + totaleBottiglie
# Fine esecuzione calcoli

#  _________                    __         .__
# /   _____/ ____  ____   _____/  |________|__| ____   ____
# \_____  \_/ ___\/  _ \ /    \   __\_  __ \  |/    \ /  _ \
# /        \  \__(  <_> )   |  \  |  |  | \/  |   |  (  <_> )
#/_______  /\___  >____/|___|  /__|  |__|  |__|___|  /\____/
#        \/     \/           \/                    \/
# Inizio creazione scontrino
print()
print("   ┌─┐┌─┐┌─┐┌┐┌┌┬┐┬─┐┬┌┐┌┌─┐")
print("   └─┐│  │ ││││ │ ├┬┘│││││ │")
print("   └─┘└─┘└─┘┘└┘ ┴ ┴└─┴┘└┘└─┘")
print()
print()
print(f"Litri vino: {numLitri:.2f}")
print(f"Costo litro: {costoLitro:.2f}")
print(f"Totale vino: {totaleVino:.2f}")
print()
print("═════════════════════════════════")
print()
print(f"Numero bottiglie: {numeroBottiglie:.2f}")
print(f"Costo bottiglia: {costoBottiglia:.2f}")
print(f"Totale bottiglie: {totaleBottiglie:.2f}")
print()
print("═════════════════════════════════")
print()
print(f"Totale finale: {totaleFinale:.2f}")
print()
# Fine creazione scontrino