# django_chart_js
**Django Chart.js** is django application that allows use Chart.js lib in django templates easy.

# Usage
In settings.py:

Add `django_chart_js` in your INSTALLED_APPS

In your view:

`data = [x**2 for x in range(30)]`

`return render(request, 'some_template.html', {'data': data})`

In your template:

`{% load chart_js_tags %}`

`{% chartjs 500x300 data line %}`

# Installation
Download ZIP

cd django_chart_js

python setup.py install

# Requirements
* django >= 1.6

# Licence
Licenced under a [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)