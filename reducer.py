#!/usr/bin/env python

from operator import itemgetter
import sys

sum_tmax = 0
sum_tmin = 0

min_tmin = 0
max_tmax = 0

cnt_tmax = 0
cnt_tmin = 0

hottest_data = { 'value': 0, 'stations': [] }
coldest_data = { 'value': 0, 'stations': [] }

cur_year = None
year = None

for line in sys.stdin:
    line = line.strip()
    timestamp, station_id, element, value = line.split('\t', 3)
    year = str(timestamp)[:4]

    try:
        value = int(value)
    except ValueError:
        continue

    if cur_year is None:
        cur_year = year

    if year != cur_year:
        print 'Year: %s' % cur_year
        print 'Average TMAX\t%s\t' % (sum_tmax * 1.0 / cnt_tmax)
        print 'Average TMIN\t%s\t' % (sum_tmin * 1.0 / cnt_tmin)
        print 'Max TMAX\t%s\t' % max_tmax
        print 'Min TMIN: %s' % min_tmin
        print 'Coldest Stations %s' % ([x['station_id'] for x in coldest_data['stations']])
        print 'Coldest Station Values %s' % ([x['value'] for x in coldest_data['stations']])
        print 'Hottest Stations %s' % ([x['station_id'] for x in hottest_data['stations']])
        print 'Hottest Station Values %s' % ([x['value'] for x in hottest_data['stations']])
        print '--------------------------------'

        cur_year = year
        sum_tmax = 0
        sum_tmin = 0
        cnt_tmax = 0
        cnt_tmin = 0
        max_tmax = 0
        min_tmin = 0
        hottest_data['stations'] = []
        coldest_data['stations'] = []

    if element == "TMAX":
        sum_tmax += value
        if value > max_tmax:
            max_tmax = value
        cnt_tmax += 1

    elif element == "TMIN":
        sum_tmin += value
        if value < min_tmin:
            min_tmin = value
        cnt_tmin += 1

    if value > hottest_data['value']:
        hottest_data = {
            'value': value,
            'station_id': station_id,
            'day': timestamp,
            'stations': hottest_data['stations']
        }

    if value < coldest_data['value']:
        coldest_data = {
            'value': value,
            'station_id': station_id,
            'day': timestamp,
            'stations': coldest_data['stations']
        }

    if len(hottest_data['stations']) < 5:
        hottest_data['stations'].append({ 'value': value, 'station_id': station_id })
    else:
        coolest_value = min([x['value'] for x in hottest_data['stations']])
        if value > coolest_value:
            idx = next((index for (index, d) in enumerate(hottest_data['stations']) if d['value'] == coolest_value), None)
            hottest_data['stations'][idx] = {
                'value': value,
                'station_id': station_id
            }

    if len(coldest_data['stations']) < 5:
        coldest_data['stations'].append({ 'value': value, 'station_id': station_id })
    else:
        hottest_value = max([x['value'] for x in coldest_data['stations']])
        if value < hottest_value:
            idx = next((index for (index, d) in enumerate(coldest_data['stations']) if d['value'] == hottest_value), None)
            coldest_data['stations'][idx] = {
                'value': value,
                'station_id': station_id
            }

if year == cur_year:
    print 'Year: %s' % cur_year
    print 'Average TMAX: %s\t' % (sum_tmax * 1.0 / cnt_tmax)
    print 'Average TMIN: %s\t' % (sum_tmin * 1.0 / cnt_tmin)
    print 'Max TMAX: %s' % max_tmax
    print 'Min TMIN: %s' % min_tmin

    print 'Hottest Day:\t%s\t%s\t%s' %(hottest_data['day'], hottest_data['value'], hottest_data['station_id'])
    print 'Coldest Day:\t%s\t%s\t%s' %(coldest_data['day'], coldest_data['value'], coldest_data['station_id'])

    print 'Coldest Stations %s' % ([x['station_id'] for x in coldest_data['stations']])
    print 'Coldest Station Values %s' % ([x['value'] for x in coldest_data['stations']])
    print 'Hottest Stations %s' % ([x['station_id'] for x in hottest_data['stations']])
    print 'Hottest Station Values %s' % ([x['value'] for x in hottest_data['stations']])