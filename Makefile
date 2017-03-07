
SUBDIRS = src
TARGET = build

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	@mkdir -p $(TARGET)
	 $(MAKE) -C $@

install-umich: subdirs
	rsync -rcavz build/ sftp.itd.umich.edu:/afs/umich.edu/group/soas/aidindia/Public/html/

install: install-umich

clean:
	rm -rf $(TARGET)
