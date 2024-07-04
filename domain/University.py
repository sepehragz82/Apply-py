class University:
<<<<<<< Updated upstream
    def __init__(self, UniversityName, CityID, InternationalsAsTA, FallDeadline, WinterDeadline):
        self.UniversityName = UniversityName
        self.CityID = CityID
        self.InternationalsAsTA = InternationalsAsTA
        self.FallDeadline = FallDeadline
        self.WinterDeadline =   WinterDeadline
=======
    def __init__(self, UniversityName, CityID, InternationalsAsTA = None, FallDeadline = None, WinterDeadline = None):
        self.UniversityName = UniversityName;
        self.CityID = CityID;
        self.InternationalsAsTA = InternationalsAsTA;
        self.FallDeadline = FallDeadline;
        self.WinterDeadline =   WinterDeadline;
>>>>>>> Stashed changes
