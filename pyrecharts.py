from IPython.display import display,HTML,SVG

def HBar(data,width=600,title='',source='',fill='#3f619b',values_sorted=False,paper='#ffffff',locale='es-CL'):

    svg_template = '''
    <svg style="padding: 10px; background: {paper}" class="chart" width="{width}" height="{height}" aria-labelledby="title desc" role="img">
        {bars}
    </svg>'''

    # Datos
    (labels,values) = (data['labels'],data['values'])    

    # Valores por defecto
    bar_width = 20
    char_width = 8
    gap = 5
    margin = 10

    # Máxima etiqueta, máximo valor y área efectiva de ploteo
    max_label = max(labels, key=len)   
    max_value = max(values)

    # Áreas para etiquetas y plot
    plot_width = width - char_width*(len(max_label) + len(str(max_value))) - margin - 5
    left = len(max_label)*char_width + margin
    height = len(labels)*(bar_width + gap)
    #print(left)
    #return

    if values_sorted:
        z = sorted(zip(labels,values), key=lambda x: x[1],reverse=values_sorted)
        (labels,values) = zip(*z)
    bar_template = '''
    <g class="bar">
        <text x="0" y="{pos_y}" dy="1.8em">
            <tspan x="{label_x}" text-anchor="end">{label}</tspan>
        </text>
        <rect width="{width}" height="{height}" x="{x}" y="{y}" fill="{fill}"></rect>
        <text x="{pos_x}" y="{pos_y}" dy="1.8em">{val}</text>
    </g>'''
    array_bars = []
    for i,v in enumerate(values):
        label = labels[i]        
        if locale=='es-CL':
            value = "{:,}".format(v).replace(",",".")
        else:
            value = "{:,}".format(v)
        y = i*(bar_width + gap)
        array_bars.append(bar_template.format(
            x = left,
            y = y,
            width = (v/max_value)*plot_width,
            height = bar_width,
            pos_x = left + (v/max_value)*plot_width + 5,
            pos_y = y - (bar_width) + gap,
            val = value,
            label_x = left - margin,
            label = label,
            fill = fill
        ))
    bars = "\n".join(array_bars)
    svg = svg_template.format(width=width,height=height,title = title,paper = paper,bars = bars)
    out = '''
    <figure>
        <figcaption>
            <h3>{title}</h3>
        </figcaption>
    {svg}
    <figcaption><h5>{source}</h5></figcaption>
    </figure>'''.format(svg=svg,title=title,source=source)
    display(HTML(out)) 