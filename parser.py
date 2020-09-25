import yaml

import pprint
import glob
import os

def metadata2html(md):
    def get(k): # Used when we do not want a 'None' strings
        v = md.get(k)
        if v is None:
            return ''
        return v
    html = '''
    <article class="article">
    <h2>{title}</h2>
    <p class="authors">{authors}</p>
    <p>
      <span class="tags">tags: {tags}</span>
      <span>status: <span class="status">{status}</span></span>
    </p>
    <p>
    <span>DOI: <span class="doi">{doi}</span></span>
    <span>preprint: <span class="preprint">{preprint}</span></span>
    <span><span class="jornal">{journal}</span></span>
    <span><span class="conference">{conference}</span></span>
    </p>
    <p class="funding-entities">{funding}</p>
    <p class="notes">{notes}</p>
    </article>
    '''.format(
        title=md['title'],
        status=get('status'),
        doi=get('doi'),
        preprint=get('preprint'),
        journal=get('journal'),
        conference=get('conference'),
        authors=md_authors2html(md['authors']),
        tags=md_tags2html(md['tags']),
        funding=md_funding2html(md['funding-entities']),
        notes=md.get('markdown'),
    )
    return html

def md_authors2html(a):
    return ' '.join(['<span class="author">%s</span>'%_ for _ in a])

def md_tags2html(t):
    return '\n'.join(['<span class="tag">%s</span>'%_ for _ in t])

def md_funding2html(f):
    return '\n'.join([
        '<p><span class="funding-agency">%s</span> <span class="all-numbers">%s</span><p>'%(
            _['name'], ' '.join(['<span class="number">%s</span>'%n for n in _['funding-numbers']])
            )
        for _ in f])

html = []

for f in os.listdir('./content/'):
    F = './content/'+f
    if not os.path.isdir(F):
        continue
    print(f)
    try:
        filecontent = open(F+"/README.md").read().split('---')
        metadata = yaml.load(filecontent[1], Loader=yaml.Loader)
        metadata['markdown'] = filecontent[2]
        html.append(metadata2html(metadata))
    except Exception as e:
        print('Problem with '+F)
        print(e)

template = open("template.html").read()
with open("out.html", "w") as f:
    articles = '<div class="articles">%s</div>'%('\n'.join(html))
    f.write(template.replace('{body}', articles))

