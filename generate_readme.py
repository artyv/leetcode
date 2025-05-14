import os

def generate_readme(base_path='.'):
    folders = [f for f in os.listdir(base_path) if os.path.isdir(f) and not f.startswith('.')]
    folders.sort()

    readme_lines = []
    readme_lines.append('# LeetCode Fastest 3 Solutions per Problem 🏎️\n')
    readme_lines.append('| # | Title | Folder |\n')
    readme_lines.append('|---|-------|--------|\n')

    for idx, folder in enumerate(folders, 1):
        title = folder.replace('_', ' ')
        line = f'| {idx} | {title} | [Link](./{folder}) |'
        readme_lines.append(line)

    return '\n'.join(readme_lines)

if __name__ == '__main__':
    with open('README.md', 'w') as f:
        f.write(generate_readme())

