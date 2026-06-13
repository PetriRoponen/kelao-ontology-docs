"""Kirjoittaa WIDOCO:n introduction-osiot dct:description-arvoista."""
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import DCTERMS

g = Graph()
g.parse("kelao-ontology-core2.ttl", format="turtle")
ont = URIRef("https://kela.fi/ontology/kelao")

fi = [str(o) for _, _, o in g.triples((ont, DCTERMS.description, None))
      if isinstance(o, Literal) and o.language == "fi"]
en = [str(o) for _, _, o in g.triples((ont, DCTERMS.description, None))
      if isinstance(o, Literal) and o.language == "en"]

with open("sections/introduction-fi.html", "w") as f:
    f.write('<h2 id="intro" class="list">Johdanto '
            '<span class="backlink"> takaisin <a href="#toc">sisällysluetteloon</a></span></h2>\n')
    for desc in fi:
        f.write(f'<span class="markdown">\n{desc}</span>\n\n')

with open("sections/introduction-en.html", "w") as f:
    f.write('<h2 id="intro" class="list">Introduction '
            '<span class="backlink"> back to <a href="#toc">ToC</a></span></h2>\n')
    for desc in en:
        f.write(f'<span class="markdown">\n{desc}</span>\n\n')

print(f"FI: {fi}")
print(f"EN: {en}")
