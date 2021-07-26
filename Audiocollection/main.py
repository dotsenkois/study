class album:

    def __init__(self, album_name, band ):
        self.album_name = album_name
        self.band = band
        self.tracklist = []

    def get_tracks(self):
        print(f'трэк-лист абльбома {self.album_name}')
        for i in self.tracklist:
            print(i.track_name, i.track_lenth )

    def add_tracks(self, track_name):
        self.tracklist.append(track_name)

    def get_duration(self):
        self.total = 0
        for i in self.tracklist:
            self.total += i.track_lenth
        print(f'Общая длительность альбома {self.album_name} исполнтеля {self.band} составляет {self.total} минут')

class track:
    def __init__(self, track_name, track_lenth):
        self.track_name = track_name
        self.track_lenth = track_lenth

    def show(self):
        print('{0} {1} минут'.format(self.track_name, self.track_lenth))

black_album = album('Black album','Metallica')

Nothing_else_metters = track('Nothing else metters',5)
sad_but_true =track('Sad but true',3)
enter_sandman =track('Enter sandman',4)

black_album.add_tracks(Nothing_else_metters)
black_album.add_tracks(sad_but_true)
black_album.add_tracks(enter_sandman)

black_album.get_duration()
black_album.get_tracks()

once = album('Once','Nightwish')

dark_chest_of_wonders = track('dark_chest_of_wonders',4)
wish_i_had_an_angel =track('wish_i_had_an_angel',4)
nemo =track('nemo',4)

once.add_tracks(dark_chest_of_wonders)
once.add_tracks(wish_i_had_an_angel)
once.add_tracks(nemo)

once.get_duration()
once.get_tracks()

