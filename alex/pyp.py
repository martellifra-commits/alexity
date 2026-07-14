import pandas as pd
import ipywidgets as widgets
from IPython.display import display, HTML

# ---------------------------------------------------------
# DATASET ITINERARIO GRECIA (Skopelos & Skiathos)
# ---------------------------------------------------------
data = [
    # SKOPELOS
    {
        "Giorno": "29 Luglio",
        "Isola": "Skopelos",
        "Titolo": "Arrivo & Primo Relax",
        "Orari / Logistica": "03:00 Partenza casa | 06:05 Volo PSA->JSI (Arr. 09:10) | 09:30 Alamo Auto | 11:05 Traghetto Seajets -> Skopelos (Arr. 12:05)",
        "Spiagge / Attività": "Limnonari Beach (Apenemo Beach Bar - ~15 min)",
        "Sera / Ristoranti / Bar": "Pranzo Skopelos Town/Check-in Anemi Studios | Sera: Donkee Skopelos (Cocktail)",
        "Note": "Check-in Anemi Studios dalle 14:00 (Già Pagato). Tel: +30 697 4103022"
    },
    {
        "Giorno": "30 Luglio",
        "Isola": "Skopelos",
        "Titolo": "Costa Nord-Ovest (Mamma Mia)",
        "Orari / Logistica": "Spostamenti brevi (~20 min)",
        "Spiagge / Attività": "Paralia Kastani (Spiaggia Mamma Mia, ~22 min) + Ftelia Beach Bar (5 min da Kastani)",
        "Sera / Ristoranti / Bar": "Visita borgo Neo Klima | Cena: Ristorante Anatoli (Skopelos Town)",
        "Note": "Kastani e Ftelia sono molto vicine tra loro."
    },
    {
        "Giorno": "31 Luglio",
        "Isola": "Skopelos",
        "Titolo": "Cuore della Costa Ovest",
        "Orari / Logistica": "Spostamenti ~20 min",
        "Spiagge / Attività": "Panormos Beach + Milia Beach (5 min tra le due) | Opzionale: Glysteri Beach Bar",
        "Sera / Ristoranti / Bar": "Cena: Korali Seafood Restaurant",
        "Note": "Ottima giornata per tramonto sulla costa ovest."
    },

    # SKIATHOS
    {
        "Giorno": "1 Agosto",
        "Isola": "Skiathos",
        "Titolo": "Spostamento a Skiathos & Megali Ammos",
        "Orari / Logistica": "10:20 Auto per Glossa (45 min) | 10:50 Traghetto Speedrunner Jet 2 -> Skiathos (Arr. 11:00)",
        "Spiagge / Attività": "Paralia Vromolimnos / Baracoa Beach Club",
        "Sera / Ristoranti / Bar": "Passeggiata Centro Skiathos Town",
        "Note": "Hotel 1 notte: Skiathos Thalassa Cape Hotel (Megali Ammos). Check-in dalle 15:00. Tel: +30 231 0592100"
    },
    {
        "Giorno": "2 Agosto",
        "Isola": "Skiathos",
        "Titolo": "Cambio Hotel & Koukounaries",
        "Orari / Logistica": "Check-out Thalassa Cape (11:00) -> Trasferimento 2° Hotel",
        "Spiagge / Attività": "Koukounaries Beach (spiaggia più famosa) + Agia Eleni Beach (tramonto)",
        "Sera / Ristoranti / Bar": "Aperitivo/Cena: Cay Beach Club",
        "Note": "Spostamento al secondo alloggio a Skiathos."
    },
    {
        "Giorno": "3 Agosto",
        "Isola": "Skiathos",
        "Titolo": "Gita via Mare a Lalaria",
        "Orari / Logistica": "Partenza dal porto di Skiathos Town per tour in barca",
        "Spiagge / Attività": "Paralia Lalaria (raggiungibile solo via mare) | Pomeriggio: Elia Beach",
        "Sera / Ristoranti / Bar": "Cena/Drink: Achinos Beach Restaurant",
        "Note": "Verificare condizioni meteo/mare per l'escursione a Lalaria."
    },
    {
        "Giorno": "4 Agosto",
        "Isola": "Skiathos",
        "Titolo": "Banana Beach Day",
        "Orari / Logistica": "Spostamenti in auto lungo la costa sud-ovest",
        "Spiagge / Attività": "Banana Beach / Paralia Mpanana (Grande Banana & Piccola Banana)",
        "Sera / Ristoranti / Bar": "Ultimo drink in centro a Skiathos Town",
        "Note": "Giornata intera dedicata al relax nella baia di Banana."
    },
    {
        "Giorno": "5 Agosto",
        "Isola": "Skiathos",
        "Titolo": "Rientro in Italia",
        "Orari / Logistica": "08:00 Restituzione Auto Alamo in aeroporto | 09:35 Volo Skiathos -> Pisa (Arr. 10:45)",
        "Spiagge / Attività": "Volo di rientro",
        "Sera / Ristoranti / Bar": "Arrivo a Pisa ore 10:45",
        "Note": "Fine del viaggio."
    }
]

# Creazione DataFrame Pandas
df = pd.DataFrame(data)

# ---------------------------------------------------------
# DASHBOARD INTERATTIVA CON IPYWIDGETS (per Jupyter Notebook / Lab)
# ---------------------------------------------------------
def visualizza_itinerario():
    filter_isola = widgets.Dropdown(
        options=["Tutte", "Skopelos", "Skiathos"],
        value="Tutte",
        description="Isola:",
        style={'description_width': 'initial'}
    )

    out = widgets.Output()

    def update_view(change):
        with out:
            out.clear_output()
            selected = filter_isola.value
            if selected == "Tutte":
                filtered_df = df
            else:
                filtered_df = df[df["Isola"] == selected]
            
            # Rendering HTML con stile per la tabella
            html_content = f"<h3>📍 Itinerario di Viaggio: Skopelos & Skiathos</h3>"
            html_content += filtered_df.to_html(index=False, classes='table table-striped table-hover', escape=False)
            display(HTML(html_content))

    filter_isola.observe(update_view, names='value')
    
    display(filter_isola)
    display(out)
    update_view(None)

if __name__ == "__main__":
    print("Dataset itinerario caricato correttamente!")
    print(df[["Giorno", "Isola", "Titolo", "Spiagge / Attività"]])
    # In un notebook Jupyter ti basterà chiamare: visualizza_itinerario()