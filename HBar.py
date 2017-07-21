def HBar(data,width=600,title='',source='',fill='#3f619b',values_sorted=False,paper='#ffffff',locale='es-CL'):

    # SVG Base template
    svg_template = '''
    <svg style="font-family: Arial; font-weight: normal; font-style: normal; padding: 10px; background: {paper}" width="{width}" height="{height}" aria-labelledby="title desc" role="img">
        {bars}
    </svg>'''

    # Data
    (labels,values) = (data['labels'],data['values'])    

    # Default values
    bar_width = 20
    char_width = 8
    gap = 5
    margin = 10

    # Max label ans value
    max_label = max(labels, key=len)   
    max_value = max(values)

    # Plot dimensionas and labels area
    plot_width = width - char_width*(len(max_label) + len(str(max_value))) - margin - char_width*(len(str(max_value))) - 5
    left = len(max_label)*char_width + margin
    height = len(labels)*(bar_width + gap)

    # Sort values option
    if values_sorted:
        z = sorted(zip(labels,values), key=lambda x: x[1],reverse=values_sorted)
        (labels,values) = zip(*z)
    
    # Bar template
    bar_template = '''
    <g class="bar">
        <text x="0" y="{pos_y}" dy="{dy}">
            <tspan x="{label_x}" text-anchor="end">{label}</tspan>
        </text>
        <rect width="{width}" height="{height}" x="{x}" y="{y}" fill="{fill}"></rect>
        <text x="{pos_x}" y="{pos_y}" dy="{dy}">{val}</text>
    </g>'''
    array_bars = []
    for i,v in enumerate(values):
        label = labels[i]        
        if locale in ('es-CL','es-ES','es-AR','de'):
            value = "{:,}".format(v).replace(",",".")
        else:
            value = "{:,}".format(v)
        y = i*(bar_width + gap)
        array_bars.append(bar_template.format(
            x = left,
            y = y,
            dy = gap*6,
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
    
    # Returning string template
    out = '''
    <figure>
        <figcaption>
            <h3>{title}</h3>
        </figcaption>
    {svg}
    <figcaption><h5>{source}</h5></figcaption>
    </figure>
    
    '''.format(svg=svg,title=title,source=source)
    
    # Returns chart
    return out 