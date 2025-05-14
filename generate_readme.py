import os
import urllib.parse

def slugify(title):
    return title.lower().replace(' ', '-').replace("'", '').replace(',', '')

def generate_readme(base_path='.'):
    folders = sorted(
        f for f in os.listdir(base_path)
        if os.path.isdir(f) and not f.startswith('.') and f != '__pycache__'
    )

    readme_lines = []
    readme_lines.append('# LeetCode Fastest 3 Solutions per Problem 🏎️\n')
    readme_lines.append('| # | Title | Folder | LeetCode |')
    readme_lines.append('|---|-------|--------|----------|')

    for idx, folder in enumerate(folders, 1):
        title = folder.replace('_', ' ')
        slug = slugify(title)
        encoded_folder = urllib.parse.quote(folder)
        leetcode_url = f'https://leetcode.com/problems/{slug}/'
        folder_link = f'[📁 {title}](./{encoded_folder})'
        leetcode_link = f'[🔗 LeetCode]({leetcode_url})'
        readme_lines.append(f'| {idx} | {title} | {folder_link} | {leetcode_link} |')

    return '\n'.join(readme_lines)

if __name__ == '__main__':
    with open('README.md', 'w') as f:
        f.write(generate_readme())
