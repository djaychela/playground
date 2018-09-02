import requests
from bs4 import BeautifulSoup

jupyter_cell_markdown_start = """{
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " """

jupyter_cell_middle = '","'

jupyter_cell_markdown_end = """
    "
   ]
  },"""

jupyter_cell_code_start = """
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    ""
   ]
  },"""


url = 'http://www.machinelearningplus.com/python/101-numpy-exercises-python'

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'lxml')

headings = soup.findAll('h2')

jupyter_code = ''
for heading in headings:
    jupyter_code += jupyter_cell_markdown_start[:-1]
    jupyter_code += '# ' + heading.text + '\n'
    jupyter_code += jupyter_cell_middle
    jupyter_code += heading.next_sibling.next_sibling.text + '\n'
    jupyter_code += jupyter_cell_markdown_end
    jupyter_code += jupyter_cell_code_start

    print(f"{heading.text} - {heading.next_sibling.next_sibling.text}")
print(jupyter_code)