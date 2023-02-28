install:
	[ -d $(DESTDIR)/usr/lib/obs/service ] || mkdir -p $(DESTDIR)/usr/lib/obs/service
	cp example $(DESTDIR)/usr/lib/obs/service
	cp example.service $(DESTDIR)/usr/lib/obs/service
