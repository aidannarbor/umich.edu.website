BUILDDIR=../build
all: ../build/index.html ../build/events.html ../build/projects.html ../build/getinvolved.html ../build/about-us.html ../build/apna-skool.html ../build/project-sec.html ../build/snehibhavan.html ../build/gallery.html copy_files

HTMLPARTS=header.html sidebar.html footer.html

../build/%.html: %.jinja $(HTMLPARTS)
	python ../scripts/jinja2html.py $< $@ $(HTMLPARTS)

copy_files:
	rsync -ruE files/ ../build/files/
	ln -s files $(BUILDDIR)/fonts; /bin/true
	ln -s files $(BUILDDIR)/events_files; /bin/true
	ln -s files $(BUILDDIR)/index_files; /bin/true

