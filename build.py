# Wraps the artifact page in a full HTML document for static hosting.
import re,urllib.parse
src=open('/home/claude/peak/peak-roasters.html',encoding='utf-8').read()
title=re.search(r'<title>.*?</title>',src).group(0)
body=src.replace(title,'',1)
logo=re.search(r'const LOGO_SVG=\'(.*?)\';',src).group(1)
icon='data:image/svg+xml,'+urllib.parse.quote(logo)
head=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#EBDCC6">
<meta name="description" content="Peak Roasters — specialty coffee roastery and bar, roasted with care in Bahrain.">
{title}
<link rel="icon" href="{icon}">
<style>*,*::before,*::after{{box-sizing:border-box}}body{{margin:0;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:100%}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
'''
open('index.html','w',encoding='utf-8').write(head+body+'\n</body>\n</html>\n')
