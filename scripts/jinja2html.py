import jinja2
import codecs
import sys
import os

def jinja2html(jinjafname, outputfname, htmlparts):
    htmldata = dict()
    for html in htmlparts:
        basefhtml = os.path.basename(html)
        basefhtml, _ = os.path.splitext(basefhtml)
        input_file = codecs.open(html, mode="r", encoding="utf-8")
        htmldata[basefhtml] = input_file.read()

    jinjastring = codecs.open(jinjafname, mode="r", encoding="utf-8").read()
    template = jinja2.Template(jinjastring)
    genhtml = template.render(htmldata)

    output_file = codecs.open(outputfname, "w", 
                              encoding="utf-8", 
                              errors="xmlcharrefreplace"
                             )
    output_file.write(genhtml)

if __name__ == '__main__':
    jinjafname = sys.argv[1]
    outputfname = sys.argv[2]
    htmlfnames = sys.argv[3:]
    jinja2html(jinjafname, outputfname, htmlfnames)
