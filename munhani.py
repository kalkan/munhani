
# this code part print and create default map

#pip install ridge_map

import ridge_map as ridge_map

from ridge_map import RidgeMap

RidgeMap().plot_map()

# this code part create map with different mountain nicely looking

rm = RidgeMap((11.098251,47.264786,11.695633,47.453630))
values = rm.get_elevation_data(num_lines=150)
values=rm.preprocess(
    values=values,
    lake_flatness=2,
    water_ntile=10,
    vertical_ratio=240)
rm.plot_map(values=values,
            label='Karwendelgebirge',
            label_y=0.1,
            label_x=0.55,
            label_size=40,
            linewidth=1)

# nazilli civarı
rm = RidgeMap((26.999817,37.673676,29.315185,38.626885))
values = rm.get_elevation_data(num_lines=100)
rm.plot_map(values=rm.preprocess(values=values, water_ntile=15, vertical_ratio=30),
            label='Nazilli',
            label_x=0.1,
            label_size=30)

# meke civarı
rm = RidgeMap((33.555781,37.574427,33.595756,37.599444))
values = rm.get_elevation_data(num_lines=75)
rm.plot_map(values=rm.preprocess(values=values, water_ntile=15, vertical_ratio=50),
            label='Meke Krater Dağı',
            label_x=0.1,
            label_size=30)

# gökçeada bozcaada
rm = RidgeMap((24.921479,39.713877,26.120050,40.272541))
values = rm.get_elevation_data(num_lines=200)
rm.plot_map(values=rm.preprocess(values=values, water_ntile=0, vertical_ratio=30),
            label='Islands Near Çanakkale - @kaankalkan',
            label_x=0.1,
            label_size=24)

# ılgaz
rm = RidgeMap((32.624512,40.794405,34.738829,41.444099))
values = rm.get_elevation_data(num_lines=100)
rm.plot_map(values=rm.preprocess(values=values, water_ntile=10, vertical_ratio=100),
            label='Ilgaz',
            label_x=0.1,
            label_size=30)

# ıhlara vadisi
rm = RidgeMap((34.239837,38.230944,34.333539,38.312613))
values = rm.get_elevation_data(num_lines=100)
rm.plot_map(values=rm.preprocess(values=values, water_ntile=0, vertical_ratio=150),
            label='Ihlara Vadisi',
            label_x=0.1,
            label_size=30)

# prince islands
rm = RidgeMap((29.024893,40.832558,29.157381,40.922117))
values = rm.get_elevation_data(num_lines=200)
rm.plot_map(values=rm.preprocess(values=values, water_ntile=0, vertical_ratio=30),
            label='Prince Islands',
            label_x=0.1,
            label_size=30)

# vezirköprü
rm = RidgeMap((35.060527,41.159702,35.801224,41.4650))
values = rm.get_elevation_data(num_lines=100)
rm.plot_map(values=rm.preprocess(values=values, water_ntile=0, vertical_ratio=30),
            label='Vezirköprü',
            label_x=0.1,
            label_size=30)

# vezirköprü2
rm = RidgeMap((35.468205,41.154187,35.593828,41.350096))
values = rm.get_elevation_data(num_lines=250)
rm.plot_map(values=rm.preprocess(values=values, water_ntile=0, vertical_ratio=60),
            label='Vezirköprü',
            label_x=0.1,
            label_size=30)
