
from selenium import webdriver
import requests
import io
import time
import re
from bs4 import BeautifulSoup
from bs4.element import Tag
from PIL import Image

# ChromeDriver help video 
# https://www.youtube.com/watch?v=bhYulVzYRng

#-------------------------------------------------------------
def get_URL(etiqueta: Tag):

	descendientes = list(etiqueta.descendants)

	for _, iii in enumerate(descendientes):
		etiqueta_imagen = str(iii.find_next("img"))
		break	
	
	partes1 = re.split(' src="', etiqueta_imagen)
	partes2 = re.split('" title', partes1[1])
	url = partes2[0]
	lista_urls.append(url)
#-------------------------------------------------------------
def download_image2(download_path: str, url: str, file_name: str):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			image.save(f)
	except Exception as e:
		print('FAILED -', e)
#-------------------------------------------------------------

lista_urls = []
SEARCH_URL = "https://www.shutterstock.com/es/search/somali-cat?image_type=photo&page="

# contador de imagen descargada para no sobreescribir, ¡¡ Ir cambiando!!
index=0

for pagina in range(1, 21):
	cadena = SEARCH_URL + str(pagina)

	driver=webdriver.Chrome()
	driver.get(cadena)

	# Scrolling to the bottom to load all images
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1.5)

	# Scrolling all the way up
	driver.execute_script("window.scrollTo(0, 0);")

	page_html = driver.page_source
	pageSoup = BeautifulSoup(page_html, 'html.parser')
	containers = pageSoup.findAll('div', {'role':"img"})

	num_containers = len(containers)
	print("Nº de contenedores de imágenes: ", num_containers)

	for i in range(num_containers): 
		get_URL(containers[i])
	
	print('Longitud lista: ', len(lista_urls))
driver.quit()

for url in lista_urls:
    download_image2("carpeta/", url, f"exotico_corto_{str(index)}.jpg") # tener carpeta creada
    index+=1


print("Nº de contenedores de imágenes: ", num_containers)
print(f"***Siguiente número a poner = {index}***")
