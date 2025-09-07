import requests

url_entrevistas = 'https://portal.anclivepa-sp.org.br/wp-content/uploads/2025/09/APRIMORAMENTO-HORARIOS-ENTREVISTAS-2025-EXTRAORDINARIO.pdf'

def send_ntfy_notification():
    try:
        requests.post(
            "https://ntfy.sh/anclivepa",
            data='Clique aqui para acessar o site da anclivepa',
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


def check_anclivepa():
    response = requests.get('https://portal.anclivepa-sp.org.br/')

    if url_entrevistas in response.text:
        print('Resultado da primeira etapa ainda presente')
    else:
        send_ntfy_notification()

check_anclivepa()
