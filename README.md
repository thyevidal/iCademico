# iCademico 
 
### Site institucional criado para o segundo desafio trainee da EJECT do processo seletivo de 2021.1

Membros responsáveis pelo projeto:
	Brenda Carvelho - Ux/Ui
	Hugo Correa - Front-End
	José Tavares - Back-End
	Thierry Vidal - Back-End

Estruturação segue o modelo padrão adotado pela EJECT em 2021.1:
*iCademico:
	core:
		static: arquivos css
		templates: arquivos html
	apps: aplicativos do projeto (a definir)
	media: arquivos de mídia
	pasta-raiz: configurações do projeto (arquivos padrões do Django)
	manage.py: arquivo padrão Django, responsável pela interação do projeto 
	requirements.txt: importações do projeto
	README.txt: você está aqui

Tecnologias:
	HTML5
	CSS3
	Python 3
	Django 3.2

Para rodar a instalção, baixe e instale o Python (https://www.python.org/downloads/), abra uma janela de comando na pasta iCademico e digite:
	pip install -r requeriments.txt
Será instalado o Django e a biblioteca Pillow, após (a partir da pasta iCademico) digite:
	.\myenve\Scripts\activate
	python manage.py runserver
Feito isso o servidor local deve ter sido inicializado, abra o seu navegador e cole: <http://127.0.0.1:8000/>. Este é o endereço padrão do projeto.
	
