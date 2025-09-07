import requests
from bs4 import BeautifulSoup
from requests import RequestException

url_entrevistas = 'https://portal.anclivepa-sp.org.br/wp-content/uploads/2025/09/APRIMORAMENTO-HORARIOS-ENTREVISTAS-2025-EXTRAORDINARIO.pdf'

def send_ntfy_notification(message):
    try:
        requests.post(
            "https://ntfy.sh/anclivepa",
            data=message.encode('UTF-8'),
            headers={
                "Title": "Site mudou!!!!!!",
                "Priority": "high",
                "Tags": "warning",
                "Click": "https://portal.anclivepa-sp.org.br/"
            }
        )
        print("-> Notificação via ntfy.sh enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar notificação ntfy.sh: {e}")

def send_ntfy_notification_error(message):
    try:
        requests.post(
            "https://ntfy.sh/anclivep",
            data=message.encode('UTF-8'),
            headers={
                "Title": "Erro na solicitacao",
                "Priority": "high",
                "Tags": "warning",
            }
        )
        print("-> Notificação via ntfy.sh enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar notificação ntfy.sh: {e}")


def check_anclivepa():
    url = 'https://portal.anclivepa-sp.org.br/'
    print(f"[{__name__}] Verificando {url}...")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        slider_items_container = soup.select_one('.jet-slider__items.sp-slides')

        if slider_items_container:
            slides = slider_items_container.select('.jet-slider__item')
            current_count = len(slides)
            print(f"-> Encontrado(s) {current_count} slides no elemento.")

            if current_count != 4:
                send_ntfy_notification('Quantidade de slides mudou!')
            elif url_entrevistas not in response.text:
                send_ntfy_notification('Link de resultados alterado!!!')
            else:
                print(f"-> Link permanece igual.")
        else:
            print("-> AVISO: Elemento do slider não encontrado na página.")
            send_ntfy_notification_error('Elemento slide não encontrado na página')
            return

    except RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        send_ntfy_notification_error('Erro ao acessar URL')

if __name__ == "__main__":
    check_anclivepa()
