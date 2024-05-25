import re

from jinja2 import Environment, FileSystemLoader

# Configure the Jinja2 environment to load templates from the current directory
env = Environment(loader=FileSystemLoader('.'))

# Get the HTML template
template = env.get_template('template.html')

def generate_filename(title):
    # Replaces spaces with underscores and removes non-alphanumeric characters
    filename = re.sub(r'\W+', '_', title)
    return f"{filename}.html"

def add_links(content, links):
    for word, url in links.items():
        # If it is 'mainlink', replace the specific word with the link
        if word == 'mainlink_word':
            content = replace_word_with_link(content, word, url)
        else:
            # Use regular expression to replace the word with the <a> tag
            content = re.sub(fr'\b{word}\b', f'<a href="{url}">{word}</a>', content)
    return content

def replace_word_with_link(content, word, url):
    # Divide the sentence into two parts: before and after the word
    parts = content.split(f'{word}')
    # Insert the link between the parts
    return f'{parts[0]}<a href="{url}">{word}</a>{parts[1]}'


# Function to style specific words
def style_words(content, words_to_style, style_class):
    for word in words_to_style:
        # Use regular expression to wrap the word with the <span> tag and CSS class
        content = re.sub(fr'\b{word}\b', f'<span class="{style_class}">{word}</span>', content)
    return content


# Data to render in the template
data = {
    'title': 'FormatSwap V2',
    'subtitle': 'Faster, Better, Powerful',
    'about': 'FormatSwap is a complete image converter/resizing tool. With just a few clicks, you can convert and resize images for individual objects or entire scenes. This not only reduces the blend file size but also cuts down on render time.',
    'mainlink': 'Why would you need to convert or resize textures? Check this page to learn more.',
    'mainlink_word': 'this page',
    'mainlink_url': 'https://example.com/',
    'content_blocks': [
        {
            'heading': 'Features',
            'list_items': [
                'Resize and convert to any image format supported by blender',
                'Batch Resizing (Resize into multiple sizes at the same time)',
                'Auto Replace textures system'
            ]
        },
        {
            'heading': 'What is new in V2?',
            'list_items': [
                'Light Speed Peformance (Up to 25x Faster)',
                'Industry standard resizing quality',
                'Brand new documentation page'
            ],
            'links': {
                'documentation page': 'https://example.com'
            }
        },
        {
            'heading': 'Image Conversion and Resizing',
            'text_lines': [
                'Never open another external software to convert or resize images. Formatswap supports all image formats that can be loaded in blender. And after processing them, the add-on will automatically replace the images in your scene.'
             ],
            'image_urls': [
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s'
            ]
        },
        {
            'heading': 'Advanced Filtering',
            'text_lines': [
                'With our updated filtering system, you`ll have precise control over the images you convert or resize. Easily filter by image dimensions, file size, format, and even PBR map type.'
            ],
            'image_urls': [
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
                 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
                   'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
            ]
        },
        {
            'heading': 'PBR Friendly',
            'text_lines': [
                'Imaging be able to resizing/convert all images in your scene with one click, without worrying about the loss of quality in environment, normal and displacement maps, I`m sure you don`t want these maps to be converted to .JPG.',
                'With formatswap, you chose how to deal with them, and the add-on will do the rest for you.'
            ],
            'image_urls': [
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s'
            ]
        },
        {
            'text_lines': [
                'Did you mess up? easily restore your original textures',
                'With just one click, restore all original images, simple like that. Any converted or resized image can be restored. '
            ],
             'words_to_style': ['restore', 'textures'],
            'image_urls': [
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s'
            ]
        }
    ],
    'image_urls': [
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlHI3BJiB7lkVxhKUKI8YxJoTrGDInnZI3gzhmvAZEGA&s',
    ]
}

# Process the links in each content block
for block in data['content_blocks']:
    if 'links' in block:
        # Add links in lines of text
        if 'text_lines' in block:
            block['text_lines'] = [add_links(line, block['links']) for line in block['text_lines']]

        # Add links to list items
        if 'list_items' in block:
            block['list_items'] = [add_links(item, block['links']) for item in block['list_items']]

    if 'words_to_style' in block:
        # Style words in lines of text
        if 'text_lines' in block:
            block['text_lines'] = [style_words(line, block['words_to_style'], 'highlight') for line in block['text_lines']]

        # Style words in list items
        if 'list_items' in block:
            block['list_items'] = [style_words(item, block['words_to_style'], 'highlight') for item in block['list_items']] 

# Add the 'mainlink' with your URL to the content
data['mainlink'] = replace_word_with_link(data['mainlink'], data['mainlink_word'], data['mainlink_url'])

# Generate file name
filename = generate_filename(data['title'])

# Render the template with the data
output = template.render(data)

# Save the output to an HTML file with the generated name
with open(filename, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Successfully generated HTML page: {filename} ✨")