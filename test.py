import unittest
from app.models import Listing
from datetime import datetime
from app import views

class SpaceBnBTestCase(unittest.TestCase):
    id,user,title,description,expiration,locationx,locationy = 1,'User','Test Title','Description',datetime.utcnow(),5.0,3.0
    listing = Listing(id=id,user=user,title=title,description=description,expiration=expiration,locationx=locationx,locationy=locationy)

    def assert_datetime_equiv(self,se,pe):
        assert se.year == pe.year
        assert se.month == pe.month
        assert se.day == pe.day
        assert se.hour == pe.hour
        assert se.minute == pe.minute
        assert se.second == pe.second

    def test_datetime_encoding(self):
        se,pe = self.expiration,views.get_datetime_from_str(views.get_str_from_datetime(self.expiration))
        self.assert_datetime_equiv(se,pe)

    def test_jsonify_listing(self):
        jl = views.jsonify_listing(self.listing)
        assert jl['id'] and jl['id'] == self.id
        assert jl['user'] and jl['user'] == self.user
        assert jl['title'] and jl['title'] == self.title
        assert jl['description'] and jl['description'] == self.description
        assert jl['expiration']
        self.assert_datetime_equiv(views.get_datetime_from_str(jl['expiration']),self.expiration)
        assert jl['location'] and jl['location']['x'] and jl['location']['x'] == self.locationx
        assert jl['location'] and jl['location']['y'] and jl['location']['y'] == self.locationy

    def test_listing_from_json(self):
        jl = views.jsonify_listing(self.listing)
        lj = views.create_listing_from_json(jl)
        assert lj.user == self.user
        assert lj.title == self.title
        assert lj.description == self.description
        assert lj.locationx == self.locationx
        assert lj.locationy == self.locationy
        self.assert_datetime_equiv(lj.expiration,self.expiration)

if __name__ == '__main__':
    unittest.main()