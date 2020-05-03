
SUBDIRS = src
TARGET = build
USER?="tell-me-your-username"

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS) venv/bin/activate

venv/bin/activate:
	virtualenv --python=python3 venv
	. venv/bin/activate && pip install jinja2

$(SUBDIRS): venv/bin/activate
	@mkdir -p $(TARGET)
	 . venv/bin/activate && $(MAKE) -C $@

install-umich: subdirs
	#rsync --delete -arcvz build/ $(USER)@sftp.itd.umich.edu:/afs/umich.edu/group/soas/aidindia/Public/html/
	rsync --delete -arcvz build/ $(USER)@login.itd.umich.edu:/afs/umich.edu/group/soas/aidindia/Public/html/

install: install-umich

clean:
	rm -rf $(TARGET)
