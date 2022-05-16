import json
import sys

ipynb = sys.argv[1]
py = sys.argv[2]

with open(f'./{ipynb}.ipynb', 'r') as f:
	text = f.readlines()
	text = list(map(str.strip, text))
	text = json.loads(' '.join(text))["cells"]

with open(f'./{py}.py', 'w') as f:
	for cell in text:
		for j in cell["source"]:
			f.write(f"{'# ' if cell['cell_type'] == 'markdown' else ''}{j}")
		f.write(f"\n\n")