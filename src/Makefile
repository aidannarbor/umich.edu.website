BUILDDIR=../build
all: ../build/index.html ../build/events.html ../build/projects.html ../build/getinvolved.html ../build/about-us.html ../build/apna-skool.html ../build/project-sec.html ../build/snehibhavan.html ../build/gallery.html ../build/project-mukti.html ../build/project-skmuk.html copy_files ../build/people-kiran-vissa.html ../build/donate.html ../build/project-kisan-mitra.html

HTMLPARTS=header.html sidebar.html footer.html

../build/%.html: %.jinja $(HTMLPARTS)
	python ../scripts/jinja2html.py $< $@ $(HTMLPARTS)

copy_files: $(BUILDDIR)/fonts $(BUILDDIR)/events_files $(BUILDDIR)/index_files
	rsync -ruE files/ ../build/files/

$(BUILDDIR)/fonts:
	ln -s files $@

$(BUILDDIR)/events_files:
	ln -s files $@

$(BUILDDIR)/index_files:
	ln -s files $@

