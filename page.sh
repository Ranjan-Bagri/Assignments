#!/usr/bin/bash
f=$1
n=$2

#usage: ./page [filename] [number]

touch ${f}${n}.md

cat <<EOF >> ${f}${n}.md
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


##


### Desciption:


### Implementation:

<kbd>Input</kbd>

\`\`\`python

\`\`\`

<kbd>Output</kbd>

\`\`\`python

\`\`\`
EOF

