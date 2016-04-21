
SUBDIRS = src

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	 $(MAKE) -C $@

install-umich: subdirs
	rsync -rcavz build/ sftp.itd.umich.edu:/afs/umich.edu/group/soas/aidindia/Public/html/

install: install-umich
