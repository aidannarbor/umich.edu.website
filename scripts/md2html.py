import markdown
import sys
import codecs
import jinja2

def md2html(inputfname, jinjafname, outputfname):
    input_file = codecs.open(inputfname, mode="r", encoding="utf-8")
    text = input_file.read()

    sections = text.split('\n\n')
    # Extract metadata at the beginning of the slide (look for key: value)
    # pairs.
    metadata_section = sections[0]
    metadata = parse_metadata(metadata_section)
    remainder_index = metadata and 1 or 0
    # Get the content from the rest of the slide.
    content_section = '\n\n'.join(sections[remainder_index:])

    html = markdown.markdown(content_section, extensions=['attr_list'])

    template = jinja2.Template(open(jinjafname).read())

    output_file = codecs.open(outputfname, "w", 
                              encoding="utf-8", 
                              errors="xmlcharrefreplace"
    )
    output_file.write(template.render({ 'html' : html, 'metadata' : metadata }))

def parse_metadata(section):
  """Given the first part of a slide, returns metadata associated with it."""
  metadata = {}
  metadata_lines = section.split('\n')
  for line in metadata_lines:
    colon_index = line.find(':')
    if colon_index != -1:
      key = line[:colon_index].strip()
      val = line[colon_index + 1:].strip()
      metadata[key] = val

  return metadata

if __name__ == '__main__':
    inputfname = sys.argv[1]
    jinjafname = sys.argv[2]
    outputfname = sys.argv[3]
    md2html(inputfname, jinjafname, outputfname)
