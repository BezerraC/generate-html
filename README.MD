# HTML Page Generator with Styled Blocks

## Project description

This project is a dynamic HTML page generator using Python and the Jinja2 library for template rendering. The goal is to create HTML pages with multiple styled content blocks, including text, lists, image galleries, and dynamic links. Specific words within texts can be styled with a different color (purple, for example).

## Project Structure

- generate_html.py: Main script that processes the data and generates the HTML page.
- template.html: HTML template that defines the structure and style of the page.
- data: Dictionary in Python containing the data that will be inserted into the HTML page.

## Dependencies

- Python 3.x
- Jinja2

## Install dependencies using pip:

```
pip install -r requirements.txt
```

## Data Structure

The data is defined in a Python dictionary:

- title: Defines the page title
- subtitle: Defines the page subtitle
- about: Provides a general description of the page content or product/service being described
- mainlink: Contains a sentence or paragraph that includes a specific word or phrase that will be turned into a link
- mainlink_word: Specifies the word or phrase within mainlink that will be turned into a link
- mainlink_url: Contains the URL where the word or phrase specified in mainlink_word should point to.

Each content block has the following properties:

- heading: Title of the content block.
- text_lines: List of text lines to be displayed in the block.
- links: Dictionary of words and URLs to replace words with links.
- words_to_style: List of words that should be highlight.
- list_items: List of items to be displayed as a list in the block.
- image_urls: List of image URLs to be displayed as a gallery in the block.

## Data Example

```
data = {
    'title': 'My Page with Multiple Blocks and Links',
    'content_blocks': [
         {
             'heading': 'Welcome to My Site',
             'text_lines': [
                 'This is an example of dynamic content generated with Python and Jinja2. Visit the page for more details.',
                 'This is the second paragraph with more information.'
             ],
             'links': {
                 'page': 'https://example.com',
                 'details': 'https://detalhes.com'
             },
             'words_to_style': ['example', 'details'],
             'list_items': [
                 'Item 1',
                 'Item 2',
                 'Item 3'
             ],
             'image_urls': [
                 'https://via.placeholder.com/150',
                 'https://via.placeholder.com/150',
                 'https://via.placeholder.com/150'
             ]
         }
    ]
}
```

## How to Execute the Project

- Make sure you have all dependencies installed (Jinja2).
- Edit the data dictionary in the generate_html.py script as needed.
- Run the generate_html.py script:

```
python generate_html.py
```

The script will generate an HTML file with a name based on the title defined in data['title'] ✨.

## Author

<img src="https://avatars.githubusercontent.com/u/41126326?v=4" width="150" style="border-radius:15px;" alt="Exemplo imagem">

[@Bezerrac](https://github.com/BezerraC)

[![Instagram Badge](https://img.shields.io/badge/-@cbezerra_-E1306C?style=flat-square&labelColor=E1306C&logo=instagram&logoColor=white&link=https://www.instagram.com/c.bezerra_/)](https://www.instagram.com/c.bezerra_/)
[![Linkedin Badge](https://img.shields.io/badge/-Carlos_Bezerra-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/devcbezerra/)](https://www.linkedin.com/in/devcbezerra/)
[![Gmail Badge](https://img.shields.io/badge/-cbezerraneto@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:cbezerraneto@gmail.com)](mailto:cbezerraneto@gmail.com)
