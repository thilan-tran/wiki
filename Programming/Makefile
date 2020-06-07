# markdown-pdf Makefile
# ---------------------
# compiles markdown to pdf, and opens pdf viewer (from WSL)

PAN_FLAGS=--pdf-engine=xelatex --listings
VIEW=cmd.exe /c start /b SumatraPDF
VIEW_FLAGS=-reuse-instance

%.pdf: %.md
	pandoc.exe $< $(PAN_FLAGS) -o $@

view-%:
	$(VIEW) $(VIEW_FLAGS) $$(echo $@ | awk -F '-' '{printf "%s.pdf", $$2}')
