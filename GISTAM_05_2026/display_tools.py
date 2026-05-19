import numpy as np
import math
from pyproj import Proj, transform
from ipyleaflet import (
    Map,
    basemaps,
    basemap_to_tiles,
    ImageOverlay,
    LayersControl,
    Rectangle,
    DrawControl,
    WidgetControl
)
from ipywidgets import Layout, IntSlider, IntRangeSlider, RadioButtons, DatePicker
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as mcm
from io import BytesIO
from base64 import b64encode
import rioxarray
import xarray as xr
import datetime


def _degree_to_zoom_level(l1, l2, margin = 0.0):
    
    degree = abs(l1 - l2) * (1 + margin)
    zoom_level_int = 0
    if degree != 0:
        zoom_level_float = math.log(360/degree)/math.log(2)
        zoom_level_int = int(zoom_level_float)
    else:
        zoom_level_int = 18
    return zoom_level_int


def map_extent(extent = None):
    """
    Description:
      Takes the latitude/longitude (EPSG:27700, i.e., official wales projection system) 
      of an area and create a map service backgroup with a red rectangle of given lat/lon.
    -----
    Input:
      extent: tuple with (min_lon, min_lat, max_lon, max_lat)
    Output:
      m: the background map/service provided by ipyleaflet
    """
    
    # check options combination
    assert not(extent is None), \
           'lat_ext and lon_ext are required'
    assert extent[1] < extent[3], 'extent values are in the wrong order must be (min_lon, min_lat, max_lon, max_lat)'
    assert extent[0] < extent[2], 'extent values are in the wrong order must be (min_lon, min_lat, max_lon, max_lat)'
    
    if (extent[0]<(-90)) | (extent[0]>90):
        # reproject extent from national system to WGS84
        training_inProj = Proj(init='EPSG:27700')
        training_outProj = Proj(init='EPSG:4326')
        min_lon,min_lat = transform(training_inProj,training_outProj,extent[0],extent[1])
        max_lon,max_lat = transform(training_inProj,training_outProj,extent[2],extent[3])
    else:
        min_lon = extent[0]
        min_lat = extent[1]
        max_lon = extent[2]
        max_lat = extent[3]
    
    lat_ext = (min_lat, max_lat)
    lon_ext = (min_lon, max_lon)
    
    # Location
    center = [np.mean(lat_ext), np.mean(lon_ext)]

    # create a basemap background (Open Street Map background) for the area
    margin = 0
    zoom_bias = 2
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *lat_ext ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *lon_ext) + zoom_bias
    zoom = min(lat_zoom_level, lon_zoom_level)

    m = Map(center=center, zoom=zoom, scroll_wheel_zoom = True,
       layout=Layout(width='800px', height='800px'))
    
    # add other basemaps to the background
    # ESRI satellite imagy
    esri = basemap_to_tiles(basemaps.Esri.WorldImagery)
    m.add_layer(esri)

    # add red rectangle with extent of the ROI
    rectangle = Rectangle(bounds = ((lat_ext[0], lon_ext[0]),
                                   (lat_ext[1], lon_ext[1])),
                          color = 'red', weight = 2, fill = False)

    m.add_layer(rectangle)
    m.add_control(LayersControl())

    return m


def map_geom(geometry = None):
    """
    Description:
      Takes the latitude/longitude (EPSG:27700, i.e., official wales projection system) 
      of an area and create a map service backgroup with a red rectangle of given lat/lon.
    -----
    Input:
      geometry: ipyleaflet GeoData
    Output:
      m: the background map/service provided by ipyleaflet with overlayed geometry
    """
    
    lat_list=[]
    lon_list=[]
    for item in range(0, len(geometry.data['features'])):
        for vertex in range(0,len(geometry.data['features'][item]['geometry']['coordinates'][0])):
            lon_list.append(geometry.data['features'][item]['geometry']['coordinates'][0][vertex][0])
            lat_list.append(geometry.data['features'][item]['geometry']['coordinates'][0][vertex][1])
    
    lat_ext = (min(lat_list), max(lat_list))
    lon_ext = (min(lon_list), max(lon_list))
    
    # Location
    center = [np.mean(lat_ext), np.mean(lon_ext)]

    # create a basemap background (Open Street Map background) for the area
    margin = 0
    zoom_bias = 2
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *lat_ext ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *lon_ext) + zoom_bias
    zoom = min(lat_zoom_level, lon_zoom_level)

    m = Map(center=center, zoom=zoom, scroll_wheel_zoom = True,
       layout=Layout(width='800px', height='800px'))
    
    # add other basemaps to the background
    # ESRI satellite imagy
    esri = basemap_to_tiles(basemaps.Esri.WorldImagery)
    m.add_layer(esri)
    
    m.add_layer(geometry)
    m.add_control(LayersControl())

    return m


def draw_select(geometry = None):
    """
    Description:
      Takes the latitude/longitude (EPSG:27700, i.e., official wales projection system) 
      of an area and create a map service backgroup with a red rectangle of given lat/lon.
    -----
    Input:
      extent: tuple with (min_lon, min_lat, max_lon, max_lat)
    Output:
      m: the background map/service provided by ipyleaflet
    """
    
    if (geometry == None):
        lat_ext = (51.508, 53.459)
        lon_ext = (-5.459, -2.643)
    else:
        lat_list=[]
        lon_list=[]
        for item in range(0, len(geometry.data['features'])):
            for vertex in range(0,len(geometry.data['features'][item]['geometry']['coordinates'][0])):
                lon_list.append(geometry.data['features'][item]['geometry']['coordinates'][0][vertex][0])
                lat_list.append(geometry.data['features'][item]['geometry']['coordinates'][0][vertex][1])

        lat_ext = (min(lat_list), max(lat_list))
        lon_ext = (min(lon_list), max(lon_list))
    
    # Location
    center = [np.mean(lat_ext), np.mean(lon_ext)]

    # create a basemap background (Open Street Map background) for the area
    margin = 0
    zoom_bias = 2
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *lat_ext ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *lon_ext) + zoom_bias
    zoom = min(lat_zoom_level, lon_zoom_level)

    m = Map(center=center, zoom=zoom, scroll_wheel_zoom = True,
       layout=Layout(width='800px', height='800px'))
    
    # add other basemaps to the background
    # ESRI satellite imagy
    esri = basemap_to_tiles(basemaps.Esri.WorldImagery)
    m.add_layer(esri)
    
    # add select option
    widgets_options = RadioButtons(
        options=['Extent', 'Selection'],
        layout={'width': 'max-content'}, # If the items' names are long
        description='Use drawn geometry for:',
        disabled=False)
    widget_control1 = WidgetControl(widget=widgets_options, position='topleft')
    
    # add option to handle drawing
    draw_control = DrawControl()
    draw_control.rectangle = {
    "shapeOptions": {
        "fillColor": "#fca45d",
        "color": "#fca45d",
        "fillOpacity": 0.2
        }
    }
    
    def handle_draw(self, action, geo_json):
        """Do something with the GeoJSON when it's drawn on the map"""  
        lat_min = 0
        lon_min = 0
        lat_max = 0
        lon_max = 0
        
        for corner in geo_json['geometry']['coordinates'][0]:
            if (corner[0]<lon_min) | (lon_min==0):
                lon_min = corner[0]
            if (corner[0]>lon_max) | (lon_max==0):
                lon_max = corner[0]

            if (corner[1]<lat_min) | (lat_min==0):
                lat_min = corner[1]
            if (corner[1]>lat_max) | (lat_max==0):
                lat_max = corner[1]
        
        global DRAW_EXTENT_COORD, DRAW_GEOJSON_GEOM
        DRAW_EXTENT_COORD = [lon_min, lat_min, lon_max, lat_max]
        DRAW_GEOJSON_GEOM = geo_json['geometry']
    
    draw_control.on_draw(handle_draw)
    
    m.add_control(draw_control)
    m.add_control(LayersControl())
    m.add_control(widget_control1)

    return m,widgets_options


def da_to_png64(da, cm):
    """
    Description:
      Takes a 2D (latitude/longitude) xarray and create a png image using a matplotlib color scheme.
    -----
    Input:
      da: an xarray of dim latitude/longitude
      cm: str indicating a matplotlib colormap
    Output:
      imgurl: image URL 
    """    
    arr = da.values
    
    # colorise xarray
    colorise = "mcm."+cm+"(arr)"
    #arr_colorised = eval(colorise)
    arr_colorised = mcm.get_cmap(cm)(arr)
    
    # create image from xarray
    arr_im = Image.fromarray(np.uint8(arr_colorised*255))
    im = Image.new('RGBA', arr.shape[::-1], color=None)
    im.paste(arr_im)
    
    # save image to png
    f = BytesIO()
    im.save(f, 'PNG')
    #data = b64encode(f.getvalue())
    #data = data.decode('ascii')
    data = b64encode(f.getvalue()).decode('ascii')
    
    # create image URL from PNG_64
    imgurl = 'data:image/png;base64,' + data
    
    return imgurl


def display_da(da, colormap):
    """
    Description:
      Display a colored xarray.DataArray on a map service backgroup
    -----
    Input:
      da: xarray.DataArray
      colormap: str indicating a matplotlib colormap
    Output:
      m: map to interact with
    """

    # Check inputs
    assert 'dataarray.DataArray' in str(type(da)), "da must be an xarray.DataArray"
    if (str(da.rio.crs) != 'EPSG:4326'):
        da = da.rio.reproject("EPSG:4326")
        
    
    if (da.attrs['_FillValue'] > 0):
        da = da.where(da < da.attrs['_FillValue'])
    else:
        da = da.where(da > da.attrs['_FillValue'])

    
    latitude = (float(da.y.min().values), float(da.y.max().values))
    longitude = (float(da.x.min().values), float(da.x.max().values))
    
    # convert DataArray to png64
    imgurl = da_to_png64(da, colormap)
    

    
    # Location
    center = [np.mean(latitude), np.mean(longitude)]

    # create a basemap background (Open Street Map background) for the area
    margin = 0
    zoom_bias = 2
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *latitude ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *longitude) + zoom_bias
    zoom = min(lat_zoom_level, lon_zoom_level)

    m = Map(center=center, zoom=zoom, scroll_wheel_zoom = True,
       layout=Layout(width='800px', height='800px'))
    
    # add other basemaps to the background
    # ESRI satellite imagy
    esri = basemap_to_tiles(basemaps.Esri.WorldImagery)
    m.add_layer(esri)

    io = ImageOverlay(name = 'DataArray', url=imgurl, bounds=[(latitude[0],longitude[0]),(latitude[1], longitude[1])],opacity=0.7)
    
    m.add_layer(io)
    m.add_control(LayersControl())

    return m


def cloud_threshold_slider():
    cloud_slider = IntSlider(value=20, min=0, max=100,step=5,
              description='Max cloud cover:',)

    return cloud_slider


def year_range_slider():
    today_year = datetime.date.today().year
    year_range = IntRangeSlider(
        value=[today_year-1, today_year],
        min=1992,
        max=2015,
#        max=today_year,
        step=1,
        description='year:'
    )
    return year_range


def calendar():
    from IPython.display import display, Javascript
    
    date = DatePicker(
        description='Pick a Date',
        disabled=False
    )
    date.add_class("start-date")
    
    script = Javascript("\
                    const query = '.start-date > input:first-of-type'; \
                    document.querySelector(query).setAttribute('min', '2017-01-01'); \
                    document.querySelector(query).setAttribute('max', '"+datetime.date.today().strftime("%Y-%m-%d")+"'); \
            ")

    display(date)
    display(script)
    return date


def rgb(ds,
        bands=['red', 'green', 'blue'],
        index=None,
        index_dim='time',
        robust=True,
        percentile_stretch=None,
        col_wrap=4,
        size=6,
        aspect=None,
        savefig_path=None,
        savefig_kwargs={},
        **kwargs):
    """
    Takes an xarray dataset and plots RGB images using three imagery 
    bands (e.g ['red', 'green', 'blue']). The `index` 
    parameter allows easily selecting individual or multiple images for 
    RGB plotting. Images can be saved to file by specifying an output 
    path using `savefig_path`.
    
    This function was designed to work as an easier-to-use wrapper 
    around xarray's `.plot.imshow()` functionality.
    
    Last modified: September 2020
    
    Parameters
    ----------  
    ds : xarray Dataset
        A two-dimensional or multi-dimensional array to plot as an RGB 
        image. If the array has more than two dimensions (e.g. multiple 
        observations along a 'time' dimension), either use `index` to 
        select one (`index=0`) or multiple observations 
        (`index=[0, 1]`), or create a custom faceted plot using e.g. 
        `col="time"`.       
    bands : list of strings, optional
        A list of three strings giving the band names to plot. Defaults 
        to '['red', 'green', 'blue']'.
    index : integer or list of integers, optional
        `index` can be used to select one (`index=0`) or multiple 
        observations (`index=[0, 1]`) from the input dataset for 
        plotting. If multiple images are requested these will be plotted
        as a faceted plot.
    index_dim : string, optional
        The dimension along which observations should be plotted if 
        multiple observations are requested using `index`. Defaults to 
        `time`.
    robust : bool, optional
        Produces an enhanced image where the colormap range is computed 
        with 2nd and 98th percentiles instead of the extreme values. 
        Defaults to True.
    percentile_stretch : tuple of floats
        An tuple of two floats (between 0.00 and 1.00) that can be used 
        to clip the colormap range to manually specified percentiles to 
        get more control over the brightness and contrast of the image. 
        The default is None; '(0.02, 0.98)' is equivelent to 
        `robust=True`. If this parameter is used, `robust` will have no 
        effect.
    col_wrap : integer, optional
        The number of columns allowed in faceted plots. Defaults to 4.
    size : integer, optional
        The height (in inches) of each plot. Defaults to 6.
    aspect : integer, optional
        Aspect ratio of each facet in the plot, so that aspect * size 
        gives width of each facet in inches. Defaults to None, which 
        will calculate the aspect based on the x and y dimensions of 
        the input data.
    savefig_path : string, optional
        Path to export image file for the RGB plot. Defaults to None, 
        which does not export an image file.
    savefig_kwargs : dict, optional
        A dict of keyword arguments to pass to 
        `matplotlib.pyplot.savefig` when exporting an image file. For 
        all available options, see: 
        https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html        
    **kwargs : optional
        Additional keyword arguments to pass to `xarray.plot.imshow()`.
        For example, the function can be used to plot into an existing
        matplotlib axes object by passing an `ax` keyword argument.
        For more options, see:
        http://xarray.pydata.org/en/stable/generated/xarray.plot.imshow.html  
        
    Returns
    -------
    An RGB plot of one or multiple observations, and optionally an image
    file written to file.
    
    """

    # Get names of x and y dims
    # TODO: remove geobox and try/except once datacube 1.8 is default
    try:
        y_dim, x_dim = ds.geobox.dimensions
    except AttributeError:
        from datacube.utils import spatial_dims
        y_dim, x_dim = spatial_dims(ds)

#     # If ax is supplied via kwargs, ignore aspect and size
#     if 'ax' in kwargs:

#         # Create empty aspect size kwarg that will be passed to imshow
#         aspect_size_kwarg = {}
#     else:
#         # Compute image aspect
#         if not aspect:
#             aspect = image_aspect(ds)

#         # Populate aspect size kwarg with aspect and size data
#         aspect_size_kwarg = {'aspect': aspect, 'size': size}

    # If no value is supplied for `index` (the default), plot using default
    # values and arguments passed via `**kwargs`
    if index is None:

        # Select bands and convert to DataArray
        da = ds[bands].to_array().compute()

        # If percentile_stretch == True, clip plotting to percentile vmin, vmax
        if percentile_stretch:
            vmin, vmax = da.quantile(percentile_stretch).values
            kwargs.update({'vmin': vmin, 'vmax': vmax})

        # If there are more than three dimensions and the index dimension == 1,
        # squeeze this dimension out to remove it
        if ((len(ds.dims) > 2) and ('col' not in kwargs) and
            (len(da[index_dim]) == 1)):

            da = da.squeeze(dim=index_dim)

        # If there are more than three dimensions and the index dimension
        # is longer than 1, raise exception to tell user to use 'col'/`index`
        elif ((len(ds.dims) > 2) and ('col' not in kwargs) and
              (len(da[index_dim]) > 1)):

            raise Exception(
                f'The input dataset `ds` has more than two dimensions: '
                f'{list(ds.dims.keys())}. Please select a single observation '
                'using e.g. `index=0`, or enable faceted plotting by adding '
                'the arguments e.g. `col="time", col_wrap=4` to the function '
                'call')

        img = da.plot.imshow(x=x_dim,
                             y=y_dim,
                             robust=robust,
                             col_wrap=col_wrap,
#                              **aspect_size_kwarg,
                             **kwargs)

    # If values provided for `index`, extract corresponding observations and
    # plot as either single image or facet plot
    else:

        # If a float is supplied instead of an integer index, raise exception
        if isinstance(index, float):
            raise Exception(
                f'Please supply `index` as either an integer or a list of '
                'integers')

        # If col argument is supplied as well as `index`, raise exception
        if 'col' in kwargs:
            raise Exception(
                f'Cannot supply both `index` and `col`; please remove one and '
                'try again')

        # Convert index to generic type list so that number of indices supplied
        # can be computed
        index = index if isinstance(index, list) else [index]

        # Select bands and observations and convert to DataArray
        da = ds[bands].isel(**{index_dim: index}).to_array().compute()

        # If percentile_stretch == True, clip plotting to percentile vmin, vmax
        if percentile_stretch:
            vmin, vmax = da.quantile(percentile_stretch).values
            kwargs.update({'vmin': vmin, 'vmax': vmax})

        # If multiple index values are supplied, plot as a faceted plot
        if len(index) > 1:

            img = da.plot.imshow(x=x_dim,
                                 y=y_dim,
                                 robust=robust,
                                 col=index_dim,
                                 col_wrap=col_wrap,
#                                  **aspect_size_kwarg,
                                 **kwargs)

        # If only one index is supplied, squeeze out index_dim and plot as a
        # single panel
        else:

            img = da.squeeze(dim=index_dim).plot.imshow(robust=robust,
#                                                         **aspect_size_kwarg,
                                                        **kwargs)

    # If an export path is provided, save image to file. Individual and
    # faceted plots have a different API (figure vs fig) so we get around this
    # using a try statement:

    
    

def rgb_stretch(ds,
                bands=['red', 'green', 'blue'],
                index=None,
                index_dim='time',
                robust=True,
                gamma=1.0,
                stretch='linear',
                percentile_stretch=None,
                col_wrap=4,
                size=6,
                aspect=None,
                savefig_path=None,
                savefig_kwargs={},
                **kwargs):
    """
    Applies RGB stretching to a dataset and generates plots for the specified bands.
    """
    try:
        y_dim, x_dim = ds.geobox.dimensions
    except AttributeError:
        from datacube.utils import spatial_dims
        y_dim, x_dim = spatial_dims(ds)

    # Function to apply stretch to RGB data
    def apply_stretch(data, gamma, stretch, bsc=None):
        data_ = data ** gamma
        if stretch == 'linear':
            return np.interp(data_, bsc, [0, 1])
        elif stretch == 'log':
            bsc[0] = max(bsc[0], 0.01)  # Avoid log(0) issues
            return np.interp(np.log(data_), np.log(bsc), [0, 1])
        elif stretch == 'sinh':
            return np.interp(np.sinh(data_), np.sinh(bsc), [0, 1])
        elif stretch == 'sqrt':
            return np.interp(np.sqrt(data_), np.sqrt(bsc), [0, 1])
        else:
            raise ValueError(f"Stretch '{stretch}' not supported")

    # Select bands and convert to DataArray
    da = ds[bands].to_array().compute()

    # Apply percentile stretch if specified
    if percentile_stretch:
        vmin, vmax = da.quantile(percentile_stretch).values
        kwargs.update({'vmin': vmin, 'vmax': vmax})

    # Apply the stretch function
    bsc = np.nanpercentile(da, percentile_stretch or (2, 98))
    da = xr.apply_ufunc(apply_stretch, da, gamma, stretch, bsc, vectorize=True)

    # Plotting logic depending on index
    if index is None:
        # No index provided, plot the entire dataset as an image or with facets
        img = da.plot.imshow(x=x_dim, y=y_dim, robust=robust, col_wrap=col_wrap, **kwargs)
    else:
        # Index specified, convert to list if needed
        index = index if isinstance(index, list) else [index]

        # Select the specified time indices
        da = da.isel(**{index_dim: index}).compute()

        # Plot as a faceted plot if multiple indices, or single panel if one index
        if len(index) > 1:
            img = da.plot.imshow(x=x_dim, y=y_dim, robust=robust, col=index_dim, col_wrap=col_wrap, **kwargs)
        else:
            img = da.squeeze(dim=index_dim).plot.imshow(x=x_dim, y=y_dim, robust=robust, **kwargs)

    # Save figure if a path is provided
    # if savefig_path:
    #     plt.savefig(savefig_path, **savefig_kwargs)

    return img




    