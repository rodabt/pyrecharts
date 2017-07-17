# pyrecharts
pyrecharts (Python Ready Charts) is a module for easy reporting in Jupyter Notebooks. Currently "es-CL" and "en" locales are supported. It renders SVG.

TODO: export to other formats, i.e.: jpg, png, pdf

## Usage:

```python
import pyrecharts
```

```python
# As is
data = dict(
    labels=['Región Metropolitana','Región de Aysén','Región de Concepción'],
    values=[65000,1200,33000]
)
pyrecharts.HBar(data=data)
```
![chart1](chart1.png)

```python
# Full detail. Height is fixed and depends on the number of data rows
data = dict(
    labels=['bananas','apples','oranges','watermelons','grapes'],
    values=[4000,8000,3000,1600,1000]
)
pyrecharts.HBar(
    data=data,
    width=500,
    title='Fruit prices',
    source='Source: WWW',
    fill="#dd3300",
    paper='#f3f3f3',
    locale='en',
    values_sorted=True)
```
![chart2](chart2.png)


