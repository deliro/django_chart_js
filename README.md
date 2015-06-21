# django_chart_js
Integrate your charts easier

# Usage
In your view:

`data = [x**2 for x in range(30)]`

`return render(request, 'some_template.html', {'data': data})`

In your template:

`{% load django_chart_js_tags %}`

`{% chartjs 500x300 data line %}`

# Installation
1) Download ZIP
2) cd django_chart_js
3) python setup.py install
