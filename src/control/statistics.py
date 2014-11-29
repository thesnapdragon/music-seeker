class Statistics:
    """docstring for Statistics"""
    def __init__(self, albums_available, callback):
        services = ['deezer', 'itunes', 'lastfm', 'spotify']
        names = ['Deezer', 'iTunes', 'Last.fm', 'Spotify']
        counters = [0, 0, 0, 0]
        for album in albums_available.values():
            for i, service in enumerate(album):
                if service:
                    counters[i] += 1
        count = len(albums_available)
        statistics = {}
        for i, service in enumerate(services):
            statistics[service] = {
                'count': counters[i],
                'percent': '{0:.2f}'.format(100 * counters[i] / float(count))
            }
        statistics['best_buy'] = names[counters.index(max(counters))]
        callback(statistics)
